# 1. Importa a biblioteca de gráficos do pyhton
import matplotlib.pyplot as plt

# 2. Cria um título com várias linhas
title = '''
Gráfico do QIRA
Gráfico gerado automaticamente
''' 
# 3. Configura o eixo X
rotulos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# 4. Configura o eixo y: 
#   Prepara uma série vazia, em seguida insere os dados através da técnica de chave e valor 
serie={}
serie['vendas'] = [5,3,8,8,2,3,4,3,6,9,8,6,3,6]
serie['pedidos'] = [3,8,8,2,3,4,3,6,9,8,6,3,6,8]
serie['produtos'] = [8,2,3,4,3,6,9,8,6,3,6,8,6,5]
serie['estoque'] = [2,3,4,3,6,9,8,6,3,6,8,6,5,7]

# 5. Plota as séries uma de cada vez   
plt.plot(rotulos,serie['vendas'])
plt.plot(rotulos,serie['pedidos'])
plt.plot(rotulos,serie['produtos'])
plt.plot(rotulos,serie['estoque'])

# 6. Formata o gráfico
plt.title(title) 
plt.xlabel('dias')
plt.ylabel('quantidade')

# 7. Abre o gráfico numa nova janela
plt.show()