from typing import Protocol, TypeVar

Driver = TypeVar('Driver')


class IExtracao(Protocol):

    def obter_dados(self, url: str):
        ...

    def obter_dados_vagas(self) -> list[tuple[str, str, str]] | None:
        ...

    def fechar_conexao(self):
        ...
