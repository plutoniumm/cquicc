package main

import (
	"io"
	"io/ioutil"
	"log"
	"os"
	"os/exec"

	"github.com/fasthttp/router"
	"github.com/fasthttp/websocket"
	"github.com/valyala/fasthttp"
)

var (
	upgrader = websocket.FastHTTPUpgrader{
		ReadBufferSize:  1024,
		WriteBufferSize: 1024,
	}
)

func handlePlot(ctx *fasthttp.RequestCtx) {
	// recieves multipart/form-data & extracts file from form
	errhold := ""
	file, err := ctx.FormFile("file")
	if err != nil {
		errhold = "extracting file from form"
		log.Println(errhold, err)
		return
	}

	dst, err := os.Create("data.txt")
	if err != nil {
		errhold = "creating file"
		log.Println(errhold, err)
		return
	}
	defer dst.Close()

	src, err := file.Open()
	if err != nil {
		errhold = "opening file"
		log.Println(errhold, err)
		return
	}
	defer src.Close()

	_, err = io.Copy(dst, src)
	if err != nil {
		errhold = "copying file"
		log.Println(errhold, err)
		return
	}

	cmd := exec.Command("sh", "./runner.sh")
	output, err := cmd.CombinedOutput()
	if err != nil {
		errhold = "running script"
		log.Println(errhold, err)
		return
	}

	// start loop
	sending = true
	startSend()

	// reply with "started plot"
	ctx.SetContentType("text/plain")
	ctx.SetStatusCode(fasthttp.StatusOK)
	if errhold != "" {
		errhold = "<div class='errCont'>Error: " + errhold + "</div>"
		ctx.Write([]byte(errhold))
	} else {
		ctx.Write(output)
	}
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
	r.GET("/kill", func(ctx *fasthttp.RequestCtx) {
		terminator()
		ctx.SetContentType("text/plain")
		ctx.SetStatusCode(fasthttp.StatusOK)
		ctx.Write([]byte("killed"))
	})
	r.GET("/pkill", func(ctx *fasthttp.RequestCtx) {
		ctx.SetContentType("text/plain")
		ctx.SetStatusCode(fasthttp.StatusOK)
		ctx.Write([]byte("killed"))
		os.Exit(0)
	})

	r.POST("/plot", handlePlot)

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
