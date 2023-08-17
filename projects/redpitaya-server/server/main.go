package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"time"

	"github.com/fasthttp/router"
	"github.com/valyala/fasthttp"
)

func csp(ctx *fasthttp.RequestCtx) *fasthttp.RequestCtx {
	cspValue := "default-src 'self'; script-src-elem 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:;object-src 'none';"
	ctx.Response.Header.Set("Content-Security-Policy", cspValue)
	return ctx
}

func handlePlot(c *fasthttp.RequestCtx) {
	fmt.Println("Got plot request")
	c.SetContentType("text/plain")
	c.SetStatusCode(fasthttp.StatusOK)

	file, err := c.FormFile("file")
	if err != nil {
		gErr("extracting file from form", c)
		return
	}

	fmt.Println("Got file: " + file.Filename)

	date := strconv.FormatInt(time.Now().Unix(), 10)
	date = "./data/input-" + date + ".csv"
	dst, err := os.Create(date)
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

	fmt.Println("Got & wrote file")

	form, err := c.MultipartForm()
	if err != nil {
		gErr("extracting form", c)
		return
	}
	N := form.Value["n"]
	if len(N) == 0 {
		gErr("extracting N", c)
		return
	}

	fmt.Println("Got N: " + N[0])

	// run the script
	cmd := runFn([]string{"sh", "./main.sh", "start", N[0]})
	if cmd != "200" {
		gErr("running script", c)
		return
	}

	c.Write([]byte(""))
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
		csp(ctx).Write(data)
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
			csp(ctx).Write([]byte("He was taken from us too soon."))
		}
		return
	})
	r.POST("/plot", handlePlot)

	log.Println("Server listening on port " + PORT)
	log.Fatal(fasthttp.ListenAndServe(":"+PORT, r.Handler))
}
