package main

import (
	"io/ioutil"
	"log"
	"os"

	"github.com/fasthttp/router"
	"github.com/valyala/fasthttp"
)

func main() {
	r := router.New()

	var PORT string
	if len(os.Args) > 1 {
		PORT = os.Args[1]
	} else {
		PORT = "1337"
	}

	r.ServeFiles("/assets/{filepath:*}", "./assets")

	r.GET("/data/{file}", dataHandler)
	r.GET("/", func(ctx *fasthttp.RequestCtx) {
		data, err := ioutil.ReadFile("./index.html")
		if err != nil {
			log.Fatal(err)
			ctx.Write([]byte("Error reading index.html"))
			return
		}

		ctx.SetContentType("text/html")
		csp(ctx).Write(data)
	})
	r.GET("/kill/{type}", killSwitch)
	r.POST("/plot", handlePlot)

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
