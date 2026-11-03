from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    # Abrir Google
    driver.get("https://www.google.com")
    sleep(2)

    # Abrir Hybridge
    driver.get("https://hybridge.education")
    sleep(2)

    # Abrir OpenAI
    driver.get("https://openai.com")
    sleep(2)

finally:
    # Cerrar el navegador
    driver.quit()