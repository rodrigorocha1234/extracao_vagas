from typing import TypeVar

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.extracao.extracao_base import ExtracaoBase

Driver = TypeVar('Driver')


class ExtracaoInrihe(ExtracaoBase):

    def __init__(self) -> None:
        super().__init__()


    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_vagas = []
        WebDriverWait(self._driver, 40).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')))
        vagas = self._driver.find_elements(By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')
        for vaga in vagas:
            try:
                titulo = vaga.find_element(By.CSS_SELECTOR, 'div[data-sentry-element="JobPositionName"]').text
                link = vaga.get_attribute("href")
                assert link is not None
                lista_vagas.append((titulo, link, self._driver.title))
            except Exception as e:
                print(f"Erro ao processar vaga: {e}")
                continue
        return lista_vagas

