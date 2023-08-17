package main

import (
	"fmt"
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

	r.ServeFiles("/data/{filepath:*}", "./data")
	r.ServeFiles("/assets/{filepath:*}", "./assets")

	// index.html
	r.GET("/", func(ctx *fasthttp.RequestCtx) {
		data, err := ioutil.ReadFile("./index.html")
		if err != nil {
			log.Fatal(err)
		}

		ctx.SetContentType("text/html")
		ctx.Write(data)
	})
	r.GET("/kill/{type}", func(ctx *fasthttp.RequestCtx) {
		ctx.SetContentType("text/plain")
		ctx.SetStatusCode(fasthttp.StatusOK)

		killType := ctx.UserValue("type").(string)
		fmt.Println("Got kill request for: " + killType)
		switch killType {
		case "parent":
			cmd := runFn([]string{"sh", "./main.sh", "stop"})
			if cmd != "200" {
				fmt.Println("Couldn't kill proc: " + cmd)
			}
			os.Exit(0)
			return

		case "child":
			cmd := runFn([]string{"sh", "./main.sh", "stop"})
			if cmd != "200" {
				gErr("Couldn't kill proc: "+cmd, ctx)
				return
			}
			ctx.Write([]byte("He was taken from us too soon."))
		}
		return
	})

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
