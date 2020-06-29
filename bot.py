from time import sleep
from login_info import user, password 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def bet_choice(flag):
        if(flag):
                wait_1_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_bet_lo_button"]')))
                return driver.find_element(By.XPATH, '//*[@id="double_your_btc_bet_lo_button"]')
        wait_1_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_bet_hi_button"]')))
        return driver.find_element(By.XPATH, '//*[@id="double_your_btc_bet_hi_button"]')
                

# start the browser
driver = webdriver.Chrome('./Drivers/chromedriver_win32 v_83/chromedriver.exe')
driver.get("https://freebitco.in/?op=home#")
driver.maximize_window()

# define the waiters
wait_1_min_or = WebDriverWait(driver, 60)
wait_1_hour_or = WebDriverWait(driver, 60*60+60) # waits for one hour and one minute for page 

# Click on login tab
wait_1_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a').click()

# Type login and password and submit
wait_1_min_or.until(EC.presence_of_element_located((By.ID, "login_form_btc_address")))
driver.find_element(By.ID, "login_form_btc_address").send_keys(user)
driver.find_element(By.ID, "login_form_password").send_keys(password)
driver.find_element(By.ID, "login_button").click()

# Close push notification pop-up
wait_1_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]')))
driver.find_element(By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]').click()
# Close cookies warn
wait_1_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a[1]')))
driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()


# click on mutiply tab
wait_1_min_or.until(EC.element_to_be_clickable((By.CLASS_NAME, 'double_your_btc_link')))
driver.find_element(By.CLASS_NAME, 'double_your_btc_link').click()

# check initial balance
wait_1_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="balance"]')))
initial_balance = float(driver.find_element(By.XPATH, '//*[@id="balance"]').text)

prev_balance = actual_balance = initial_balance

bet_flag = True
time = 1

while(abs(actual_balance-initial_balance) <= 0.00000512):

        bet_choice(bet_flag).click()


        wait_1_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="balance"]')))
        actual_balance = float(driver.find_element(By.XPATH, '//*[@id="balance"]').text)
        
        if(actual_balance > prev_balance):
                bet_flag = not bet_flag
                wait_1_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_min"]')))
                driver.find_element(By.XPATH, '//*[@id="double_your_btc_min"]').click()
                time = 1
        else:
                wait_1_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_2x"]')))
                driver.find_element(By.XPATH, '//*[@id="double_your_btc_2x"]').click() 
                time = time*5 
        prev_balance = actual_balance
        
        sleep(time)

        # //*[@id="balance"]
        # //*[@id="double_your_btc_2x"]
        # //*[@id="double_your_btc_min"]

        # //*[@id="double_your_btc_bet_lo_button"]
        # //*[@id="double_your_btc_bet_hi_button"]

if(actual_balance > initial_balance):
        print('YOU WIN!')
else:
        print('Sorry, you lose.')