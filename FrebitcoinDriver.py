from config import chrome_driver, budget, user, password
from selenium import webdriver
from decimal import Decimal
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FreebitcoinDriver:
  driver = webdriver.Chrome(chrome_driver)
  wait_a_min_or = WebDriverWait(driver, 60)
    
  def start(self):

    self.driver.get("https://freebitco.in/?op=home#")
    self.driver.maximize_window()
    self.login(user, password)
    self.go_to_mutiplyBTC()
    self.bet(budget)

  def login(self, user, password):
    # Click on login tab
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a')))
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a').click()

    # Type login and password and submit
    self.wait_a_min_or.until(EC.presence_of_element_located((By.ID, "login_form_btc_address")))
    self.driver.find_element(By.ID, "login_form_btc_address").send_keys(user)
    self.driver.find_element(By.ID, "login_form_password").send_keys(password)
    self.driver.find_element(By.ID, "login_button").click()

    # Close push notification pop-up
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]')))
    self.driver.find_element(By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]').click()
    # Close cookies warn
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a[1]')))
    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()
  
  def go_to_mutiplyBTC(self):
    # click on mutiply tab
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.CLASS_NAME, 'double_your_btc_link')))
    self.driver.find_element(By.CLASS_NAME, 'double_your_btc_link').click()


  def bet_choice(self, flag):
    if(flag):
      self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_bet_lo_button"]')))
      return self.driver.find_element(By.XPATH, '//*[@id="double_your_btc_bet_lo_button"]')
    self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_bet_hi_button"]')))
    return self.driver.find_element(By.XPATH, '//*[@id="double_your_btc_bet_hi_button"]')
                
  def bet(self, budget):
    # check initial balance
    self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="balance"]')))
    initial_balance = Decimal(self.driver.find_element(By.XPATH, '//*[@id="balance"]').text)

    prev_balance = actual_balance = initial_balance

    bet_flag = True
    time = 1

    while(abs(actual_balance-initial_balance) <= budget):

      sleep(time)
      
      self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="balance"]')))
      actual_balance = Decimal(self.driver.find_element(By.XPATH, '//*[@id="balance"]').text)
      
      if(actual_balance > prev_balance):
        bet_flag = not bet_flag
        self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_min"]')))
        self.driver.find_element(By.XPATH, '//*[@id="double_your_btc_min"]').click()
        time = 1
      else:
        self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="double_your_btc_2x"]')))
        self.driver.find_element(By.XPATH, '//*[@id="double_your_btc_2x"]').click() 
        time = time*5 
        
      self.bet_choice(bet_flag).click()
      prev_balance = actual_balance
            

            

    if(actual_balance > initial_balance):
      print('YOU WIN!')
    else:
      print('Sorry, you lose.')
    
    print('Bot has stoped.')
