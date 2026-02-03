import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://andressRM.github.io/Pagina-Pruebas-/")
        # 1. TRUCO: Esperar 3 segundos para asegurar que la página cargó completamente
        time.sleep(3)

    def testAcciones(self):
        # 2. CAMBIO: Usamos PARTIAL_LINK_TEXT que es más "todo terreno"
        # Busca cualquier enlace que tenga las palabras "Pagina 2"
        liga = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Pagina 2")
        
        if liga is not None:
            # Hacer CLICK
            liga.click()
            print("Click realizado en Pagina 2")
            
            # Espera a que cargue la nueva página
            time.sleep(3)

            # 3. Buscar el campo "Nombre" en la nueva página
            # El ID debe coincidir con el de tu archivo nuevaPagina.html
            nombre = self.driver.find_element(By.ID, "Segundo")
            
            if nombre is not None:
                # Escribir
                nombre.send_keys("Andres") 
                print("Texto escrito correctamente")
                
                # Pausa final para disfrutar el éxito
                time.sleep(5)

    def tearDown(self):
        self.driver.quit()