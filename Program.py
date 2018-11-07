import RPi.GPIO as GPIO
import time

LedPin = 11

def settings():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(LedPin, GPIO.OUT)
  GPIO.output(LedPin, GPIO.HIGH)

def start():
  while True:
    GPIO.output(LedPin, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(LedPin, GPIO.LOW)
    time.sleep(10)

def destroy():
  GPIO.output(LedPin, GPIO.LOW)
  GPIO.cleanup()

if __name__ == '__main__':
  settings()
  try:
    start()
  except KeyboardInterrupt:
    destroy()
