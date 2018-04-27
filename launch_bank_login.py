from selenium import webdriver
import time

def navigate_to_bank(url, chromedriver_path):
	driver = webdriver.Chrome(chromedriver_path)
	driver.get(url)

def login_to_splash_page(username):
	bank_login_entry_script = 'var i, list = document.querySelectorAll(".button-online-banking")[0];var click = new Event("click");list.dispatchEvent(click);var inputField = document.querySelector("#UserName");inputField.value="', username, '";var loginButton = document.querySelector(".login-button");loginButton.click();'

	driver.execute_script(bank_login_entry_script);

def navigate_password_page(password):
	bank_password_entry_script = 'var passwordField=document.querySelector("#Password");passwordField.value="', password, '";var signIn=document.querySelector("input[value=\'Sign In\']");signIn.click()'

	driver.execute_script(bank_password_entry_script)

def pay_credit_card():
	navigate_to_bank('https://lmcu.org', '/Users/John/SOFTWAREPROJECTS/LMCU_CC_Automator/chromedriver')
	login_to_splash_page(#username here)
	navigate_password_page(#password here)

if __name__ == '__main__':
	pay_credit_card()