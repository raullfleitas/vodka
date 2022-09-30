from asyncio import _enter_task
from tkinter import BOTTOM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./Nueva Raul/chromedriver.exe")
driver.maximize_window()
driver.get ("https://www.redcoatic.com/login")
time.sleep (3)
email = "fkeitasraularielokk@gmail.com"
password = "Posadas1155"
email_textfield = driver.find_element("id", ":r0:")
password_textfield = driver.find_element("id",":r1:")
#login_button = driver.find_element("data-testid", "login-button")
email_textfield.send_keys(email)
time.sleep (1)
password_textfield.send_keys(password)
time.sleep (1)
Keys.ENTER
time.sleep (1)

