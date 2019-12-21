from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

inpaField = driver.find_element_by_xpath('//*[@id="sum1"]')
inpaField.send_keys('10')
inpbField = driver.find_element_by_xpath('//*[@id="sum2"]')
inpbField.send_keys('20')
msgTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
msgTotalButton.click()
