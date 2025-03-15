import numpy as np
import plotly.graph_objs as go

"""A plotly é uma biblioteca que plota os mais diversos gráficos. O módulo plotly.graph_objects possui uma hierarquia de classes e 'graph_objects' refere-se a um nível dessas classes."""

def pontos_grafico_com_erros(gotas, blue_data, red_data, green_data, erro_blue, erro_red, erro_green):

    """ Essa função coloca os pontos no gráfico com as suas respectivas barras de erro, nesse caso, apenas vertical pois o número de gotas é constante. O scatter é utilizado em gráficos de dispersão e são utilizados para determinar a relação entre duas variáveis numéricas"""
    trace2 = go.Scatter(x=gotas, y=red_data, mode='markers', marker=dict(color="red"), name='Vermelho',
                        error_y=dict(type='data', array=erro_red, visible=True, color="red"))
    trace3 = go.Scatter(x=gotas, y=green_data, mode='markers', marker=dict(color="green"), name='Verde',
                        error_y=dict(type='data', array=erro_green, visible=True, color="green"))
    trace1 = go.Scatter(x=gotas, y=blue_data, mode='markers', marker=dict(color="blue"), name='Azul',
                        error_y=dict(type='data', array=erro_blue, visible=True, color="blue"))

    return trace1, trace2, trace3

def plotar_grafico(media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas):

    trace1, trace2, trace3 = pontos_grafico_com_erros(n_de_gotas, media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde)

    layout = go.Layout(
    xaxis=dict(
        title='Número de gotas de leite',
        showline=True,  # Mostra a linha do eixo
        linecolor='black',  # Define a cor da linha do eixo
        rangemode='tozero',
        autorange=True,
        ticks="outside"
    ),
    yaxis=dict(
        title='Intensidade Média (u.a.)',
        showline=True,
        linecolor='black',
        ticks="outside"
    ),
    plot_bgcolor='white',  
    paper_bgcolor='white',
    margin=dict(l=30, r=20, t=10, b=10),
    legend=dict(
        yanchor="top",
        xanchor="right",
    )
)



    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

    fig.show()
