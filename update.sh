echo "\033[0;34mUpdating Red...\033[0m"
wget https://github.com/plutoniumm/red/releases/latest/download/release.zip 2>&1 | grep -i "failed\|error"
rm -rf server
unzip -q release.zip
rm -rf __MACOSX release.zip

mv build server
echo "\033[0;34mUpdated Red!\033[0m"
ls ./server