import polars as pl  
from datetime import datetime


ENDERECO_DADOS = './../dados/'

try:
    inicio = datetime.now()

    # Polars 0:00:00.990826
    df_scan = (
        pl.scan_parquet(ENDERECO_DADOS + 'AuxilioEmergencial.parquet')
        .select(['NOME MUNICÍPIO', 'VALOR BENEFÍCIO'])
        .with_columns([
            pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
        ])
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR BENEFÍCIO').sum())
        .sort('VALOR BENEFÍCIO', descending=True)
    )

    df_auxilio_emergencial = df_scan.collect()
    print(df_auxilio_emergencial.head())

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet {e}')