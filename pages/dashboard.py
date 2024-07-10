from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_button = (By.XPATH,"//span[.='Admin']")
        self.search_bar = (By.XPATH,"//input[@placeholder='Search']")
        self.page_title = (By.XPATH,"//h6[normalize-space()='Admin']")
    
    def search_dashboard(self,text):
        self.driver.find_element(*self.search_bar).send_keys(text)
    
    def click_admin(self):
        self.driver.find_element(*self.admin_button).click()

    def dashboard_page_title(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*self.page_title).text
    
    
        
        



