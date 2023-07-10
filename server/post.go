package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"time"

	"github.com/valyala/fasthttp"
)

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
