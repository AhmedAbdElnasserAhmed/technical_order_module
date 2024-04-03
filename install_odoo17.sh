#!/bin/bash
###############################################################################
# Script for installing Odoo 17 on Ubuntu 18.04 and 20.04 (could be used for other version too)
# Author: Hesham Aboalsoud
#-------------------------------------------------------------------------------
# sudo chmod +x install_odoo17.sh
# Execute the script to install Odoo:
# ./install_odoo17
################################################################################
# Update package list
sudo apt-get update
echo -e "\e[31m Done Update System.\e[0m"

# Upgrade installed packages
sudo apt-get upgrade -y

echo -e "\e[31m Done Upgrade System.\e[0m"

# Remove unnecessary packages
sudo apt-get autoremove -y

echo -e "\e[31m Done Remove unnecessary packages In  System.\e[0m"

# Clean up package cache
sudo apt-get clean
echo -e "\e[31m Clean up package cache.\e[0m"


# Install Python 3.11 (replace the version with the desired one)
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.11

echo -e "\e[31m Done Install Python 3.11.\e[0m"

#install essential packages
sudo apt-get install -y git python3.11-dev python3-pip build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev libldap2-dev libsasl2-dev node-less libjpeg-dev libpq-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev poppler-utils libevent-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev libxml2-dev libxslt1-dev zlib1g-dev libldap2-dev libsasl2-dev

echo -e "\e[31m Done Install Essential Packages.\e[0m"

# Install virtualenv and create a virtual environment
sudo apt-get install -y python3.11-venv
python3.11 -m venv odoo17-env
source odoo17-env/bin/activate

echo -e "\e[31m Created Venv for odoo17.\e[0m"

# Clone Odoo 17 repository
git clone --depth 1 --branch 17.0 --single-branch https://www.github.com/odoo/odoo.git odoo-17
echo -e "\e[31m Done Clone odoo17.\e[0m"

# Install Odoo dependencies
pip install -r odoo-17/requirements.txt


# Deactivate the virtual environment
deactivate

echo "Odoo 17 installation completed successfully!"

