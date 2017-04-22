import requests
from random import getrandbits
url = 'https://www.boutique1.com/competition/yeezy'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit):
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'competition_name': '', # put your first name
            'surname': '', # put your last name
            'competition_email': email, # DO NOT CHANGE
            'mobile': '', # put your number without spaces, like 1234567890
            'shoe_size': '' # put ONE shoe size, like 10, 9.5, etc.
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(200)
