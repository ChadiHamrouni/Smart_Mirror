import time
import board
import busio as io
import adafruit_mlx90614
import pyrebase
 
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)
 #Change the config with your personal firebase config chunk of code found in the firebase website, specifically in the project settings.
config = {
 "apiKey": "JvaiCrp25mTTEh4rH28vqaoJjT3svy7IyzmMSK92",
 "authDomain": "temperature-data-3ff19.firebaseapp.com",
 "databaseURL": "https://temperature-data-3ff19-default-rtdb.europe-west1.firebasedatabase.app/",
 "storageBucket": "temperature-data-3ff19.appspot.com"
}
 
firebase = pyrebase.initialize_app(config)
db = firebase.database()
 
print("Send Data to Firebase Using Raspberry Pi")
print("—————————————-")
print()
 
while True:
 
 objectString = "{:.2f}".format(mlx.object_temperature)
 
 
 objectCelsius = float(objectString)
 

 print("Object Temp: {} °C".format(objectString))
 print()
 
 data = {
 "object": objectCelsius,
 }
 db.child("mlx90614").child("1-set").set(data)

 
 time.sleep(2)