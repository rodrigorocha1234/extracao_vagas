from src.extracao.extracao_inhire.extracao_base import ExtracaoInhire
from src.extracao.iextracao import IExtracao


class MainExtracao:
    def __init__(self, extracao_inhire: IExtracao):
        self.__url_inhire = ['https://goflow.inhire.app/azcorp/vagas', 'https://bixtecnologia.inhire.app/vagas']
        self.__extracao_inhire = extracao_inhire

    def rodar_servico_inrire(self):
        for site in self.__url_inhire:
            self.__extracao_inhire.obter_dados(url=site)
            vagas = self.__extracao_inhire.obter_dados_vagas()
            if vagas:
                for vaga in vagas:
                    print(vaga)

        self.__extracao_inhire.fechar_conexao()


if __name__ == "__main__":
    extracao_inhire = ExtracaoInhire()
    me = MainExtracao(extracao_inhire)
    me.rodar_servico_inrire()






