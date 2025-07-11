import numpy as np
from plota import plota_sinais, plota_FFT
from estima import estimar_componentes_frequencia

sinais = np.loadtxt('signals.txt')
FREQUENCIA_AMOSTRAGEM = 8000
DURACAO_MS = 50

plota_sinais(FREQUENCIA_AMOSTRAGEM, sinais, DURACAO_MS)

plota_FFT(FREQUENCIA_AMOSTRAGEM, sinais) # Gera um arquivo txt com as componentes

#Plota_FFT já chama essa função!!! (tá aqui pra teste)
#estimar_componentes_frequencia(FREQUENCIA_AMOSTRAGEM, sinais)