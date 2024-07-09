# config.py

API_KEY = 'autradex_api_key'
SECRET = 'autradex_secret'

api_urls = {
    'getMarket': 'https://wallet.autradex.systems/api/v2/peatio/public/markets/{}/order-book',
    'createOrder': 'https://wallet.autradex.systems/api/v2/peatio/market/orders',
}

xeg_urls = {
    'getMarket': 'https://api.xeggex.com/api/v2/market/getorderbookbysymbol/{}',
}

markets = {
    'btcusdt': {
        'loop_time': 1 * 60,
        'rounding': 2,
        'xeg_format': 'btc_usdt',
        'volume': {
            'max': 20,
            'divisor': 100000000,
            'precision': 8
        },
        'precision': 8
    },
    'ltcusdt': {
        'loop_time': 1 * 60,
        'rounding': 2,
        'xeg_format': 'ltc_usdt',
        'volume': {
            'max': 20,
            'divisor': 1000000,
            'precision': 6
        },
        'precision': 6
    },
    'dogeusdt': {
        'loop_time': 1.1 * 60,
        'rounding': 5,
        'xeg_format': 'doge_usdt',
        'volume': {
            'max': 20,
            'divisor': 1,
            'precision': 1
        },
        'precision': 5
    },
    'ethusdt': {
        'loop_time': 1.1 * 60,
        'rounding': 5,
        'xeg_format': 'eth_usdt',
        'volume': {
            'max': 20,
            'divisor': 100000,
            'precision': 5
        },
        'precision': 5
    },
    'dingousdt': {
        'loop_time': 1.1 * 60,
        'rounding': 8,
        'xeg_format': 'dingo_usdt',
        'volume': {
            'max': 200,
            'divisor': 1,
            'precision': 1
        },
        'precision': 8
    },
    'dogebtc': {
        'loop_time': 1.2 * 60,
        'rounding': 9,
        'xeg_format': 'doge_btc',
        'volume': {
            'max': 20,
            'divisor': 1,
            'precision': 1
        },
        'precision': 9
    },
    'ltcbtc': {
        'loop_time': 1.3,
        'rounding': 6,
        'xeg_format': 'ltc_btc',
        'volume': {
            'max': 10,
            'divisor': 10000,
            'precision': 4
        },
        'precision': 6
    },
    'dgbbtc': {
        'loop_time': 1.4 * 60,
        'rounding': 9,
        'xeg_format': 'dgb_btc',
        'volume': {
            'max': 20,
            'divisor': 1,
            'precision': 1
        },
        'precision': 9
    },
    'pndltc': {
        'loop_time': 1.5 * 60,
        'rounding': 9,
        'xeg_format': 'pnd_ltc',
        'volume': {
            'max': 200,
            'divisor': 1,
            'precision': 1
        },
        'precision': 9
    },
    'btczltc': {
        'loop_time': 1.55 * 60,
        'rounding': 9,
        'xeg_format': 'btcz_ltc',
        'volume': {
            'max': 200,
            'divisor': 1,
            'precision': 1
        },
        'precision': 9
    },
    'pnddoge': {
        'loop_time': 1.6 * 60,
        'rounding': 6,
        'xeg_format': 'pnd_doge',
        'volume': {
            'max': 200,
            'divisor': 1,
            'precision': 1
        },
        'precision': 6
    }
}



#markets = {
#    'btcusdt': {'rounding': 2, 'loop_time': 0.1 * 60, 'volume': {'max': 20, 'divisor': 100000000, 'precision': 8}, 'xeg_format': 'btc_usdt'},
#    'dogeusdt': {'rounding': 5, 'loop_time': 2.0 * 60, 'volume': {'max': 20, 'divisor': 1, 'precision': 1}, 'xeg_format': 'doge_usdt'},
#    'dogebtc': {'rounding': 9, 'loop_time': 0.1 * 60, 'volume': {'max': 20, 'divisor': 1, 'precision': 1}, 'xeg_format': 'doge_btc'},
#    'ltcbtc': {'rounding': 6, 'loop_time': 0.1 * 60, 'volume': {'max': 10, 'divisor': 1000, 'precision': 3}, 'xeg_format': 'ltc_btc'},
#    'dgbbtc': {'rounding': 9, 'loop_time': 2.8 * 60, 'volume': {'max': 25, 'divisor': 1, 'precision': 1}, 'xeg_format': 'dgb_btc'},
#}
