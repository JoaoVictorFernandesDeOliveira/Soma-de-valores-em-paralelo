import time
from multiprocessing import Pool

def ler_arquivo(caminho):
    """Lê os números do ficheiro e retorna uma lista de inteiros."""
    with open(caminho, 'r') as f:
        # Lê cada linha, converte para inteiro e ignora linhas vazias
        return [int(linha.strip()) for linha in f if linha.strip()]

def soma_parcial(sublista):
    """Função auxiliar para somar uma parte da lista."""
    return sum(sublista)

def executar_paralelo(dados, num_processos):
    """Divide os dados e executa a soma em paralelo."""
    tamanho_parte = len(dados) // num_processos
    partes = [dados[i:i + tamanho_parte] for i in range(0, len(dados), tamanho_parte)]
    
    inicio = time.time()
    with Pool(processes=num_processos) as pool:
        resultados = pool.map(soma_parcial, partes)
        soma_total = sum(resultados)
    fim = time.time()
    
    return soma_total, fim - inicio

if __name__ == '__main__':
    arquivo = 'numero2.txt'
    
    print(f"Lendo dados do arquivo {arquivo}...")
    dados = ler_arquivo(arquivo)
    print(f"Total de elementos: {len(dados)}\n")

    # --- Solução Serial ---
    print("Executando Soma Serial...")
    inicio_serial = time.time()
    soma_s = sum(dados)
    fim_serial = time.time()
    tempo_serial = fim_serial - inicio_serial
    print(f"Resultado Serial: {soma_s} | Tempo: {tempo_serial:.6f}s\n")

    # --- Solução Paralela (Experimentos) ---
    print(f"{'Processos':<12} | {'Resultado':<12} | {'Tempo (s)':<12}")
    print("-" * 40)
    
    threads_para_testar = [2, 4, 8, 12]
    for n in threads_para_testar:
        res, tempo = executar_paralelo(dados, n)
        print(f"{n:<12} | {res:<12} | {tempo:.6f}s")