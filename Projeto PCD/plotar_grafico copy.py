import numpy as np
import plotly.graph_objs as go

"""A plotly é uma biblioteca que plota os mais diversos gráficos. O módulo plotly.graph_objects possui uma hierarquia de classes e 'graph_objects' refere-se a um nível dessas classes."""

# Dados
gotas_data = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
blue_data = [0, -0.7199999999999989, -1.9399999999999977, -2.9599999999999937, -3.519999999999996, -4.8799999999999955, -6.140000000000001, -7.459999999999994, -8.799999999999997, -11.079999999999998, -12.179999999999993, -13.439999999999998, -15.579999999999998, -15.739999999999995, -17.89999999999999, -19.89999999999999, -21.419999999999987, -22.83999999999999, -24.83999999999999, -26.39999999999999, -27.559999999999988]
red_data = [0, -0.519999999999996, -0.7999999999999972, -1.559999999999988, -2.019999999999996, -2.8799999999999955, -3.4199999999999875, -4.359999999999999, -4.97999999999999, -5.61999999999999, -7.11999999999999, -7.459999999999994, -9.379999999999995, -10.199999999999989, -10.959999999999994, -11.659999999999997, -12.639999999999986, -13.219999999999999, -14.0, -14.899999999999991, -15.739999999999995]
green_data = [0, -0.8799999999999955, -1.9399999999999977, -2.5999999999999943, -2.6199999999999903, -4.019999999999996, -4.8799999999999955, -6.259999999999991, -7.559999999999988, -8.399999999999991, -9.1799999999993, -11.14, -12.47999999999999, -13.079999999999998, -14.659999999999997, -15.959999999999994, -16.69999999999999, -18.379999999999995, -19.86, -20.5, -22.61999999999999]
y_error_blue = [0.12121830534626525, 0.21119678414372928, 0.17981850260068066, 0.06857142857142859, 0.10629185850136154, 0.2696028825619529, 0.2217002941093296, 0.21382808276648746, 0.34404555939406556, 0.16718558672374617, 0.28868456056776587, 0.3837090734674181, 0.2563320550555073, 0.37363083384538814, 0.25753937681885647, 0.3672845752052125, 0.3633068079938686, 0.31887557550408485, 0.3975024066157413, 0.44629998148038025, 0.46066500290119633]  # Erros verticais para Y1
y_error_red = [0.17009001218442524, 0.0857142857142857, 0.12202375145178637, 0.2658217908482973, 0.26840420325794206, 0.12828539611796363, 0.28030595529069396, 0.12108354343095484, 0.20919671437697682, 0.34787987605388354, 0.3257644071711822, 0.34286904741237484, 0.23974476223769353, 0.14182484166846698, 0.20356015006350708, 0.25492696032793544, 0.2029174960521679, 0.32103150077491754, 0.3973791691591704, 0.29704668773423065, 0.3693237062523878] # Erros verticais para Y2
y_error_green = [0.2568410927767897, 0.13999999999999987, 0.13997084244475302, 0.1829687159609754, 0.30188523295708075, 0.12135291760911608, 0.2321329668222811, 0.21990721605592975, 0.2170112383058083, 0.28515659858100023, 0.38878145584397833, 0.28428212488760557, 0.2811202081469267, 0.2224354985617362, 0.22649052780121612, 0.3684385142401785, 0.4019950248448357, 0.267658021225837, 0.43390961157873453, 0.46560033662937544, 0.3575882936494177]  # Erros verticais para Y3


def calculo_de_ajuste(gotas, blue, red, green):

    """ Essa função faz o cálculo do ajuste dos dados para que resultem em uma curva de grau 2. O polifit faz ajuste polinomial por meio dos  mínimos quadrados."""
    blue_fit = np.polyfit(gotas, blue, 2)
    red_fit = np.polyfit(gotas, red, 2)
    green_fit = np.polyfit(gotas, green, 2)

    """Código de criação das linhas de ajuste. O polyval vai avaliar um polinômio em valores específicos"""
    blue_fit_line = np.polyval(blue_fit, gotas)
    red_fit_line = np.polyval(red_fit, gotas)
    green_fit_line = np.polyval(green_fit, gotas)

    return blue_fit_line, red_fit_line, green_fit_line

def pontos_grafico_com_erros(gotas):
    
    """ Essa função coloca os pontos no gráfico com as suas respectivas barras de erro, nesse caso, apenas vertical pois o número de gotas é constante. O scatter é utilizado em gráficos de dispersão e são utilizados para determinar a relação entre duas variáveis numéricas"""

    trace1 = go.Scatter(x=gotas_data, y=blue_data, mode='markers', marker= dict(color = "Black"), name='Y1',
                        error_y=dict(type='data', array=y_error_blue, visible=True, color = "black"))
    trace2 = go.Scatter(x=gotas_data, y=red_data, mode='markers', marker= dict(color = "Black"), name='Y2', 
                        error_y=dict(type='data', array=y_error_red, visible=True, color = "black"))
    trace3 = go.Scatter(x=gotas_data, y=green_data, mode='markers', marker= dict(color = "Black"),name='Y3',        error_y=dict(type='data', array=y_error_green, visible=True, color = "black"))

def curvas_grafico_com_ajuste(linha_azul, linha_vermelha, linha_verde)
    
    """ Essa função faz a linha já ajustada e incrementa com os pontos no gráfico com as suas respectivas barras de erro. """

    trace4 = go.Scatter(x=gotas_data, y= linha_azul, mode='lines', name='Blue', line = dict(color = "Blue"))
    trace5 = go.Scatter(x=gotas_data, y= linha_vermelha, mode='lines', name='Red', line = dict(color = "Red"))
    trace6 = go.Scatter(x=gotas_data, y= linha_verde, mode='lines', name='Green', line = dict(color = "Green"))




    layout = go.Layout(title='Gráfico Linear Interativo com Ajuste',
                    xaxis=dict(title='Gotas'),
                    yaxis=dict(title='Médias'))

fig = go.Figure(data=(trace1, trace2, trace3, trace4, trace5, trace6), layout=layout)

# Exibir o gráfico
fig.show()




