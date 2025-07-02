from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

trips = {
    "Barcelona to Floripa": "https://www.google.com/travel/flights?tfs=CBwQARohagwIAxIIL20vMDFmNjJyEQgDEg0vZy8xMWJjNnhscHBkQAFIAXABggELCP___________wGYAQI&tfu=KgIIAw",
    "Floripa to Buenos Aires": "https://www.google.com/travel/flights?tfs=CBwQARoiahEIAhINL2cvMTFiYzZ4bHBwZHINCAMSCS9tLzAxbHk1bRoiag0IAxIJL20vMDFseTVtchEIAhINL2cvMTFiYzZ4bHBwZEABSAFwAYIBCwj___________8BmAEB&tfu=KgIIAw",
    "Buenos Aires to Rio": "https://www.google.com/travel/flights?tfs=CBwQARodag0IAxIJL20vMDFseTVtcgwIAxIIL20vMDZnbXIaHWoMCAMSCC9tLzA2Z21ycg0IAxIJL20vMDFseTVtQAFIAXABggELCP___________wGYAQE&tfu=KgIIAw",
    "Rio to Buenos Aires": "https://www.google.com/travel/flights?tfs=CBwQARodagwIAxIIL20vMDZnbXJyDQgDEgkvbS8wMWx5NW0aHWoNCAMSCS9tLzAxbHk1bXIMCAMSCC9tLzA2Z21yQAFIAXABggELCP___________wGYAQE&tfu=KgIIAw",
    "Rio to Barcelona": "https://www.google.com/travel/flights?tfs=CBwQARocagwIAxIIL20vMDZnbXJyDAgDEggvbS8wMWY2MhocagwIAxIIL20vMDFmNjJyDAgDEggvbS8wNmdtckABSAFwAYIBCwj___________8BmAEB&tfu=KgIIAw",
    "Buenos Aires to Barcelona": "https://www.google.com/travel/flights?tfs=CBwQARodag0IAxIJL20vMDFseTVtcgwIAxIIL20vMDFmNjIaHWoMCAMSCC9tLzAxZjYycg0IAxIJL20vMDFseTVtQAFIAXABggELCP___________wGYAQE&tfu=KgIIAw",
}

def extrair_voos(destination, url):
    options = EdgeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    driver.get(url)

    print(f"\nLooking for flights for day {destination}")

    time.sleep(3)

    # Click in date input
    dateInput = driver.find_element(By.CSS_SELECTOR, '[aria-describedby="i34"]')
    dateInput.click()

    time.sleep(5)

    # Extract dates and its respectives prices
    date_cells = driver.find_elements(By.XPATH, '//div[@role="gridcell" and @jsname="mG3Az"]')

    count = 0
    for cell in date_cells:
        if count >= 60:
            break 

        date = cell.find_element(By.XPATH, './/div[@jsname="nEWxA"]').get_attribute('aria-label')
        try:
            price_element = cell.find_element(By.XPATH, './/div[@jsname="qCDwBb"]')
            price = price_element.text if price_element.text else "Price unavailable"
        except:
            price = "Price unavailable"

        print(f"Date: {date}, Price: {price}")
        count += 1
    driver.quit()

for destination, url in trips.items():
    extrair_voos(destination, url)