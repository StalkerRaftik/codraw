#!/bin/bash

if ! [ $(id -u) = 0 ]; then
   echo "Access denied! Run script with a SUDO rights!" >&2
   exit 1
fi

apt update

mkdir centrifugo
cd centrifugo
wget https://github.com/centrifugal/centrifugo/releases/download/v2.8.4/centrifugo_2.8.4_linux_amd64.tar.gz
tar zxvf centrifugo_2.8.4_linux_amd64.tar.gz centrifugo
rm centrifugo_2.8.4_linux_amd64.tar.gz

centrifugo version
echo Centrifuge was successfully installed

sudo apt install nodejs
npm install --global yarn
yarn --version
npm list -g
echo nodejs + npm + yarn was installed

yarn global add @vue/cli
vue --version
echo vue-cli installed

mkdir /etc/codraw
touch /etc/codraw/settings.ini

echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')
" | python manage.py shell