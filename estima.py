import numpy as np

def estimar_componentes_frequencia(frequencia_amostragem, sinais):
    quantidade_sinais = len(sinais)
    amostras = sinais.shape[1]
    freq = np.fft.fftfreq(amostras, 1/frequencia_amostragem)
    metade_amostras = amostras // 2  # frequências positivas

    resultados = []

    for i in range(quantidade_sinais):
        fft = np.fft.fft(sinais[i])
        amplitude = np.abs(fft) / amostras
        freq_pos = freq[:metade_amostras]
        amp_pos = amplitude[:metade_amostras]

        amp_sem_dc = amp_pos[1:] #Tiro o primeiro índice (Componente DC no índice 0)
        indices_ordenados = np.argsort(amp_sem_dc) #Ordeno os índices em função da amplitude 
        maiores_indices_sem_dc = indices_ordenados[-2:] #Pega os dois maiores picos (os dois últimos valores do vetor ordenado são os dois maiores)
        idx_maiores = maiores_indices_sem_dc + 1 #Faço a correção dos índices já que eu tinha tirado a componente DC

        #Pego as duas frequencias e ordeno para que f1 < f2
        f1 = freq_pos[idx_maiores[0]]
        f2 = freq_pos[idx_maiores[1]]
        f1, f2 = sorted([f1, f2])

        resultado = f"Sinal {i+1}: componentes de frequencia estimadas = {f1:.2f} Hz e {f2:.2f} Hz"
        print(resultado)
        resultados.append(resultado)

    # Cria um arquivo txt com as componentes
    with open("componentes.txt", "w") as arquivo:
        arquivo.write("\n".join(resultados))
