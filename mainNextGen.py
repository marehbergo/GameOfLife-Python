# ---------- GAME OF LIFE ----------

# ---------- REGRAS DO JOGO ----------
# 1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
# 2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
# 3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
# 4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.

import random   #importa a biblioteca que implementa a geração randômica de 0s e 1s que irão compor a matriz

mundo = []   #cria a matriz mundo
proxGeracao = []   #cria uma matriz para armazenar a próxima geração
vizinhos = []   #cria uma matriz para armazenar o número de vizinhos

tamanho = raw_input('qual o tamanho do seu mundo?')   #o usuário escolhe o tamanho da matriz mundo

#preenche a matriz com 0s ou 1s de modo aleatorio
for i in range(int(tamanho)):
  linha = []   #cria uma linha na matriz
  
  for j in range(int(tamanho)):
    linha.append(random.randint(0,1))   #preenche cada posição da linha com 0 ou 1 randomicamente
  
  mundo.append(linha)   #insere na matriz a linha preenchida

#---------------------------------------------------------------------------------------------------

for i in range(len(mundo)):   #percorre as linhas da matriz mundo
  linha = []
  proxEstado = []
  for j in range(len(mundo)):   #percorre as colunas da matriz mundo
    vivos = 0   #zera o contador de vizinhos vivos
    estado = 0   #estado inicial das celulas na proxima geração
    
    #---------------------------------------------------------------------------------------------------
    #contando os vizinhos
    
    #primeira coluna
    if j == 0:
      if i == 0: vivos += mundo[i][j+1] + mundo[i+1][j] + mundo[i+1][j+1]   #primeira linha
      elif i == (len(mundo)-1): vivos += mundo[i-1][j] + mundo[i-1][j+1] + mundo[i][j+1]   #ultima linha
      else: vivos += mundo[i-1][j] + mundo[i-1][j+1] + mundo[i][j+1] + mundo[i+1][j] + mundo[i][j+1]   #demais linhas da primeira coluna
    
    #ultima coluna
    elif j == (len(mundo)-1):
      if i == 0: vivos += mundo[i][j-1] + mundo[i+1][j-1] + mundo[i+1][j]   #primeira linha
      elif i == (len(mundo)-1): vivos += mundo[i-1][j-1] + mundo[i-1][j] + mundo[i][j-1]   #ultima linha
      else: vivos += mundo[i-1][j-1] + mundo[i-1][j] + mundo[i][j-1] + mundo[i+1][j-1] + mundo[i+1][j]   #demais linhas da ultima coluna

    #primeira linha
    elif i == 0: vivos += mundo[i][j-1] + mundo[i][j+1] + mundo[i+1][j-1] + mundo[i+1][j] + mundo[i+1][j+1]
    
    #ultima linha
    elif i == (len(mundo)-1): vivos += mundo[i-1][j-1] + mundo[i-1][j] + mundo[i-1][j+1] + mundo[i][j-1] + mundo[i][j+1]
    
    #demais linhas e colunas
    else: vivos += mundo[i-1][j-1] + mundo[i-1][j] + mundo[i-1][j+1] + mundo[i][j-1] + mundo[i][j+1] + mundo[i+1][j-1] + mundo[i+1][j] + mundo[i+1][j+1]
    
    linha.append(vivos)   #salva no vetor "linha" os vizinhos vivos encontrados
    
    #---------------------------------------------------------------------------------------------------
    #aplicacao das regras
    if mundo[i][j] == 1:   #celula viva
      if vivos < 2 or vivos > 3: estado = 0   #menos de 2 ou mais de 3 vizinhos vivos, celula morre
      else: estado = mundo[i][j]   #2 ou 3 vizinhos, mantém o estado
    else:   #celula morta    
      if vivos == 3: estado = 1   #com 3 vizinhos vivos, celula revive
    
    proxEstado.append(estado)   #salva no vetor "linha" os vizinhos vivos encontrados
  proxGeracao.append(proxEstado)   #salva na matriz "proxGeracao" a linha gerada
  vizinhos.append(linha)   #salva na matriz "vizinhos" a linha gerada

#------------------------------------------------------------------------------------------------------------------------------------
#imprime as matrizes na tela
print 'Geracao atual        NumVizinhos       proxima Geracao'
for i in range(len(mundo)):   #imprime na tela a matriz original e a matriz de vizinhos
  print mundo[i],'  ',vizinhos[i],'  ',proxGeracao[i]
