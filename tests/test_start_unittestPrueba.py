import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindbyIdName(unittest.TestCase):
    
    
    def setUp(self):
        
        self.driver = webdriver.Edge()
        
        self.driver.get("https://andressRM.github.io/Pagina-Pruebas-/")

    
    def testIdName(self):
        
        elemento = self.driver.find_element(By.ID, "noimportante")
        
        
        if elemento is not None:
            print("El elemento by ID fue encontrado")

    def tearDown(self):
        self.driver.quit()