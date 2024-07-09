# api_requests.py

import aiohttp
import hmac
import hashlib
import time
import config
import json

async def make_api_request(api_url, method='GET', data=None):
    api_key = config.API_KEY
    secret = config.SECRET
    current_timestamp = str(int(time.time() * 1000))
    
    hmac_obj = hmac.new(secret.encode(), (current_timestamp + api_key).encode(), hashlib.sha256)
    auth_signature = hmac_obj.hexdigest()
    
    headers = {
        'X-Auth-Apikey': api_key,
        'X-Auth-Nonce': current_timestamp,
        'X-Auth-Signature': auth_signature,
        'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as session:
        try:
            if method.upper() == 'GET':
                async with session.get(api_url, headers=headers) as response:
                    response.raise_for_status()
                    return await response.json()
            elif method.upper() == 'POST':
                async with session.post(api_url, headers=headers, json=data) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f"Error response: {e.status} {e.message}")
            if data:
                print(f"Request data: {json.dumps(data, indent=2)}")
            print(f"Response headers: {e.headers}")
            raise
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise

    return None
