# Freebitcoin Auto Better

  This is a simple python auto better for the [Freebiicoin site](https://freebitco.in/?r=8521028)

## Warning 
  This bot has NO guarantee to win the bets. Try it at your own risk.

## Use Instructions

  * **Requirements**
    - Instaled Google Chrome Browser.
    - Download Chrome Webdriver for your Chrome version. [Chrome Webdriver Download](https://chromedriver.chromium.org/downloads)
    - Python 3.x. [Python Download](https://www.python.org/downloads/)
    - Active account on the Freebiicoin site, you can create an account [here](https://freebitco.in/?r=8521028)
  
  1. Copy the chromedriver.exe file to the Drivers folder
  2. Open the config.py file to set up your login, password, and the budget. Use a budget in the form of x^2-1 will give an exact value to win or lose the budget.
  3. Open CMD on the project folder and run de command **pip3 install -r requirements.txt**  

  * **You have 3 options to start the bot:**
    1. Run the bot.py file
    2. Run the start.bat file (the command prompt will remain active)
    3. Run the run.vbs file (only opens the browser)
  
  You also could put the run.vbs file in the Windows's starts folder to start the bot with the system boot.
  
## Betting Mode

  The bot bets until you lose or win at least the defined budget.

  It starts betting 1 satoshi.
  In case of a win, it alternates the bet choice lo to hi or hi to lo, and bets 1 satoshi again with a delay of a second.
  In case of loss, it repeats de bet choice and doubles the amount of the bet, the delay will be 5 times longer cumulative at each loss.
