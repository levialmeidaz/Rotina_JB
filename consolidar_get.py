import os
import pandas as pd

# Definindo os caminhos das pastas
input_folder = r'C:\Users\indic\OneDrive - grupojb.log.br\DATABASE PAINEL\BASE - GET ALERT (NOVO)'
output_file = r'C:\Users\indic\OneDrive - grupojb.log.br\DATABASE PAINEL\BASE GET CONSOLIDADA\get_consolidado.csv'

# Lista para armazenar os dataframes
df_list = []

# Loop para ler todos os arquivos Excel na pasta
for file in os.listdir(input_folder):
    if file.endswith('.xlsx'):
        file_path = os.path.join(input_folder, file)
        
        # Lendo o arquivo Excel
        df = pd.read_excel(file_path)
        
        # Adicionando uma nova coluna com o nome do arquivo (sem a extensão)
        df['Nome da Origem'] = os.path.splitext(file)[0]
        
        # Reorganizando as colunas para que "Nome da Origem" seja a primeira
        cols = ['Nome da Origem'] + [col for col in df.columns if col != 'Nome da Origem']
        df = df[cols]
        
        # Adicionando o dataframe à lista
        df_list.append(df)

# Concatenando todos os dataframes
df_consolidado = pd.concat(df_list, ignore_index=True)

# Exportando para CSV
df_consolidado.to_csv(output_file, index=False, sep=',')

print(f'Arquivo consolidado salvo em: {output_file}')
