from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
import logging
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

# Test case ui login
@pytest.mark.html
def test_case1_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang đăng nhập không
    assert "Login - API Dashboard" in driver.title
    assert driver.find_element(By.TAG_NAME, 'h2').text=="Login"
    
@pytest.mark.html
def test_case2_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường username và password có tồn tại không
    assert driver.find_element(By.ID, 'username')
    assert driver.find_element(By.ID, 'password')
    
@pytest.mark.html
def test_case3_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút đăng nhập có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
    
@pytest.mark.html
def test_case4_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra 2 link quên mật khẩu và create an account có tồn tại không
    assert driver.find_element(By.LINK_TEXT, "Forgot Password?")
    assert driver.find_element(By.LINK_TEXT, "Create an account")
    
@pytest.mark.html
def test_case5_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com")
    # Thực hiện các thao tác kiểm tra giao diện  
    #Lấy url từ các link
    forgotlink = driver.find_element(By.LINK_TEXT, "Forgot Password?")
    forgotlink_url = forgotlink.get_attribute("href")
    signuplink = driver.find_element(By.LINK_TEXT, "Create an account")
    signuplink_url = signuplink.get_attribute("href")
    
    # Sử dụng requests để gửi yêu cầu GET đến đường dẫn và kiểm tra mã trạng thái (status code)
    try:
        response = requests.get(forgotlink_url)
        assert response.status_code == 200, "Link is accessible"
        response = requests.get(signuplink_url)
        assert response.status_code == 200, "Link is accessible"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
        
#Test case ui sign up
@pytest.mark.html
def test_case1_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang đăng ký không
    assert "SignUp - API Dashboard" in driver.title
    assert driver.find_element(By.TAG_NAME, 'h2').text=="SignUp"
    
@pytest.mark.html
def test_case2_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường đăng ký có tồn tại không
    assert driver.find_element(By.ID, 'username')
    assert driver.find_element(By.ID, 'password')
    assert driver.find_element(By.ID, 'fullname')
    assert driver.find_element(By.ID, 'age')
    assert driver.find_element(By.ID, 'email')
    assert driver.find_element(By.ID, 'avatar')
    
@pytest.mark.html
def test_case3_signup(driver): 
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút đăng ký có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
    
@pytest.mark.html
def test_case4_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng nhập có tồn tại không và đường link có truy cập được hay không
    loginlink = driver.find_element(By.LINK_TEXT, "Login")
    assert loginlink
    
@pytest.mark.html
def test_case5_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng nhập có tồn tại không và đường link có truy cập được hay không
    loginlink = driver.find_element(By.LINK_TEXT, "Login")
    assert loginlink
    login_url = loginlink.get_attribute("href")
    try:
        # Sử dụng requests để gửi yêu cầu GET đến đường dẫn và kiểm tra mã trạng thái (status code)
        response = requests.get(login_url)
        assert response.status_code == 200, "Link is accessible"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
    assert driver.find_element(By.LINK_TEXT, "Login")

#Test case ui gửi mail
@pytest.mark.html
def test_case1_forgot(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/forgot-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang gửi mail quên mật khẩu không
    assert driver.find_element(By.TAG_NAME, 'h2').text=="Forgot Password"
    
@pytest.mark.html
def test_case2_forgot(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/forgot-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường có tồn tại không
    assert driver.find_element(By.ID, 'email')
    
@pytest.mark.html
def test_case3_forgot(driver): 
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/forgot-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút gửi email có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
     
@pytest.mark.html
def test_case4_forgot(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/forgot-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng ký có tồn tại không
    signuplink = driver.find_element(By.LINK_TEXT, "Create an account")
    assert signuplink

@pytest.mark.html
def test_case5_forgot(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/forgot-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng ký có tồn tại không và đường link có truy cập được hay không
    signuplink = driver.find_element(By.LINK_TEXT, "Create an account")
    signuplink_url = signuplink.get_attribute("href")
    try:
        # Sử dụng requests để gửi yêu cầu GET đến đường dẫn và kiểm tra mã trạng thái (status code)
        response = requests.get(signuplink_url)
        assert response.status_code == 200, "Link is accessible"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
        
#Test case ui đổi mật khẩu
@pytest.mark.html
def test_case1_reset(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/reset-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang đổi mật khẩu không
    assert driver.find_element(By.TAG_NAME, 'h2').text=="Reset Password"
    
@pytest.mark.html
def test_case2_reset(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/reset-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường có tồn tại không
    assert driver.find_element(By.ID, 'OTP')
    assert driver.find_element(By.ID, 'new_password')
    assert driver.find_element(By.ID, 'confirm_password')
    
@pytest.mark.html
def test_case3_reset(driver): 
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/reset-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút đổi mật khẩu có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
     
@pytest.mark.html
def test_case4_reset(driver):
    
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/reset-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng nhập có tồn tại không
    loginlink = driver.find_element(By.LINK_TEXT, "Login")
    assert loginlink

@pytest.mark.html
def test_case5_reset(driver):
    # Điều hướng đến trang web cần kiểm tra
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com/auth/reset-password" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng nhập có tồn tại không và đường link có truy cập được hay không
    loginlink = driver.find_element(By.LINK_TEXT, "Login")
    assert loginlink
    login_url = loginlink.get_attribute("href")
    try:
        # Sử dụng requests để gửi yêu cầu GET đến đường dẫn và kiểm tra mã trạng thái (status code)
        response = requests.get(login_url)
        assert response.status_code == 200, "Link is accessible"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
    assert driver.find_element(By.LINK_TEXT, "Login")
    
@pytest.mark.html
def test_case1_index(driver):
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
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
    # Kiểm tra nút đăng xuất
    menu = driver.find_element(By.XPATH, "//button[@id='menu-toggle']")
    driver.execute_script("arguments[0].click();",menu)
    sleep(2)
    logout_button = driver.find_element(By.XPATH, " //a[@class='main-btn primary-btn btn-hover' and @target='_blank']")
    assert logout_button.is_displayed()
    #Xóa các cookie và refresh lại trang
    driver.delete_all_cookies()
    driver.refresh()
        
@pytest.mark.html
def test_case2_index(driver):
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
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

    # Kiểm tra hiển thị số liệu tổng hợp
    total_item = driver.find_element(By.CSS_SELECTOR, ".text-bold")
    assert total_item.is_displayed()
    assert total_item.text !=None or total_item.text != ''
    
    #Xóa các cookie và refresh lại trang
    driver.delete_all_cookies()
    driver.refresh()
    
@pytest.mark.html
def test_case3_index(driver):
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
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

    # Kiểm tra biểu đồ dự đoán gây ra status fail
    chart1 = driver.find_element(By.ID, "Chart1")
    assert chart1.is_displayed()
    
    chart1 = driver.find_element(By.ID, "Chart4")
    assert chart1.is_displayed()

    # Kiểm tra biểu đồ predict_result gây ra status fail
    chart5 = driver.find_element(By.ID, "Chart5")
    assert chart5.is_displayed()
    
    #Xóa các cookie và refresh lại trang
    driver.delete_all_cookies()
    driver.refresh()
    
@pytest.mark.html
def test_case4_index(driver):
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
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
    # Kiểm tra lịch chọn data trong tháng
    calendar = driver.find_element(By.XPATH, "//input[@type='date']")
    assert calendar.is_displayed()
    
    #Xóa các cookie và refresh lại trang
    driver.delete_all_cookies()
    driver.refresh()    
     
@pytest.mark.html
def test_case5_index(driver):
    url = "http://ec2-54-166-21-94.compute-1.amazonaws.com" 
    response = requests.get(url)
    assert response.status_code == 200
    driver.get(url)
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
    
    # Kiểm tra nút đăng xuất
    menu = driver.find_element(By.XPATH, "//button[@id='menu-toggle']")
    driver.execute_script("arguments[0].click();",menu)
    sleep(2)
    logout_button = driver.find_element(By.XPATH, " //a[@class='main-btn primary-btn btn-hover' and @target='_blank']")
    assert logout_button.is_displayed()
    
    #Lấy url từ các link
    link_url = logout_button.get_attribute("href")
    try:
        response = requests.get(link_url)
        assert response.status_code == 200, "Link is accessible"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to access link: {e}")
    
    #Xóa các cookie và refresh lại trang    
    driver.delete_all_cookies()
    driver.refresh()