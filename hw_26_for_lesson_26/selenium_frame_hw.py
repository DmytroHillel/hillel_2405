import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Ініціалізуємо драйвер Chrome
driver = webdriver.Chrome()

# Відкриваємо головну сторінку
driver.get("http://localhost:8000/dz.html")

"""Перший Фрейм"""
# Знаходження та перехід до Фрейму
frame1 = driver.find_element(By.XPATH, "//iframe[@id='frame1']")
driver.switch_to.frame(frame1)

# Введення секретного тексту
secret_text_input = driver.find_element(By.ID, "input1")
secret_text_input.send_keys("Frame1_Secret")

 # Натискання кнопки
check_button = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
check_button.click()

# Перевірка введеного тексту
dialog_text = driver.switch_to.alert.text
expected_dialog_text = "Верифікація пройшла успішно!"  # Очікуваний текст

if dialog_text == expected_dialog_text:
    print("Верифікація пройшла успішно!")
else:
    print("Введено неправильний текст!")

# Закриття вікна
driver.switch_to.alert.accept()

# Повернення до головного контенту
driver.switch_to.default_content()


"""Другий Фрейм"""
# Знаходження та перехід до Фрейму
frame2 = driver.find_element(By.XPATH, "//iframe[@id='frame2']")
driver.switch_to.frame(frame2)

# Введення секретного тексту
secret_text_input_2 = driver.find_element(By.ID, "input2")
secret_text_input_2.send_keys("Frame2_Secret")

 # Натискання кнопки
check_button = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
check_button.click()

# Перевірка введеного тексту
dialog_text = driver.switch_to.alert.text
expected_dialog_text = "Верифікація пройшла успішно!"  # Очікуваний текст

if dialog_text == expected_dialog_text:
    print("Верифікація пройшла успішно!")
else:
    print("Введено неправильний текст!")

# Закриття вікна
driver.switch_to.alert.accept()

# Повернення до головного контенту
driver.switch_to.default_content()

# Зачекати 5 секунд перед завершенням
time.sleep(5)

# Закриття браузера
driver.quit()