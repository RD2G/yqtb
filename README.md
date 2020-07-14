### 疫情填报系统~~又来给自己挖坑了~~

#### 一、准备工作

##### 1.1 安装Chrome

- 阿里云Ubuntu安装流程

```
sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
sudo apt-get update
sudo apt-get install google-chrome-stable
```

- Chrome启动

##### 1.2 安装ChromeDriver

- 注意要安装Chrome相应版本的ChromeDriver

- Chrome版本查看

```
google-chrome --version
```
