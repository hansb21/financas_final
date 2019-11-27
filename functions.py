from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

def get_sma(symbol, interval, time_period):
    ti = TechIndicators(key='NARUTO', output_format='pandas')
    data, metadata = ti.get_sma(symbol=symbol, interval=interval, time_period=time_period, series_type='close')
    return data, metadata

def plot(sma7, sma21):
    #color = 'r' if (sma7 < 0).all() else 'g'
    plt.plot(sma7, color='g')
    plt.plot(sma21, color='r')
    plt.show()
sma1, smax = get_sma('MSFT', '60min', 7)
sma2, smay = get_sma('MSFT', '60min', 21)
plot(sma1, sma2)