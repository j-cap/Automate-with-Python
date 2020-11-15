
# sendMail.py - Send text to email, both specified via command line

import pyinputplus
import time
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

NSE = "no such element"
CENTER = 30

def send_mail(mailAddress, pw, mailMessage):
    # TODO: open browser and email program
    # Open page
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://hotmail.com")
    time.sleep(0.2)
    # Click login
    print("Login".center(CENTER, "-"))
    signin_link = driver.find_element_by_link_text("Anmelden")
    signin_link.click()
    time.sleep(1)
    # Insert email address
    print("Entering address".center(CENTER, "-"))
    login_username = driver.find_element_by_xpath('//*[@id="i0116"]')
    login_username.send_keys("delta_kappa_omega@hotmail.com")
    login_username.send_keys(Keys.ENTER)
    time.sleep(1)
    # Insert pw
    print("Entering password".center(CENTER, "-"))
    login_pw = driver.find_element_by_xpath('//*[@id="i0118"]') 
    login_pw.send_keys(pw)
    time.sleep(1)
    #login_pw.send_keys(Keys.Enter)
    login = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    login.click()
    time.sleep(2)
    print("Wait for complete login".center(CENTER, "-"))
    # falls nutzungsbedingungen aktualisiert werden m+ssen
    try:
        termsAndConditions = driver.find_element_by_xpath('//*[@id="iNext"]')
        termsAndConditions.click()
    except Exception as e:
        if NSE in str(e):
            pass
        
    # falls frage nach angemeldet bleiben kommt
    try:
        dont_stay_logged = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
        dont_stay_logged.click()
    except Exception as e:
        if NSE in str(e):
            pass
    # falls cookies
    try:
        accept_cookies = driver.find_element_by_xpath("//*[@id='id__950']")
        accept_cookies.click()
    except Exception as e:
        if NSE in str(e):
            pass

    # TODO: write the mail and send it
    # Open new mail
    newmail = driver.find_element_by_xpath('//*[@id="id__3"]')
    newmail.click()
    time.sleep(1)
    # Insert text
    mail_text = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]')
    mail_text.send_keys(mailMessage)
    time.sleep(1)

    reciever_mail = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input')
    reciever_mail.send_keys(mailAddress)
    time.sleep(1)

    subject = driver.find_element_by_xpath('//*[@id="TextField704"]')
    subject.send_keys("No Subject")
    time.sleep(1)

    sendMail = driver.find_element_by_id("id__708")
    sendMail.click()
    print("Email sent".center(CENTER, "-"))
    # TODO: close browser again
    driver.close()

def main():
    
    mailAddress = pyinputplus.inputEmail("Enter email address: \n")
    pw = pyinputplus.inputPassword("Enter password for sending the mail: \n", timeout=10)
    mailMessage = pyinputplus.inputStr("Enter message to send: \n")
    send_mail(mailAddress, pw, mailMessage)

if __name__ == "__main__":
    main()
