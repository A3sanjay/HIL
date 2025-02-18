#!/usr/bin/env python3

# Simulate the functionality of the BMS board
# Peripherals to simulate include: 1 x I2C peripheral (MAX17261) and ...

import peripherals.max17621 as max17261

import serial

# MAX17261 I2C Address (change based on your setup)
MAX_I2C_ADDRESS = max17261.MAX17261_ADDRESS

# Create a peripherals master class with these classes overloading the original functions
class BMS:
    # Initialize the state of the periperals on this board
    def __init__(self):
        # TODO: Add initialization for peripherals on board
        self.max_17261 = max17261.MAX17261()
        
        # TODO: Start up DAC with pre-programmed analog signals
        # pedal_dac = dac.DAC()
        # pedal_dac.start(dac.PEDAL)
        
        # steering_dac = dac.DAC()
        # steering_dac.start(dac.STEERING)

    def get_i2c_address():
        return MAX_I2C_ADDRESS

    def handle_message(self, message, message_type):
        if message_type == "I2C":
            # TODO: Decide what the encoding looks like and parse accordingly to retrieve message components
            i2c_message = message

            # max17261 is being addressed
            # Message will be a write (reads are handled by the slave directly)
            max17261_command = ...
            max17261_data = ...
            # if (max17261_command == max17261.INPUT_PORT_0) or (max17261_command == max17261.OUTPUT_PORT_0) or (max17261_command == max17261.POLARITY_INVERSION_0) or (max17261_command == max17261.CONFIGURATION_0):
            #     # Valid command byte

            #     # Write to the pair of registers
            #     max17261_first_data_byte = ...
            #     max17261_second_data_byte = ...
            #     self.max_17261.write_register(max17261_command, max17261_first_data_byte)
            #     self.max_17261.write_register(max17261_command + 1, max17261_second_data_byte)

            #     # Read the updated registers to send back 
            #     response = self.max17261.read_all_registers()

            #     return response
            # else:
            #     # TODO: Handle error case (return error message)


        # TODO: Handle SPI messages