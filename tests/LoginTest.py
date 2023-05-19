from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
import logging
import pytest
from selenium.common.exceptions import NoSuchElementException

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

class LoginTestSelenium:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def get_screen_shot(self, name):
        sleep(2)
        i = 1
        while os.path.exists(os.path.join(image_dir, 'screen_shot_' + name + '(' + str(i) + ').png')):
            i += 1
        self.driver.save_screenshot(os.path.join(image_dir, 'screen_shot_' + name + '(' + str(i) + ').png'))

    def login(self, username, password, user):
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        sleep(1)
        user_checkbox = self.driver.find_element(By.ID, 'user')
        if user:
            user_checkbox.click()
        sleep(1)    
        # Nhấn nút đăng nhập
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(2)
        # So sánh địa chỉ URL trước và sau khi đăng nhập
        if self.driver.current_url != 'http://127.0.0.1:50001/auth/login?next=%2F':
            logging.info("Đăng nhập thành công")
        else:
            try:
                message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
                # In ra thông báo
                logging.error("Đăng nhập thất bại. Thông báo lỗi là %s", message.text)
            except NoSuchElementException:
                # Xử lý khi không tìm thấy element
                print("Không tìm thấy element")
        logging.info("")

    def run_test_case(self, username, password, user, screenshot_name):
        logging.info("Running test case: %s", screenshot_name)
        self.login(username, password, user)
        self.get_screen_shot(screenshot_name)
        self.driver.delete_all_cookies()
        self.driver.refresh()


@pytest.fixture(scope="module")
def login_fixture(request):
    login = LoginTestSelenium('http://127.0.0.1:50001')
    yield login
    login.driver.close()

@pytest.mark.html
#Đăng nhập đúng user và pass
def test_case1(login_fixture):
    case = {'username': 'test1', 'password': '123loI', 'user': True, 'screenshot_name': 'testcase1'}
    login_fixture.run_test_case(case['username'], case['password'], case['user'], case['screenshot_name'])

@pytest.mark.html
#Đăng nhập sai mật khẩu
def test_case2(login_fixture):
    case = {'username': 'test1', 'password': 'test', 'user': True, 'screenshot_name': 'testcase2'}
    login_fixture.run_test_case(case['username'], case['password'], case['user'], case['screenshot_name'])

@pytest.mark.html
#Đăng nhập sai user đúng mật khẩu
def test_case3(login_fixture):
    case = {'username': 'test123', 'password': '123loI', 'user': True, 'screenshot_name': 'testcase3'}
    login_fixture.run_test_case(case['username'], case['password'], case['user'], case['screenshot_name'])

@pytest.mark.html
#Đăng nhập với username là số âm
def test_case4(login_fixture):
    case = {'username': '-1', 'password': '123loI', 'user': True, 'screenshot_name': 'testcase4'}
    login_fixture.run_test_case(case['username'], case['password'], case['user'], case['screenshot_name'])
    
@pytest.mark.html
#Đăng nhập không nhập username đúng nhưng chữ hoa thường lẫn lộn
def test_case5(login_fixture):
    case = {'username': 'tEsT1', 'password': 'test', 'user': True, 'screenshot_name': 'testcase5'}
    login_fixture.run_test_case(case['username'], case['password'], case['user'], case['screenshot_name'])
