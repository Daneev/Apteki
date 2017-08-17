import time

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Application:

    def __init__(self):
        self.wd = WebDriver()


    def init_apteki(self):
        wd = self.wd
        wd.get("https://allapteki.ru/")
        try:
            element = WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mainiconh4")))
        finally:
            time.sleep(1)
            element = wd.find_elements_by_class_name("mainiconh4")
            element[2].click()
            wd.find_element_by_id("Labelt1").click()
            if not wd.find_element_by_id("Radiot1").is_selected():
                wd.find_element_by_id("Radiot1").click()
            wd.find_element_by_id("inputl1").click()
            wd.find_element_by_id("inputl1").clear()


    def search_apteki(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='open_close']//p[.='ПОИСК']").click()
        wd.find_element_by_id("inputl1").click()
        wd.find_element_by_id("inputl1").clear()


    def choice_togliatty(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='open_close']//p[.='ПОИСК']").click()
        wd.find_element_by_link_text("САМАРА").click()
        wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
        wd.find_element_by_id("inputl1").click()
        wd.find_element_by_id("inputl1").clear()

    def choice_samara(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='open_close']//p[.='ПОИСК']").click()
        wd.find_element_by_link_text("ТОЛЬЯТТИ").click()
        wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='САМАРА']").click()
        wd.find_element_by_id("inputl1").click()
        wd.find_element_by_id("inputl1").clear()

    def search_lekarstvo(self, lekarstvo):
        wd = self.wd
        wd.find_element_by_id("inputl1").send_keys(lekarstvo.name)
        wd.find_element_by_id("searchb").click()

    def city_apteka(self, city):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='townchose_chosen']/a/div/b").click()
        if city == "Тольятти":
            wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
        else:
            wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='САМАРА']").click()

    def quit(self):
        wd = self.wd
        wd.quit()