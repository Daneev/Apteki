# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def sity_apteka():
    wd.find_element_by_xpath("//div[@id='townchose_chosen']/a/div/b").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='АЛЕКСЕЕВКА']").click()


try:
    wd.get("https://allapteki.ru/")
    wd.find_element_by_css_selector("h4.mainiconh4.mainiconh4_focus").click()
    wd.find_element_by_id("Labelt1").click()
    if not wd.find_element_by_id("Radiot1").is_selected():
        wd.find_element_by_id("Radiot1").click()
    wd.find_element_by_link_text("Выберите город...").click()
    wd.find_element_by_css_selector("li.active-result").click()
    wd.find_element_by_link_text("Выберите город...").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
    wd.find_element_by_link_text("Выберите город...").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
    wd.find_element_by_link_text("ТОЛЬЯТТИ").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']/div/div/input").click()
    wd.find_element_by_css_selector("li.active-result").click()
    wd.find_element_by_link_text("САМАРА").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']/a/div/b").click()
    wd.find_element_by_css_selector("li.active-result").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']/a/div/b").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']//li[.='ТОЛЬЯТТИ']").click()
    wd.find_element_by_xpath("//div[@id='townchose_chosen']/a/div/b").click()
    wd.find_element_by_css_selector("li.active-result").click()
    sity_apteka()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
