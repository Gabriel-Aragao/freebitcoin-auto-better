from login import user, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 
driver = webdriver.Chrome('drivers\chromedriver')
driver.get("https://freebitco.in/?op=home#")
driver.maximize_window()
wait_1_min_or = WebDriverWait(driver, 60)
wait_1_hour_or = WebDriverWait(driver, 60*60+60) # waits for one hour and one minute for page refresh delay
#driver.implicitly_wait(10) # seconds


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


while(True):

        driver.refresh()
        # Click free roll
        wait_1_hour_or.until(EC.element_to_be_clickable((By.ID, 'free_play_form_button')))
        driver.find_element(By.ID, 'free_play_form_button').click()

        # Close mutiply BTC pop-up
        try:
                wait_1_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="myModal22"]/a')))
                driver.find_element(By.XPATH, '//*[@id="myModal22"]/a').click()
        except:
                pass

        try:
                wait_1_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="play_without_captchas_button"]/span')))
                driver.find_element(By.XPATH, '//*[@id="play_without_captchas_button"]/span').click()

        except:
                pass

        try:
                wait_1_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="free_play_link_li"]/a')))
                driver.find_element(By.XPATH, '//*[@id="free_play_link_li"]/a').click()

        except:
                pass
        
