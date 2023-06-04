import os
import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from threading import Thread

BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME", "BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY", "BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL", "https://hub.browserstack.com/wd/hub")

capabilities = [
    {
        "os": "OS X",
        "osVersion": "Ventura",
        "buildName": "TestChallenge",
        "sessionName": "BStack parallel python",
        "browserName": "Firefox",
        "browserVersion": "latest"
    },
    {
        "os": "Windows",
        "osVersion": "10",
        "buildName": "TestChallenge",
        "sessionName": "BStack parallel python",
        "browserName": "Chrome",
        "browserVersion": "latest"
    },
    {
        "osVersion": "12.0",
        "deviceName": "Samsung Galaxy S22",
        "buildName": "TestChallenge",
        "sessionName": "BStack parallel python",
        "browserName": "chrome",
    },
]

def get_browser_options(browser):
    switcher = {
        "chrome": ChromeOptions,
        "firefox": FirefoxOptions,
        "edge": EdgeOptions,
        "safari": SafariOptions,
    }
    return switcher.get(browser, ChromeOptions)()

def run_session(cap):
    bstack_options = {
        "osVersion": cap.get("osVersion"),
        "buildName": cap.get("buildName"),
        "sessionName": cap.get("sessionName"),
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }

    if "os" in cap:
        bstack_options["os"] = cap["os"]
    if "deviceName" in cap:
        bstack_options['deviceName'] = cap["deviceName"]
    bstack_options["source"] = "python:sample-main:v1.1"
    if cap.get('browserName') == 'ios':
        cap['browserName'] = 'safari'
    options = get_browser_options(cap.get("browserName", "chrome").lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    if cap.get('browserName', '').lower() == 'samsung':
        options.set_capability('browserName', 'samsung')
    driver = webdriver.Remote(command_executor=URL, options=options)
    try:
        driver.get('https://www.browserstack.com/users/sign_in')
        driver.maximize_window()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "accept-cookie-notification-cross-icon")))
        cookie_button = driver.find_element(By.ID, "accept-cookie-notification-cross-icon")
        cookie_button.click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "user_email_login")))
        email_field = driver.find_element(By.ID, "user_email_login")
        password_field = driver.find_element(By.ID, "user_password")

        signin_action = ActionChains(driver)

        email_field.clear()
        email_field.send_keys(os.getenv('BROWSER_STACK_EMAIL'))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user_password")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user_password")))

        password_field.clear()
        password_field.send_keys(os.getenv('BROWSER_STACK_PW'))
 
        # Sign In
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "commit")))
        signin = driver.find_element(By.NAME, "commit")
        signin.click()

        if cap.get('deviceName', '').lower() == 'samsung galaxy s22':
           WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "primary-menu-toggle")))
           primary_menu_toggle = driver.find_element(By.ID, "primary-menu-toggle")
           primary_menu_toggle.click()
           time.sleep(2)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "invite-link")))
        #assert that the homepage includes a link to Invite Users
        assert EC.presence_of_element_located((By.ID, "invite-link"))(driver), "invite-link is not present"
        invite_link = driver.find_element(By.ID, "invite-link")
        invite_action = ActionChains(driver)
        invite_action.click(invite_link)
        invite_action.perform()
        time.sleep(2)
        
        #retrieve the link’s URL
        if cap.get('deviceName', '').lower() == 'samsung galaxy s22':
           current_height = driver.execute_script("return window.innerHeight;")
           new_height = current_height + int(current_height * 0.25)
           driver.execute_script("window.scrollTo(0, {});".format(new_height))

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "manage-users__invite-copy-cta")))
        driver.find_element(By.CLASS_NAME, "manage-users__invite-copy-cta").click()
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, 0);")

        #logout
        if cap.get('deviceName', '').lower() == 'samsung galaxy s22':
            primary_menu_toggle = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "primary-menu-toggle")))
            primary_menu_toggle.click()

            sign_out_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/header/div/div/nav/ul[1]/li[10]/a')))
            sign_out_link.click()
        else:
            account_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "account-dropdown-toggle")))
            logout_action = ActionChains(driver).move_to_element(account_dropdown)
            sign_out_link = driver.find_element(By.ID, "sign_out_link")
            logout_action.move_to_element(sign_out_link).click(sign_out_link).perform()

    except (NoSuchElementException, TimeoutException) as err:
        # Handle NoSuchElementException and TimeoutException
        message = "Exception: " + str(err.__class__) + " " + str(err)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(
                message) + '}}')
    except Exception as err:
        # Handle other exceptions
        message = "Exception: " + str(err.__class__) + " " + str(err)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(
                message) + '}}')
    else:
        # If no exception occurred, set the session status as passed
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Assertion passed"}}')
    finally:
        # Quit the driver
        driver.quit()

for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
