import random
from emoji_dict import *
from settings import FIXER_KEY, SYMBOL_KEY, C_AS_CURR, S_AS_CURR
import requests
import sqlite3


def get_price_info(selected):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    placeholder = '?'
    placeholders = ', '.join(placeholder for _ in selected)
    query = 'SELECT currency, price from prices WHERE currency IN (%s)' % placeholders

    with_data = c.execute(query, selected).fetchall()

    return with_data


def compose_scheduled_tweet(selected):
    if len(selected) == 12:
        print('inside compose', selected)
    to_be_tweeted = '1 #satoshi =        '

    for i in range(len(selected)):
        curr = selected[i][0]
        price = selected[i][1]
        emoji = emoji_dict[curr]
        price = '{0:.5f}'.format(price)

        if i == 0:
            to_be_tweeted += str(price) + ' $' + curr + ' ' + emoji + '\n'

        elif i % 2 != 0:
            to_be_tweeted += str(price) + ' $' + curr + ' ' + emoji

        else:
            to_be_tweeted += '   ' + \
                str(price) + ' $' + curr + ' ' + emoji + '\n'

    to_be_tweeted += '                       #Bitcoin'
    return to_be_tweeted


def scheduled_tweet(currencies, region_name=None):
    _global = ['USD', 'EUR']
    max_num = 13 if len(currencies) > 13 else len(currencies)

    # Select currencies at random
    selected = random.sample(currencies, max_num)

    # ensure there is 13 currencies
    if region_name == 'S_AS':
        selected += _global
        iterator = random.randint(0, len(C_AS_CURR)-1)
        while len(selected) < 13:
            selected.append(C_AS_CURR[iterator])
            iterator = (iterator + 1) % len(C_AS_CURR)
    elif region_name in ['C_AS', 'E_AS']:
        selected += _global
        iterator = random.randint(0, len(S_AS_CURR)-1)
        while len(selected) < 13:
            selected.append(S_AS_CURR[iterator])
            iterator = (iterator + 1) % len(S_AS_CURR)

    # retrieve data from database
    select_with_data = get_price_info(selected)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data)

    return tweet


def fetch_price_data():
    rates_data = {}
    fixer_url = 'http://data.fixer.io/api/latest?access_key=' + \
        FIXER_KEY + '&base=EUR&symbols=BTC,EUR, SDG, CUP, KPW, SYP, IRR'
    url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'
    try:
            # retrieve data from coinbase and fixer apis
        cb_json_data = requests.get(url).json()['data']['rates']
        fixer_json_data = requests.get(fixer_url).json()['rates']

        # from cb data, store data there are emojis for in rates_data, convert to sats
        for key in emoji_dict:
            if key in cb_json_data:
                price_sats = float(cb_json_data[key])
                rates_data[key] = str(price_sats / 100000000)

        # for fixer data, get conversion based on EUR/BTC pair, multiply fixer currency with conversion rate
        EUR = fixer_json_data['EUR']
        BTC = fixer_json_data['BTC']
        bitprice = (EUR / BTC)
        fixer_json_data.update((x, y*bitprice / 100000000)
                               for x, y in fixer_json_data.items())
        for key in fixer_json_data:
            if not key == 'BTC' and not key == 'EUR':
                rates_data[key] = str(fixer_json_data[key])

        for key in rates_data:
            rates_data[key] = float(rates_data[key])

        return rates_data

    except:
        print('fixer or coinbase request failed')


def regional_tweet(currencies):
    # select 13 currencies from the region
    random_select = random.sample(currencies, 13)

    # get price data from database then shuffle the order
    select_with_data = get_price_info(random_select)
    random.shuffle(select_with_data)

    # compose tweet
    tweet = compose_scheduled_tweet(select_with_data)

    return tweet


def tweet_weakest():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    query = 'SELECT currency,price FROM prices ORDER BY price DESC LIMIT 13'
    data = c.execute(query).fetchall()

    tweet = compose_scheduled_tweet(data)

    return tweet