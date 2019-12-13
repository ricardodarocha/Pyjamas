from bokeh.plotting import figure, output_file, save, show
import requests

url = "http://localhost:8082/api/READOBJECT"
listIndicadores  = {"psql":"SELECT Codigo, Nome FROM indicadores"} 
listMedicoes = {"psql":"SELECT distinct medicoes.Percentual FROM indicadores JOIN medicoes ON medicoes.indicador = indicadores.id  where indicadores.codigo = 2"}

indicadores = requests.get(url,params=listIndicadores).json()['RESULT']
medicoes = requests.get(url,params=listMedicoes).json()['RESULT']
print(indicadores)
print(medicoes)

valores = [float(element['Percentual'].replace(',','.')) for element in medicoes ]
y = valores
x = range(len(y))
output_file('grafico.html')
p = figure(
    title = 'Meu indicador',
    plot_width=1200,
    x_axis_label = 'x',
    y_axis_label = 'y'
)

p.line(x, y, legend='legenda', line_width=2)    
# p.hbar(y,right=x, left=0, height=0.4,)

show(p)