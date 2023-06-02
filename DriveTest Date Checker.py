import undetected_chromedriver as uc 
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

license_number = "" # input('Enter your driver\'s license number, exactly as it appears on your license: ')
license_expiry_date = "" # input('Enter your driver\'s license expiry date, exactly as it appears on your license: ')

options = uc.ChromeOptions() 
#options.headless = True 
driver = uc.Chrome(use_subprocess=True, options=options) 
driver.delete_all_cookies()
driver.get("https://drivetest.ca/dtbookingngapp/registration/confirmRegistration") 
driver.maximize_window() 


# Wait for the page to load
try:
    wait = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign in')]")))
except TimeoutException:
    print ("Loading took too much time.")


driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]").click()

# Wait
try:
    wait = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-app-layout/div/div/mat-sidenav-container/mat-sidenav-content/main/app-registration-confirmation/div/div/form/div[4]/app-progress-button")))
except TimeoutException:
    print ("Loading took too much time.")

driver.find_element("name",'driverLicenceNumber').send_keys(license_number)
driver.find_element("id",'driverLicenceExpiry').send_keys(license_expiry_date)

time.sleep(1)

driver.find_element(By.XPATH,"/html/body/app-root/app-app-layout/div/div/mat-sidenav-container/mat-sidenav-content/main/app-registration-confirmation/div/div/form/div[4]/app-progress-button").click()

# Wait
try:
    wait = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headingDiv"]/div[3]/div/div/div[2]/div[3]/ul/li[2]/button')))
except TimeoutException:
    print ("Loading took too much time.")


driver.find_element(By.XPATH,'//*[@id="headingDiv"]/div[3]/div/div/div[2]/div[3]/ul/li[2]/button').click()

# Wait
try:
    wait = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-dialog-0"]/app-appt-modal/div[2]/div[2]/div[1]/app-progress-button/button/span[1]/span')))
except TimeoutException:
    print ("Loading took too much time.")

driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-appt-modal/div[2]/div[2]/div[1]/app-progress-button/button/span[1]/span').click()


# Wait
try:
    wait = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/app-drivetest-locations/div/div/div[5]/app-progress-button/button')))
except TimeoutException:
    print ("Loading took too much time.")

driver.find_element(By.XPATH, '//*[@id="targetLoc34"]').click()
driver.find_element(By.XPATH, '//*[@id="main"]/app-drivetest-locations/div/div/div[5]/app-progress-button/button').click()


# Go through every date in the availability calendar and see if it has an opening based on its CSS class
#dates = ['//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[3]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[4]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[5]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[6]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td[7]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[1]/div/div/div/a', '//*[@id="driver-info"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td[2]/div/div/div/a']
# dates = ['//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[4]/div[5]/app-date-selection']

dates = ['//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[5]/div[2]/app-date-selection/button',
     '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[5]/div[3]/app-date-selection/button',
     '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[5]/div[4]/app-date-selection/button',
     '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[5]/div[5]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[5]/div[6]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[6]/div[2]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[6]/div[3]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[6]/div[4]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[6]/div[5]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[6]/div[6]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[7]/div[2]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[7]/div[3]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[7]/div[4]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[7]/div[5]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[7]/div[6]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[8]/div[2]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[8]/div[3]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[8]/div[4]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[8]/div[5]/app-date-selection/button',
    '//*[@id="main"]/app-select-date/div/app-calendar-selection-container/div[8]/div[6]/app-date-selection/button'
    ]



print(len(dates))

# time.sleep(1)
# driver.find_element(By.XPATH,'/html/body/app-root/app-app-layout/div/div/mat-sidenav-container/mat-sidenav-content/main/app-select-date/div/app-calendar-selection-container/div[1]/button[2]/span[1]/mat-icon').click()
# time.sleep(1)


# available_dates = []
# for i in dates:
#     date = driver.find_element(By.XPATH,i)
#     availability = str(date.get_attribute("class"))

# #    print()
# #    print(availability)
# #    print()
#     if "date-available" in availability:
#         print("yuh")
#         available_dates.append(str(date.get_attribute("title")))


# for i in available_dates:
#             print(str(i))

while True:
    pass

driver.close()