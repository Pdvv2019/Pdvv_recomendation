import pandas as pd
tabela_carregada = pd.read_hdf('similaridade_cosseno.h5', key='df')
linhas, colunas = tabela_carregada.shape

def recomendar_jogos(nome_jogo, tabela, n=6):
    if nome_jogo not in tabela.columns:
        print(f"O jogo '{nome_jogo}' não foi encontrado.")
        return []

    # Obter o índice do jogo
    indice_jogo = tabela.columns.get_loc(nome_jogo)

    # Obter as similaridades do jogo
    similaridades = tabela.iloc[indice_jogo]

    # Ordenar os jogos pela similaridade
    jogos_recomendados = similaridades.sort_values(ascending=False).head(n + 1)

    # Remover o próprio jogo da lista de recomendações
    jogos_recomendados = jogos_recomendados.drop(nome_jogo)

    return jogos_recomendados.index.tolist()

# Digitar o nome do jogo
jogo_input = input("Digite o nome do jogo: ")

# Chamar a função de recomendação
recomendados = recomendar_jogos(jogo_input, tabela_carregada)

# Exibir resultados
print("Jogos recomendados:")
for jogo in recomendados:
    print(jogo)