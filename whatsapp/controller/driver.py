import os

from selenium import webdriver

class WhatsappDriver: 

   
    def __init__(self):
        
        self.dir_path = os.getcwd()

        self.chrome = self.dir_path + '/chromedriver'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir" + self.dir_path + "/profile/Driver")
        self.driver = webdriver.Chrome(self.chrome, chrome_options = self.options)

    def start(self):
        self.driver.get('https://web.whatsapp.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(600)
        