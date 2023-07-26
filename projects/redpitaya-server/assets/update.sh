cd /webapp/
rm -rf server/
sleep 1

if [ ! -d "/webapp/cquicc" ]; then
  git clone https://github.com/plutoniumm/cquicc.git --depth 1
fi
sleep 1

# Get file out
mv cquicc/projects/redpitaya-server server

rm -rf cquicc

mv server/assets/start.sh start.sh
chmod +777 start.sh
mv -f server/assets/update.sh update.sh