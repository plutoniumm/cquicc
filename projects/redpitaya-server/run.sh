cd server
# https://gist.github.com/asukakenji/f15ba7e588ac42795f421b48b8aede63#platform-values
env GOOS=darwin GOARCH=arm64 go build
cd ..
./server/red