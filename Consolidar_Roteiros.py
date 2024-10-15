import os
import pandas as pd

# Caminho principal das subpastas
base_path = r'C:\Users\levia\OneDrive - grupojb.log.br\DATABASE PAINEL\BASE - ROTEIROS'
subpastas = ['FOR', 'IMP', 'JUA', 'SLZ', 'SOB', 'THE']

# Lista para armazenar todos os DataFrames
dfs = []

# Loop por cada subpasta
for subpasta in subpastas:
    subpasta_path = os.path.join(base_path, subpasta)
    
    # Loop por cada arquivo CSV na subpasta
    for file in os.listdir(subpasta_path):
        if file.endswith('.csv'):
            file_path = os.path.join(subpasta_path, file)
            # Ler o CSV e adicionar à lista de DataFrames
            df = pd.read_csv(file_path, encoding='utf-8', sep=',')
            dfs.append(df)

# Combinar todos os DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Caminho de saída
output_path = r'C:\Users\levia\OneDrive\Área de Trabalho\BASE ROTEIROS CONSOLIDADA\base_roteiros_consolidada.csv'

# Salvar o arquivo combinado
combined_df.to_csv(output_path, index=False, encoding='utf-8')

print(f'Arquivo salvo em: {output_path}')
