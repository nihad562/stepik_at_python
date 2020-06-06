from selenium import webdriver

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]

try:
    for link in links:
        browser = webdriver.Chrome()
        browser.get(link)
        # заполняем поле для имени
        browser.find_element_by_xpath("//label[text() = 'First name*']/following-sibling::input").send_keys("Ivan")
        # заполняем поле для фамилии
        browser.find_element_by_xpath("//label[text() = 'Last name*']/following-sibling::input").send_keys("Petrov")
        # заполняем поле для e-mail
        browser.find_element_by_class_name("third").send_keys("test@test.ru")
        # заполняем поле для телефона
        browser.find_element_by_xpath("//div[2]/div/input[1]").send_keys("88005553535")
        # заполняем поле для адресса
        browser.find_element_by_xpath("//div[2]/input").send_keys("Irinovskiy")
        # подтверждаем форму
        browser.find_element_by_css_selector("button.btn").click()
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()