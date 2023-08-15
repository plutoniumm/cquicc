package main

import (
	"io"
	"io/ioutil"
	"log"
	"os"
	"os/exec"

	"github.com/fasthttp/router"
	"github.com/valyala/fasthttp"
)

func gErr(err string) []byte {
	err = "<div class='errCont'>Error: " + err + "</div>"
	return []byte(err)
}

func handlePlot(c *fasthttp.RequestCtx) {
	// get ready to exit anytime
	c.SetContentType("text/plain")
	c.SetStatusCode(fasthttp.StatusOK)

	file, err := c.FormFile("file")
	if err != nil {
		c.Write(gErr("extracting file from form"))
		return
	}

	dst, err := os.Create("./data/input.txt")
	if err != nil {
		c.Write(gErr("creating file"))
		return
	}
	defer dst.Close()

	src, err := file.Open()
	if err != nil {
		c.Write(gErr("opening file"))
		return
	}
	defer src.Close()

	_, err = io.Copy(dst, src)
	if err != nil {
		c.Write(gErr("copying file"))
		return
	}

	cmd := exec.Command("sh", "./main.sh")
	_, err = cmd.CombinedOutput()
	if err != nil {
		c.Write(gErr("running script"))
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
