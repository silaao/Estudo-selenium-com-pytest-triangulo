#Para executar este script, digitar no terminal o comando "test_auto_selenium.py"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()


driver.get("http://127.0.0.1:5000/")
time.sleep(2)
#testando triângulo equilátero
driver.find_element_by_name('vertice-1').send_keys("5" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-2').send_keys("5" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-3').send_keys("5")
time.sleep(2)
driver.find_element_by_name('botao-id').click()
time.sleep(6)

#testando triangulo isósceles
driver.find_element_by_name('vertice-1').send_keys("2" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-2').send_keys("5" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-3').send_keys("5")
time.sleep(2)
driver.find_element_by_name('botao-id').click()
time.sleep(6)

#testando triangulo escaleno
driver.find_element_by_name('vertice-1').send_keys("4" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-2').send_keys("7" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-3').send_keys("9")
time.sleep(2)
driver.find_element_by_name('botao-id').click()
time.sleep(6)

#testando triangulo inválido

driver.find_element_by_name('vertice-1').send_keys("2" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-2').send_keys("20" + Keys.TAB)
time.sleep(2)
driver.find_element_by_name('vertice-3').send_keys("80")
time.sleep(2)
driver.find_element_by_name('botao-id').click()
time.sleep(6)

# driver.back()
# driver.forward()
# driver.refresh()
# driver.minimize_window()

driver.quit()