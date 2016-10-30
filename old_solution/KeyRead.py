#!/usr/bin/env python
# -*- coding: utf8 -*-

import signal
import sqlite3
import threading

import RPi.GPIO as GPIO
import zmq

import MFRC522

continue_reading = True
teacher_id = 0

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

def readCardData():
    global continue_reading
    global teacher_id
    teacher_id = 0
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)
    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    threading.Timer(5.0, stop,[])
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

            # Print UID
            #print "Card read UID: " + ".".join([str(x) for x in uid])

            # This is the default key for authentication
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                with sqlite3.connect('visitors.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        'SELECT id FROM rooms as r WHERE r.rfid="' + ".".join([str(x) for x in uid]) + '";')
                    for id in cursor.fetchall():
                        room_id = id[0]
                        break
                continue_reading = False
                MIFAREReader.MFRC522_StopCrypto1()
            else:
                print "Authentication error"
                
def stop():
    global continue_reading  
    continue_reading = False         
                
def start():
    global continue_reading
    # server
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://127.0.0.1:5555')
    print "service stated"
    while True:
        msg = socket.recv()
        if msg == 'start':
            continue_reading = True
            readCardData()
            socket.send('reading started')
        elif msg == 'getTeacherId':
            continue_reading = False
            socket.send(str(teacher_id))
        elif msg == 'stop':
            continue_reading = False
            socket.send("reading stopped")
        else:
            print "Unsuported"
  
start()