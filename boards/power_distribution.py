#!/usr/bin/env python3

# Simulate the functionality of the Power Distribution board
# Peripherals to simulate include: 1 x I2C peripheral (GPIO Expander) and ...

import peripherals.pca9555 as pca9555

import serial

# PCA9555 I2C Address (change based on your setup)
PCA9555_I2C_ADDRESS = pca9555.PCA9555_ADDRESS


# Create a peripherals master class with these classes overloading the original functions
class PowerDistribution:
    # Initialize the state of the periperals on this board
    def __init__(self):
        # TODO: Add initialization for peripherals on board
        self.pca_9555 = pca9555.PCA9555()
        
        # TODO: Start up DAC with pre-programmed analog signals
        # pedal_dac = dac.DAC()
        # pedal_dac.start(dac.PEDAL)
        
        # steering_dac = dac.DAC()
        # steering_dac.start(dac.STEERING)

    def get_i2c_address():
        return PCA9555_I2C_ADDRESS

    def handle_message(self, message, message_type):
        if message_type == "I2C":
            # TODO: Decide what the encoding looks like and parse accordingly to retrieve message components
            i2c_message = message

            # PCA9555 is being addressed
            # Message will be a write (reads are handled by the slave directly)
            pca9555_command = ...
            pca9555_data = ...
            if (pca9555_command == pca9555.INPUT_PORT_0) or (pca9555_command == pca9555.OUTPUT_PORT_0) or (pca9555_command == pca9555.POLARITY_INVERSION_0) or (pca9555_command == pca9555.CONFIGURATION_0):
                # Valid command byte

                # Write to the pair of registers
                pca9555_first_data_byte = ...
                pca9555_second_data_byte = ...
                self.pca_9555.write_register(pca9555_command, pca9555_first_data_byte)
                self.pca_9555.write_register(pca9555_command + 1, pca9555_second_data_byte)

                # Read the updated registers to send back 
                response = self.pca_9555.read_all_registers()

                return response
            else:
                # TODO: Handle error case (return error message)


        # TODO: Handle other messages