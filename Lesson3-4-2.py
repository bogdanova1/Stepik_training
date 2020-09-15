from selenium import webdriver
browser = webdriver.Chrome()
import math
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
print(x)
y = calc(x)
print(y)

input = browser.find_element_by_id("answer")
input.send_keys(y)
checkbox = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()
radiobutton = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()
button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True