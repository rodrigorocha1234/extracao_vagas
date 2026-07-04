from src.extracao.extracao_ccm.extracao_ccm import ExtracaoCcm
from src.extracao.extracao_inhire.extracao_inhire import ExtracaoInrihe
from src.extracao.iextracao import IExtracao
from src.mensageiro.imensageiro import IMensageiro
from src.mensageiro.telegram_mensageiro.telegram_mensageiro import TelegramMensageiro


class MainExtracao:
    def __init__(self, extracao_vagas: IExtracao, servico_mensageiro: IMensageiro, url_extracao: str):
        self.__url_extracao = url_extracao
        self.__extracao_vagas = extracao_vagas
        self.__servico_mensageiro = servico_mensageiro

    def rodar_servico_extracao(self):

        self.__extracao_vagas.obter_dados(url=self.__url_extracao)
        vagas = self.__extracao_vagas.obter_dados_vagas()
        if vagas:
            for vaga in vagas:
                texto_formatado = self.__servico_mensageiro.formatar_texto(vaga)
                self.__servico_mensageiro.enviar_mensagem(mensagem=texto_formatado)

        self.__extracao_vagas.fechar_conexao()


if __name__ == "__main__":
    extracao_inhire = ExtracaoInrihe()
    servicos_extracao = [(ExtracaoInrihe(), "https://goflow.inhire.app/azcorp/vagas"),
        (ExtracaoCcm(), "https://recrutamento.ccmtecnologia.com.br/jobs/Careers")]
    servico_telegram = TelegramMensageiro()
    for site in servicos_extracao:
        me = MainExtracao(site[0], servico_telegram, site[1])
        me.rodar_servico_extracao()
