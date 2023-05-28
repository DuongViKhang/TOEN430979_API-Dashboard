from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
# Fixture setup
@pytest.fixture(scope="module")
def driver():
    # Cài đặt các tùy chọn cho Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy trình duyệt ẩn không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Đường dẫn đến Chrome WebDriver (Phải là đường dẫn tới chromedriver trong Github Actions)
    webdriver_service = Service('/driver/')  # Thay thế đường dẫn tới chromedriver

    # Khởi tạo trình điều khiển Chrome
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    yield driver
    # Teardown - Đóng trình duyệt sau khi hoàn thành
    driver.quit()

@pytest.mark.html
def test_case1(driver):
    #Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    #Đăng nhập vào hệ thống bằng tài khoản admin
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('admin')
    sleep(1)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('admin')
    sleep(1)   
    # Gửi phím Enter để kích hoạt nút
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.send_keys(Keys.ENTER)
    sleep(2)
    link_user_manager = "http://ec2-54-166-21-94.compute-1.amazonaws.com//admin/user-manage/"
    #Kiểm tra xem link vào chức năng quản lý user có truy cập bình thường hay không
    try:
        response = requests.get(link_user_manager)
        assert response.status_code == 200, "Link is accessible"
        driver.get(link_user_manager)   
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
    driver.delete_all_cookies()

@pytest.mark.html
def test_case2(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    #Đăng nhập vào hệ thống bằng tài khoản admin
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('admin')
    sleep(1)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('admin')
    sleep(1)   
    # Gửi phím Enter để kích hoạt nút
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.send_keys(Keys.ENTER)
    sleep(2)
    link_user_deleted = "http://ec2-54-166-21-94.compute-1.amazonaws.com//admin/user-manage/trash"
    #Kiểm tra xem link vào chức năng xem các user đã xóa có truy cập bình thường hay không
    try:
        response = requests.get(link_user_deleted)
        assert response.status_code == 200, "Link is accessible"
        driver.get(link_user_deleted)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
    driver.delete_all_cookies()
    
@pytest.mark.html
def test_case3(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    #Đăng nhập vào hệ thống bằng tài khoản admin
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('admin')
    sleep(1)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('admin')
    sleep(1)   
    # Gửi phím Enter để kích hoạt nút
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.send_keys(Keys.ENTER)
    sleep(2)
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com//admin/user-manage/")
    cell = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[3]")
    edits = driver.find_elements(By.XPATH, "//i[@class='lni lni-pencil-alt']")
    if cell.text == "admin@gmail.com":
        driver.execute_script("arguments[0].click();", edits[0])
    else:
        driver.execute_script("arguments[0].click();", edits[1])
    sleep(2)
    fullname = driver.find_element(By.ID, "fullname")
    fullname.clear()
    fullname.send_keys('Edit Admin')
    sleep(1)
    age = driver.find_element(By.ID, "age")
    age.clear()
    age.send_keys('30')
    sleep(1)
    address= driver.find_element(By.ID, "address")
    address.clear()
    address.send_keys('Admin Ngau nhien')
    sleep(1)
    button_ok = driver.find_element(By.XPATH, "//button[@type='button' and text()='OK']")
    button_ok.click()
    
    # sleep(2)
    # button_cancel = driver.find_element(By.XPATH, "//button[@type='button' and text()='Cancel']")
    # button_cancel.click()
    sleep(5)
    driver.delete_all_cookies()

@pytest.mark.html
def test_case4(driver):
     # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    #Đăng nhập vào hệ thống bằng tài khoản admin
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('admin')
    sleep(1)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('admin')
    sleep(1)   
    # Gửi phím Enter để kích hoạt nút
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.send_keys(Keys.ENTER)
    sleep(2)
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com//admin/user-manage/")
    cell = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[3]")
    edits = driver.find_elements(By.XPATH, "//i[@class='lni lni-pencil-alt']")
    if cell.text == "admin@gmail.com":
        driver.execute_script("arguments[0].click();", edits[1])
    else:
        driver.execute_script("arguments[0].click();", edits[0])
    sleep(2)
    fullname = driver.find_element(By.ID, "fullname")
    fullname.clear()
    fullname.send_keys('Edit User')
    sleep(1)
    age = driver.find_element(By.ID, "age")
    age.clear()
    age.send_keys('30')
    sleep(1)
    address= driver.find_element(By.ID, "address")
    address.clear()
    address.send_keys('Ngau nhien')
    sleep(1)
    button_ok = driver.find_element(By.XPATH, "//button[@type='button' and text()='OK']")
    button_ok.click()
    sleep(5)
    driver.delete_all_cookies()
    
@pytest.mark.html
def test_case5(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    #Đăng nhập vào hệ thống bằng tài khoản admin
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('admin')
    sleep(1)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('admin')
    sleep(1)   
    # Gửi phím Enter để kích hoạt nút
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.send_keys(Keys.ENTER)
    sleep(2)
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com//admin/user-manage/")
    delete = driver.find_element(By.XPATH, "//i[@class='lni lni-trash-can']")
    driver.execute_script("arguments[0].click();", delete)
    sleep(2)

