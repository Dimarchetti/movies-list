import requests
import json

def requisicao(titulo):
  try:
    req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&type=movie' + '&apikey=e968a439') # Pega os dados do filme Matrix 
    dicionario = json.loads(req.text) # Coloca os textos de req dentro da variável dicionario
    return dicionario
  except Exception as error:
    print('Erro ', error)
    return None

def mostrarFilme(filme):
  print('==============')
  print('Filme ', filme['Title']) # Mostra o Title do Filme
  print('==============')
  print('Atores ', filme['Actors'])
  print('==============')
  print('Diretor ', filme['Director'])
  print('==============')
  print('Prêmios ', filme['Awards'])
  print('==============')
  print('Lançamento ', filme['Year'])
  print('==============')
  print('Gênero ', filme['Genre'])
  print('==============')
  print('Nota ', filme['imdbRating'])
  print('==============')
  print('Poster', filme['Poster']) 
  print('==============')
  print('')

sair = False
while not sair:
  opcao = input('Escolha o nome de um filme o digite sair: ')

  if opcao == 'sair':
    sair = True
    print('Saindo...')
  else:
    filme = requisicao(opcao)
    if filme == 'False':
      print('Filme não encontrado')
    else:
      mostrarFilme(filme)
