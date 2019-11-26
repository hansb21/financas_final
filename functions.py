from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

def get_sma(symbol, interval, time_period):
    ti = TechIndicators(key='NARUTO', output_format='pandas')
    data, metadata = ti.get_sma(symbol=symbol, interval=interval, time_period=time_period, series_type='close')
    return data, metadata

def plot(sma7, sma21, sma3):
    plt.plot(sma7)
    plt.plot(sma21)
    plt.plot(sma3)
    plt.show()
sma1, smax = get_sma('MSFT', 'daily', 7)
sma2, smay = get_sma('MSFT', 'weekly', 21)
sma3, x = get_sma('MSFT', 'monthly', 21)
plot(sma1, sma2, sma3)