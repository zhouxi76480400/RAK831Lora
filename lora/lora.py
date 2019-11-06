import serial
import lora.rak811 as rak811


class LoRa:
    port = ''
    baudrate = 115200
    bytesize = serial.EIGHTBITS
    stopbits = serial.STOPBITS_ONE
    parity = serial.PARITY_NONE
    xonxoff = False

    ser = None

    def __init__(self):
        print("LoRa __init__")

    def connect(self):
        if self.ser is None:
            self.ser = serial.Serial()
        self.disconnect()
        self.ser = serial.Serial()
        self.ser.port = self.port
        self.ser.baudrate = self.baudrate
        self.ser.bytesize = self.bytesize
        self.ser.stopbits = self.stopbits
        self.ser.parity = self.parity
        self.ser.xonxoff = self.xonxoff
        self.ser.timeout = 2
        print("LoRa connect")
        print(self.ser.port)
        self.ser.open()
        if self.ser.is_open is True:
            print("set module")
            rak811.init_rak811(self.ser)

    def send_message(self, byte_array):
        send_message_byte_array_count = len(byte_array)
        send_message_byte_check = len(byte_array) % 2 is 0
        if send_message_byte_array_count > 0 and send_message_byte_check is True:
            rak811.rak811_send_msg(self.ser, byte_array)
        else:
            raise Exception

    def get_signal(self):
        rak811.rak811_signal(self.ser)

    def disconnect(self):
        if self.ser is not None:
            if self.ser.is_open is True:
                self.ser.close()

