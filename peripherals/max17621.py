#!/usr/bin/env python3

import helpers.max17261_defs as MAX17261_DEFS

# MAX17261 I2C Address
MAX17261_ADDRESS = 0x36

class MAX17261:
    def __init__(self):
        """Simulates the MAX17261 battery monitoring IC."""
        # TODO: Simulate the initialization procedure
        # TODO: Vary the current and voltage outputted and if they exceed the set thresholds, then send an alert
        # A lot of these registers won't be used as we are not simulating anything other than current and voltage sense (and maybe temp sense)
        self.registers_to_read = {
            MAX17261_DEFS.VCELL: 0x1F40,  # Simulated voltage = 8000 mV
            MAX17261_DEFS.CURR: 0x03E8,  # Simulated current = 1000 mA
            MAX17261_DEFS.TEMP: 0x0FA0,  # Simulated temperature = 25°C
            MAX17261_DEFS.F_STAT: 0x00000, # No faults
            MAX17261_DEFS.SOC: 0x0000,
            MAX17261_DEFS.CAP: 0x0000,
            MAX17261_DEFS.FULL_CAP_REP: 0x0000,
            MAX17261_DEFS.TIME_TO_EMPTY: 0x0000,
            MAX17261_DEFS.TIME_TO_FULL: 0x0000,
        }
        self.registers_to_read_and_write = {
            MAX17261_DEFS.STATUS: 0x0000, # Initialized
            MAX17261_DEFS.CONFIG: 0x0000,  # Default config settings
            MAX17261_DEFS.I_ALRT_THRSH: 0x07D0,  # Alert if current > 2000 mA
            MAX17261_DEFS.DESIGN_CAP: 0x1F40,  # Design capacity = 8000 mAh
            MAX17261_DEFS.COMMAND: 0x0000, # No active command
            MAX17261_DEFS.RCOMP0: 0x0000,
            MAX17261_DEFS.RTEMP_CO: 0x0000,
            MAX17261_DEFS.CYCLES: 0x0000,
            MAX17261_DEFS.FULL_CAP_NOM: 0x0000,
            MAX17261_DEFS.HIB_CFG: 0x0000,
            MAX17261_DEFS.SOFT_WAKEUP: 0x0000,
            MAX17261_DEFS.I_CHG_TERM: 0x0000,
            MAX17261_DEFS.V_EMPTY: 0x0000,
            MAX17261_DEFS.SOC_HOLD: 0x0000,
            MAX17261_DEFS.MODEL_I_CFG: 0x0000,
            MAX17261_DEFS.I_ALRT_THRSH: 0x0000,
            MAX17261_DEFS.TEMP_ALRT_THRSH: 0x0000,
            MAX17261_DEFS.VOLT_ALRT_THRSH: 0x0000,
            MAX17261_DEFS.SOC_ALRT_THRSH: 0x0000,
        }
        self.soc = 100  # Start at 100% SoC

    def write_register(self, register, value):
        """Handles writes to the MAX17261 registers."""
        if register in self.registers_to_read_and_write:
            self.registers_to_read_and_write[register] = value

            # Handle special commands
            if register == MAX17261_DEFS.COMMAND:
                if value == 0x4000:
                    self.quick_start()
                elif value == 0x0000:
                    self.reset_device()

    def read_register(self, register):
        """Handles reads from the MAX17261 registers."""
        if register in self.registers_to_read:
            value = self.registers_to_read[register]
            return value
        
        return 0x0000

    def quick_start(self):
        """Handles QuickStart command (0x4000 to register 0x06)."""
        self.registers[MAX17261_DEFS.VCELL] = 0x1F40  # Reset voltage
        self.registers[MAX17261_DEFS.CURR] = 0x03E8  # Reset current
        self.registers[MAX17261_DEFS.TEMP] = 0x0FA0  # Reset temperature

    def reset_device(self):
        """Handles reset (0x0000 written to register 0x06)."""
        self.__init__()  # Reinitialize registers

