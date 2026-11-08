from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.extracao.extracao_base import ExtracaoBase


class ExtracaoCcm(ExtracaoBase):

    def __init__(self) -> None:
        super().__init__()

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_dados_vagas: list[tuple[str, str, str]] = []

        try:
            WebDriverWait(self._driver, 15).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'cw-1-title'))
            )
        except Exception as e:
            print(f"Erro ao aguardar carregamento dos elementos CCM: {e}")
            return lista_dados_vagas

        self.scroll_ate_o_final(pausa=1.0)

        vagas = self._driver.find_elements(By.CLASS_NAME, 'cw-1-title')

        for vaga in vagas:
            try:
                titulo = vaga.text.strip()
                href = vaga.get_attribute("href")

                if not titulo or not href:
                    continue

                lista_dados_vagas.append((titulo, href, "CCM TECNOLOGIA"))
            except Exception as e:
                print(f"Erro ao processar vaga CCM: {e}")
                continue

        return lista_dados_vagas
