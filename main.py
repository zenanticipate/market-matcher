# main.py

import aiohttp
import asyncio
from api_requests import make_api_request
import config
import random
from decimal import Decimal

async def trade_logic(market, settings):
    api_url_with_currency = config.api_urls['getMarket'].format(market)
    xeg_url_with_currency = config.xeg_urls['getMarket'].format(settings['xeg_format'])
    
    while True:
        try:
            #print(f"_________Beginning Market Matching For {market} From Xeggex_________")
            
            autradex_data = await make_api_request(api_url_with_currency)
            xeggex_data = await make_api_request(xeg_url_with_currency)
            # print(f"{autradex_data}")

            if autradex_data and 'asks' in autradex_data and autradex_data['asks']:
                sell_ask = next((ask for ask in autradex_data['asks'] if ask['side'].lower() == 'sell'), None)
                buy_bid = next((ask for ask in autradex_data['bids'] if ask['side'].lower() == 'buy'), None)
                # print(f"{sell_ask}")

                if sell_ask and buy_bid:
                    selling_autx = float(sell_ask['price'])
                    buying_autx = float(buy_bid['price'])
                
    #                print(f"Autradex Selling At: {selling_autx:.{settings['precision']}f}")
    #                print(f"Autradex Buying At: {buying_autx:.{settings['precision']}f}")
                
                    selling_grav = float(xeggex_data['asks'][0]['price'])
                    buying_grav = float(xeggex_data['bids'][0]['price'])
                
                    sell_price_autx = round(selling_grav, settings['rounding'])
                    buy_price_autx = round(buying_grav, settings['rounding'])
                    sell_price_grav = round(selling_autx, settings['rounding'])
                    buy_price_grav = round(buying_autx, settings['rounding'])
                
                    if buy_price_grav != buy_price_autx and buy_price_grav < buy_price_autx:
                        print("Adjusting Markets")
                        random_volume = round(random.uniform(0, settings['volume']['max']) / settings['volume']['divisor'], settings['volume']['precision'])
                        buy_order_data = {
                            'price': f'{buy_price_autx:.{settings["precision"]}f}',
                            'volume': str(random_volume),
                            'side': 'buy',
                            'ord_type': 'limit',
                            'market': market.lower()
                        }
                        print(f"Buy order data: {buy_order_data}")
                        buy_order_response = await make_api_request(config.api_urls['createOrder'], method='POST', data=buy_order_data)
                        if 'error' not in buy_order_response:
                            print(f"Buy Order Created! {market}")
                        else:
                            print(buy_order_response)
                
                    if sell_price_grav != sell_price_autx and sell_price_grav > sell_price_autx:
                        print("Adjusting Markets")
                        random_volume = round(random.uniform(0, settings['volume']['max']) / settings['volume']['divisor'], settings['volume']['precision'])
                        sell_order_data = {
                            'price': f'{sell_price_autx:.{settings["precision"]}f}',
                            'volume': str(random_volume),
                            'side': 'sell',
                            'ord_type': 'limit',
                            'market': market.lower()
                        }
                        print(f"Sell order data: {sell_order_data}")
                        sell_order_response = await make_api_request(config.api_urls['createOrder'], method='POST', data=sell_order_data)
                        if 'error' not in sell_order_response:
                            print(f"Sell Order Created! {market}")
                        else:
                            print(sell_order_response)
        
            await asyncio.sleep(settings['loop_time'])

        except aiohttp.ClientResponseError as e:
            print(f"Received 422 Unprocessable Entity error for {market}. Continuing loop...")
            await asyncio.sleep(300)
        except Exception as e:
            print(f"Unexpected error occurred: {str(e)}")
            print(f"Stopping the {market} market for 5 mins due to unexpected error.0.2")
            await asyncio.sleep(300)

# Run the trade logic for each market sequentially
async def main():
    tasks = []
    for market, settings in config.markets.items():
        task = asyncio.create_task(trade_logic(market, settings))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
