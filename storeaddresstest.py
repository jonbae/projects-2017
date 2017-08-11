#!/usr/bin/env python
import sys
import argparse
import csv
from pprint import pprint


parser = argparse.ArgumentParser()
parser.add_argument('--storeid')    

if __name__ == "__main__":
    args = parser.parse_args()
    if args.storeid:
        stores = [line for line in csv.DictReader(open('dealer_locator.csv'))]
        # code goes here
        # print the store address and fix any broken info
        # address must inclue the full address (1 & 2 (if available)) and the city/state.
        # also show if the store status...eg. is open or opening soon
        foundStore=False
        for store in stores:
            if store['dealerlocator_id']==args.storeid:
                print store['address1'], store['address2']
                print store['city'], store['state']
                print store['dealer_store_status']
                foundStore=True
        if foundStore==False:
            print 'store not found'        



    else:
        print parser.print_help()
        parser.exit(2)


