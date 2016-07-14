#!/bin/bash 

sudo apt-get -y update 
sudo apt-get -y upgrade 
sudo apt-get -y install python-dev 
sudo apt-get install -y build-essential 
sudo apt-get install -y libssl-dev 
sudo apt-get install -y libffi-dev 
sudo apt-get -y install libpq-dev  
sudo apt-get -y install python-pip 
sudo apt-get -y install postgresql

sudo pip install virtualenvwrapper  
mkvirtualenv composite

# add these lines to .bashrc 
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'export PROJECT_HOME=$HOME/Devel' >> ~/.bashrc 
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc 
##############################################
cd /vagrant 
pip install -r requirements.txt 

# su postgres -c 'createuser -dPRS vagrant'
sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant';"
sudo -i -u vagrant -c 'createdb ascii'