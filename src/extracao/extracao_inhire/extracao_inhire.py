from typing import TypeVar

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.extracao.extracao_base import ExtracaoBase

Driver = TypeVar('Driver')


class ExtracaoInhire(ExtracaoBase):

    def __init__(self) -> None:
        super().__init__()

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        lista_vagas: list[tuple[str, str, str]] = []

        try:
            WebDriverWait(self._driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]'))
            )
        except Exception as e:
            print(f"Erro ao aguardar carregamento dos elementos Inhire: {e}")
            return lista_vagas

        self.scroll_ate_o_final(pausa=1.0)

        vagas = self._driver.find_elements(By.CSS_SELECTOR, 'a[data-component-name="job-position-link"]')
        for vaga in vagas:
            try:
                titulo_el = vaga.find_element(By.CSS_SELECTOR, 'div[data-sentry-element="JobPositionName"]')
                titulo = titulo_el.text.strip()
                link = vaga.get_attribute("href") or self._driver.current_url

                if not titulo:
                    continue

                if "USINA DA PEDRA" in titulo.upper():
                    lista_vagas.append((titulo, link, "USINA DA PEDRA"))
                    print(f"Vaga Inhire encontrada: {titulo} | Link: {link}")
            except Exception as e:
                print(f"Erro ao processar vaga Inhire: {e}")
                continue

        return lista_vagas


# Alias para retrocompatibilidade
ExtracaoInrihe = ExtracaoInhire

