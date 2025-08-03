import urllib.request
from urllib.error import HTTPError
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# Настройки для headless режима
options = Options()
#options.add_argument("--headless")

# Инициализация драйвера Chrome
service = ChromeService()
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

# URL целевой страницы
url = "https://www.sravni.ru/biznes-marketplace/info/top-marketplejsov-rossii-i-mira/"
driver.get(url)

# Создание папки для сохранения изображений
SAVE_DIR = "yandex_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Выбор всех узлов изображений на странице
image_html_nodes = driver.find_elements(By.TAG_NAME, "img")

image_urls = []

# Извлечение URL-адресов изображений
for image_html_node in image_html_nodes:
    try:
        image_url = image_html_node.get_attribute("src")
        if image_url and image_url.startswith("http"):
            image_urls.append(image_url)
    except StaleElementReferenceException:
        continue

# Добавляем заголовок User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Скачивание и сохранение изображений
for index, image_url in enumerate(image_urls, start=1):
    print(f"Скачивание изображения {index} ...")
    file_name = os.path.join(SAVE_DIR, f"image_{index}.jpg")

    try:
        req = urllib.request.Request(image_url, headers=headers)
        with urllib.request.urlopen(req) as response, open(file_name, "wb") as file:
            file.write(response.read())

        print(f"Изображение сохранено: {file_name}")

    except HTTPError as e:
        print(f"Ошибка при скачивании изображения {index}: {e}")

# Закрытие браузера
driver.quit()