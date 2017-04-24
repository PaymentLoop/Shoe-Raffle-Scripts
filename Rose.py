import requests
import time
from random import getrandbits
from bs4 import BeautifulSoup
url = 'http://18montrose.us11.list-manage.com/subscribe/post?u=6b0a46846ebdd9e62be420915&id=6c8b7c85ee'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
                    'MERGE0'  : email, #Dont change
                    'MERGE1'  : '', #Enter first name
                    'MERGE2'  : '', #Enter last name
                    'MERGE9'  : '', #Enter your instagram @, Be following Montrose also.
                    'MERGE10' : '', #Enter your twitter @, Be following Montrose also.
                    'MERGE7'  : 'UK 9', #Enter shoe size in the format 'UK 11, UK 11.5, UK 12, etc.'
                    'MERGE8'  : '', #Enter your country, for USA enter 'United States of America'
                    'submit'  : 'Enter the draw' #Dont change


        }
        time.sleep (30)
        resp = session.post(url, data=payload, headers=headers)
        print('Raffle has been entered {}/{} times.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
