# EC2 Web Server Project

## About

This repository contains the files needed to connect to an Amazon EC2 instance, which runs the Video Games Catalog project. To access this instance visit the following address: https://18.225.34.242

## Configuration

### Server Setup

Once the server was created and connected, packages were installed that were needed to run the Video-Game-Catalog as well as the Apache2 and mod-wsgi functionality.

First the server was upgraded by using the `sudo apt-get update` and `sudo apt-get upgrade` functionality. Following with the installation of python and pip through the `sudo apt-get install python` and `sudo apt-get install python-pip` commands.

To run the Video-Game-Catalog project the following packages were installed after :
  * Sqlite3
  * requests
  * Sqlalchemy
  * httplib2
  * Flask

To run Apache 2 and mod-wsgi modules, the following installations were made:
  * apache2
  * libpache2-mod-wsgi

### Remote login and port setup

Once initial setup, the remote logon to the root account was disabled and the default SSH port was changed to 2200 through the configuration file located in the /etc/ssh/sshd_config directory

Port communication rules were established to allow ports for HTTP (80), NTP (123), SSH (2200), and HTTPS (443). These rules were established by running the `sudo ufw allow *port #*` and `sudo ufw enable` commands. Note that the same ports had to be enabled in EC2 by editing the Security Groups for the instance.

### Installing Video Game Catalog Application

The files from the Video-Game-Catalog repo were copied to the /var/www directory by using the command `git clone https://github.com/alvaropc216/Video-Game-Catalog.git`. Minor edits were made to the `videogames.py` file to facilitate functionality with wsgi and apache2.

A user named `catalog` was created, with limited but sufficient access to run the application, as specified in the Apache2 configuration file, as seen in the following section.

### Installing Apache 2 and WSGI

The Apache 2 and WSGI module installed were later configured to serve the Video Game Catalog application. Due to Facebook Login Authorization requirements, the application needed to run through a secure HTTPS connection. To establish this HTTPS connection, Apache was configured to redirect all request from port 80 to port 443 and a TLS certificate was created in the /roots/certs directory. Copies of the `myapp.wsgi` and `000-default.conf` files can be found in the repository

## Grader Account Setup and Login

A `grader` account was created, which was set up to belong to the Sudoers group. The RSA key pair was generated on a local environment with the ssh-key command. The public key generated was then stored in grader's .ssh directory.

In order to login as grader into the instance please type the following in your terminal and using the `projectGrader` key found in the repository:

`ssh grader@18.225.34.242 -p 2200 -i ~/.ssh/projectGrader`

## Resources Utilized

The resources below were used for this project:

1. Configure WSGI Application to serve Catalog: https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/#creating-a-wsgi-file

2. Create a TLS Certificate: https://www.linode.com/docs/security/ssl/create-a-self-signed-tls-certificate/

3. Configure 000-default.conf to include TLS Certificate: https://www.linode.com/docs/security/ssl/ssl-apache2-debian-ubuntu/

4. Configure 000-default.conf to redirect request from HTTP to HTTPS: https://www.namecheap.com/support/knowledgebase/article.aspx/9821/38/apache-redirect-to-https

5. Suggested changes to videogames.py to open fb_client_secrets.json: https://stackoverflow.com/questions/44742566/wsgi-cant-find-file-in-same-directory-in-app
