from abc import abstractmethod, ABC
from time import sleep
from typing import TypeVar

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

Driver = TypeVar('Driver')


class ExtracaoBase(ABC):

    def __init__(self, headless: bool = True) -> None:
        self.__options = Options()
        if headless:
            self.__options.add_argument("--headless=new")
        self.__options.add_argument("--no-sandbox")
        self.__options.add_argument("--disable-dev-shm-usage")
        self.__options.add_argument("--disable-gpu")
        self.__options.add_argument("--window-size=1920,1080")
        self.__options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        self.__servico = Service(ChromeDriverManager().install())

        self._driver = webdriver.Chrome(
            service=self.__servico, options=self.__options)

    def obter_dados(self, url: str):
        self._driver.get(url)

    def scroll_ate_o_final(self, pausa: float = 2.0, max_scrolls: int = 20):
        """
        Realiza scroll até que a altura da página não aumente mais ou atinja max_scrolls.
        """
        altura_anterior = self._driver.execute_script(
            "return Math.max(document.body ? document.body.scrollHeight : 0, document.documentElement ? document.documentElement.scrollHeight : 0);"
        )

        scrolls = 0
        while scrolls < max_scrolls:
            self._driver.execute_script(
                "window.scrollTo(0, Math.max(document.body ? document.body.scrollHeight : 0, document.documentElement ? document.documentElement.scrollHeight : 0));"
            )

            sleep(pausa)

            nova_altura = self._driver.execute_script(
                "return Math.max(document.body ? document.body.scrollHeight : 0, document.documentElement ? document.documentElement.scrollHeight : 0);"
            )

            if nova_altura == altura_anterior:
                break

            altura_anterior = nova_altura
            scrolls += 1

    @abstractmethod
    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        pass

    def fechar_conexao(self):
        try:
            self._driver.quit()
        except Exception:
            pass
