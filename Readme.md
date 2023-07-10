# RedPitaya LocalServer

## Run
Note: for linux use `red-nix` and for macos use `red-mac`. The `red` here is a placeholder for either of the two.
```sh
# run on port 1337
./server/red

# specify port
./server/red 4242
```

If specifying a port, make sure it is not already in use. Try to avoid using the following ports anyway:
- 80, 443 (http, https)
- 22 (ssh)

### Customise
To specify which script to run. Change the `main.sh` file. Note, it will allow only 1 instance of the process to run at a time since it forces a custom Process name
```sh
# py, bash
cmd="python3 /path/to/script.py"
cmd="bash /path/to/script.sh"
# bin
cmd="/path/to/script.bin"
# and so on
```

# Development
## Dependencies
You need Go to run build the server. You can install it from [here](https://golang.org/doc/install).

The build arches are:
```sh
# macos m1+
env GOOS=darwin GOARCH=amd64 go build

# redpitaya
env GOOS=linux GOARCH=arm go build
```

**Build**
```sh
# from the dir containing the go.mod file
go build
```

## Structure
The server is structured as follows:
```
.
|-- get.go (GET requests)
|-- post.go (POST requests)
|-- main.go (main)
|-- utils.go (utils)
```