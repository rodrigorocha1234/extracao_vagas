from abc import abstractmethod, ABC
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

    @abstractmethod
    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        pass

    def fechar_conexao(self):
        self._driver.quit()
