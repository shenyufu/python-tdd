配置新网站
==========

## 需要安装的包：

* nginx
* Python3
* Git
* pip
* virtualenv

以Ubuntu为例，可以执行下面的命令安装：

	sudu apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv
	
## 配置Nginx虚拟主机

* 参考nginx.template.conf
* 把SITENAME替换成所需的域名，例如staging.my-domain.com

## Upstart任务

* 参考gunicorn-upstart.template.com
* 把SITENAME替换成所需的域名，例如staging.my-domain.com

## 文件夹结构

假如有用户账户，home目录为/home/username

/home/username

