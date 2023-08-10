package main

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"

	"github.com/fasthttp/router"
	"github.com/fasthttp/websocket"
	"github.com/valyala/fasthttp"
)

var (
	upgrader = websocket.FastHTTPUpgrader{
		ReadBufferSize:  1024,
		WriteBufferSize: 1024,
	}
	filepath = "./data.json"
)

func handlePlot(ctx *fasthttp.RequestCtx) {
	// recieves multipart/form-data & extracts file from form
	file, err := ctx.FormFile("file")
	if err != nil {
		log.Println("Error extracting file from form:", err)
		return
	}

	f, err := file.Open()
	if err != nil {
		log.Println("Error opening file:", err)
		return
	}
	defer f.Close()

	buf := new(bytes.Buffer)
	_, err = io.Copy(buf, f)
	if err != nil {
		log.Println("Error copying file to buffer:", err)
		return
	}

	contents := buf.Bytes()
	fmt.Println("Contents:", string(contents))

	// reply with "started plot"
	ctx.SetContentType("text/plain")
	ctx.SetStatusCode(fasthttp.StatusOK)
	ctx.Write([]byte("<img id='spinner' class='spinner' src='/assets/bars.svg' />"))
}

func main() {
	r := router.New()

	var PORT string
	if len(os.Args) > 1 {
		PORT = os.Args[1]
	} else {
		PORT = "1337"
	}

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

	r.GET("/ws", func(ctx *fasthttp.RequestCtx) {
		err := upgrader.Upgrade(ctx, func(conn *websocket.Conn) {
			handleWS(conn)
		})
		if err != nil {
			log.Println("Websocket upgrade error:", err)
			return
		}

		defer ctx.Response.ConnectionClose()
	})
	r.POST("/plot", handlePlot)

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
