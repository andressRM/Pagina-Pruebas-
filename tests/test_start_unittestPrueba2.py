import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindbyIdName(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        
        self.driver.get("https://andressrm.github.io/Pagina-Pruebas-/")

    # Prueba 1: 
    def testIdName(self):
        elemento = self.driver.find_element(By.ID, "noimportante")
        if elemento is not None:
            print("El elemento by ID fue encontrado")

    # Prueba 2
    def testName(self):
        
        elemento2 = self.driver.find_element(By.NAME, "ultimo")
        if elemento2 is not None:
            print("El elemento by NAME fue encontrado")

    def tearDown(self):
        self.driver.quit()