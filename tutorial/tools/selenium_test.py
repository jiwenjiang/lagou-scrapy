from selenium import webdriver

browser = webdriver.Chrome(executable_path="E:\JDK\selenium\chromedriver.exe")

browser.get("https://jiwenjiang.github.io/#/login")

print(browser.page_source)
