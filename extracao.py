from src.extracao.extracao_azcorp.extracao_azcorp import ExtracaoAzcorp
from src.extracao.extracao_ccm.extracao_ccm import ExtracaoCcm


extracao_ccm = ExtracaoAzcorp()
extracao_ccm.obter_dados(url='https://azone.aalves.org/contratacao/cadastro')
extracao_ccm.obter_dados_vagas()
extracao_ccm.fechar_conexao()
