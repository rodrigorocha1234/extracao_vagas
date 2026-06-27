from src.extracao.extracao_inhire.extracao_base import ExtracaoInhire
from src.extracao.iextracao import IExtracao
from src.mensageiro.imensageiro import IMensageiro
from src.mensageiro.telegram_mensageiro.telegram_mensageiro import TelegramMensageiro


class MainExtracao:
    def __init__(self, extracao_inhire: IExtracao, servico_mensageiro: IMensageiro):
        self.__url_inhire = ['https://goflow.inhire.app/azcorp/vagas']
        self.__extracao_inhire = extracao_inhire
        self.__servico_mensageiro = servico_mensageiro

    def rodar_servico_inrire(self):
        for site in self.__url_inhire:
            self.__extracao_inhire.obter_dados(url=site)
            vagas = self.__extracao_inhire.obter_dados_vagas()
            if vagas:
                for vaga in vagas:
                    texto_formatado = self.__servico_mensageiro.formatar_texto(vaga)
                    self.__servico_mensageiro.enviar_mensagem(mensagem=texto_formatado)

        self.__extracao_inhire.fechar_conexao()


if __name__ == "__main__":
    extracao_inhire = ExtracaoInhire()
    servico_telegram = TelegramMensageiro()
    me = MainExtracao(extracao_inhire, servico_telegram)
    me.rodar_servico_inrire()






