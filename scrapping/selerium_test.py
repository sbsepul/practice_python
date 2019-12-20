from selenium import webdriver

#Ocupando selenium con el navegador de Chrome

#browser = webdriver.Chrome(r"C:\Users\Sebastian\Downloads\chromedriver_win32\chromedriver.exe")
#browser.get("https://www.python.org/")
#nav = browser.find_element_by_id("mainnav")
#print(nav.text)

#Ocupando selerium con PhantomJS


browser = webdriver.PhantomJS()
browser.get("https://www.python.org/")
print(browser.find_element_by_class_name("introduction").text)
browser.close()

