import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import QuadraticModel, LinearModel

modelo = QuadraticModel()

modelo2 = LinearModel()

parametros = modelo.make_params()

parametros2 = modelo2.make_params()

dados_x = [0.10, 0.13, 0.17, 0.20, 0.23, 0.27, 0.30, 0.33, 0.37, 0.40, 0.43, 0.47, 0.50]
dados_y = [ 1.65, 2.14, 2.59, 2.94, 3.28, 3.44, 3.63, 
    3.83, 3.96, 4.53, 4.80, 5.50, 6.10]

erro_velocidade = (((1.5 * (1/30)) + (0.5640999999999998 * 0.005)) / 0.5543999999999999**2 )
erro_tempo = 1/30

print(erro_velocidade)

resultado_fit = modelo2.fit(dados_y, parametros2, x=dados_x)

SIGMA = 3
erro = resultado_fit.eval_uncertainty(sigma=SIGMA)
print(erro)

#plt.plot(dados_x, dados_y, '.', label='Pontos coletados')
plt.errorbar(dados_x, dados_y, xerr=erro_tempo, yerr=erro_velocidade, fmt='.', capsize=4, label="Dados coletados")
plt.plot(dados_x, resultado_fit.best_fit, '-', label='Melhor ajuste encontrado', color="red")
plt.fill_between(
    dados_x,
    resultado_fit.best_fit - erro,
    resultado_fit.best_fit + erro,
    color="#ABABAB",
    label=rf"Banda de confiança considerando {SIGMA}$\sigma$",
)

plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.title("Velocidade da Bola Vermelha em Queda Livre")

print(resultado_fit.fit_report())

plt.legend()
plt.savefig("grafico.png", dpi=300)
plt.show()