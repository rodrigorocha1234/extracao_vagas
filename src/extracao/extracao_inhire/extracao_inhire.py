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

        WebDriverWait(self._driver, 100).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')))
        self.scroll_ate_o_final()
        titulo_vaga = ''

        vagas = self._driver.find_elements(By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')
        for vaga in vagas:
            try:
                titulo = vaga.find_element(By.CSS_SELECTOR, 'div[data-sentry-element="JobPositionName"]').text

                if titulo.split('-')[-1].strip() == "USINA DA PEDRA":
                    titulo_vaga += '- ' +  titulo + '\n' + '\n'


            except Exception as e:
                print(f"Erro ao processar vaga: {e}")
                continue
        lista_vagas.append((titulo_vaga, f'{self._driver.current_url}', self._driver.title))
        return lista_vagas

