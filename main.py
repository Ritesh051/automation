import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from oauth2client.service_account import ServiceAccountCredentials
import gspread

options = Options()
# Specify the path to chromedriver.exe if it's not in the same directory as your script
options.add_argument("executable_path=chromedriver")

driver = webdriver.Chrome(options=options)
driver.get("Enter the URL of the website")

Scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

# Correct the path to your JSON credentials file
Credentials = ServiceAccountCredentials.from_json_keyfile_name("Your key.json")
file = gspread.authorize(credentials=Credentials)
sheet = file.open("Google sheet Name")

sheet = sheet.sheet1

for i in range(11, 25):
    department_name = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[2]/td/b").text
    services = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[3]/td/a").text
    location = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[1]/td/span[1]").text
    biz_value = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[1]/td/span[2]/i").text
    Bid_before = driver.find_element(By.XPATH, f"/html/body/form/div[3]/div[1]/div/div[6]/div[1]/div[1]/div[3]/div[3]/div/div/div[{i}]/div[1]/table/tbody/tr[1]/td/span[3]").text
    print("----------------------------------------")
    print("Department Name:", department_name)
    print(services)
    print("Location:", location)
    print("Business Value:", biz_value)
    print(Bid_before)

    sheet.update_acell('A'+str(i+1), department_name)
    sheet.update_acell('B'+str(i+1), services)
    sheet.update_acell('C'+str(i+1), location)
    sheet.update_acell('D'+str(i+1), biz_value)
    sheet.update_acell('E'+str(i+1), Bid_before)

driver.quit()
