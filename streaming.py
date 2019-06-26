import tweepy as tp
from settings import *
from emoji_dict import *
import pickle


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY

# import current price data from file
pickle_in = open('price_data.txt', 'rb')
price_data = pickle.load(pickle_in)


# override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tp.StreamListener):

    def on_status(self, status):
        # filter
        split = status.text.split()
        currency = [i.upper() for i in split if len(i) == 3]
        for item in currency:
            if item in price_data:
                self.compose(status, item)

    def compose(self, status, curr):
        larger_baseline = ['JPY', 'INR', 'KRW']

        emoji = emoji_dict[curr]

        sats = float(price_data[curr])
        hundred = sats * 100
        thousand = sats * 1000
        ten_thousand = sats * 10000
        hundred_k = sats * 100000
        million = sats * 1000000
        bitcoin = sats * 100000000

        single_unit = 1 / sats
        hundredths_unit = single_unit / 100
        ten_units = single_unit * 10
        hundred_units = single_unit * 100
        five_hundred_units = single_unit * 500
        thousand_units = single_unit * 1000
        ten_thousand_units = single_unit * 10000
        hundred_thousand_units = single_unit * 100000
        # five_hundred_thousand_units = single_unit * 500000

        #  format numbers

        bitcoin = '{0:,}'.format(round(bitcoin))

        if sats > 1:
            sats = '{0:.2f}'.format(sats)
        else:
            sats = '{0:.5f}'.format(sats)

        if hundred > 1:
            hundred = '{0:.2f}'.format(hundred)
        else:
            hundred = '{0:.5f}'.format(hundred)

        if thousand > 1:
            thousand = '{0:,.2f}'.format(thousand)
        else:
            thousand = '{0:.5f}'.format(thousand)

        if ten_thousand > 1:
            ten_thousand = '{0:,.2f}'.format(ten_thousand)
        else:
            ten_thousand = '{0:.5f}'.format(ten_thousand)

        if hundred_k > 1:
            hundred_k = '{0:,.2f}'.format(hundred_k)
        else:
            hundred_k = '{0:.5f}'.format(hundred_k)

        if million > 1:
            if million > 1000:
                million = '{:,d}'.format(round(million))
            else:
                million = '{0:.2f}'.format(million)
        else:
            million = '{0:.5f}'.format(million)

        # satoshi equivalent to currency
        if single_unit > 1:
            single_unit = '{:,d}'.format(round(single_unit))
        else:
            single_unit = '{0:.2f}'.format(single_unit)

        if ten_units > 100:
            ten_units = '{:,}'.format(round(ten_units))
        else:
            ten_units = '{0:.2f}'.format(ten_units)

        if hundred_units > 100:
            hundred_units = '{:,}'.format(round(hundred_units))
        else:
            hundred_units = '{0:.2f}'.format(hundred_units)

        if thousand_units > 100:
            thousand_units = '{:,}'.format(round(thousand_units))
        else:
            thousand_units = '{0:.2f}'.format(thousand_units)

        if five_hundred_units > 100:
            five_hundred_units = '{:,}'.format(round(five_hundred_units))
        else:
            five_hundred_units = '{0:.2f}'.format(five_hundred_units)

        if ten_thousand_units > 100:
            ten_thousand_units = '{:,}'.format(round(ten_thousand_units))
        else:
            ten_thousand_units = '{0:.2f}'.format(ten_thousand_units)

        if hundred_thousand_units > 100:
            hundred_thousand_units = '{:,}'.format(
                round(hundred_thousand_units))
        else:
            hundred_thousand_units = '{0:.2f}'.format(hundred_thousand_units)

        if hundredths_unit > 1:
            hundredths_unit = '{:,}'.format(round(hundredths_unit))
        else:
            hundredths_unit = '{0:.2f}'.format(hundredths_unit)

            # '\n' + f'100,000 #satoshis = {hundred_k} ${curr}' + \

        if curr in larger_baseline:
            text = f'{emoji} ${curr} to #satoshi conversions:' + '\n' + \
                '\n' + f'   1 {curr} = {single_unit} sats' + \
                '\n' + f'   1,000 {curr} = {thousand_units} sats' + \
                '\n' + f'   10,000 {curr} = {ten_thousand_units} sats' + \
                '\n' + f'   100,000 {curr} = {hundred_thousand_units} sats' + \
                '\n' + '\n' + \
                '\n' + f'   1 sat = {sats} {curr}' + \
                '\n' + f'   100 sats = {hundred} {curr}' + \
                '\n' + f'   1,000 sats = {thousand} {curr}' + \
                '\n' + f'   1,000,000 sats = {million} {curr}' + \
                '\n' + '\n' + \
                f'1 #bitcoin = {bitcoin} {curr} {emoji}'
        else:
            text = f'{emoji} ${curr} to #satoshi conversions:' + '\n' + \
                '\n' + f'   .01 {curr} = {hundredths_unit} sats' + \
                '\n' + f'   1 {curr} = {single_unit} sats' + \
                '\n' + f'   100 {curr} = {hundred_units} sats' + \
                '\n' + f'   1,000 {curr} = {thousand_units} sats' + \
                '\n' + '\n' + \
                '\n' + f'   1 sat = {sats} {curr}' + \
                '\n' + f'   100 sats = {hundred} {curr}' + \
                '\n' + f'   10,000 sats = {ten_thousand} {curr}' + \
                '\n' + f'   1,000,000 sats = {million} {curr}' + \
                '\n' + '\n' + \
                f'1 #bitcoin = {bitcoin} {curr} {emoji}'

        print(text)
        print('length:', len(text))

        self.tweet_it(text, status.id)

    def tweet_it(self, text, reply_id):
        api.update_status(
            status=text, in_reply_to_status_id=reply_id, auto_populate_reply_metadata=True)
        # api.update_status(status,)
        print('reply ID:', reply_id)
        print('tweeted')


auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth=api.auth, listener=myStreamListener)


myStream.filter(track=['@1satoshibot'], is_async=True)
