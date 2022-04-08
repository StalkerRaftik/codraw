#!/bin/bash

if ! [ $(id -u) = 0 ]; then
   echo "Access denied! Run script with a SUDO rights!" >&2
   exit 1
fi

apt update

apt install python3.9

apt install snap
snap install node --classic
npm install --global yarn
yarn --version
npm list -g
echo nodejs + npm + yarn was installed