#!/usr/bin/env python3

import requests
import time

def parseMarketPages(nbPages):
  for i in range(1, (nbPages + 1)):
    res = requests.get('https://steamcommunity.com/market/search?appid=730#p{}_price_desc'.format(i))
    print(res.status_code, res.url)
    time.sleep(1)

def main():
  print('Script Running!')
  parseMarketPages(3)

if __name__ == '__main__':
  main()
