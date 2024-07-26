# 1. Open Web Browser (Chrome/Firefox/Edge).
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin).
# 4. Enter password (admin123).
# 5. Click on Login.
# 6. Capture title of the home page. (Actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
# 8. Close browser. webdriver is a module which is available in
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# serv_obj = Service(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, 'text')
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.ID, 'password').send_keys('admin123')
driver.find_element(By.ID, 'oxd-button').click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()