cd /webapp/
rm -rf /webapp/cquicc/ /webapp/server/
git clone https://github.com/plutoniumm/cquicc.git --depth 1
sleep 1

# Get file out
mv /webapp/cquicc/projects/redpitaya-server /webapp/server

# copy start script
cp /webapp/server/start.sh /webapp/start.sh