#!/usr/bin/env python3

# The start point for the HIL system on the RPi (controls which "board" is currently being simulated)

import boards.power_distribution as power_distribution
import boards.centre_console as centre_console
import bms
import imu

import serial

valid_boards = {"Power Distribution": power_distribution, "Centre Console": centre_console, "BMS": bms, "IMU": imu}
default_board = "Power Distribution"

i2c_slave_port = '/dev/ttyACM0'
baud_rate = 9600

def start_simulation(board_to_simulate):
    # Initialize board that was requested
    board = valid_boards[board_to_simulate]
    board = ...

    # Wait for message over Serial
    ser = serial.Serial(i2c_slave_port, baud_rate)

    # TODO: If board has I2C peripheral enabled, then "program" the slave with the I2C address of the peripheral so that it accepts messages

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()

            # TODO: Use Protobuf to encode/decode these Serial messages to handle things like message types, addressing, etc (for Total Phase Aardvark)

            # If I2C message, we only handle write commands
            message_type = ...
            message = ...
            if message_type == "I2C" or message_type == "SPI":
                # Update peripheral state, retrieve new state of peripheral, and send back to slave
                response = board.handle_message(message, message_type)

                ser.write(response.encode())
            else:
                # TODO: Handle analog signals and error messages

if __name__ == "__main__":
    # Retrieve board to simulate from command line arguments
    board_to_simulate = default_board

    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        argument = " ".join(arguments)
        
        if argument in valid_boards.keys():
            board_to_simulate = argument

    start_simulation(board_to_simulate)