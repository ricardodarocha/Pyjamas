# Pyjamas
Apresentação da lib Python4Delphi

# Pré requisitos
Instalar o python no seu computador
Instalar as bibliotecas do python que você for usar, usando ``` pip install ?``` . Ver nos exemplos a cláusula ``` import``` 
Instalar o Delphi Community Edition ou superior através do link https://www.embarcadero.com/br/products/delphi/starter
Instalar o componente Python4Delphi através do repositório https://github.com/pyscripter/python4delphi

~ Você também pode utilizar o Lazarus FPC em vez do Delphi, mas eu não testei este exemplo no Lazarus

# Recomendado
Instalar o componente SynEdit para Delphi através do repositório https://github.com/SynEdit/SynEdit
Instalar o componente RestDW para Delphi através do source forge https://svn.code.sf.net/p/rest-dataware-componentes/dataware/trunk

``` python
help("modules") #lista das bibliotecas dos exemplos
>>output
PIL                 kivy                matplotlib          termcolor
colorama            numpy               dash                pip                 
plotly              fdb                 pymongo             pandas
io                  socket              xmlrpc              sklearn
sqlite3             itertools           zlib
```
# Como testar
Após configurar o ambiente, baixe este repositório inteiro via ``` git clone ``` ou faça download do arquivo zipado.
Descompactar e abrir com o delphi o projeto ProjPy.dpr
Compilar

# Como ir além
Abrir os demos do próprio componente Python4Delphi para aprender mais
Realizar tutoriais de python para aprender a utilizar as libs

# Libs recomendadas
matplotlib (gráficos)
requests (requisições http)
fdb (firebird)
sqlite3 
pandas (dataframe)
asyncio (assíncrono)

# Erros comuns
O componente SynEdit não está instalado.
  Não tem problema, basta utilizar o TRichEdit ou TMemo
  
Python não encontrado
  Adicione o diretório do Python às variáveis de ambiente do Windows
  
A biblioteca xxx não está instalada
  Instalar usando o pip install

