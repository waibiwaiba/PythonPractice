import requests
from bs4 import BeautifulSoup



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

if __name__ == '__main__':
    email = get_10min_mail()
