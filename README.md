# CoinVisualize
 Coin chart for the terminal as command line ultil<br>

### Requirements
- Python3

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
usage: CoinPlot.py [-h] [-f FSYM [FSYM ...]] [-d {minute,hour,day}] {list} ...

positional arguments:
   list                List all available coin
options:
  -h, --help                     Show this help message and exit
  -f FSYM [FSYM ...]             The crypto currency symbol (default: BTC)
  -d {minute,hour,day}           Time unit. Can be minute, hour or day (default: minute)
```
# Examples
![](https://i.imgur.com/a/5p8trji)
