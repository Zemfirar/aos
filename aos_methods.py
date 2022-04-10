import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import aos_locators as locators

chrome_service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)


def set_up():
    print(f'Test started at: {datetime.datetime.now()}')

    driver.maximize_window()

    # to wait for the web browser implicitly
    driver.implicitly_wait(30)

    driver.get(locators.AOS_URL)
    sleep(3)

    # Check that the url address and the title are correct
    if (driver.current_url == locators.AOS_URL or driver.current_url == f'{locators.AOS_URL}#/') \
            and driver.title == locators.AOS_TITLE:
        print(f'We are at the correct web page: {driver.current_url}')
        print(f"We are seeing the correct title page: '{driver.title}'")
    else:
        print(f'We are not at the correct home page. Try again/check your code')
        driver.close()  # close the current tab
        driver.quit()  # close the browser completely


def tear_down():
    if driver is not None:
        print(f'--------------------')
        print(f'Test was completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def open_user_menu():
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "menuUserLink"))
    ).click()


def validate_user_logged_in(username):
    assert driver.find_element(
        by=By.XPATH, value="//a[@id='menuUserLink']/span"
    ).text == username


def create_new_account(username, password):
    # WebDriverWait(driver, 10).until(
    #     lambda x: x.find_element(By.ID, "menuUserLink").is_displayed()
    # )
    # driver.find_element(by=By.ID, value='menuUserLink').click()
    open_user_menu()
    sleep(1)

    driver.find_element(by=By.LINK_TEXT, value='CREATE NEW ACCOUNT').click()
    print('Navigating to Create New Account page')
    sleep(1)

    assert driver.find_element(
        by=By.XPATH, value="//h3[.='CREATE ACCOUNT']"
    ).is_displayed()

    driver.find_element(
        by=By.XPATH, value="//input[@name='usernameRegisterPage']"
    ).send_keys(username)
    driver.find_element(
        by=By.XPATH, value="//input[@name='emailRegisterPage']"
    ).send_keys(locators.email)

    driver.find_element(
        by=By.XPATH, value="//input[@name='passwordRegisterPage']"
    ).send_keys(password)
    driver.find_element(
        by=By.XPATH, value="//input[@name='confirm_passwordRegisterPage']"
    ).send_keys(password)

    sleep(1)

    # WebDriverWait(driver, 10).until(
    #     expected_conditions.element_to_be_clickable(
    #         (By.XPATH, "//sec-view[@sec-name='registrationAgreement']")
    #     )
    # ).click()
    # driver.find_element(
    #     by=By.XPATH, value="//sec-view[@sec-name='registrationAgreement']"
    # ).click()
    # driver.find_element(
    #     by=By.XPATH, value="//input[@name='i_agree']"
    # ).click()
    agreement_checkbox = driver.find_element(
        by=By.XPATH, value="//sec-view[@sec-name='registrationAgreement']"
    )
    register_button = driver.find_element(By.ID, "register_btnundefined")
    while "invalid" in register_button.get_attribute("class"):
        # print("register_button is not clickable")
        agreement_checkbox.click()
        sleep(0.5)

    print('Entered information about the new user')

    driver.find_element(By.ID, "register_btnundefined").click()
    print('Creating new user now')
    sleep(2)

    validate_user_logged_in(locators.new_username)

    print(f'New user {username} successfully created')


def log_in(username, password):
    open_user_menu()

    print(f'Going to log in user {username} now')

    driver.find_element(
        by=By.XPATH, value="//input[@name='username']"
    ).send_keys(username)

    driver.find_element(
        by=By.XPATH, value="//input[@name='password']"
    ).send_keys(password)

    driver.find_element(By.ID, "sign_in_btnundefined").click()
    sleep(1)

    print(f'Successfully logged in user {username}')


def log_out(username):
    driver.find_element(
        by=By.XPATH, value="//a[@id='menuUserLink']/span"
    ).click()
    sleep(0.5)

    print('Going to log out now')

    driver.find_element(
        by=By.XPATH,
        value="//div[@id='loginMiniTitle']/label[@translate='Sign_out']"
    ).click()
    sleep(2)

    # look for username element (should be none of them)
    username_menu_elements = driver.find_elements(
            by=By.XPATH, value=f"//a[@id='menuUserLink']/span[.='{username}']"
        )

    assert len(username_menu_elements) == 0

    print('Successfully logged out')
