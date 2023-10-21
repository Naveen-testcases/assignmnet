import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#inliziting webdriver

service_obj = Service("C:\Testing\chromedriver-win32\chromedriver-win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=service_obj,options=options)
driver.maximize_window()

#max wait for an element 6secs
driver.implicitly_wait("6")

#input_selector = "#jsondata"
#data need to pass for reflect in web table.
json_data = '[{"name" : "Bob", "age" : 20, "gender": "male"}, {"name": "George", "age" : 42, "gender": "male"}, {"name": "Sara", "age" : 42, "gender": "female"}, {"name": "Conor", "age" : 40, "gender": "male"}, {"name": "Jennifer", "age" : 42, "gender": "female"}]'

#hitiing website and locationing elemnets
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
driver.find_element(By.CSS_SELECTOR,"body div div details summary").click()
driver.find_element(By.CSS_SELECTOR,"#jsondata").clear()
driver.find_element(By.CSS_SELECTOR,"#jsondata").send_keys(json_data)
driver.find_element(By.CSS_SELECTOR,"#refreshtable").click()

#xpath that pointing all names in table
table_names = len(driver.find_elements(By.XPATH,"//tr[*]//*[1]"))
print(table_names)

capured_names= [] #empty list to capter data in list
for r in range(2,table_names+1):
    a = driver.find_element(By.XPATH, "//tr[" + str(r) + "]//*[1]").text #dynamic xpath
    capured_names.append(a) #writes data in list

    print(a)

print("Caputed names on table",capured_names)
# Parse the JSON data
data_list = json.loads(json_data) #converts json data to list

# Extract only the "name" values
names = [item['name'] for item in data_list] #extrating only names in  given json data

# names now contains ['Bob', 'George', 'Sara', 'Conor', 'Jennifer']
print("Given names as Json",names)

#comparing is diven data with caputred data
#or we can use assert captured_names = names it is false assertion will faile
if capured_names == names:
    print("assertion paased")
driver.quit()
