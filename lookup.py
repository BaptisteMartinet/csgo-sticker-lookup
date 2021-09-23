#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import threading

def parseMarketPage(pageId):
  print('- Parsing MaketPage {}'.format(pageId))
  url = 'https://steamcommunity.com/market/search?appid=730#p{}_price_desc'.format(pageId)
  res = requests.get(url)
  if (res.status_code != 200):
    print(res.status_code)
    return
  soup = BeautifulSoup(res.text, 'html.parser')
  itemsList = soup.find('div', attrs={ 'id': 'searchResultsRows'})
  items = itemsList.find_all('a', attrs={ 'class': 'market_listing_row_link' })
  for item in items:
    itemURL = item.get('href')
    print(itemURL)
  print('Finished parsing MarketPage')

def parseMarketPages(nbPages):
  threadPool = []
  for i in range(1, (nbPages + 1)):
    threadPool.append(threading.Thread(target=parseMarketPage, args=(i,)))
  for thread in threadPool:
    thread.start()
  for thread in threadPool:
    thread.join()

def main():
  print('Script Running!')
  parseMarketPages(200)
  print('Script Finished!')

if __name__ == '__main__':
  main()
