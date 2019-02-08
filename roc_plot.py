import matplotlib.pyplot as plt

taxaVerdadeiroPositivo = 0.80
taxaFalsoPositivo = 0.53

plt.plot(taxaFalsoPositivo, taxaVerdadeiroPositivo, 'o')

plt.plot([0.1, 1],[0.1, 1], 'red')

plt.text(0.1, 0.95, 'Céu ROC')
plt.text(0.85, 0.1, 'Inferno ROC')

plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Gráfico ROC do Modelo')

plt.xticks([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1])
plt.yticks([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1])

plt.grid()

plt.show()