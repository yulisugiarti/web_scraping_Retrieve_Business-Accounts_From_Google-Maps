from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.google.com/maps/search/pabrik+di+bandung/@-6.8084251,106.902712,10z/data=!3m1!4b1?entry=ttu")

company_list = driver.find_elements(By.CLASS_NAME, value="Nv2PK")

data = []

for x in range(len(company_list)):
    element = company_list[x].text
    data.append(element)

data_dictionary = {
    "Data Usaha": data
}

table = pandas.DataFrame(data_dictionary)
print(table)

table.to_csv('datausaha_Bandung.csv', index=False)
