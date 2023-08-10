# RedPitaya LocalServer
## Run
Add whatever scripts/programs need to be run to `runner.sh`. It will be called everytime `/plot` is POST to. And every second send.txt will be sent

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