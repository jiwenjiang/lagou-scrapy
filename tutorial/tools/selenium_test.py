from selenium import webdriver

browser = webdriver.Chrome(executable_path="E:\JDK\selenium\chromedriver.exe")

browser.get("https://www.zhihu.com/signup?next=%2F")


def click_ele(c):
    browser.find_element_by_css_selector(c).click()


def select_ele(c, k):
    browser.find_element_by_css_selector(c).send_keys(k)


click_ele(".SignContainer-switch span")
select_ele(".SignFlow-accountInput input[name='username']", "18380464714")
select_ele(".SignFlow-password input[name='password']", "xxxxxxxxxxxxxxx")
click_ele("button.SignFlow-submitButton")

# print(browser.page_source)
