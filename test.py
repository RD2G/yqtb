from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#填报
def tianbao(usrname,paswrd):
    #静默模式
    option = webdriver.ChromeOptions() 
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--remote-debugging-port=9222 http://chromium.org')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(chrome_options=chrome_options)    #声明使用Chrome
    url = r'http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp'
    browser.get(url)    #打开网页
    #登录信息
    username = browser.find_element_by_id('username')
    stu_number = usrname    #翱翔账户
    username.send_keys(stu_number)
    stu_password = paswrd   #翱翔密码
    password = browser.find_element_by_id('password')
    password.send_keys(stu_password)
    #点击登录
    browser.find_element_by_class_name('submit_button').click()
    #点击健康登记按钮
    browser.find_element_by_partial_link_text('健康登记').click()
    #点击提交信息
    browser.find_element_by_partial_link_text('提交填报信息').click()
    time.sleep(1)
    #承诺
    browser.find_element_by_xpath('/html/body/div[3]/form/div[6]/div[2]/div[10]').click()
    #确认提交
    browser.find_element_by_partial_link_text('确认提交').click()
    time.sleep(1)
    print('-'*100)
    print(browser.page_source)  #打印网页源代码
    print('-'*100)
    browser.close()



#发邮件
def email(srt):
    pass

#主函数
def main():
    n = input('请输入翱翔账号：')
    p = input('请输入翱翔密码：')
    tianbao(n,p)
    #if (tianbao()):
    #    email("成功")
    #else:
    #    email("失败")

if __name__ == '__main__':
    main()
