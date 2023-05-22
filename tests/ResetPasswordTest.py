from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import logging
import pytest
from datetime import datetime

# Tạo thư mục logs nếu chưa tồn tại
if not os.path.exists('logs'):
    os.makedirs('logs')

# Thiết lập logger
logging.basicConfig(filename='logs/test_report.log', level=logging.INFO,encoding='utf-8',
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Lưu đường dẫn tới thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Tạo đường dẫn đầy đủ tới thư mục TestCaseImage
image_dir = os.path.join(current_dir, 'TestCaseImage')

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

class ResetPasswordTestSelenium:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys('khang1379@gmail.com')
        time.sleep(1)
        sentOTP = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        sentOTP.click()

    def get_screen_shot(self, name):
        time.sleep(5)
        i = 1
        while os.path.exists(os.path.join(image_dir, 'screen_shot_' + name + '(' + str(i) + ').png')):
            i += 1
        self.driver.save_screenshot(os.path.join(image_dir, 'screen_shot_' + name + '(' + str(i) + ').png'))
   
    def resetPassword(self, otp, password1, password2):
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "OTP").send_keys(otp)
        time.sleep(1)
        self.driver.find_element(By.ID, "new_password").send_keys(password1)
        time.sleep(1)
        self.driver.find_element(By.ID, "confirm_password").send_keys(password2)
        time.sleep(1)
        sentOTP = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        sentOTP.click()
        time.sleep(5)
       
    def run_test_case(self, otp, password1, password2, screenshot_name):
        logging.info("Running test case: %s", screenshot_name)
        self.resetPassword(otp, password1, password2)
        self.get_screen_shot(screenshot_name)
        self.driver.delete_all_cookies()
        self.driver.refresh()

@pytest.fixture(scope="module")
def resetPassword_fixture(request):
    resetPassword = ResetPasswordTestSelenium('http://localhost:50001/auth/forgot-password')
    yield resetPassword
    resetPassword.driver.close()


@pytest.mark.html
def test_case1(resetPassword_fixture):
    #Input không có điền otp
    case = {'otp': '', 'password1': 'Khang123', 'password2': 'Khang123', 'screenshot_name': 'testcase1'}
    resetPassword_fixture.run_test_case(case['otp'], case['password1'], case['password2'], case['screenshot_name'])

@pytest.mark.html
def test_case2(resetPassword_fixture):
    #Input với otp không chính xác
    case = {'otp': '123', 'password1': 'Khang123', 'password2': 'Khang123', 'screenshot_name': 'testcase2'}
    resetPassword_fixture.run_test_case(case['otp'], case['password1'], case['password2'], case['screenshot_name'])

@pytest.mark.html
def test_case3(resetPassword_fixture):
    #Input không có điền mật khẩu
    case = {'otp': '123', 'password1': '', 'password2': 'Khang123', 'screenshot_name': 'testcase3'}
    resetPassword_fixture.run_test_case(case['otp'], case['password1'], case['password2'], case['screenshot_name'])

@pytest.mark.html
def test_case4(resetPassword_fixture):
    #Input không có xác nhận mật khẩu
    case = {'otp': '123', 'password1': 'Khang123', 'password2': '', 'screenshot_name': 'testcase4'}
    resetPassword_fixture.run_test_case(case['otp'], case['password1'], case['password2'], case['screenshot_name'])

@pytest.mark.html
def test_case5(resetPassword_fixture):
    #Input có mật khẩu khác với xác nhận mật khẩu
    case = {'otp': '123', 'password1': 'Khang123', 'password2': 'Vikhang123', 'screenshot_name': 'testcase5'}
    resetPassword_fixture.run_test_case(case['otp'], case['password1'], case['password2'], case['screenshot_name'])