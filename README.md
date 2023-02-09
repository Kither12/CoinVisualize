# CoinVisualize
 Coin chart for the terminal as command line ultil<br>

### Requirements
-Python3

### Usage
 ```bash
 # install
pip install requirement.txt
# run default
python CoinPlot.py
# run with options
python CoinPlot.py -f ETH -d hour
```
### Options

```bash
bitcoin-chart-cli --help
  Usage: index [options]


  Options:

  -V, --version                         output the version number
  -d, --days <n>                        number of days the chart will go back
  --hours <n>                           number of hours the chart will go back
  --mins <n>                            number of minutes the chart will go back
  -w, --width <n>                       max terminal chart width
  -h, --height <n>                      max terminal chart height
  --max <n>                             max y-axis value
  --min <n>                             min y-axis value
  --min-range <n>                       min range between min and max y-axis value
  -c, --coin <string>                   specify the coin e.g. ETH (default: "BTC")
  --currency <string>                   specify the trading pair currency (default: "USD")
  -l, --list                            list all available coins
  -t, --toplist <n>                     list of top n coins
  --disable-legend                      disable legend text
  -ti, --technical-indicator <type...>  add a technical indicator: RSI SMA BB EMA MACD
  -h, --help                            display help for command
```
