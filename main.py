import serial
import lora.lora as l

lo = l.LoRa()

lo.port = '/dev/tty.usbserial-14140'
lo.baudrate = 115200
lo.bytesize = serial.EIGHTBITS
lo.stopbits = serial.STOPBITS_ONE
lo.parity = serial.PARITY_NONE
lo.xonxoff = False

# connect
lo.connect()

# send message without gateway wait
lo.send_message(b'AABBCCDDEEFFAAAABBCCDD')

lo.get_signal()

# disconnect
lo.disconnect()
