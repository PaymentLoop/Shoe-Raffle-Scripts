import requests
import time
from random import getrandbits
from bs4 import BeautifulSoup
url = 'http://dtlr.us5.list-manage.com/subscribe/post?u=e63d3ec47059b6abdf6a36c8f&id=759208b064'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'MERGE0'          : email, #DO NOT EDIT
            'MERGE1'          : '', #Enter your first name
            'MERGE2'          : '', #Enter your last name
            'MERGE3[month]'   : '', #Enter your month of birth in MM format
            'MERGE3[day]'     : '', #Enter your date of birth in DD format
            'MERGE6'          : '', #Enter your shoe size
            'MERGE5'          : '', #Enter your phone number
            'MERGE4[addr1]'   : '', #Enter your street address
            'MERGE4[city]'    : '', #Enter your city
            'MERGE4[state]'   : '', #Enter your state/province/region
            'MERGE4[zip]'     : '', #Enter your postal/zip code
            'MERGE4[country]' : '', #Enter your country. Use 'USA' instead of United states or US.
            'group[149][1]'   : '1', #Dont change
            'subscribe'       : 'Register' #Dont change


        }
        time.sleep(30)
        resp = session.post(url, data=payload, headers=headers)
        print('Raffle has been entered {}/{} times.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
