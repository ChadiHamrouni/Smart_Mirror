# Smart_Mirror Extending functionality and Features.
Website controlling some modules of the Magic Mirror API with an addition of an Object sensor data display in the website.

The Smart Mirror is a famous project among tech enthusiasts. It's unique, easy to implement and makes great use of a spare monitor even if shows only the date, time and weather.

In this project I tried to contribute and hop in the Smart Mirror wagon by adding a room temperature sensor, an object temperature sensor (working as body temperature sensor) and a motion sensor (for turning the mirror on and off wirelessly).

Further on all features and data added from the Smart mirror community and specifically those in blabal can be Shown and Hidden in your smart mirror using our website. Showing and hiding modules such as temperature, gmail, time, date, news, calendar...

# Pre-Requisites:
* Intalling the Magic Mirror API following https://github.com/MichMich/MagicMirror and updating it.
* Install PIR Motion Sensor module using https://github.com/paviro/MMM-PIR-Sensor  to control switching the Mirror on and off.
* Install MMM-temp-ds18b20 module using https://github.com/Thlb/MMM-temp-ds18b20 to display room temperature in the mirror (not necessary since this data won't be displayed in the website.
- REMARK: I2C on the Raspberry pi should be enabled!
- for More modules: https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules

# Raspberry Pi files:
- Magic Mirror API 
- Magic Mirror remote API
- temp.py : This file will take the input from the object temperature sensor and send it to a real time database using firebase. This file can be executed on raspberry start.

# Local Machine files:
- Rest of the project files.
