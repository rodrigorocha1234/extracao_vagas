from time import sleep

from selenium.webdriver.common.by import By

from src.extracao.extracao_base import ExtracaoBase


class ExtracaoAzcorp(ExtracaoBase):

    def __init__(self):
        super().__init__()

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_vagas = []
        sleep(80)

        vagas = self._driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[2]/select')

        for vaga in vagas:
            nome_vaga = " \n  ".join(
                ' - ' + linha.strip()
                for linha in vaga.text.splitlines()
                if linha.strip()
            ) + "\n"
            lista_vagas.append((nome_vaga, 'https://azone.aalves.org/contratacao/cadastro', "AZCORP TECH"))
        return lista_vagas
