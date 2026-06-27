from typing import Protocol


class IMensageiro(Protocol):

    def formatar_texto(self, mensagem: tuple[str, str, str]) -> str:
        ...

    def enviar_mensagem(self, mensagem: str) -> None:
        ...