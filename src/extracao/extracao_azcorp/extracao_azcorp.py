from selenium.webdriver.common.by import By
from time import sleep
from src.extracao.extracao_base import ExtracaoBase


class ExtracaoAzcorp(ExtracaoBase):

    def __init__(self) -> None:
        super().__init__()

    def obter_dados_vagas(self) -> list[tuple[str, str, str]]:
        sleep(120)
        lista_vagas: list[tuple[str, str, str]] = []

        self.scroll_ate_o_final(pausa=1.0)

        # 1. Busca cards de oportunidades na página de talentos (azcorp.tech/talentos/)
        cards = self._driver.find_elements(
            By.CSS_SELECTOR,
            "#vagas article, .opportunities article, article.op-card"
        )

        for card in cards:
            try:
                titulo_el = card.find_element(By.TAG_NAME, "h3")
                titulo_vaga = titulo_el.text.strip()

                botao_link = card.find_element(By.TAG_NAME, "a")
                link_vaga = botao_link.get_attribute("href")

                if not titulo_vaga or not link_vaga:
                    continue

                lista_vagas.append((titulo_vaga, link_vaga, "AZCORP"))
                print(f"Vaga/Oportunidade encontrada: {titulo_vaga} | Link: {link_vaga}")
            except Exception as e:
                print(f"Erro ao processar card: {e}")
                continue

        # 2. Busca opções de vagas no formulário do portal de cadastro (azone.azcorp.tech)
        selects = self._driver.find_elements(By.TAG_NAME, "select")
        for select in selects:
            options = select.find_elements(By.TAG_NAME, "option")
            for option in options:
                texto_option = option.text.strip()
                if texto_option and texto_option.lower() != "selecione":
                    url_atual = self._driver.current_url
                    lista_vagas.append((texto_option, url_atual, "AZCORP"))
                    print(f"Vaga no portal AZOne encontrada: {texto_option} | Link: {url_atual}")

        # 3. Fallback para seletor Divi antigo caso a página volte a utilizar
        if not lista_vagas:
            headers = self._driver.find_elements(By.CSS_SELECTOR, "section.et_pb_fullwidth_header")
            for header in headers:
                try:
                    titulo_elemento = header.find_element(By.CSS_SELECTOR, ".et_pb_module_header")
                    titulo_vaga = titulo_elemento.text.strip()

                    botao_link = header.find_element(By.CSS_SELECTOR, "a.et_pb_button")
                    link_vaga = botao_link.get_attribute("href")

                    if not titulo_vaga or not link_vaga:
                        continue

                    lista_vagas.append((titulo_vaga, link_vaga, "AZCORP"))
                except Exception:
                    continue

        return lista_vagas
