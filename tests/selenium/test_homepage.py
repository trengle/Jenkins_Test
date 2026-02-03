import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage_loads():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:5000")
    time.sleep(1)
    assert "Hello" in driver.page_source
    driver.quit()
