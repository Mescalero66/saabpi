## log in via terminal
ssh pi@raspberrypi.local

## update pi and reboot
sudo apt update && sudo apt full-upgrade --yes && sudo reboot

## install  Git, Pip
sudo apt install git python3-dev python3-pip --yes

## clone grove.py repo
git clone https://github.com/Seeed-Studio/grove.py
cd grove.py
sudo pip3 install .

## enable I2C interface
sudo raspi-config nonint do_i2c 0

## install i2Ctools
sudo apt-get install i2c-tools

## install SoftI2C on I2C bus8, GPIO 23(SDA) and GPIO24(SCL)
dtoverlay=i2c-gpio,bus=8

this should be added to /boot/config.txt (then reboot)

<https://learn.adafruit.com/raspberry-pi-i2c-clock-stretching-fixes/software-i2c>
<https://github.com/fivdi/i2c-bus/blob/master/doc/raspberry-pi-software-i2c.md>

## identify I2C buses
ls /dev/i2c*

## scan I2C devices
i2cdetect [bus] -y

i.e.
i2cdetect 1 -y
would scan I2C bus #1 for devices

## reboot
sudo reboot