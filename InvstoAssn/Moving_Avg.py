import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from Testing.sources.data_fetch import get_data_from_sql



 
df = get_data_from_sql()
print(df.head())
df['SMA50'] = df['close'].rolling(window=50).mean()
df['SMA200'] = df['close'].rolling(window=200).mean()

print(df[['SMA50','SMA200']].head(210))


df['Signal'] = 0 
df['Signal'][50:] = np.where(df['SMA50'][50:] > df['SMA200'][50:], 1, 0) 
df['Position'] = df['Signal'].diff() 
# Print the strategy 
print("DataFrame with Trading Signals:") 
print(df[['datetime', 'close', 'SMA50', 'SMA200', 'Signal', 'Position']].tail(10)) 
# Plotting the Moving Averages and Signals 
plt.figure(figsize=(14,7)) 
plt.plot(df['datetime'], df['close'], label='Close Price', color='blue') 
plt.plot(df['datetime'], df['SMA50'], label='50-Day SMA', color='green') 
plt.plot(df['datetime'], df['SMA200'], label='200-Day SMA', color='red') 
plt.plot(df[df['Position'] == 1]['datetime'], df['SMA50'][df['Position'] == 1], '^', markersize=10, color='m', lw=0, label='Buy Signal') 
plt.plot(df[df['Position'] == -1]['datetime'], df['SMA50'][df['Position'] == -1], 'v', markersize=10, color='k', lw=0, label='Sell Signal') 
plt.title('Moving Average Crossover Strategy') 
plt.xlabel('Date') 
plt.ylabel('Price') 
plt.legend() 
plt.grid() 
plt.show()
