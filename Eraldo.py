import requests
from random import getrandbits
from bs4 import BeautifulSoup as bs
url = 'http://www.eraldo.it/yeezy-350-v2-raffle-registration/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()

        r = session.get(url)
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {

        'your-name'        : '', #Enter first name
        'your-surname'     : '', #Enter last name
        'your-email'       : email, #DONT CHANGE
        'mobile'       : '', #ENTER PHONE NUMBER
        'instagram'     : '', #Enter instagram account (Be sure to follow eraldo on there)
        'facebook' : '', #Enter your facebook profile URL (Be sure to like eraldo on there)
        'submit'       : 'btn btn-primary', #DONT CHANGE
        'uksize'       : '7.5', #Edit for what size you want
        'country'      : '', #Enter Country
        'city'         : '', #Enter City
        'acceptance-462' : '1', #DONT CHANGE
        'submit'       : 'Send' #DONT CHANGE

        }

        resp = session.post(url, data=payload, headers=headers)
        print('Raffle has been entered {}/{} times.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
