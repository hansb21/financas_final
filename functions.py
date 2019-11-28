from alpha_vantage.techindicators import TechIndicators

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from random import randint

from datetime import date
from DataFile import *

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

def get_sma(symbol):
    #Gera uma key aleatoria cada vez
    ti = TechIndicators(key=str(randint(99994, 447389428)), output_format='pandas')
    
    data7, metadata = ti.get_sma(symbol=symbol, interval='60min', time_period=7, series_type='close')
    data21, metadata = ti.get_sma(symbol=symbol, interval='60min', time_period=21, series_type='close')
    
    return data7, data21


def plot(acao, nome):
    figura, eixo = plt.subplots()
    plt.subplots_adjust(bottom=0.2)

    sma7, sma21 = get_sma(acao)
    opcao, cor, ultimo = analiseMedia(acao, nome)
    eixo.plot(sma7, color='#9a5cad', alpha=0.75, label='Média Móvel - 7')
    eixo.plot(sma21, color='#00FFFF', alpha=0.75, label='Média Móvel - 21')
    
    eixo.axhline(y=ultimo, xmin=0.0, xmax=1.0, color=cor, label=opcao)

    eixo.set(xlabel='Tempo', ylabel='Preço', title="{} Stocks 60min".format(nome))
    
    #Arruma a data
    eixo.xaxis_date()
    
    #Gira os labels do gráfico para ficar menos poluido
    for label in eixo.get_xticklabels():
            label.set_rotation(20)
    
    #Mostra os labels
    plt.legend()
    
    plt.show()

def analiseMedia(acao, nome):
        Opcao = ''
        Cor = ''
        dG = DataFile(nome, acao)
        sma7 = dG.getData(7)
        sma21 = dG.getData(21)
        label, sma7 = exportLastDataPlot(sma7,'SMA')
        label, sma21 = exportLastDataPlot(sma21, 'SMA')
        if sma7[-1] < sma21[-1]:
                opcao = 'Comprar'
                cor = 'green'
        elif sma7[-1] > sma21[-1]:
                opcao = 'Vender'
                cor = 'red'
        else:
                opcao = 'Incerteza, não faça nada'
                cor = 'grey'
        return opcao, cor, sma21[-1]
        
