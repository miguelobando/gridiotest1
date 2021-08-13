import unittest
from selenium import webdriver
from time import sleep
from datetime import datetime
import sqlite3



class Waits(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver 
        driver.maximize_window() 
        driver.get('https://www.nordpoolgroup.com/Market-data1/#/nordic/table')

    def test_findland(self):
        driver = self.driver
        sleep(2)
        price = driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[7]').text
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            con = sqlite3.connect('./db/price.db')
            cur = con.cursor()
            cur.execute("insert into energy_price (price, time) values (?, ?)", (price,dt))
            con.commit()
            cur.close()
        except sqlite3.Error as error:
            print(error)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
    