from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import logging
import pytest
from selenium.webdriver.chrome.options import Options
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

class EnterEmailTestSelenium:
    def __init__(self, url):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)

    def get_screen_shot(self, name):
        time.sleep(5)
        i = 1
        while os.path.exists(os.path.join(image_dir, 'screen_shot_' + name + '(' + str(i) + ').png')):
            i += 1
        self.driver.save_screenshot(os.path.join(image_dir, 'screen_shot_' + name + '(' + str(i) + ').png'))
   
    def enterEmail(self, email):
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys(email)
        time.sleep(1)
        sentOTP = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", sentOTP)
        time.sleep(5)
        # So sánh địa chỉ URL trước và sau khi đăng nhập
        if self.driver.current_url != 'http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/reset-password':
            logging.info("Email chính xác, truy cập trang reset password thành công.")
        else:
            message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
            # In ra thông báo
            logging.error("Truy cập trang reset password thất bại. Thông báo lỗi là %s", message.text)
        logging.info("")

    def run_test_case(self, email, screenshot_name):
        logging.info("Running test case: %s", screenshot_name)
        self.enterEmail(email)
        self.get_screen_shot(screenshot_name)
        self.driver.delete_all_cookies()
        self.driver.refresh()

@pytest.fixture(scope="module")
def enterEmail_fixture(request):
    enterEmail = EnterEmailTestSelenium('http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/forgot-password')
    yield enterEmail
    enterEmail.driver.close()


@pytest.mark.html
def test_case1(enterEmail_fixture):
    #Input với email đã đăng ký nhưng được viết hoa thường lẫn lộn
    case = {'email': 'KhAnG1379@gmail.com', 'screenshot_name': 'enteremail_testcase1'}
    enterEmail_fixture.run_test_case(case['email'], case['screenshot_name'])

@pytest.mark.html
def test_case2(enterEmail_fixture):
    #Input với email chưa đăng ký
    case = {'email': 'abcd@gmail.com', 'screenshot_name': 'enteremail_testcase2'}
    enterEmail_fixture.run_test_case(case['email'], case['screenshot_name'])

@pytest.mark.html
def test_case3(enterEmail_fixture):
    #Input với email đã đăng ký nhưng có kí tự đặc biệt ở trước @
    case = {'email': 'khang_1379@gmail.com', 'screenshot_name': 'enteremail_testcase3'}
    enterEmail_fixture.run_test_case(case['email'], case['screenshot_name'])

@pytest.mark.html
def test_case4(enterEmail_fixture):
    #Input với email đã đăng ký nhưng có kí tự đặc biệt ở sau @
    case = {'email': 'khang1379@gmai_l.com', 'screenshot_name': 'enteremail_testcase4'}
    enterEmail_fixture.run_test_case(case['email'], case['screenshot_name'])

@pytest.mark.html
def test_case5(enterEmail_fixture):
    #Input không có email
    case = {'email': '', 'screenshot_name': 'enteremail_testcase5'}
    enterEmail_fixture.run_test_case(case['email'], case['screenshot_name'])
