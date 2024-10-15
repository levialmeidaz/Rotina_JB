import pandas as pd

# Caminho do arquivo de origem
file_path = r'C:\Users\indic\OneDrive\Área de Trabalho\Ferramentas\NC Faltas\padronização da base\NC Falta JB Outubro.csv'

# Leitura do arquivo CSV com codificação especificada
df = pd.read_csv(file_path, sep=';', encoding='latin1')  # Tente 'latin1', 'ISO-8859-1' ou outra se necessário

# Lista de colunas desejadas na ordem especificada
desired_columns = [
    'Cd Centro', 'Desc Reg Estrategica', 'Filial', 'Transportador', 'Marca', 'Tipo NC', 'NM_PAIS', 'Expurgos',
    'Desc Ger Mercado', 'Rota', 'Nm Ciclo', 'Nome da Consultora', 'Desc Ger Vendas', 'Desc Setor Vendas',
    'Grupo  (Descrição)', 'Responsável do Grupo - CRM (Descrição)', 'UF', 'Dc Cidade', 'CN: Bairro (Chave)', 'Cod Mat',
    'Valor', 'Categoria', 'Nível de Risco', 'Status da operação', 'Solução da NC (Geral)', 'Assunto', 'Resultado',
    'Cd Zona Transp', 'Obs', 'Linha de Separação', 'Data Separação', 'Data Faturamento', 'Data Criação NF',
    'Data de Conclusão', 'Solução segundo nível', 'Origem', 'N° da operação', 'Nm Pedido', 'Solução Geral', 'Cod Venda',
    'Nome Produto', 'Parte Afetada', 'Cód CN', 'Motivo - CRM (nível 1)', 'Motivo', 'Num Nfe', 'Problema do Produto',
    'Seleção Dimensão_NCProdutos', 'Seleção Dimensão_NCProdutos - CD', 'Seleção Dimensão_NCProdutos - Cidade',
    'Seleção Dimensão_NCProdutos - Filial', 'Seleção Dimensão_NCProdutos - RE', 'Seleção Dimensão_NCProdutos - UF',
    'Seleção Dimensão_NCProdutos - Zoneamento', 'NC SIM Não', 'Quantidade', 'Cd Venda Ina', 'Cd Venda Ina-1', 'Chave',
    'Chave1', 'Data Criação do Registro', 'Expurgos1', 'NC Duplicidade', 'NC Expurgo', 'Nm Transportadora', 'NM_PAIS',
    'Pedido Conquista'
]

# Verificar quais colunas estão faltando
missing_columns = [col for col in desired_columns if col not in df.columns]

# Adicionar as colunas faltantes com valores vazios
for col in missing_columns:
    df[col] = ''

# Reordenar as colunas na ordem desejada
df = df[desired_columns]

# Caminho para salvar o arquivo CSV
output_path = r'C:\Users\indic\OneDrive\Área de Trabalho\Ferramentas\NC Faltas\padronização da base\arquivo_padronizado_out.csv'

# Salvando como CSV
df.to_csv(output_path, index=False, sep=',')