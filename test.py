from selenium import webdriver
import time

#填报
def tianbao():
    option = webdriver.ChromeOptions()
    # 静默模式
    option.add_argument('headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome()    #声明使用Chrome
    url = 'www.qq.com'
    browser.get(url)    #打开网页
    print('*'*100)
    print(browser.title)  #打印网页源代码
    print('*'*100)
    browser.close()    #关闭浏览器



#发邮件
def email(srt):
    pass

def main():
    if (tianbao()):
        email("成功")
    else:
        email("失败")

if __name__ == '__main__':
    #main()
    tianbao()
