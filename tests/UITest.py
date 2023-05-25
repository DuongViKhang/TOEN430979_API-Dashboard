from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
import logging
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# Fixture setup
@pytest.fixture(scope="module")
def driver():
    # Cài đặt các tùy chọn cho Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy trình duyệt ẩn danh
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
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang đăng nhập không
    assert "Login - API Dashboard" in driver.title
    assert driver.find_element(By.TAG_NAME, 'h2').text=="Login"
    
@pytest.mark.html
def test_case2_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường username và password có tồn tại không
    assert driver.find_element(By.ID, 'username')
    assert driver.find_element(By.ID, 'password')
    
@pytest.mark.html
def test_case3_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút đăng nhập có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
    
@pytest.mark.html
def test_case4_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra checkbox user và admin có tồn tại không
    assert driver.find_element(By.ID, 'user')
    assert driver.find_element(By.ID, 'admin')
    
@pytest.mark.html
def test_case5_login(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra 2 link quên mật khẩu và create an account có tồn tại không
    assert driver.find_element(By.LINK_TEXT, "Forgot Password?")
    assert driver.find_element(By.LINK_TEXT, "Create an account")
    
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
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang đăng ký không
    assert "SignUp - API Dashboard" in driver.title
    assert driver.find_element(By.TAG_NAME, 'h2').text=="SignUp"
    
@pytest.mark.html
def test_case2_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/signup")
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
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút đăng ký có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
    
@pytest.mark.html
def test_case4_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/signup")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các radio có tồn tại
    assert driver.find_element(By.ID, 'radio-normal')
    assert driver.find_element(By.ID, 'radio-admin')
    #kiểm tra radio normal có được chọn mặc định
    radio_button = driver.find_element(By.ID, "radio-normal")
    is_selected = radio_button.is_selected()
    assert is_selected, "Default radio button should be selected"
    
@pytest.mark.html
def test_case5_signup(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/signup")
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
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/forgot-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang gửi mail quên mật khẩu không
    assert driver.find_element(By.TAG_NAME, 'h2').text=="Forgot Password"
    
@pytest.mark.html
def test_case2_forgot(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/forgot-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường có tồn tại không
    assert driver.find_element(By.ID, 'email')
    
@pytest.mark.html
def test_case3_forgot(driver): 
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/forgot-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút gửi email có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
     
@pytest.mark.html
def test_case4_forgot(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/forgot-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra link đăng ký có tồn tại không và đường link có truy cập được hay không
    signuplink = driver.find_element(By.LINK_TEXT, "Create an account")
    assert signuplink
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
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/reset-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra tiêu đề trang có phải là trang đổi mật khẩu không
    assert driver.find_element(By.TAG_NAME, 'h2').text=="Reset Password"
    
@pytest.mark.html
def test_case2_reset(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/reset-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra các trường có tồn tại không
    assert driver.find_element(By.ID, 'OTP')
    assert driver.find_element(By.ID, 'new_password')
    assert driver.find_element(By.ID, 'confirm_password')
    
@pytest.mark.html
def test_case3_reset(driver): 
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/reset-password")
    # Thực hiện các thao tác kiểm tra giao diện
    # kiểm tra nút đổi mật khẩu có tồn tại không
    driver.find_element(By.XPATH, "//button[@type='submit']")
     
@pytest.mark.html
def test_case4_reset(driver):
    # Điều hướng đến trang web cần kiểm tra
    driver.get("http://ec2-34-227-149-56.compute-1.amazonaws.com:50001/auth/reset-password")
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