### 疫情填报系统~~又来给自己挖坑了~~

#### 一、准备工作

##### 1.1 安装Chrome

- 阿里云Ubuntu安装流程

```
#sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
#wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
#sudo apt-get update
#sudo apt-get install google-chrome-stable
```

- Chrome启动

```
#google-chrome --headless --remote-debugging-port=9222 http://chromium.org --disable-gpu --no-sandbox
```

##### 1.2 安装ChromeDriver

\# 注意要安装Chrome相应版本的ChromeDriver

- Chrome版本查看

```
#google-chrome --version
```

- ChromeDrive下载

这里我选择在 [淘宝镜像](https://developer.aliyun.com/mirror/NPM?from=tnpm) 下载

```
#wget https://npm.taobao.org/mirrors/chromedriver/83.0.4103.39/chromedriver_linux64.zip
```

- ChromeDrive解压

```
#x chromedriver_linux64.zip
```

- ChromeDriver权限设置

```
#mv -f chromedriver /usr/local/share/chromedriver  && ln -s /usr/local/share/chromedriver /usr/bin/chromedriver && ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver  &&  chmod +x /usr/bin/chromedriver
```

#### 二、提交脚本编写（python+selenium）

```python
print('见test.py')
```

#### 三、服务器部署

##### 3.1.1 Shell脚本定时运行.py

```
#vim dh.sh
```

##### 3.1.2 利用crontab服务

格式：：分 时 日 月 星期几 使用者  [命令]

```
#vim /etc/crontab
```
