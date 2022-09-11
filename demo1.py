#等待条件
import os
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        path='file:///'+os.path.abspath('html1.html')
        self.driver.get(path)
    def test(self):
        self.driver.find_element('id','btn').click()
        #显示等待
        wait=WebDriverWait(self.driver,3)
        wait.until(EC.text_to_be_present_in_element(By.ID,'id2'),'id 2')
        print('ok')
if __name__ =="__main__":
    case = TestCase()
    case.test()
