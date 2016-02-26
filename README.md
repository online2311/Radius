# UniFi Cloud Key Radius 功能特性

- 标准Radius认证记账支持，提供完整的AAA实现。
- 支持pap，chap，mschap-v2验证。
- 提供基于WEB的管理控制台界面。
- 提供基于WEB的自助服务系统，支持界面定制。
- 基于Python Twisted高性能异步网络框架开发的认证计费引擎。
- 支持各种主流接入设备(RouterOS,思科，华为，爱立信，中兴，阿尔卡特，H3C等)并轻松扩展，支持多设备接入管理。
- 支持使用Oracle, MySQL, PostgreSQL, MSSQL等主流数据库存储数据，并支持高速数据缓存。
- 支持预付费时长，预付费流量，预付费包月，买断包月，买断时长，买断流量资费策略。
- 支持会话时长定制。
- 支持数据库定时备份，支持FTP远程备份。
- 支持用户在线查询，解锁，批量解锁，强制下线。
- 支持用户在线统计，流量统计。
- 支持WEB界面上网日志查询。
- 支持灵活的授权策略扩展。
- 支持操作员权限分级管理。
- 支持第三方支付在线充值续费。
- 支持用户数据，财务数据，记账数据导出管理。
- 支持批量用户导入开户。
- 支持在线实时开通账号使用。
- 支持COA强制下线功能。
- 支持实时记账扣费。
- 支持全局与资费级别的自定义记账间隔下发
- 支持不同类型设备自动限速适配。
- 支持账号到期自动下线。
- 支持到期特定地址池下发。
- 支持到期提前通知，通过邮件和webhook触发实现。
- 详细的操作日志记录，条件查询。

# 安装教程
本教程仅适用于UniFi Cloud Key设备上的Radius安装与使用，
	
## 添加Debian源
	echo "deb http://debian.ustc.edu.cn/debian/ jessie main contrib non-free" >> /etc/apt/sources.list && \
	echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ jessie main contrib non-free" >> /etc/apt/sources.list && \
	echo "deb http://debian.bjtu.edu.cn/debian/ jessie main non-free contrib" >> /etc/apt/sources.list 

## 安装支持库
	apt-get update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential && \
	apt-get install -y software-properties-common && \
	apt-get install -y byobu curl git htop man unzip vim wget && \
	apt-get install -y  wget zip libffi-dev openssl libssl-dev git gcc tcpdump && \
	apt-get install -y  mysql-client libmysqlclient-dev libzmq-dev && \
	apt-get clean all && \
	rm -rf /var/lib/apt/lists/*
  
## Git Radius代码至本地
	git clone -b UCK https://github.com/online2311/Radius.git /opt/toughradius

## 安装ARM架构pypy及pip、distribute
	cp /opt/toughradius/pysetup/pypy-4.0.0-linux-armhf-raring.tar.bz2 /opt/pypy-4.0.0-linux-armhf-raring.tar.bz2 && \
	cd /opt && tar -xf pypy-4.0.0-linux-armhf-raring.tar.bz2 && \
    ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/pypy /usr/local/bin && \
   	cd /opt/toughradius/pysetup && unzip distribute-0.7.3.zip && cd distribute-0.7.3 && pypy setup.py install && \
	pypy /opt/toughradius/pysetup/get-pip.py && ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/pip /usr/local/bin && \
	pypy -m pip install  --upgrade setuptools && \
	pypy -m pip install  supervisor && \
	ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/supervisord /usr/local/bin && \
    ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/supervisorctl /usr/local/bin

## 其他系统设置
	echo "set nocompatible" >> /root/.vimrc && echo "set backspace=2" >> /root/.vimrc && \
	cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

## 安装PYPY 支持库
	pypy -m  pip install --upgrade pip && \
	pypy -m  pip install bottle && \
	pypy -m  pip install Mako && \
	pypy -m  pip install Beaker && \
	pypy -m  pip install MarkupSafe && \
	pypy -m  pip install PyYAML && \
	pypy -m  pip install Twisted && \
	pypy -m  pip install treq && \
	pypy -m  pip install tablib && \
	pypy -m  pip install cyclone && \
	pypy -m  pip install six && \
	pypy -m  pip install autobahn && \
	pypy -m  pip install pycrypto && \
	pypy -m  pip install pyOpenSSL>=0.14 && \
	pypy -m  pip install service_identity && \
	pypy -m  pip install MySQL-python && \
	pypy -m  pip install SQLAlchemy && \
	pypy -m  pip install pyzmq && \
	pypy -m  pip install txzmq && \
	pypy -m  pip install msgpack-python && \
	pypy -m  pip install python-memcached && \
	pypy -m  pip install psutil && \
	pypy -m  pip install IPy
	

## radius 安装

	cp /opt/toughradius/scripts/radiusrun /usr/local/bin/radiusrun && \
	chmod +x /usr/local/bin/radiusrun && \
	/usr/local/bin/radiusrun install

## 初始化数据库
	radiusrun initserv

##  启动Radius全部程序
	radiusrun standalone



