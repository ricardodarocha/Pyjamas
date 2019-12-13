from decimal import getcontext, Decimal

#getcontext().prec = 3 #Configura número de casas decimais

vendas = {
2016: [72, 64, 63, 75, 68, 65, 70],
2017: [82, 65, 66, 72, 53, 55, 89],
2018: [76, 60, 62, 70, 70, 64, 68],
}

medias = {}
prop = {} #proporções

for ano in range(2016, 2019):
  medias[ano] = round(sum(vendas[ano]) / len(vendas[ano]), 3)
  prop[ano] = []
  for value in vendas[ano]:
    prop[ano].append(round(value /  medias[ano],2) )
 
#sazonalidade = [sum([i[0] for i in prop.values()])] 
sazonalidade = []
for j in range(7):
  sazonalidade.append(round(sum([i[j] for i in prop.values()])/3,  2) ) 
  

print('médias', medias)
print('proporções')
print('sazonalidade', sazonalidade)

# todo Planilificar :: planificacao = vendas[ano][mes] / sazonalidade[mes] 