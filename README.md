# SHTC3 Code Example
Setup and use the SHTC3 Digital Temperature Sensor on a Raspberry Pi with Flask REST API

# Clone the repo and install Flask

Thanks to [geerlingguy](https://github.com/geerlingguy) for the code! Big fan!

````
git clone https://github.com/timothysteffes/SHTC3-Code-Example.git
cd SHTC3-Code-Example/
sudo pip3 install adafruit-circuitpython-shtc3 --break-system-packages
pip3 install flask netifaces --break-system-packages
````

# Raspberry Pi Setup

Enable I2C in Interface Options.

````
sudo raspi-config
````
The API host IP address is defined in the api_temp.py. Change this to the IP Address that you want to use.

# Run the code

````
python api_temp.py
````

# Wiring

* (+) to Pin 1 (3.3v)
* (-) to Pin 14 (ground)
* SDA to Pin 3 (GPIO 2 / SDA)
* SCI to Pin 5 (GPIO 3 / SCL)

# References
https://learn.adafruit.com/adafruit-sensirion-shtc3-temperature-humidity-sensor/python-circuitpython

https://github.com/adafruit/Adafruit_CircuitPython_SHTC3

https://docs.circuitpython.org/projects/shtc3/en/latest/

[Amazon link to example product](https://www.amazon.com/dp/B08ZMWHT8M?ref_=cm_sw_r_cp_ud_dp_D1N9N92FZS8VWPVQN4NQ) (not an affiliate link)
