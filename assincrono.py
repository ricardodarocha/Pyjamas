import asyncio
import time

async def tic(tempo, mensagem):
    await asyncio.sleep(tempo)
    print(mensagem)

async def main():
    print(f"Processo assíncrono iniciado {time.strftime('%X')}")

    await tic(1, 'Olá')
    await tic(2, 'Eu sou o Python')
    await tic(3, 'Eu estou rodando dentro do Delphi')
    await tic(5, 'Acesse github/Python4Delphi')
    await tic(6, '...')
    print(f"Pyjamas  {time.strftime('%X')}")

asyncio.run(main())