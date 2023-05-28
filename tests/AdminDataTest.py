from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

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
    # kiểm tra tiêu đề trang có phải là trang api không
    assert "API Dashboard" in driver.title
    assert driver.find_element(By.XPATH,"//h2[text()='Data API 12/2022']")
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
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nhập ngày tháng năm hợp lệ
    date_input = driver.find_element(By.XPATH, "//input[@type='date']")
    date_input.clear()
    date_input.send_keys('11-03-2022')
    sleep(1)
    getdata_button = driver.find_element(By.XPATH, "//button[@type='submit'and text()='Lấy dữ liệu']")
    getdata_button.send_keys(Keys.ENTER)
    sleep(1)

    assert driver.find_element(By.XPATH,"//h2[text()='Data API 11/2022']")
    
    # Kiểm tra các biểu đồ 
    chart1 = driver.find_element(By.ID, "Chart1")
    assert chart1.is_displayed()
    
    chart1 = driver.find_element(By.ID, "Chart4")
    assert chart1.is_displayed()

    chart5 = driver.find_element(By.ID, "Chart5")
    assert chart5.is_displayed()
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
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra lấy ngày tháng năm lớn hơn giá trị nhỏ nhất
    date_input = driver.find_element(By.XPATH, "//input[@type='date']")
    date_input.clear()
    date_input.send_keys('01-01-2017')
    sleep(1)
    getdata_button = driver.find_element(By.XPATH, "//button[@type='submit'and text()='Lấy dữ liệu']")
    getdata_button.send_keys(Keys.ENTER)
    sleep(1)
    assert driver.find_element(By.XPATH,"//h2[text()='Data API 12/2022']")
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
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra lấy ngày tháng năm lớn hơn giá trị lớn nhất
    date_input = driver.find_element(By.XPATH, "//input[@type='date']")
    date_input.clear()
    date_input.send_keys('11-03-2100')
    sleep(1)
    getdata_button = driver.find_element(By.XPATH, "//button[@type='submit'and text()='Lấy dữ liệu']")
    getdata_button.send_keys(Keys.ENTER)
    sleep(1)
    assert driver.find_element(By.XPATH,"//h2[text()='Data API 12/2022']")
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
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nếu tháng là số âm
    date_input = driver.find_element(By.XPATH, "//input[@type='date']")
    date_input.clear()
    date_input.send_keys('-12-03-2022')
    sleep(1)
    getdata_button = driver.find_element(By.XPATH, "//button[@type='submit'and text()='Lấy dữ liệu']")
    getdata_button.send_keys(Keys.ENTER)
    sleep(1)
    assert driver.find_element(By.XPATH,"//h2[text()='Data API 12/2022']")
