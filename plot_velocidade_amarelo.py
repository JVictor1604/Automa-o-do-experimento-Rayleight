import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import QuadraticModel, LinearModel

modelo = QuadraticModel()

modelo2 = LinearModel()

parametros = modelo.make_params()

parametros2 = modelo2.make_params()

dados_x = [0.00, 0.03, 0.07, 0.10, 0.13, 0.17, 0.20, 0.23, 0.27, 0.30, 0.33, 0.37, 0.40, 0.43, 0.47, 0.50, 0.53]
dados_y = [0.00, 0.51, 0.85, 1.27, 1.59, 1.99, 2.43, 2.84, 3.16, 3.29, 3.63, 3.79, 3.72, 3.98, 4.02, 3.91, 4.34]

erro_tempo = 1/30
erro_velocidade = ((1.5 * (1/30)) + (0.5640999999999998 * 0.005)) / (0.5640999999999998**2) 

print(f" o erro associado a velocidade é {erro_velocidade}")

resultado_fit = modelo2.fit(dados_y, parametros2, x=dados_x)

SIGMA = 3
erro = resultado_fit.eval_uncertainty(sigma=SIGMA)
print(erro)

#plt.plot(dados_x, dados_y, '.', label='Pontos coletados')
plt.errorbar(dados_x, dados_y, xerr=erro_tempo, yerr=erro_velocidade, fmt='.', capsize=4, label="Dados coletados")
plt.plot(dados_x, resultado_fit.best_fit, '-', label='Melhor ajuste encontrado')
plt.fill_between(
    dados_x,
    resultado_fit.best_fit - erro,
    resultado_fit.best_fit + erro,
    color="#ABABAB",
    label=rf"Banda de confiança considerando {SIGMA}$\sigma$",
)

plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.title("Velocidade da Bola Amarela em Queda Livre")

print(resultado_fit.fit_report())

plt.legend()
plt.savefig("grafico.png", dpi=300)
plt.show()