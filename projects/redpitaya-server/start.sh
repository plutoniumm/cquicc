# Start SCPI server
systemctl enable redpitaya_scpi

# Start web server
cd /webapp/server
python3 ./index.py 10.21.16.751