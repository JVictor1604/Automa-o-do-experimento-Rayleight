import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import QuadraticModel, LinearModel

modelo = QuadraticModel()

modelo2 = LinearModel()

parametros = modelo.make_params()

parametros2 = modelo2.make_params()

dados_x = [0.00, 0.03, 0.07, 0.10, 0.13, 0.17, 0.20, 0.23, 0.27, 0.30, 0.33, 0.37, 0.40, 0.43, 0.47, 0.50, 0.53]
dados_y = [1.43,1.30,1.17,1.03,0.91,0.78,0.65,0.54,0.44,0.33,0.25,0.17,0.11,0.07,0.03,0.01,0.00]

erro_posicao = 0.05
erro_tempo = 1/30

resultado_fit = modelo.fit(dados_y, parametros, x=dados_x)

SIGMA = 3
erro = resultado_fit.eval_uncertainty(sigma=SIGMA)
print(erro)

#plt.plot(dados_x, dados_y, '.', label='Pontos coletados')
plt.errorbar(dados_x, dados_y, xerr=erro_tempo, yerr=erro_posicao, fmt='.', capsize=3, label="Dados coletados")
plt.plot(dados_x, resultado_fit.best_fit, '-', label='Melhor ajuste encontrado')
plt.fill_between(
    dados_x,
    resultado_fit.best_fit - erro,
    resultado_fit.best_fit + erro,
    color="#ABABAB",
    label=rf"Banda de confiança considerando {SIGMA}$\sigma$",
)

plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.title("Posição da Bola Amarela em Queda Livre")

plt.legend()
plt.savefig("grafico.png", dpi=300)
plt.show()