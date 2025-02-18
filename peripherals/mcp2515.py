#!/usr/bin/env python3

import helpers.mcp2515_defs

# MCP2515 SPI Registers (Partial List)
CANCTRL = 0x0F  # Control register
CANSTAT = 0x0E  # Status register
CNF1 = 0x2A  # Baud rate config 1
CNF2 = 0x29  # Baud rate config 2
CNF3 = 0x28  # Baud rate config 3
TXB0CTRL = 0x30  # Transmit Buffer 0 Control
RXB0CTRL = 0x60  # Receive Buffer 0 Control
RXF0SIDH = 0x00  # RX Filter 0 High Byte
RXB0SIDH = 0x61  # Receive Buffer 0 High Byte
RXB0D0 = 0x66  # Receive Buffer Data Byte 0
RXB0DLC = 0x65  # Receive Data Length Code

class MCP2515:
    def __init__(self):
        """Simulates the MCP2515 CAN Controller."""
        self.registers = {
            CANCTRL: 0x00,  # Default control state
            CANSTAT: 0x80,  # Reset Mode
            CNF1: 0x00,  # Baud rate not set
            CNF2: 0x00,
            CNF3: 0x00,
            TXB0CTRL: 0x00,  # TX buffer empty
            RXB0CTRL: 0x00,  # RX buffer empty
            RXB0SIDH: 0x00,  # Received message ID
            RXB0DLC: 0x00,  # Received message data length
            RXB0D0: [0x00] * 8,  # CAN message data (max 8 bytes)
        }
        self.tx_queue = []  # Simulated transmission queue
        self.rx_queue = []  # Simulated reception queue

    def write_register(self, register, value):
        """Handles writes to the MCP2515 registers."""
        if register in self.registers:
            self.registers[register] = value
            print(f"[WRITE] Register 0x{register:02X} <- 0x{value:02X}")

            # Handle Special Cases
            if register == CANCTRL:
                self.handle_mode_change(value)
        else:
            print(f"[ERROR] Invalid register write: 0x{register:02X}")

    def read_register(self, register):
        """Handles reads from the MCP2515 registers."""
        if register in self.registers:
            value = self.registers[register]
            print(f"[READ] Register 0x{register:02X} -> 0x{value:02X}")
            return value
        print(f"[ERROR] Invalid register read: 0x{register:02X}")
        return 0x00

    def handle_mode_change(self, value):
        """Handles CAN mode changes based on the CANCTRL register."""
        mode = value & 0xE0
        mode_str = {
            0x00: "Normal Mode",
            0x40: "Sleep Mode",
            0x60: "Loopback Mode",
            0x80: "Listen-Only Mode",
            0xE0: "Configuration Mode",
        }.get(mode, "Unknown Mode")

        print(f"🔄 MCP2515 Mode Change: {mode_str}")
        self.registers[CANSTAT] = mode  # Update status register

    def send_can_message(self, can_id, data):
        """Simulate sending a CAN message."""
        if len(data) > 8:
            print("❌ Error: CAN message cannot exceed 8 bytes!")
            return

        self.tx_queue.append((can_id, data))
        print(f"📡 Sent CAN Message: ID=0x{can_id:03X}, Data={data}")

        # Simulate the MCP2515 moving the message into TX buffer
        self.registers[TXB0CTRL] |= 0x08  # Mark TX buffer as full

    def receive_can_message(self):
        """Simulate receiving a CAN message."""
        if not self.rx_queue:
            return None

        can_id, data = self.rx_queue.pop(0)
        self.registers[RXB0SIDH] = (can_id >> 3) & 0xFF  # Store ID
        self.registers[RXB0DLC] = len(data)  # Store DLC
        self.registers[RXB0D0] = data  # Store data bytes
        self.registers[RXB0CTRL] |= 0x01  # Mark RX buffer as full

        print(f"📥 Received CAN Message: ID=0x{can_id:03X}, Data={data}")

        return can_id, data
