#!/usr/bin/env python3

# Simulate the functionality of the Centre Console board
# Peripherals to simulate include: 1 x I2C peripheral (GPIO Expander) and 2 x analog signal (DAC)

import peripherals.pca9555 as pca9555

import serial

# PCA9555 I2C Address (change based on your setup)
PCA9555_I2C_ADDRESS = 0x20

class CenterConsole:
    # Initialize the state of the periperals on this board
    def init():
        # TODO: Add initialization for peripherals on board
        pca_9555 = pca9555.PCA9555()

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


        # TODO: Handle other message types (SPI/analog)