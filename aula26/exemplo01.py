# importar pandas, numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'http://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# obter os dados
try:
    print("Obtendo os dados...")

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando as variavéis
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # agrupar por cisp
    df_veiculos = df_veiculos.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()
    print(df_veiculos)
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f"Erro ao obter os dados: {e}")
    exit()

# Calculando Correlação entre roubos e recuperações de veículos
    
try:
    correlacao = np.corrcoef(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])[0, 1]

    print(f'Correlação entre roubos e recuperações de veículos: {correlacao}')

    # Criar um gráfico de dispersão
    plt.scatter(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])
    plt.title('Correlação entre roubos e recuperações de veículos')
    plt.xlabel('Roubos de veículos')
    plt.ylabel('Recuperações de veículos')
    plt.show()

except Exception as e:

    print(f"Erro ao calcular a correlação: {e}")
    exit()