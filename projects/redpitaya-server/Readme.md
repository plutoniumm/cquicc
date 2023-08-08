# RedPitaya LocalServer
## Run
Runs on all versions of python3.5+. Program

- Run: `sh ./start.sh`
- Open: `http://10.21.16.75:1337/`

## First time setup
```bash
# Get repo
git clone https://github.com/plutoniumm/cquicc.git

# Extract Files
mv cquicc/projects/redpitaya-server server
mv server/start.sh start.sh
mv -f server/update.sh update.sh

# Cleanup
rm -rf cquicc
```

## Update
```bash
./update.sh
```

### Setup
- Install `request_toolbelt`
- rm -rf certifi from `site-packages`/`dist-packages`
- Run server.


```redmine/text
I have attached the files for the Wireframes of how convergence UI should look

Implementation
- Attach File -> Start Plot -> Iterates
- Each second plot is rerendered with iterations & new plot
- Kill Plot -> Stop Iterating

This might take some time to implement since HTTP Keep-Alive has a default timeout of 5s and it's not easy to enforce a longer timeout. Despite all attempts to avoid it, it seems this will have to be done with WebSockets



```