echo "deb http://ftp.us.debian.org/debian/ jessie main contrib non-free" >> /etc/apt/sources.list && \
echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" >> /etc/apt/sources.list && \
echo "deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib" >> /etc/apt/sources.list && \
echo "deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib" >> /etc/apt/sources.list && \
echo "deb-src http://mirrors.163.com/debian/ jessie main non-free contrib" >> /etc/apt/sources.list && \
echo "deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib" >> /etc/apt/sources.list && \
echo "deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib" >> /etc/apt/sources.list && \
echo "deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib" >> /etc/apt/sources.list && \
echo "deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib" >> /etc/apt/sources.list





  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install -y  wget zip libffi-dev openssl libssl-dev git gcc tcpdump && \
  apt-get install -y  mysql-client libmysqlclient-dev libzmq-dev && \
  apt-get clean all && \
  rm -rf /var/lib/apt/lists/*

git clone -b master https://github.com/online2311/Radius.git /opt/toughradius

cd /opt/toughradius/pysetup && unzip distribute-0.7.3.zip && cd distribute-0.7.3 && pypy setup.py install
    
cp /opt/toughradius/pysetup/pypy-4.0.0-linux-armhf-raring.tar.bz2 /opt/pypy-4.0.0-linux-armhf-raring.tar.bz2
cd /opt && tar -xf pypy-4.0.0-linux-armhf-raring.tar.bz2 && \
    ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/pypy /usr/local/bin && \
    pypy --version

pypy /opt/toughradius/pysetup/get-pip.py && ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/pip /usr/local/bin

pypy -m pip install  --upgrade setuptools

pypy -m pip install  supervisor

ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/supervisord /usr/local/bin && \
    ln -s /opt/pypy-4.0.0-linux-armhf-raring/bin/supervisorctl /usr/local/bin

echo "set nocompatible" >> /root/.vimrc && echo "set backspace=2" >> /root/.vimrc
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

pypy -m  pip install --upgrade pip
pypy -m  pip install bottle
pypy -m  pip install Mako
pypy -m  pip install Beaker
pypy -m  pip install MarkupSafe
pypy -m  pip install PyYAML
pypy -m  pip install Twisted
pypy -m  pip install treq
pypy -m  pip install tablib
pypy -m  pip install cyclone
pypy -m  pip install six
pypy -m  pip install autobahn
pypy -m  pip install pycrypto
pypy -m  pip install pyOpenSSL>=0.14
pypy -m  pip install service_identity
pypy -m  pip install MySQL-python
pypy -m  pip install SQLAlchemy
pypy -m  pip install pyzmq
pypy -m  pip install txzmq
pypy -m  pip install msgpack-python
pypy -m  pip install python-memcached
pypy -m  pip install psutil
pypy -m  pip install IPy


cp /opt/toughradius/scripts/radiusrun /usr/local/bin/radiusrun

chmod +x /usr/local/bin/radiusrun
/usr/local/bin/radiusrun install




pypy /opt/toughradius/toughctl --initdb

vi /etc/rc.local

pypy /opt/toughradius/toughctl --standalone



