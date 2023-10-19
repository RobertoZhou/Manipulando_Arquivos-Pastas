from pathlib import Path

estados = ['RJ', 'PR', 'SP', 'MG', 'AM']

#   Criando Pastas
for pastas in estados:
    arquivo = Path(r"Projeto\Arquivos/{}".format(pastas)).mkdir()
