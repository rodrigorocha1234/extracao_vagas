from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.extracao.extracao_base import ExtracaoBase


class ExtracaoAzcorp(ExtracaoBase):

    def __init__(self) -> None:
        super().__init__()

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_vagas: list[tuple[str, str, str]] = []

        try:
            WebDriverWait(self._driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section.et_pb_fullwidth_header"))
            )
        except Exception as e:
            print(f"Erro ao aguardar carregamento dos elementos: {e}")
            return lista_vagas

        self.scroll_ate_o_final()

        vagas = self._driver.find_elements(
            By.CSS_SELECTOR,
            "section.et_pb_fullwidth_header"
        )

        for vaga in vagas:
            try:
                titulo_elemento = vaga.find_element(
                    By.CSS_SELECTOR,
                    ".et_pb_module_header"
                )
                titulo_vaga = titulo_elemento.text.strip()

                botao_link = vaga.find_element(
                    By.CSS_SELECTOR,
                    "a.et_pb_button"
                )
                link_vaga = botao_link.get_attribute("href")

                if not titulo_vaga or not link_vaga:
                    continue

                lista_vagas.append((titulo_vaga, link_vaga, "AZCORP"))
                print(f"Vaga encontrada: {titulo_vaga} | Link: {link_vaga}")
            except Exception as e:
                print(f"Erro ao processar vaga: {e}")
                continue

        return lista_vagas
