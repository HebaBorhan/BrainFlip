#!/usr/bin/env bash
# This script is used to setup the packages needed for BrainFlip game


sudo apt update

sudo apt install -y mysql-server

sudo systemctl start mysql
sudo systemctl enable mysql

sudo mysql_secure_installation

curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

sudo apt install -y python3 python3-pip

sudo pip3 install sqlalchemy

sudo pip3 install python-dotenv

sudo pip3 install Flask

mkdir brainflip
cd brainflip
npm init -y

npm install express bcryptjs body-parser cors mysql2 sequelize
