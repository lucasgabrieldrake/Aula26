import polars as pl  
from datetime import datetime 
import os

ENDERECO_DADOS = './../dados/'

try:
    inicio = datetime.now()
    print('Carregando...')

    df_auxilio_emergencial = None
    lista_arquivos = []

    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
        
    for nome in lista_arquivos:
        print(f'Processando o arquivo {nome}')

        # Pandas
        # df = pd.read_csv(ENDERECO_DADOS + nome, sep=';', encoding='iso-8859-1')

        # Polars 0:02:42.375248
        df = pl.read_csv(ENDERECO_DADOS + nome, separator=';', encoding='iso-8859-1')

        if df_auxilio_emergencial is None:
            df_auxilio_emergencial = df
        else:
            df_auxilio_emergencial = pl.concat([df_auxilio_emergencial, df])

        del df

        print(f'Arquivo {nome} processado com sucesso!')
        print(df_auxilio_emergencial.head())

    print(df_auxilio_emergencial.columns)
    print(df_auxilio_emergencial.shape)

    df_auxilio_emergencial = df_auxilio_emergencial.with_columns(
        pl.col('VALOR BENEFÍCIO').str.replace(',', '.').cast(pl.Float64))

    print('Iniciando a gravação do arquivo parquet...')
    df_auxilio_emergencial.write_parquet(ENDERECO_DADOS + 'AuxilioEmergencial.parquet')

    print('\nGravação do arquivo parquet concluída com sucesso!')
    print(df_auxilio_emergencial.head())
    print(df_auxilio_emergencial.shape)

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')
except Exception as e:
    print(f'Erro ao obter os dados {e}')