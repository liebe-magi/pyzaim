import requests
from requests_oauthlib import OAuth1Session

request_token_url = 'https://api.zaim.net/v2/auth/request'
authorize_url = 'https://auth.zaim.net/users/auth'
access_token_url = 'https://api.zaim.net/v2/auth/access'
callback_uri = 'https://www.zaim.net/'

def get_access_token():
    consumer_key = input('Please input consumer key : ')
    consumer_secret = input('Please input consumer secret : ')
    print('\n')

    auth = OAuth1Session(client_key=consumer_key,
                         client_secret=consumer_secret,
                         callback_uri=callback_uri)
    
    auth.fetch_request_token(request_token_url)

    # Redirect user to zaim for authorization
    authorization_url = auth.authorization_url(authorize_url)
    print('Please go here and authorize : ', authorization_url)
    
    oauth_verifier = input('Please input oauth verifier : ')
    access_token_res = auth.fetch_access_token(url=access_token_url,
                                               verifier=oauth_verifier)
    access_token = access_token_res.get('oauth_token')
    access_token_secret = access_token_res.get('oauth_token_secret')
    
    print('\n')
    print('access token : {}'.format(access_token))
    print('access token secret : {}'.format(access_token_secret))
    print('oauth verifier : {}'.format(oauth_verifier))

class ZaimApi:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, oauth_verifier):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

        self.verify_url = 'https://api.zaim.net/v2/home/user/verify'
        self.money_url = 'https://api.zaim.net/v2/home/money'
        self.create_payment_url = 'https://api.zaim.net/v2/home/money/payment'
        self.create_income_url = 'https://api.zaim.net/v2/home/money/income'
        self.create_transfer_url = 'https://api.zaim.net/v2/home/money/transfer'
        self.category_url = 'https://api.zaim.net/v2/home/category'
        self.genre_url = 'https://api.zaim.net/v2/home/genre'
        self.account_url = 'https://api.zaim.net/v2/home/account'

        self.auth = OAuth1Session(client_key=self.consumer_key,
                                  client_secret=self.consumer_secret,
                                  resource_owner_key=access_token,
                                  resource_owner_secret=access_token_secret,
                                  callback_uri=callback_uri,
                                  verifier=oauth_verifier)
    
    def verify(self):
        return self.auth.get(self.verify_url).json()
    
    def get_money_data(self):
        return self.auth.get(self.money_url).json()
    
    def insert_payment(self, date, category_id, genre_id, amount, account_id, comment, name, place):
        pass
    
    def get_account(self):
        return self.auth.get(self.account_url).json()
    
    def get_category(self):
        return self.auth.get(self.category_url).json()
    
    def get_genre(self):
        return self.auth.get(self.genre_url).json()