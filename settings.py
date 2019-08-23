import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")
FIXER_KEY = os.environ.get("FIXER_KEY")
SYMBOL_KEY = ['GBP', 'JPY', 'EUR', 'USD', 'KZT', 'AUD', 'CAD', 'INR', 'RUB', 'TRY', 'VES', 'ZWL', 'MXN', 'ARS', 'AOA', 'BRL', 'ZAR', 'LRD', 'LYD', 'LSL', 'NAD', 'SZL', 'TND', 'MMK', 'SEK', 'PKR', 'NPR', 'BTN', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'BDT', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BSD', 'BMD', 'BWP', 'BYN', 'BZD', 'XAF', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GGP', 'GHS', 'GIP', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
              'HUF', 'IDR', 'ILS', 'IQD', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MGA', 'MKD', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RWF', 'SAR', 'SBD', 'SCR', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'YER', 'ZMW', 'CUP', 'KPW', 'SYP', 'SDG', 'IRR', 'BYR', 'GMD']

NA_CURR = ['USD', 'MXN' 'CAD', 'NIO', 'JMD', 'HTG', 'HNL', 'GTQ',
           'DOP', 'CUP', 'CRC', 'KYD', 'BMD', 'BZD', 'BBD', 'BSD', 'AWG']
SA_CURR = ['ARS', 'BOB', 'BRL', 'CLP', 'COP',
           'FKP', 'GYD', 'PYG', 'PEN', 'SRD', 'UYU', 'VES', 'USD', 'EUR', 'GBP']
EUR_CURR = ['EUR', 'GBP', 'ALL', 'AMD', 'AZN', 'BYN', 'BAM', 'BGN', 'HRK', 'CZK', 'DKK', 'GEL',
            'HUF', 'ISK', 'CHF', 'MDL', 'MKD', 'NOK', 'PLN', 'RON', 'RUB', 'RSD', 'SEK', 'TRY', 'UAH']
AF_CURR = ['NGN', 'KES', 'BWP', 'EGP', 'RWF', 'GHS', 'MWK',
           'MUR', 'MAD', 'ZAR', 'TZS', 'UGX', 'ZMW', 'NAD', 'DZD', 'AOA', 'BIF', 'CVE', 'KMF', 'CDF', 'XAF', 'DJF', 'ERN', 'SZL', 'ETB', 'GMD', 'GNF', 'LSL', 'LRD', 'LYD', 'MGA', 'MZN', 'SCR', 'SLL', 'SOS', 'SDG']
S_AS_CURR = ['AFN', 'BDT', 'BTN', 'INR', 'MVR', 'NPR', 'PKR', 'LKR']
E_AS_CURR = ['CNY', 'JPY', 'MNT', 'KPW', 'KRW', '']
SE_AS_CURR = []
ME_CURR = []
