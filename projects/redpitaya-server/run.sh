# https://gist.github.com/asukakenji/f15ba7e588ac42795f421b48b8aede63#platform-values

system=$(uname -s)
if [ "$system" = "Darwin" ]; then
  cd server
  env GOOS=darwin GOARCH=arm64 go build
  cd ..
  ./server/red
else
  # env GOOS=linux GOARCH=arm go build
  chmod +777 ./start
  ./start
fi