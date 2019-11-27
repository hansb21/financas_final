from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

def get_sma(symbol):
    ti = TechIndicators(key='SAKEHDUIAJSIJAISK', output_format='pandas')
    data7, metadata = ti.get_sma(symbol=symbol, interval='60min', time_period=7, series_type='close')
    data21, metadata = ti.get_sma(symbol=symbol, interval='60min', time_period=21, series_type='close')
    return data7, data21

def plot(acao):
    #color = 'r' if (sma7 < 0).all() else 'g'

    sma7, sma21 = get_sma(acao)
    
    figura, eixo = plt.subplots()
    
    plt.subplots_adjust(bottom=0.2)
    plt.plot(sma7, color='g', alpha=0.75, label='Média Móvel - 7')
    plt.plot(sma21, color='r', alpha=0.75, label='Média Móvel - 21')
    eixo.set(xlabel='Tempo', ylabel='Preço', title="{} Stocks 60min".format(acao))
    
    #Arruma a data
    eixo.xaxis_date()
    
    #Gira os labels do gráfico para ficar menos poluido
    for label in eixo.get_xticklabels():
            label.set_rotation(20)
    
    #Mostra os labels
    plt.legend()
    
    plt.show()
