import matplotlib.pyplot as plt
import numpy as np
from estima import estimar_componentes_frequencia

NUM_COLUNAS_SUBPLOT = 1

def plota_sinais(frequencia_amostragem, sinais, duracao):
    quantidade_amostras = int(frequencia_amostragem * (duracao/1000)) # Fs = amostras/seg, quando multiplico pela duração em seg eu fico só com amostras
    quantidade_sinais = len(sinais)

    plt.figure(figsize=(12, 8))
    plt.suptitle(f"Primeiros {duracao} ms de Cada Sinal", fontsize=16)

    for i in range(quantidade_sinais):
        plt.subplot(quantidade_sinais, NUM_COLUNAS_SUBPLOT, i + 1)
        x = np.arange(quantidade_amostras) 
        y = sinais[i, :quantidade_amostras]
        plt.plot(x, y)
        plt.title(f'Sinal {i+1}') # O +1 é pra aparecer o número bonitinho no plot sem começar de 0
        plt.xlabel('Amostras')
        plt.ylabel('Amplitude')
        plt.grid(True)

    plt.tight_layout()
    plt.show()


def plota_FFT(frequencia_amostragem, sinais):
    amostras = sinais.shape[1] # o N do somatório. Como o arquivo txt tá com o mesmo número de amostras para os 5 sinais,
                                                    #dá pra usar isso já que é uma matriz 2D com 5 linhas e 800 colunas
    quantidade_sinais = len(sinais)
    freq = np.fft.fftfreq(amostras, 1/frequencia_amostragem) # Retorna as frequências associadas aos índices da FFT (usa no eixo X)

    plt.figure(figsize=(12, 8))
    plt.suptitle(f"Plot da DFT dos {quantidade_sinais} sinais", fontsize=16)

    for i in range(quantidade_sinais):
        fft = np.fft.fft(sinais[i])  # FFT
        amplitude = np.abs(fft) / amostras  # Espectro de amplitude normalizado
        metade_amostras = amostras // 2  # usamos só a metade positiva
        plt.subplot(quantidade_sinais, NUM_COLUNAS_SUBPLOT, i + 1)
        plt.plot(freq[:metade_amostras], amplitude[:metade_amostras])  #freq positivas (depois da metade das amostras ele pega a freq negativa que é redundante)
                                                                        #É aquela parada dos complexos conjugados a partir da metade das amostras                                                                                    
        plt.title(f'Sinal {i+1} - Espectro de Amplitude')
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Amplitude')
        plt.grid(True)
    
    plt.tight_layout()
    estimar_componentes_frequencia(frequencia_amostragem, sinais)
    plt.show()