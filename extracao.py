from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

# Remova esta linha se quiser ver o navegador
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
print(type(driver))

try:
    url = "https://bixtecnologia.inhire.app/vagas"
    driver.get(url)

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR,
             'a[data-component-name="job-position-link"]')
        )
    )

    vagas = driver.find_elements(
        By.CSS_SELECTOR,
        'a[data-component-name="job-position-link"]'
    )

    for vaga in vagas:
        try:
            titulo = vaga.find_element(
                By.CSS_SELECTOR,
                'div[data-sentry-element="JobPositionName"]'
            ).text

            link = vaga.get_attribute("href")

            print(f"Título: {titulo}")
            print(f"Link: {link}")
            print("-" * 50)

        except Exception as e:
            print(f"Erro ao processar vaga: {e}")

finally:
    driver.quit()