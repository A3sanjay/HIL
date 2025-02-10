#!/usr/bin/env python3

# PCA9555 Register Map
INPUT_PORT_0 = 0x00
INPUT_PORT_1 = 0x01
OUTPUT_PORT_0 = 0x02
OUTPUT_PORT_1 = 0x03
POLARITY_INVERSION_0 = 0x04
POLARITY_INVERSION_1 = 0x05
CONFIGURATION_0 = 0x06
CONFIGURATION_1 = 0x07

class PCA9555:
    def __init__(self):
        # Registers initialized to default values
        self.registers = {
            INPUT_PORT_0: 0x00,  # Input values (simulate external state)
            INPUT_PORT_1: 0x00,
            OUTPUT_PORT_0: 0x00,  # Output register (what the user writes)
            OUTPUT_PORT_1: 0x00,
            POLARITY_INVERSION_0: 0x00,  # No polarity inversion by default
            POLARITY_INVERSION_1: 0x00,
            CONFIGURATION_0: 0xFF,  # All pins default to inputs
            CONFIGURATION_1: 0xFF,
        }

    def write_register(self, register, value):
        """Handles writes to the PCA9555 registers."""
        if register in (OUTPUT_PORT_0, OUTPUT_PORT_1):
            # Ensure we're only modifying pins set as outputs
            config_reg = CONFIGURATION_0 if register == OUTPUT_PORT_0 else CONFIGURATION_1
            output_mask = ~self.registers[config_reg]  # Mask to allow only outputs to change
            self.registers[register] = (self.registers[register] & ~output_mask) | (value & output_mask)
        else:
            self.registers[register] = value
    
    def read_register(self, register):
        """Handles reads from the PCA9555 registers."""
        if register in self.registers:
            value = self.registers[register]
            print(f"[READ] Register 0x{register:02X} -> 0x{value:02X}")
            return value
        print(f"[ERROR] Invalid register read: 0x{register:02X}")
        return 0x00

    def read_all_registers(self):
        """Reads all the registers at once"""
        registers = self.registers.copy()

        return registers