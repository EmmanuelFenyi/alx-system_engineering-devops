#!/bin/bash

# Update package index
sudo apt update

# Download and install the MySQL APT repository package
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo apt install ./mysql-apt-config_0.8.12-1_all.deb

# Update package index again
sudo apt update

# Install MySQL Server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

# Secure MySQL installation
sudo mysql_secure_installation

# Start MySQL service
sudo systemctl start mysql

# Enable MySQL service to start at boot time
sudo systemctl enable mysql

echo "MySQL 5.7.x has been installed and configured successfully."

