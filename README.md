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

##### 1.2 安装ChromeDriver

- 注意要安装Chrome相应版本的ChromeDriver

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
#cp chromedriver_linux64/chromedriver /usr/bin &&  chmod +x /usr/bin/chromedriver
```
