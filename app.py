from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import i2clcd
from time import sleep

app = Flask(__name__)


# Variables
basicledpin = 16
redpin = 25
greenpin = 24
bluepin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setting GPIOs
GPIO.setup(basicledpin,GPIO.OUT)
GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)
GPIO.setup(bluepin,GPIO.OUT)

red_pwm = GPIO.PWM(redpin,100)
green_pwm = GPIO.PWM(greenpin,100)
blue_pwm = GPIO.PWM(bluepin,100)


red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

#lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
#lcd.init()


# Routes

# Main
@app.route("/")
def welcome():
    GPIO.output(basicledpin, GPIO.LOW)
    return render_template('index.html')


# Basic LED
@app.route("/ledon")
def ledon():
    GPIO.output(basicledpin, GPIO.HIGH)
    return render_template('ledon.html')
    
@app.route("/ledoff")
def ledoff():
    GPIO.output(basicledpin, GPIO.LOW)
    return render_template('ledoff.html')
    



# RGB LED
@app.route("/ledrgb", methods=['POST','GET'])
def ledrgb():

    if request.method == 'POST':
        redvalue = 0
        greenvalue = 0
        bluevalue = 0

        GPIO.output(redpin, GPIO.LOW)
        GPIO.output(greenpin, GPIO.LOW)
        GPIO.output(bluepin, GPIO.LOW)

        redvalue = request.form.get("redvalue",False)
        greenvalue = request.form.get("greenvalue",False)
        bluevalue = request.form.get("bluevalue",False)

        redvalue = int(redvalue)
        greenvalue = int(greenvalue)
        bluevalue = int(bluevalue)

        redvalue = int(redvalue/2.55)
        greenvalue = int(greenvalue/2.55)
        bluevalue = int(bluevalue/2.55)

        red_pwm.ChangeDutyCycle(redvalue)
        green_pwm.ChangeDutyCycle(greenvalue)
        blue_pwm.ChangeDutyCycle(bluevalue)

        print(redvalue)
        print(bluevalue)
        print(greenvalue)

    return render_template('ledrgb.html')





# LCD
@app.route("/lcd", methods=['POST','GET'])
def lcd():
    if request.method == 'POST':
        L1 = ' '
        L2 = ' '

        L1 = request.form.get("L1",False)
        L2 = request.form.get("L2",False)

        """lcd.print_line(L1, line=0)
        sleep(.7)
        lcd.print_line(L2, line=1)"""
        print(type(L1))
        print(L1)

    return render_template('lcd.html')







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)