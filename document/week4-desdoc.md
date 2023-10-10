---
topic: "Redpitaya Design Document"
author: "Manav Seksaria"
from: "MCQuICC, IIT Madras"
---

===

## Context & Scope
The Webserver is a web application that allows users to plot the current state of Convergence of spin states

## Goals
User will be able to
- Refresh Manually or Automatically
- Set Refresh Rate (if Auto Refresh)
- Enter `N` (for NxN)
- Kill Process and/or Server

The system will be able to
- AutoRefresh if enabled at a provided rate
- Get $N\times N$ from `spingrid.csv` and plot a heatmap
- Get $k$ rows of $(x,y)$ from `convergence.csv` and plot a loss plot

Parameters
```ts
type RefreshRate = number // sec
// default: 1
type N = number // NxN
// default: 50
type AutoRefresh = boolean
// default: true
```

## Design
Architecture & Data Flow for the application, treating frontend & backend separately

### Architecture
When refresh is triggered (manually or else), the client sends a GET to the server and renders the+++data as images
```mermaid
graph RL
  subgraph Client
  direction RL
    CA[User] -->|Refresh| CB["Call GET /data/*"]
    CB --> |Render| CA
  end
```
The server listens for GET requests and responds with the requested data from the `data/` directory
```mermaid
graph RL
  subgraph Server
  direction RL
    S["Handle GET /data/*"] -->|Read| SB["data/{file}.csv"]
    SB -->|Send| S
  end
```

### Directory Structure
The following is the directory structure on the board. The program will serve `*.csv` data from the `/webapp/server/data/` dir to the client
```
/webapp/server/
  ├── assets/
  │  ├─ *.css, *.js
  │  ├─ vendors/ (dependencies)
  │  ├── bars.svg (loading spinner)
  │  └── update.sh (update server)
  ├─ data/ (MAIN DATA)
  │  ├── sendgrid.csv
  │  └── convergence.csv
  ├─ demo.py
  ├─ index.html
  ├─ main.sh (runner script)
  └── server/
      ├── *.go files
      └── red (executable)
```


### APIs
The following are the APIs that the server will expose to the client
/===
===

```yaml
# Ok is when Request is 200
# Err is when 40x or 50x
GET:
"/" : "index.html",
"/data/{file}" : {
  // get file from server
  ok: "data/{file}.csv",
  err: 404
},
"/assets/{file}" : {
  // get file from server
  ok: "(server) /assets/{file}",
  err: 404
},
"/kill/parent": {
  // kill parent webserver
  ok: null,
  err: 500, text() /* forwarded */
},
"/kill/child": {
  // kill all child processes
  ok: "He was taken from us too soon",
  err: "Couldn't kill proc:"+text()
},
"*": 404
# Note:
# all server err will be forwarded
# to the client as text as is
POST:
"/plot":{
  ok:(file saved: input-{timestamp}.txt),
  err: 500, text() /* forwarded */
}
```

### Sample User Flow
1. User visits the page (AutoRefresh `off`)
```mermaid
sequenceDiagram
  participant U as User
  participant C as Client
  participant S as Server
  U->>C: Visit Page
  C->>S: GET /data/*
  S->>C: data/{file}.csv
  C->>C: Render Images
```
+++
2. User enables AutoRefresh
```mermaid
sequenceDiagram
  participant U as User
  participant C as Client
  participant S as Server
  U->>C: Enable AutoRefresh
  C->>S: GET /data/*
  S->>C: data/{file}.csv
  C->>C: Render Images
  C->>U: Show waiting 1s
  C->>S: GET /data/*
  S->>C: data/{file}.csv
  C->>C: Render Images
  C->>C: And so on...
```

### Interface
The user must have the following interactions

<style>
  .btn{
    padding: 10px;
    border-radius: 5px;
    background: #aaf;
    margin: 5px;
  }
  .disp{
    background: #ccc;
    padding: 2px 5px;
    border-radius: 2px;
  }
  input[type="number"]{
    border-radius: 2px;
    border: 1px solid #888;
  }
</style>

- Refresh Button <button class="btn">Refresh<button>

This button calls refresh regardless of AutoRefresh's state.
if AutoRefresh is on, we will force a refresh and reset the timer
if AutoRefresh is off, we will just refresh once

- AutoRefresh Toggle: toggles AutoRefresh on/off along with the refresh rate

<div class="disp f j-bw">
  Rate(s): <input type="number" value="1">
  AutoRefresh: <input type="checkbox" checked>
</div>

- N Input
This input allows the user to set the value of N

<div class="disp">
  <span> N: <input type="number" value="50"></span>
</div>

- Kill Buttons: allow the user to kill the server and/or the process

<div class="disp">
  <button class="btn">Kill Server</button>
  <button class="btn">Kill Process</button>
</div>

/===
===

## Rendered Images

### Heatmap
The following is an example of a 50x50 heatmap which should be expected from data and updated every second
![Heatmap](https://i.imgur.com/TSw8D3P.png)

The data for this is expected to be of the form
```csv
1,0,0...N...0,1
0,0,1...N...1,0
.
. N rows
.
0,1,0...N...0,0
```

This will be a matrix of $N\times N$ with binary values and we expect it to keep updating in the background (with unknown frequency). We will keep fetching and displaying whatever comes & show it to the user at the set frequency. We will rerender the data whether or not it has changed on the given frequency.

### Loss Plot
The following is an example of a loss plot which should be expected from data and updated every second
+++

![Loss Plot](https://i.imgur.com/2jx0oOj.png)

The data for this is expected to be of the form with k rows of $(x,y)$
```csv
0,10.0
1,9.25
2,8.94
3,8.7
4,8.5
...
```

This data is passed on to an external library `Chart.js` and we let them render it since it happens efficiently.

## Usage
```sh
# run on port 1234
./server/red 1234
# unspecified port is ok
./server/red # runs on 1337
```

**Run** If specifying a port, make sure it is not already in use. Try to avoid using the following ports anyway:
- 80, 443 (http, https)
- 22 (ssh)
- 5000 (possibly scpi)

/===
===

**Customise**
To specify which script to run. Change the `main.sh` file. Note, it will allow only 1 instance of the process to run at a time since it forces a custom Process name (`ICING`)
```sh
# py
cmd="python3 /path/to/script.py"
# bash
cmd="bash /path/to/script.sh"
# bin
cmd="/path/to/script"
# and so on
```

Each time a script is run it does the following:

(START)
- Receive an input and save it as `input-{timestamp}.txt`
- Run the script with received $N$ as input
- Loop outputs to `convergence.csv` & `spingrid.csv`

(STOP)
- Rename `convergence.csv` to `convergence-{timestamp}.csv`
- Rename `spingrid.csv` to `spingrid-{timestamp}.csv`

NO FILE IS EVER DELETED. Please watch out for memory usage.

The format for `{timestamp}` is Unix Epoch `int32` (seconds since 1970). For example,

`August 22, 2023. 13:04:00` is `1692689640.`

**Update**
To find out your config, run `go env GOOS GOARCH`. Some common architectures are

<style>
  td{padding:1px 12px 1px 0;}
</style>
| Device | GOOS | GOARCH |
| --- | --- | --- |
| Apple Silicon | darwin | arm64 |
| Redpitaya | linux | arm |
| Linux | linux | amd64 |
| Windows | windows | amd64 |
+++

**Build**
```sh
# Example config for Redpitaya
env GOOS=linux GOARCH=arm go build

# or Linux intel
env GOOS=linux GOARCH=amd64 go build
```

All of the `Go` dependencies are maintained in `go.mod` and `go.sum` files. To update them run
```sh
go get -u
```

**Caveats**
- **Implemented**: Do not `staticServe` the `/data` directory. Go will try to cache the files and will not update them. Instead, use the `data` endpoint to read the files each time manually.
- **Not Implemented**: The server can close only the process it starts since its name is hardcoded. If you want to kill a process that was started manually, you will have to kill it manually as well OR find a way to set the process name to `ICING` (or whatever is set in `main.sh`)

/===