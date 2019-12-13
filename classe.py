class Contexto:
  def __init__(Self, Parametros):
    Self.Parametros = Parametros
  def __str__(Self):
    return "<Contexto atual contém: " + str(Self.Parametros) + ">"
print (f"Contexto padrao. ", qiracontext)
qiracontext.Value = Contexto('Cidade', 'Uba', 'teste')
print (f"Contexto disponível. ", qiracontext)