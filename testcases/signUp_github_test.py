from selenium import webdriver
import time
import pytest

@pytest.fixture(scope="session")
def test_setup():
    '''Create the object for Webdriver'''
    global driver
    driver = webdriver.Chrome(executable_path=r"/driver/chromedriver.exe")

    '''Open the URL and maximize the window'''
    driver.get("https://github.com/")
    driver.maximize_window()
    time.sleep(2)
    yield
    '''Close the browser'''
    driver.close()
    driver.quit()
    print("Test Completed")
#
def test_SignUpButton(test_setup):

    el = driver.find_element_by_xpath("(//a[contains(text(),'Sign')])[3]")
    el.click()
    time.sleep(5)

    assert ("Create your account" in driver.page_source)

def test_CreateAccountButton(test_setup):

    driver.find_element_by_id("user_login").send_keys("shalini348")
    time.sleep(2)
    driver.find_element_by_id("user_email").send_keys("vshalini")
    time.sleep(2)
    driver.find_element_by_id("user_password").send_keys("November-2020")
    time.sleep(2)

    createAccButt = driver.find_element_by_xpath("//button[contains(text(),'Create account')]").is_enabled()
    print(createAccButt)

    if createAccButt==False:
        print("Create button still greyed our some of information is not correct")