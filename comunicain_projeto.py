import sqlite3
import pandas as pd

# Conectando ao banco, e executando a query para pegar os dados da tabela "Vendas"
conexao = sqlite3.connect('banco.db')
tabela_db = pd.read_sql_query("SELECT * FROM Vendas", conexao)

# Ler os arquivos .CSV
csv1 = pd.read_csv('periodo_1.csv')
csv2 = pd.read_csv('periodo_2.csv')

# Combinar os dados dos dois arquivos CSV
vendas_portal = pd.concat([csv1, csv2], ignore_index=True)

# Comparando os dados do CSV com o SQL usando como base as ID não registradas no banco
diferenca = vendas_portal[~vendas_portal['ID_Venda'].isin(tabela_db['ID_Venda'])]

# Usando o comando para exibir as linhas que faltam no banco
print("Inconsistências encontradas no banco de dados:")
print(diferenca)

diferenca.to_csv('diferencas.csv', index=False)

conexao.close()
