import os
import pandas as pd

# Defina o caminho da pasta com os arquivos Excel
input_folder = r'C:\Users\indic\OneDrive - grupojb.log.br\DATABASE PAINEL\BASE - PEDIDOS EM ABERTO'

# Defina o caminho onde o arquivo consolidado será salvo
output_file = r'C:\Users\indic\OneDrive\Área de Trabalho\Consolidado_Ped_Aberto\pedidos_em_aberto_consolidados.csv'

# Lista para armazenar os DataFrames
df_list = []

# Ordem desejada das colunas (incluindo "Nome da Origem")
colunas_ordenadas = [
    'Nome da Origem', 'TRP', 'FILIAL', 'CENTRO_ORIGEM', 'PEDIDO', 'NM_NFE', 'NUMERO_OV', 'TIPO_ENTREGA', 'UF', 
    'CD_PRIO_REM', 'CD_SETOR', 'ITINERARIO', 'QT_CAIXAS', 'ROTA', 'SUBROTA', 'Range D2', 
    'ZONEAMENTO_RECEB', 'DTFAT', 'DT2', 'DT1', 'DATA 3', 'Total Atrasado DT2', 'Status NATURA', 
    'Status TRP', 'Região', 'Inconsistência', 'CICLO', 'NF_SERIE', 'TRANSP.COD', 'TIPO PEDIDO', 
    'TAREFA_NAT', 'TAREFA ETAPA', 'TAREFA DATA SLA', 'ROTA2', 'Concatenar', 
    'Pedido com reclamação', 'AVON'
]

# Percorre todos os arquivos da pasta
for file in os.listdir(input_folder):
    if file.endswith('.xlsx') or file.endswith('.xls'):
        file_path = os.path.join(input_folder, file)
        # Lê o arquivo Excel
        df = pd.read_excel(file_path)
        
        # Adiciona uma coluna "Nome da Origem" com o nome completo do arquivo (incluindo pontos, mas sem a extensão)
        df['Nome da Origem'] = file.rsplit('.', 1)[0]  # Remove apenas a extensão, mantendo os pontos no nome
        
        # Reorganiza as colunas de acordo com a ordem desejada, ignorando colunas faltantes
        df = df.reindex(columns=['Nome da Origem'] + colunas_ordenadas[1:])  # Mantém a coluna "Nome da Origem" como a primeira
        
        # Adiciona o DataFrame à lista
        df_list.append(df)

# Concatena todos os DataFrames em um só
df_combined = pd.concat(df_list, ignore_index=True)

# Salva o DataFrame combinado em um arquivo CSV
df_combined.to_csv(output_file, index=False, sep=',')

print(f"Arquivos combinados e salvos em: {output_file}")