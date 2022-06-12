# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# nostarch_soup = bs4.BeautifulSoup(res.text)
#
# # 这里用到css选择器
# print(nostarch_soup.select('div'))

from selenium import webdriver

browser = webdriver.Edge(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
browser.get('https://mail.163.com/')
try:
    emailElem = browser.find_elements_by_css_selector('h2.loginbox-title')
    for index, _ele in enumerate(emailElem):
        print(f'{index}:{_ele.text}')
    # emailElem.send_keys('not_my_real_email@gmail.com')
except Exception as error:
    print(f'{error}')
