import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initializing webdriver
service_obj = Service("C:\Testing\chromedriver-win32\chromedriver-win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()

# Set maximum wait time for an element to 6 seconds
driver.implicitly_wait(6)

# Data to pass to the web table.
json_data = '[{"name" : "Bob", "age" : 20, "gender": "male"}, {"name": "George", "age" : 42, "gender": "male"}, {"name": "Sara", "age" : 42, "gender": "female"}, {"name": "Conor", "age" : 40, "gender": "male"}, {"name": "Jennifer", "age" : 42, "gender": "female"}]'

# Navigate to the website and locate elements
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
driver.find_element(By.CSS_SELECTOR, "body div div details summary").click()
driver.find_element(By.CSS_SELECTOR, "#jsondata").clear()
driver.find_element(By.CSS_SELECTOR, "#jsondata").send_keys(json_data)
driver.find_element(By.CSS_SELECTOR, "#refreshtable").click()

# Locate the table element
table = driver.find_element(By.XPATH, "//table[@id='dynamictable']").text

# Split the text into lines and process each line
lines = table.split('\n')

# Parse the JSON data into a list of dictionaries
data_list = json.loads(json_data)

# Iterate through the data and compare each row with the formatted data
for i, line in enumerate(lines[2:]):
    formatted_data = f"{data_list[i]['name']} {data_list[i]['age']} {data_list[i]['gender']}"
    assert line == formatted_data
    print(f"Row {i + 1} matches: {line}")

driver.quit()
