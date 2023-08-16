package main

import (
	"io"
	"io/ioutil"
	"log"
	"os"

	"github.com/fasthttp/router"
	"github.com/valyala/fasthttp"
)

func handlePlot(c *fasthttp.RequestCtx) {
	// get ready to exit anytime
	c.SetContentType("text/plain")
	c.SetStatusCode(fasthttp.StatusOK)

	file, err := c.FormFile("file")
	if err != nil {
		gErr("extracting file from form", c)
		return
	}

	dst, err := os.Create("./data/input.txt")
	if err != nil {
		gErr("creating file", c)
		return
	}
	defer dst.Close()

	src, err := file.Open()
	if err != nil {
		gErr("opening file", c)
		return
	}
	defer src.Close()

	_, err = io.Copy(dst, src)
	if err != nil {
		gErr("copying file", c)
		return
	}

	// run the script
	cmd := runFn([]string{"sh", "./main.sh", "start"})
	if cmd != "200" {
		gErr("running script", c)
		return
	}

	spinner := "<div class='spinner w-100'><img class='mx-a' src='bars.svg' alt='loading' /></div>"
	c.Write([]byte(spinner))
	return
}

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
	r.GET("/kill/:type", func(ctx *fasthttp.RequestCtx) {
		ctx.SetContentType("text/plain")
		ctx.SetStatusCode(fasthttp.StatusOK)

		killType := ctx.UserValue("type").(string)

		switch killType {
		case "system":
			cmd := runFn([]string{"shutdown", "now"})
			if cmd != "200" {
				ctx.SetStatusCode(fasthttp.StatusInternalServerError)
				gErr("Couldn't Shutdown: "+cmd, ctx)
				return
			}
			// no confirmation sent if shutdown works

		case "parent":
			cmd := runFn([]string{"sh", "./main.sh", "stop"})
			if cmd != "200" {
				ctx.SetStatusCode(fasthttp.StatusInternalServerError)
				gErr("Child will be orphaned: "+cmd, ctx)
				return
			}
			ctx.Write([]byte("Server killed"))
			// send confirmation before exiting
			os.Exit(0)

		case "child":
			cmd := runFn([]string{"sh", "./main.sh", "stop"})
			if cmd != "200" {
				ctx.SetStatusCode(fasthttp.StatusInternalServerError)
				gErr("Couldn't Kill Child: "+cmd, ctx)
				return
			}
			ctx.Write([]byte("He was taken from us too soon."))
		}
	})

	r.POST("/plot", handlePlot)

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
