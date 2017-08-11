#!/usr/bin/env python
import sys
import argparse
import csv
from pprint import pprint


parser = argparse.ArgumentParser()
parser.add_argument('--storeid')
parser.add_argument('--isopen', action='store_true', help='test if the store is open now')
if __name__ == "__main__":
    args = parser.parse_args()
    if args.storeid:
        stores = [line for line in csv.DictReader(open('dealer_locator.csv'))]
        hours = [line for line in csv.DictReader(open('store_hours.csv'))]
         # code goes here
         # using the storeid, display hours
         # if args.isopen is true check if the store is open now.
        foundStore=False
        for store in stores: 
            if store['dealerlocator_id']==args.storeid:
                foundStore=True
                for hour in hours:
                    if store['address1']==hour['address1']:
                        print 'Monday: '+hour['mon_start']+'-'+hour['mon_end']
                        print 'Tuesday: '+hour['tue_start']+'-'+hour['tue_end']
                        print 'Wednesday: '+hour['wed_start']+'-'+hour['wed_end']
                        print 'Thursday: '+hour['thus_start']+'-'+hour['thus_end']
                        print 'Friday: '+hour['fri_start']+'-'+hour['fri_end']
                        if args.isopen:
                            print '\n'
                            print 'Monday: '+hour['mon_start_openclose']
                            print 'Tuesday: '+hour['tue_start_openclose']
                            print 'Wednesday: '+hour['wed_start_openclose']
                            print 'Thursday: '+hour['thu_start_openclose']
                            print 'Friday: '+hour['fri_start_openclose']
                            print '\n'   
        if foundStore==False:
            print 'store not found'                  

    else:
        print parser.print_help()
        parser.exit(2)


