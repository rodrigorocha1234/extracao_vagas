from src.extracao.extracao_azcorp.extracao_azcorp import ExtracaoAzcorp
from src.extracao.extracao_ccm.extracao_ccm import ExtracaoCcm
from src.extracao.extracao_inhire.extracao_inhire import ExtracaoInhire, ExtracaoInrihe
from src.extracao.iextracao import IExtracao
from src.mensageiro.imensageiro import IMensageiro
from src.mensageiro.telegram_mensageiro.telegram_mensageiro import TelegramMensageiro


class MainExtracao:
    def __init__(self, extracao_vagas: IExtracao, servico_mensageiro: IMensageiro, url_extracao: str):
        self.__url_extracao = url_extracao
        self.__extracao_vagas = extracao_vagas
        self.__servico_mensageiro = servico_mensageiro

    def rodar_servico_extracao(self):
        try:
            self.__extracao_vagas.obter_dados(url=self.__url_extracao)
            vagas = self.__extracao_vagas.obter_dados_vagas()
            if vagas:
                for vaga in vagas:
                    texto_formatado = self.__servico_mensageiro.formatar_texto(vaga)
                    self.__servico_mensageiro.enviar_mensagem(mensagem=texto_formatado)
        except Exception as e:
            print(f"Erro ao executar extração para {self.__url_extracao}: {e}")
        finally:
            self.__extracao_vagas.fechar_conexao()


if __name__ == "__main__":
    servicos_extracao = [
        (ExtracaoInhire, "https://pedraagroindustrial.inhire.app/vagas"),
        (ExtracaoCcm, "https://recrutamento.ccmtecnologia.com.br/jobs/Careers"),
        (ExtracaoAzcorp, "https://azcorp.tech/talentos/"),
    ]
    servico_telegram = TelegramMensageiro()
    for extrator_item, url in servicos_extracao:
        # Permite passar tanto a classe para instanciação sob demanda quanto a instância pronta
        extrator = extrator_item() if isinstance(extrator_item, type) else extrator_item
        me = MainExtracao(extrator, servico_telegram, url)
        me.rodar_servico_extracao()
