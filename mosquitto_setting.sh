#!/bin/sh

sudo cp ~/confer_pw.txt /etc/mosquitto/confer_pwfile
sudo mosquitto_passwd -U /etc/mosquitto/confer_pwfile
sudo tee /etc/mosquitto/conf.d/confer.conf << EOF > /dev/null
listener 1883
allow_anonymous false
password_file /etc/mosquitto/confer_pwfile
EOF
sudo systemctl reload mosquitto
