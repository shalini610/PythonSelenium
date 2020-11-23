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
def test_SignInButton(test_setup):

    el = driver.find_element_by_xpath("(//a[contains(text(),'Sign')])[2]")
    el.click()
    time.sleep(5)
    signInPage_HeaderName = driver.find_element_by_xpath("//h1")
    if signInPage_HeaderName.text == 'Sign in to GitHub':
        print("User is redirected to login page")
    else:
        assert False, "login page is NOT displayed"

def test_mandtoryLoginPage(test_setup):
    el = driver.find_element_by_name("commit")
    el.click()
    time.sleep(2)

    error_mssg_exist = driver.find_element_by_xpath("((//form//div)[2]//div)[2]").is_displayed()
    if error_mssg_exist==True:
        error_messg = driver.find_element_by_xpath("((//form//div)[2]//div)[2]").text
        assert False, error_messg
    else:
        print("Logged in successfully")

def test_reset_password_page(test_setup):
    el = driver.find_element_by_xpath("//*[contains(text(),'Forgot password?')]")
    el.click()
    time.sleep(2)

    reset_pss_header = driver.find_element_by_xpath("//h1").text
    if reset_pss_header=='Reset your password':
        print("User navigated to Reset password page")
    else:
        pytest.fail("Reset password page is Not displayed")

def test_resetPassword_errorMessage(test_setup):
    el = driver.find_element_by_name("commit")
    el.click()
    time.sleep(2)

    error_mssg_exist = driver.find_element_by_xpath("((//form//div)[2]//div)[2]").is_displayed()
    if error_mssg_exist==True:
        error_messg = driver.find_element_by_xpath("((//form//div)[2]//div)[2]").text
        assert False, error_messg
    else:
        print("Logged in successfully")