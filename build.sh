echo "\033[0;34mUpdating build...\033[0m"
rm -rf build
mkdir build
mkdir build/assets

echo "\033[0;34mCreating Go Binary\033[0m"
cd server
env GOOS=darwin GOARCH=arm64 go build -o ../build/red-mac
env GOOS=linux GOARCH=arm go build -o ../build/red-nix
cd ../

echo "\033[0;34mCopying Assets...\033[0m"
cp -r assets/* build/assets/
cp index.html build/
cp main.sh build/
cp demo.sh build/

rm release.zip
echo "\033[0;34mGenerating Archive...\033[0m"
zip -r release.zip build