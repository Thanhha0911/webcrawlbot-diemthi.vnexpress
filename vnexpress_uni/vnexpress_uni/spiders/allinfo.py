import scrapy
from scrapy.spiders import SitemapSpider
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from vnexpress_uni.items import VnexpressUniItem

class AlluniSpider(SitemapSpider):
    name = "allinfo"
    allowed_domains = ["diemthi.vnexpress.net"]
    sitemap_urls = ['https://diemthi.vnexpress.net/sitemap.xml']
    #set id = 1 to test the spider 
    sitemap_rules = [('/nhom-nganh/', 'parse')]

    def parse(self, response):
        """Initial parse method called by SitemapSpider"""
        # Use Selenium to handle dynamic content
        self.logger.info(f"Processing sitemap URL: {response.url}")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.get(response.url)
        item =dict(VnexpressUniItem())

        item['urls'] = response.url
        
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.university__table"))
            )
        # Extract the header text
        program_group = driver.find_element(By.CSS_SELECTOR,'.main__content ul strong').text
        item['program_group'] = program_group.strip() 
        # Extract program names from the table
        program_elements = driver.find_elements(By.CSS_SELECTOR, "table.university__table tbody td:nth-child(2) strong:nth-child(2) a")
        program_names = [elem.text.strip() for elem in program_elements if elem.text.strip()]
        item['program_name'] = program_names
        
        # Extract program names from the table
        program_code = driver.find_elements(By.CSS_SELECTOR, "table.university__table tbody td:nth-child(2) span")
        program_codes = [element.text.strip() for element in program_code if element.text.strip()]
        item['program_code'] = program_codes
        # Extract program entry score from the table
        entry_score = driver.find_elements(By.CSS_SELECTOR, "table.university__table tbody td:nth-child(3) span")
        entry_scores = [element.text.strip() for element in entry_score if element.text.strip()]
        item['entry_score'] = entry_scores
        # Extract tuition fee from the table
        tuition_fee = driver.find_elements(By.CSS_SELECTOR, "table.university__table tbody td:nth-child(5)")
        tuition_fees = [element.text.strip() for element in tuition_fee if element.text.strip()]
        item['tuition_fee'] = tuition_fees

        # Extract university names from the table
        university_elements = driver.find_elements(By.CSS_SELECTOR, ".university__benchmark-name a")
        university_names = [elem.text.strip() for elem in university_elements if elem.text.strip()]
        item['university_name'] = university_names

        driver.quit()
        yield item
                
        

