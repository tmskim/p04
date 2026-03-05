import requests
from datetime import datetime
import time

def get_samsung_stock_info():
    # Use the mobile integration API (basic endpoint)
    # This returns JSON and is less likely to be cached if we add a timestamp
    code = "005930"
    timestamp = int(time.time() * 1000)
    url = f"https://m.stock.naver.com/api/stock/{code}/basic?_={timestamp}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Referer': f'https://m.stock.naver.com/item/main.nhn?code={code}'
        }
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            print(data)
            if 'closePrice' in data:
                price_str = data['closePrice']
                price = int(price_str.replace(',', ''))
                
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # User requested ONLY price (and time)
                print(f"[{current_time}] Price: {price:,.0f} KRW")
            else:
                 # Fallback for debugging
                 print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Unexpected structure.")
                 pprint.pprint(data)
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Connection failed: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        print("Starting real-time stock check for Samsung Electronics (005930) - Price Only...")
        while True:
            get_samsung_stock_info()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")
