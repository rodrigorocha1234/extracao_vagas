from src.extracao.extracao_ccm.extracao_ccm import ExtracaoCcm


extracao_ccm = ExtracaoCcm()
extracao_ccm.obter_dados(url='https://recrutamento.ccmtecnologia.com.br/jobs/Careers')
extracao_ccm.obter_dados_vagas()
extracao_ccm.fechar_conexao()
