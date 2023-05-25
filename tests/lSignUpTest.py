import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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

#Test chức năng đăng ký bằng selenium
class SignUpTestSelenium:
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
    
    def signup(self, username, password, fullname, age, address, email, avatar):
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "username").send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.ID, "fullname").send_keys(fullname)
        time.sleep(1)
        self.driver.find_element(By.ID, "age").send_keys(age)
        time.sleep(1)
        self.driver.find_element(By.ID, "address").send_keys(address)
        time.sleep(1)
        self.driver.find_element(By.ID, "email").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.ID, "avatar").send_keys(avatar)
        time.sleep(1)
        signup = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        self.driver.execute_script("arguments[0].scrollIntoView();", signup)
        self.driver.execute_script("arguments[0].click();", signup)
        time.sleep(5)

    def run_test_case(self, username, password, fullname, age, address, email, avatar, screenshot_name):
        logging.info("Running test case: %s", screenshot_name)
        self.signup(username, password, fullname, age, address, email, avatar)
        self.get_screen_shot(screenshot_name)
        self.driver.delete_all_cookies()
        self.driver.refresh()

@pytest.fixture(scope="module")
def signup_fixture(request):
    signup = SignUpTestSelenium('http://ec2-34-239-74-119.compute-1.amazonaws.com:50001/auth/signup')
    yield signup
    signup.driver.close()

@pytest.mark.html
def test_case1(signup_fixture):
    #Input để kiểm tra việc tạo tài khoản với vai trò user thành công hay không
    case = {'username': 'khangduong', 'password': 'Khang123', 'fullname': 'DuongViKhang', 'age': '21', 
            'address': 'Thu Duc, HCM City', 'email': 'testipa33zz@gmail.com', 
            'avatar': 'https://www.google.com/search?q=avatar+facebook&tbm=isch&ved=2ahUKEwintfjTmej-AhVvg1YBHR3HBYYQ2-cCegQIABAA&oq=avatar+fa&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6BwgAEIoFEEM6CggAEIoFELEDEENQrwJY5RBgjhtoAHAAeACAAXyIAd8IkgEDMi44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=kjdaZKekOu-G2roPnY6XsAg&bih=609&biw=1280#imgrc=oUEjntRh9lGh7M', 
            'screenshot_name': 'signup_testcase1'}
    signup_fixture.run_test_case(case['username'], case['password'], 
                                 case['fullname'], case['age'],
                                 case['address'], case['email'], 
                                 case['avatar'], case['screenshot_name'])

@pytest.mark.html
def test_case2(signup_fixture):
    #Input để kiểm tra thông báo khi đăng ký mà không điền Username
    case = {'username': '', 'password': 'Khang123', 'fullname': 'DuongViKhang', 'age': '21', 
            'address': 'Thu Duc, HCM City', 'email': 'khang1379@gmail.com', 
            'avatar': 'https://www.google.com/search?q=avatar+facebook&tbm=isch&ved=2ahUKEwintfjTmej-AhVvg1YBHR3HBYYQ2-cCegQIABAA&oq=avatar+fa&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6BwgAEIoFEEM6CggAEIoFELEDEENQrwJY5RBgjhtoAHAAeACAAXyIAd8IkgEDMi44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=kjdaZKekOu-G2roPnY6XsAg&bih=609&biw=1280#imgrc=oUEjntRh9lGh7M', 
            'screenshot_name': 'signup_testcase2'}
    signup_fixture.run_test_case(case['username'], case['password'], 
                                 case['fullname'], case['age'],
                                 case['address'], case['email'], 
                                 case['avatar'], case['screenshot_name'])

@pytest.mark.html
def test_case3(signup_fixture):
    #Input để kiểm tra thông báo khi đăng ký mà không điền hoặc điền không đúng yêu cầu Password
    case = {'username': 'khangduong', 'password': '', 'fullname': 'DuongViKhang', 'age': '21', 
            'address': 'Thu Duc, HCM City', 'email': 'khang1379@gmail.com', 
            'avatar': 'https://www.google.com/search?q=avatar+facebook&tbm=isch&ved=2ahUKEwintfjTmej-AhVvg1YBHR3HBYYQ2-cCegQIABAA&oq=avatar+fa&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6BwgAEIoFEEM6CggAEIoFELEDEENQrwJY5RBgjhtoAHAAeACAAXyIAd8IkgEDMi44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=kjdaZKekOu-G2roPnY6XsAg&bih=609&biw=1280#imgrc=oUEjntRh9lGh7M', 
            'screenshot_name': 'signup_testcase3'}
    signup_fixture.run_test_case(case['username'], case['password'], 
                                 case['fullname'], case['age'],
                                 case['address'], case['email'], 
                                 case['avatar'], case['screenshot_name'])
@pytest.mark.html
def test_case4(signup_fixture):
    #Input để kiểm tra thông báo khi đăng ký mà không điền Fullname
    case = {'username': 'khangduong', 'password': 'Khang123', 'fullname': '', 'age': '21', 
            'address': 'Thu Duc, HCM City', 'email': 'khang1379@gmail.com', 
            'avatar': 'https://www.google.com/search?q=avatar+facebook&tbm=isch&ved=2ahUKEwintfjTmej-AhVvg1YBHR3HBYYQ2-cCegQIABAA&oq=avatar+fa&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6BwgAEIoFEEM6CggAEIoFELEDEENQrwJY5RBgjhtoAHAAeACAAXyIAd8IkgEDMi44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=kjdaZKekOu-G2roPnY6XsAg&bih=609&biw=1280#imgrc=oUEjntRh9lGh7M', 
            'screenshot_name': 'signup_testcase4'}
    signup_fixture.run_test_case(case['username'], case['password'], 
                                 case['fullname'], case['age'],
                                 case['address'], case['email'], 
                                 case['avatar'], case['screenshot_name'])

@pytest.mark.html
def test_case5(signup_fixture):
    #Input để kiểm tra thông báo khi đăng ký mà không điền Age
    case = {'username': 'khangduong', 'password': 'Khang123', 'fullname': 'DuongViKhang', 'age': '', 
            'address': 'Thu Duc, HCM City', 'email': 'khang1379@gmail.com', 
            'avatar': 'https://www.google.com/search?q=avatar+facebook&tbm=isch&ved=2ahUKEwintfjTmej-AhVvg1YBHR3HBYYQ2-cCegQIABAA&oq=avatar+fa&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICAAQgAQQsQM6BwgAEIoFEEM6CggAEIoFELEDEENQrwJY5RBgjhtoAHAAeACAAXyIAd8IkgEDMi44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=kjdaZKekOu-G2roPnY6XsAg&bih=609&biw=1280#imgrc=oUEjntRh9lGh7M', 
            'screenshot_name': 'signup_testcase5'}
    signup_fixture.run_test_case(case['username'], case['password'], 
                                 case['fullname'], case['age'],
                                 case['address'], case['email'], 
                                 case['avatar'], case['screenshot_name'])