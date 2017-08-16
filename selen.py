# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import time

from lekarstvo import Lekarstvo

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):

    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def init_apteki():
    wd.get("https://allapteki.ru/")
    wd.find_element_by_css_selector("h4.mainiconh4.mainiconh4_focus").click()
    wd.find_element_by_id("Labelt1").click()
    if not wd.find_element_by_id("Radiot1").is_selected():
        wd.find_element_by_id("Radiot1").click()
    wd.find_element_by_id("inputl1").click()
    wd.find_element_by_id("inputl1").clear()


def search_apteki():
    wd.find_element_by_xpath("//div[@id='open_close']//p[.='ПОИСК']").click()
    wd.find_element_by_id("inputl1").click()
    wd.find_element_by_id("inputl1").clear()


def choice_togliatty():
    wd.find_element_by_xpath("//div[@id='open_close']//p[.='ПОИСК']").click()
    wd.find_element_by_link_text("САМАРА").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
    wd.find_element_by_id("inputl1").click()
    wd.find_element_by_id("inputl1").clear()

def choice_samara():
    wd.find_element_by_xpath("//div[@id='open_close']//p[.='ПОИСК']").click()
    wd.find_element_by_link_text("ТОЛЬЯТТИ").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='САМАРА']").click()
    wd.find_element_by_id("inputl1").click()
    wd.find_element_by_id("inputl1").clear()

def search_lekarstvo(lekarstvo):
    wd.find_element_by_id("inputl1").send_keys(lekarstvo.name)
    wd.find_element_by_id("searchb").click()

def city_apteka(city):
    wd.find_element_by_xpath("//div[@id='townchose_chosen']/a/div/b").click()
    if city == "Тольятти":
        wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
    else:
        wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='САМАРА']").click()

try:
    init_apteki()
    search_lekarstvo(Lekarstvo(name = "парацетамол"))
    time.sleep(5)
    search_apteki()
    search_lekarstvo(Lekarstvo(name = "нурофен"))
    time.sleep(5)
    search_apteki()
    city_apteka("Тольятти")
    #choice_togliatty()
    search_lekarstvo(Lekarstvo(name = "амиксин"))
    time.sleep(5)
    search_apteki()
    city_apteka("Самара")
    #choice_samara()
    search_lekarstvo(Lekarstvo(name = "аугментин"))
    time.sleep(5)
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
