#features , input
#labels , output
from sklearn import tree
# Atributos para treinar a máquina
# Produto TemNoEstoque  TemPedido  Faturado ABC Comprado Cliente Preco Sazonal
# ------------------------------------------------------------------------------
#  AAA1    1            1           1       A    0        1      0      1
#  BAA2    0            1           0       B    0        1      1      1
#  BAB3    1            0           0       B    0        1      0      0
#-------------------------------------------------------------------------------
#  teste   0            1           1       A    0        1      1      0  
features = [[1,1,1,1,0,1,0,1],[0,1,0,0,0,1,1,1],[1,0,0,0,1,0,1,0]]
labels = [0,1,1]
clf=tree.DecisionTreeClassifier().fit(features, labels)

Estoque=0
Pedido=1
Faturado=1
A=1
Comprado=0
ClienteBom=1
PrecoBom=1
Sazonal=1
Problema = [Estoque, Pedido,Faturado,A,Comprado,ClienteBom,PrecoBom,Sazonal]
print(clf.predict([Problema]))