arquivo = open(
    "D:/DioBootcamp/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo. Feito por alex Sandro")
arquivo.writelines(["\n", "escrevendo", "\n", "tudo", "\n", "de novo", "\n", "texto"])
arquivo.close()
