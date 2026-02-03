import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindByElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://andressRM.github.io/Pagina-Pruebas-/")

    # Prueba 1:
    def testCeldas(self):
       
        elementos = self.driver.find_elements(By.TAG_NAME, "td")
        
        if elementos is not None:
            print("Se encontraron las celdas:")
           
            for celda in elementos:
                print(celda.text)

    # Prueba 2
    def testFilas(self):
       
        elementos2 = self.driver.find_elements(By.XPATH, "//tr")
        
        if elementos2 is not None:
            print("Las filas fueron encontradas")
            
            print("Cantidad de filas encontradas:", len(elementos2))

    def tearDown(self):
        self.driver.quit()