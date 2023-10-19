from pathlib import Path
import shutil

estados = ['RJ', 'PR', 'SP', 'MG', 'AM']

#   Criando Pastas
"""
for pastas in estados:
    arquivo = Path(r"Projeto\Arquivos/{}".format(pastas)).mkdir()
"""

#   Separando Arquivos por pasta
caminho = Path(r"Projeto\Arquivos")
for arquivos in caminho.iterdir():
    nome_arquivo = arquivos.name
    if nome_arquivo[-3:] == 'csv':
        estado = nome_arquivo[-6:-4]
        local_final = caminho / Path(r"{}/{}".format(estado, nome_arquivo))
        shutil.move(arquivos, local_final)