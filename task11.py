from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://jqueryui.com/droppable/")


frame = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(frame)


drag = driver.find_element(By.ID, "draggable")


drop = driver.find_element(By.ID, "droppable")


actions = ActionChains(driver)
actions.drag_and_drop(drag, drop).perform()


time.sleep(5)

driver.quit()