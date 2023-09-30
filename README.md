# esp-sss

## Useful commands
Put file onto board
```
sudo ampy -p /dev/ttyUSB0 put <file>
``` 

Connect to esp32 board with `screen` command
```
sudo screen /dev/ttyUSB0 115200,cs8,ixon
```

Launch mosquitto server on `localhost` with topic `sss`
```
mosquitto_sub -v -h localhost -t sss
```