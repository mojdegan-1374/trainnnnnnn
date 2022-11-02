from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re
#import convert_numbers
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) , options=options)

driver.get("https://www.iranjib.ir/showgroup/23/realtime_price/")

print ("Headless Chrome Initialized")

tala = driver.find_element(By.ID, 'f_127_63_pr').text
seke = driver.find_element(By.ID, 'f_87_63_pr').text
dollar = driver.find_element(By.ID, 'f_16390_68_pr').text



pattern = r"(?m)(?<=\d)\d{3}(?=(?:\d{3})*$)"

# print("Tala: ", re.sub(pattern, r",\g<0>", convert_numbers.persian_to_english(tala)))
# print("Seke: ", re.sub(pattern, r",\g<0>", convert_numbers.persian_to_english(seke)))
# print("Dollar: ", re.sub(pattern, r",\g<0>", convert_numbers.persian_to_english(dollar)))

print("Tala: ", re.sub(pattern, r",\g<0>", tala))
print("Seke: ", re.sub(pattern, r",\g<0>", seke))
print("Dollar: ", re.sub(pattern, r",\g<0>", dollar))

driver.quit()