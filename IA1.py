#features , input
#labels , output
from sklearn import tree
# from sklearn.externals.six import StringIO
# import pydotplus 
# import graphviz   
# from sklearn.metrics import accuracy_score
 
# dot_data = StringIO()
features = [[140,1],[130,1],[131,1],[150,0],[170,0],[170,0],[130,1],[180,0],[180,1],[120,1]]
labels = [0,0,0,1,1,1,0,1,0,1]
clf=tree.DecisionTreeClassifier().fit(features, labels)
prediction = clf.predict([[150,0]])
print(prediction)

# tree.export_graphviz(clf,out_file=dot_data)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf('iris.pdf')
# print accuracy_score()
