from src.extracao.extracao_azcorp.extracao_azcorp import ExtracaoAzcorp

extracao_azcorp = ExtracaoAzcorp()
extracao_azcorp.obter_dados(url="https://azcorp.tech/talentos/")
vagas = extracao_azcorp.obter_dados_vagas()
print(f"Total de vagas encontradas: {len(vagas)}")
for vaga in vagas:
    print(vaga)
extracao_azcorp.fechar_conexao()

