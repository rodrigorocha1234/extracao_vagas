from typing import TypeVar

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

Driver = TypeVar('Driver')


class ExtracaoInhire:

    def __init__(self) -> None:
        self.__options = Options()
        self.__options.add_argument("--headless=new")
        self.__servico = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=self.__servico, options=self.__options)

    def obter_dados(self, url: str):
        self.__driver.get(url)

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_vagas = []
        WebDriverWait(self.__driver, 40).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')))
        vagas = self.__driver.find_elements(By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')
        for vaga in vagas:
            try:
                titulo = vaga.find_element(By.CSS_SELECTOR, 'div[data-sentry-element="JobPositionName"]').text
                link = vaga.get_attribute("href")
                assert link is not None
                lista_vagas.append((titulo, link, self.__driver.title))
            except Exception as e:
                print(f"Erro ao processar vaga: {e}")
                continue
        return lista_vagas

    def fechar_conexao(self):
        self.__driver.quit()
