from selenium.webdriver.common.by import By

from src.extracao.extracao_base import ExtracaoBase


class ExtracaoCcm(ExtracaoBase):

    def __init__(self) -> None:
        super().__init__()

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_dados_vagas = []
        titulos_vagas = self._driver.find_elements(By.CLASS_NAME, 'cw-1-title')
        links = self._driver.find_elements(By.CLASS_NAME, 'cw-1-title')

        for titulo, link in zip(titulos_vagas, links):
            lista_dados_vagas.append((titulo.text, link.get_attribute('href'), "CCM TECNOLOGIA"))

        return lista_dados_vagas
