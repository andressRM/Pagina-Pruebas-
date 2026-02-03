import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://andressRM.github.io/Pagina-Pruebas-/")
        
        time.sleep(3)

    def testAcciones(self):
       
        liga = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Pagina 2")
        
        if liga is not None:
           
            liga.click()
            print("Click realizado en Pagina 2")
            
           
            time.sleep(3)

            
            nombre = self.driver.find_element(By.ID, "Segundo")
            
            if nombre is not None:
                
                nombre.send_keys("Andres") 
                print("Texto escrito correctamente")
                
                
                time.sleep(5)

    def tearDown(self):
        #self.driver.quit()
        pass