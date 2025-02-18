#!/usr/bin/env python3

# The start point for the HIL system on the RPi (controls which "board" is currently being simulated)

import boards.power_distribution as power_distribution
import boards.centre_console as centre_console
import boards.bms as bms

import sys
import serial

i2c_slave_port = '/dev/ttyACM0'
baud_rate = 9600

# TODO: Use Protobuf to encode/decode Serial messages prior to writing to slave

def start_simulation(board_to_simulate):
    # Initialize board that was requested
    board = None
    # TODO: Add more boards that we want to simulate
    if board_to_simulate == "Centre Console":
        print("Simulating Centre Console")
        board = centre_console.CenterConsole()
    elif board_to_simulate == "Power Distribution":
        print("Simulating Power Distribution")
        board = power_distribution.PowerDistribution()
    elif board_to_simulate == "BMS":
        print("Simulating BMS")
        board = bms.BMS()
    else:
        # Default is Power Distribution
        board = power_distribution.PowerDistribution()
        print("Simulating Power Distribution")

    # Wait for message over Serial
    ser = serial.Serial(i2c_slave_port, baud_rate)

    # TODO: If board has I2C peripheral enabled, then "program" the slave with the I2C address of the peripheral so that it accepts messages
    # i2c_address = board.get_i2c_address()
    # if i2c_address:
    #     ser.write(i2c_address)

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"Received message: {data}")

            # If I2C message, we only handle write commands
            message_type = ...
            message = ...
            if message_type == "I2C" or message_type == "SPI":
                # Update peripheral state, retrieve new state of peripheral, and send back to slave
                response = board.handle_message(message, message_type)

                ser.write(response.encode())
            else:
                # TODO: Handle error messages
                pass

if __name__ == "__main__":
    # Retrieve board to simulate from command line arguments
    argument = None
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        argument = " ".join(arguments)

    start_simulation(arguments)