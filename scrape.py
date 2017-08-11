#!/usr/bin/env python
import sys
import argparse
import csv
from pprint import pprint
import requests 
import json   

if __name__ == "__main__":
   json_object = requests.get('http://www.acmoore.com//dealerlocator/index/searchdealer').json()

   dealer_headers=json_object[0].keys()
   dealer_headers.remove('store_hours')
   hours_headers=json_object[0]['store_hours'][0].keys()


   with open('dealer_locator.csv', 'w') as outf:
   	dw = csv.DictWriter(outf, dealer_headers,extrasaction='ignore')
   	dw.writeheader()
   	for row in json_object:
   		dw.writerow(row)

   i=0
   with open('store_hours.csv','w') as outf:
   	dw =csv.DictWriter(outf,hours_headers)
   	dw.writeheader()
   	for row in json_object:
   		for nestrow in json_object[i]['store_hours']:
   			dw.writerow(nestrow)
   		i+=1
