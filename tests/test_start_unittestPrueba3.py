import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindbyIdName(unittest.TestCase):
    
    def setUp(self):
       
        self.driver = webdriver.Edge()
        
        self.driver.get("https://andressRM.github.io/Pagina-Pruebas-/")

    # Pruebas Anteriores
    def testIdName(self):
        elemento = self.driver.find_element(By.ID, "noimportante")
        if elemento is not None:
            print("El elemento by ID fue encontrado")

    def testName(self):
        elemento = self.driver.find_element(By.NAME, "ultimo")
        if elemento is not None:
            print("El elemento by NAME fue encontrado")

  
    
  
    def testClase(self):
        
        elemento = self.driver.find_element(By.CLASS_NAME, "rojo")
        if elemento is not None:
            print("El elemento by CLASS NAME rojo fue encontrado")

    
    def testLink(self):
        
        elemento = self.driver.find_element(By.LINK_TEXT, "Pagina 2")
        if elemento is not None:
            print("El elemento by LINK TEXT Pagina 2 fue encontrado")

    
    def testLinkParcial(self):
        
        elemento = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Pagina")
        if elemento is not None:
            print("El elemento by PARTIAL LINK NAME fue encontrado")

    def tearDown(self):
        self.driver.quit()