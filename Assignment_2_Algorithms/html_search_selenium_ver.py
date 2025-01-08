from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_html_tags(file_path):
    driver = webdriver.Chrome()
    driver.get(f"file://{file_path}")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        input("Press Enter to continue...")
        
        opening_tags = driver.find_elements(By.CSS_SELECTOR, "*")
        closing_tags = driver.find_elements(By.CSS_SELECTOR, "*")

        if len(opening_tags) == len(closing_tags):
            return "Valid HTML"
        else:
            return "Invalid HTML"
    finally:
        driver.quit()

file_path = input("Enter HTML file path: ")
result = check_html_tags(file_path)
print(result)
