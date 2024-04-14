#   Gerador de Arquivos CSV

import pandas as pd
import random

arquivos = pd.DataFrame()

qtd = 30
for arquivo in range(1, qtd):
    estados = ['RJ', 'PR', 'SP', 'MG', 'AM']
    siglaEstado = random.choice(estados)
    numCode = str(random.random())[2:8]
    arquivos.to_csv(r'Projeto/Arquivos/{}_{}.csv'.format(numCode, siglaEstado))
