#!/usr/bin/env python3
import socket


def check(string):

    # defining variables for parity checks
    parity = 0
    parityBit = 0

    # looping through and seeing if odd or even and parity bit
    for n,i in enumerate(string):
        if n == 0:
            n + 1
        elif n == len(string) - 2:
            parityBit = i
            break
        else:
            if i == '1':
                parity += 1

    # determining if parity is valid or not
    if parity%2 == 0:
        if parityBit == '0':

            # correct parity based off of parity bit
            return str(1)
        else:

            # incorrect parity based off of parity bit
            return str(0)
    else:
        if parityBit == '1':

            # correct parity based off of parity bit
            return str(1)
        else:

            # incorrect parity based off of parity bit
            return str(0)


# making connection
s = socket.socket()
s.connect(("misc.chal.csaw.io", 4239))

# used to skip the intro message and keep track of connection times
i = 0

# used to print out the flag
message = ''

# untill no more connection
while True:

    # connections first one is weird
    if i == 0:
        i += 1
        data = s.recv(1000).decode().split('\n')[1]
    else:
        i += 1
        data = s.recv(1000).decode()

    # check to see if data recieved
    if data:
        # check if parity is right
        stat = check(data.strip())
        print("Data: %s Sol = %s"% (data, stat))
        if stat == '1': message += chr(int(data.strip()[1:9], 2))
        s.send(stat.encode())


    elif not data:

        # end of connection
        print('amount of times connected = ' + str(i))
        print(message)
        s.close()
        break
