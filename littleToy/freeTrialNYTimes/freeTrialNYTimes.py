import requests
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import string


def get_10min_mail():
    url = 'https://10minutemail.org'
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        print('请求超时，请稍后再试。')
    except requests.exceptions.RequestException as e:
        print('发生错误：', e)
    else:
        pass
        # print(response.content)
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')
    # 获取邮箱地址
    email = soup.find('input', {'id': 'fe_text'})['value']
    print('10分钟邮箱地址:', email)
    return email




# 获取当前脚本文件所在目录的路径
dir_path = os.path.dirname(os.path.abspath(__file__))

# 构造 chromedriver.exe 的路径
driver_path = os.path.join(dir_path, 'tools', 'chromedriver_win32', 'chromedriver.exe')

# 设置目标网站的 URL
target_url = 'https://www.guilfordfreelibrary.org/adults/the-new-york-times-online-access/'

# 模拟打开第一个网站
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 将通配符替换为正则表达式中的通配符 '.+'
to_click_link = 'https://www.nytimes.com/subscription/*'
to_click_link = to_click_link.replace('*', '.+')

# 使用正则表达式查找符合要求的超链接
pattern = re.compile(to_click_link)
target_link = soup.find('a', href=pattern).get('href')


# 使用 Selenium WebDriver 跳转到第二个网站

# 创建 Service 对象
chrome_service = Service(driver_path)

# 创建 Google Chrome WebDriver 对象
options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get(target_link)


# 找到需要点击的按钮的 HTML 元素，并点击
# 等待10s按钮元素出现
wait = WebDriverWait(driver, 60)
button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="giftRedeem__submitButton"]')))
button = driver.find_element(By.XPATH, '//input[@class="giftRedeem__submitButton"]')
time.sleep(1)
button.click()

# 在注册页面中填写邮箱地址，并提交表单
email_address = get_10min_mail()  # 设置邮箱地址
wait = WebDriverWait(driver, 60)
email_input = wait.until(EC.presence_of_element_located((By.ID, 'email')))
time.sleep(0.7)
email_input.send_keys(email_address)
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
time.sleep(0.4)
submit_button.click()

# 生成随机密码
password_length = 10  # 设置密码长度
password_characters = string.ascii_letters + string.digits  # 密码可选字符
password = ''.join(random.choice(password_characters) for i in range(password_length))
print('设置的密码:', password)
# 在密码栏中填写随机密码，并提交表单
wait = WebDriverWait(driver, 60)
password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))
# password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
time.sleep(1.7)
password_field.send_keys(password)
time.sleep(0.4)
create_account_button = driver.find_element(By.XPATH, '//button[@type="submit" and span[contains(text(),"Create Account")]]')
time.sleep(0.7)
create_account_button.click()

# 点击“Continue”按钮
wait = WebDriverWait(driver, 60)
continue_button = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-testid="get-started-btn"]')))
time.sleep(0.5)
continue_button.click()

time.sleep(1.5)

wait = WebDriverWait(driver, 60)
welcome_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="welcome-screen-button"]')))
time.sleep(0.6)
welcome_button.click()

time.sleep(2)

news_ss_button = driver.find_element(By.XPATH, '//button[@data-testid="newsletter-signup-sheet-button"]')
time.sleep(0.7)
news_ss_button.click()

time.sleep(2.5)

con_sms_button = driver.find_element(By.XPATH, '//button[@data-testid="continue-without-sms"]')
con_sms_button.click()

# 关闭浏览器
driver.quit()

print(email_address)
print(password)

new_account_path = os.path.join(dir_path, 'new_account.txt')
# 打开文件
with open(new_account_path, 'w') as f:
    # 写入 email_address 和 password
    f.write(email_address + '\n')
    f.write(password + '\n\n')


if __name__ == '__main__':
    email = get_10min_mail()
    