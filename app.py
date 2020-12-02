from flask import Flask, render_template
import RPi._GPIO as GPIO
app = Flask(__name__)


# Variables
ledpin = 16

# Setting GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin,GPIO.OUT)


# Routes

# Main
@app.route("/")
def hello():
    return("Here I am Server Side")

# LED ON
@app.route("/on")
def on():
    GPIO.output(ledpin, GPIO.HIGH)
    return render_template('ledon.html')
    

# LED OFF
@app.route("/off")
def off():
    GPIO.output(ledpin, GPIO.LOW)
    return render_template('ledoff.html')
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)