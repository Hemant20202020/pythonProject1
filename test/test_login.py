import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage
from utilities import customLogger
from utilities.excelUtils import getRowCount, readData
from utilities.readConfigData import ReadConfig


class TestLogin:
    base_url = ReadConfig.getCommonData("commonData","base_url")
    userName = ReadConfig.getCommonData("commonData","userName")
    password = ReadConfig.getCommonData("commonData","password")
    logger = customLogger.get_logger("LoginPage")
    path = ".\\testdata\\Book1.xlsx"

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_verifying_home_page_title(self,setup):
        self.logger.info("=============== TC01 verifying home page title ==============")
        self.driver = setup
        self.driver.get(self.base_url)
        title = self.driver.title
        self.logger.info("=============== getting title = "+title)
        if title == ReadConfig.getCommonData("message","home_title"):
            self.driver.save_screenshot(".\\screenshots\\home_page_title.png")
            self.logger.info("=============== successful home page title ==============")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\home_page_title_failed.png")
            self.logger.info("=============== failed home page title ==============")
            assert False
        self.driver.close()

    def test_loginPage_validation(self,setup):
        self.logger.info("=============== TC02 verifying login page title ==============")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.click_submit_button()
        title = self.driver.title
        self.logger.info("=============== getting login page title = "+title)
        if title == ReadConfig.getCommonData("message","login_title"):
            self.driver.save_screenshot(".\\screenshots\\login_page_title.png")
            self.logger.info("=============== successful login title ==============")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\login_page_title_failed.png")
            self.logger.info("=============== failed login title ==============")
            assert False

        self.driver.close()

    @pytest.mark.regression
    def test_excel_loginPage_validation(self,setup):
        self.logger.info("=============== TC03 verifying login page title ==============")
        rows = getRowCount(self.path,"Sheet1")
        test_status = []
        for r in range(1,rows+1):
            username = readData(self.path,"Sheet1",r,1)
            password = readData(self.path,"Sheet1",r,2)
            result = readData(self.path,"Sheet1",r,3)
            self.driver = setup
            self.driver.get(self.base_url)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(username)
            self.lp.setPassword(password)
            self.lp.click_submit_button()
            title = self.driver.title
            self.logger.info("=============== getting login page title = "+title)
            if title == ReadConfig.getCommonData("message","login_title"):
                if result == "Pass":
                    self.driver.save_screenshot(".\\screenshots\\login_page_title.png")
                    self.logger.info("=============== successful login title ==============")
                    test_status.append("Pass")

                elif result == "Fail":
                    self.driver.save_screenshot(".\\screenshots\\login_page_title_failed.png")
                    self.logger.info("=============== failed login title ==============")
                    test_status.append("Fail")
            elif title != ReadConfig.getCommonData("message","login_title"):
                if result == "Pass":
                    self.driver.save_screenshot(".\\screenshots\\login_page_title.png")
                    self.logger.info("=============== Fail login title ==============")
                    test_status.append("Fail")

                elif result == "Fail":
                    self.driver.save_screenshot(".\\screenshots\\login_page_title_failed.png")
                    self.logger.info("=============== passed login title ==============")
                    test_status.append("Pass")

            if "Fail" not in test_status:
                assert True
            else:
                assert False




