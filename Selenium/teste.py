from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Asimov Academy")
search_box.submit()

try:
	# Espera até que o título contenha o termo buscado, por até 20 segundos
	WebDriverWait(driver, 20).until(
		EC.title_contains("Asimov Academy")
	)
	print("Título da página:", driver.title)
except TimeoutException:
	print("Tempo esgotado ao esperar pelos resultados da busca.")
finally:
	print("Fechando o navegador.")