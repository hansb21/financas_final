from alpha_vantage.techindicators import TechIndicators

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from random import randint

from datetime import date

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

def get_sma(symbol):
    #Gera uma key aleatoria cada vez
    ti = TechIndicators(key=str(randint(99994, 447389428)), output_format='pandas')
    
    data7, metadata = ti.get_sma(symbol=symbol, interval='60min', time_period=7, series_type='close')
    data21, metadata = ti.get_sma(symbol=symbol, interval='60min', time_period=21, series_type='close')
    
    return data7, data21


def plot(acao):
    #color = 'r' if (sma7 < 0).all() else 'g'
    
    figura, eixo = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    sma7, sma21 = get_sma(acao)
    
    eixo.plot(sma7, color='g', alpha=0.75, label='Média Móvel - 7')
    eixo.plot(sma21, color='r', alpha=0.75, label='Média Móvel - 21')
    eixo.set(xlabel='Tempo', ylabel='Preço', title="{} Stocks 60min".format(acao))
    
    #Arruma a data
    eixo.xaxis_date()
    
    #Gira os labels do gráfico para ficar menos poluido
    for label in eixo.get_xticklabels():
            label.set_rotation(20)
    
    #Mostra os labels
    plt.legend()
    
    plt.show()
"""
def analiseMedia(acao):
        Comprar = False
        Vender = False

        sma7, sma21 = get_sma(acao)
        ultimo = len(sma7) - 1
        if sma7.last(offset='60min') > sma21.last(offset='60min'):
                Comprar = True
        elif sma7.last(offset='60min') < sma21.last(offset='60min'):
                Vender = True
        else:
                pass
        return Comprar, Vender
        
        Só uma ideia ainda que preciso pensar, talvez trocar o pandas por json.
        """