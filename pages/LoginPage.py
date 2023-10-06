from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    txt_login_userName = "userName"
    txt_login_pwd = "password"
    btn_submit = "submit"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.txt_login_userName).clear()
        self.driver.find_element(By.NAME, self.txt_login_userName).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.txt_login_pwd).clear()
        self.driver.find_element(By.NAME, self.txt_login_pwd).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.NAME,self.btn_submit).click()




