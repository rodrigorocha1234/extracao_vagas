from abc import abstractmethod, ABC
from time import sleep
from typing import TypeVar

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

Driver = TypeVar('Driver')


class ExtracaoBase(ABC):

    def __init__(self) -> None:
        self.__options = Options()
        self.__options.add_argument("--headless=new")
        self.__servico = Service(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=self.__servico, options=self.__options)


    def obter_dados(self, url: str):
        self._driver.get(url)

    def scroll_ate_o_final(self, pausa: float = 2.0):
        """
        Realiza scroll até que a altura da página não aumente mais.
        """
        altura_anterior = self._driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            self._driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            sleep(pausa)

            nova_altura = self._driver.execute_script(
                "return document.body.scrollHeight"
            )

            if nova_altura == altura_anterior:
                break

            altura_anterior = nova_altura

    @abstractmethod
    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        pass

    def fechar_conexao(self):
        self._driver.quit()
