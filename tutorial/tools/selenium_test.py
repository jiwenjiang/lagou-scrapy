from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="E:\JDK\selenium\chromedriver.exe")

browser.get("https://www.zhihu.com/signup?next=%2F")


def click_ele(c):
    browser.find_element_by_css_selector(c).click()


def select_ele(c, k):
    browser.find_element_by_css_selector(c).send_keys(k)


click_ele(".SignContainer-switch span")
select_ele(".SignFlow-accountInput input[name='username']", "18380464714")
select_ele(".SignFlow-password input[name='password']", "xxxxx")
click_ele("button.SignFlow-submitButton")
time.sleep(3)
for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var num=document.body.scrollHeight; return num;")
    time.sleep(3)


# print(browser.page_source)
