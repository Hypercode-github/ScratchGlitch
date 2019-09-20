from selenium import webdriver
import time
x = 10
driver = webdriver.Chrome()
driver.get("https://scratch.mit.edu")
#button = driver.find_element_by_class_name('ignore-react-onclickoutside')
#button.click()

#username = driver.find_element_by_name('username')
#username.click()
#username.send_keys("HyperTerminator")

#password = driver.find_element_by_id('frc-password-1088')
#password.send_keys("darin123")

for i in range(1, 200000):
    time.sleep(1)
    driver.get('https://scratch.mit.edu/projects/327885643/')

    time.sleep(x)
    startflag = driver.find_element_by_class_name('green-flag_green-flag_1kiAo')
    startflag.click()
    x = 2
