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
- mlx90614.py: This file will take the input from the object temperature sensor and send it to a real time database using firebase. This file can be executed on raspberry start.

# Local Machine files:
- Rest of the project files.

# Build:
1) Download and install the latest Node.js version:
2) curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
3) sudo apt install -y nodejs
4) Clone the repository and check out the master branch: git clone https://github.com/MichMich/MagicMirror
5) Enter the repository: cd MagicMirror/
6) Install the application: npm install --only=prod --omit=dev
7) Make a copy of the config sample file: cp config/config.js.sample config/config.js
8) Start the application: npm run start

# License:
The MIT License (MIT)
Copyright © 2016-2021 Michael Teeuw

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
