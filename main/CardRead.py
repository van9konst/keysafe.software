# -*- coding: utf8 -*-
import signal
import threading
import time
import RPi.GPIO as GPIO
import zmq
import MFRC522

continue_reading = True
teacher_id = 0
room_id = 0


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal, frame):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()


def readTeacherCardData():
    global continue_reading
    global teacher_id
    teacher_id = 0
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)
    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    threading.Timer(5.0, stop, [])
    timeout = time.time() + 15
    while continue_reading:
        print "read cycle"
        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"
        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # This is the default key for authentication
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                teacher_id = ','.join([str(x) for x in uid])
                continue_reading = False
                MIFAREReader.MFRC522_StopCrypto1()
        elif time.time() > timeout:
            stop()
            print "Authentication error"


def stop():
    global continue_reading
    continue_reading = False
    print 'stop cycle'


def start():
    global continue_reading
    # server
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://127.0.0.1:5555')
    print "service stated"
    while True:
        msg = socket.recv()
        if msg == 'readTeacherId':
            continue_reading = True
            readTeacherCardData()
            socket.send('reading started')
        elif msg == 'getTeacherId':
            continue_reading = False
            socket.send(str(teacher_id))
        elif msg == 'stop':
            continue_reading = False
            socket.send("reading stopped")
        else:
            print "Unsupported"

start()
