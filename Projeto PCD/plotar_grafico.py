import numpy as np
import plotly.graph_objs as go

"""A plotly é uma biblioteca que plota os mais diversos gráficos. O módulo plotly.graph_objects possui uma hierarquia de classes e 'graph_objects' refere-se a um nível dessas classes."""


def calculo_de_ajuste(gotas, blue, red, green):

    print(gotas)

    print(blue)

    """ Essa função faz o cálculo do ajuste dos dados para que resultem em uma curva de grau 2. O polifit faz ajuste polinomial por meio dos  mínimos quadrados."""
    blue_fit = np.polyfit(gotas, blue, 2)
    red_fit = np.polyfit(gotas, red, 2)
    green_fit = np.polyfit(gotas, green, 2)

    """Código de criação das linhas de ajuste. O polyval vai avaliar um polinômio em valores específicos"""
    blue_fit_line = np.polyval(blue_fit, gotas)
    red_fit_line = np.polyval(red_fit, gotas)
    green_fit_line = np.polyval(green_fit, gotas)

    return blue_fit_line, red_fit_line, green_fit_line

def pontos_grafico_com_erros(gotas, blue_data, red_data, green_data, erro_blue, erro_red, erro_green):

#  """ Essa função coloca os pontos no gráfico com as suas respectivas barras de erro, nesse caso, apenas vertical pois o número de gotas é constante. O scatter é utilizado em gráficos de dispersão e são utilizados para determinar a relação entre duas variáveis numéricas"""
    trace1 = go.Scatter(x=gotas, y=blue_data, mode='markers', marker= dict(color = "Black"), name='Y1',
                        error_y=dict(type='data', array=erro_blue, visible=True, color = "black"))
    trace2 = go.Scatter(x=gotas, y=red_data, mode='markers', marker= dict(color = "Black"), name='Y2', 
                        error_y=dict(type='data', array=erro_red, visible=True, color = "black"))
    trace3 = go.Scatter(x=gotas, y=green_data, mode='markers', marker= dict(color = "Black"),name='Y3', error_y=dict(type='data',       array=erro_green, visible=True, color = "black"))

    return trace1, trace2, trace3

    
def curvas_grafico_com_ajuste(gotas, linha_azul, linha_vermelha, linha_verde):
    
    """ Essa função faz a linha já ajustada e incrementa com os pontos no gráfico com as suas respectivas barras de erro. """

    trace4 = go.Scatter(x=gotas, y= linha_azul, mode='lines', name='Blue', line = dict(color = "Blue"))
    trace5 = go.Scatter(x=gotas, y= linha_vermelha, mode='lines', name='Red', line = dict(color = "Red"))
    trace6 = go.Scatter(x=gotas, y= linha_verde, mode='lines', name='Green', line = dict(color = "Green"))

    return trace4, trace5, trace6 

def plotar_grafico(media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas):

    linha_azul, linha_vermelha, linha_verde =  calculo_de_ajuste(n_de_gotas, media_Azul, media_Vermelho, media_Verde)

    trace1, trace2, trace3 = pontos_grafico_com_erros(n_de_gotas, media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde)

    trace4, trace5, trace6 = curvas_grafico_com_ajuste(n_de_gotas, linha_azul, linha_vermelha, linha_verde)


    # Exibir o gráfico

    layout = go.Layout(title='Gráfico Linear Interativo com Ajuste',
                    xaxis=dict(title='Gotas'),
                    yaxis=dict(title='Médias'))

    fig = go.Figure(data=(trace1, trace2, trace3, trace4, trace5, trace6), layout=layout)

    fig.show()








