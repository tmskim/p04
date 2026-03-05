import requests
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import matplotlib.dates as mdates

# Configuration
CODE = "005930"
UPDATE_INTERVAL = 1000*60 # ms

# Data storage
times = []
prices = []

def get_price():
    timestamp = int(time.time() * 1000)
    url = f"https://m.stock.naver.com/api/stock/{CODE}/basic?_={timestamp}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Referer': f'https://m.stock.naver.com/item/main.nhn?code={CODE}'
        }
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if 'closePrice' in data:
                return int(data['closePrice'].replace(',', ''))
    except Exception as e:
        print(f"Error fetching price: {e}")
    return None

def update(frame):
    current_time = datetime.now()
    price = get_price()
    
    if price is not None:
        times.append(current_time)
        prices.append(price)
        
        # Keep only the last 500 data points to avoid overcrowding
        if len(times) > 500:
            times.pop(0)
            prices.pop(0)
        
        plt.cla() # Clear axis
        plt.plot(times, prices, label='Price (KRW)', color='blue', marker='o')
        
        # Formatting
        plt.title(f"Samsung Electronics ({CODE}) Real-time Price")
        plt.xlabel("Time")
        plt.ylabel("Price (KRW)")
        plt.grid(True)
        plt.legend(loc='upper left')
        
        # Format X-axis time
        plt.gcf().autofmt_xdate()
        myFmt = mdates.DateFormatter('%H:%M:%S')
        plt.gca().xaxis.set_major_formatter(myFmt)
        
        # Add current price annotation
        plt.text(times[-1], prices[-1], f"{prices[-1]:,} KRW", verticalalignment='bottom')
        
        print(f"[{current_time.strftime('%H:%M:%S')}] Updated Price: {price:,} KRW")

def main():
    print("Starting real-time stock graph...")
    
    # Set up the plot
    fig = plt.figure(figsize=(10, 6))
    
    # Create animation
    ani = FuncAnimation(fig, update, interval=UPDATE_INTERVAL, cache_frame_data=False)
    
    plt.show()

if __name__ == "__main__":
    main()
