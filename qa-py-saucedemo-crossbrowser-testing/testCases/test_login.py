from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()

    # Testing the homepage title of the page
    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Swag Labs":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            assert False

    # Testing login-ing with valid credentials
    def test_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.lp.logout()
        self.driver.close()

