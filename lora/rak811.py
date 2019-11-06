import serial

rak811_dev_addr = b'260412DB'
rak811_dev_nwks_key = b'ACB024E988E7F0C28C76D83772A4EB3D'
rak811_dev_apps_key = b'A069E1D1B42A1C4EB6C8554AA4863B73'
rak811_dev_tx_power = b'14'
rak811_message_port = b'1'
rak811_dev_eui = b'3530353065375C14'

rak811_mode_abp = b'abp'

rak811_command_and = b'&'

rak811_command_start_code = b'at+'
rak811_command_cr = b'\r'
rak811_command_lf = b'\n'

rak811_command_restart = b'reset=0'
rak811_command_restart_resp_code = b'Welcome to RAK811'

rak811_command_set_mode_lora_wan = b'mode=0'
rak811_command_set_mode_lora_wan_resp_code = b'OK'

rak811_command_set_config = b'set_config='
rak811_command_dev_addr = b'dev_addr:'
rak811_command_dev_nwks_key = b'nwks_key:'
rak811_command_dev_apps_key = b'apps_key:'
rak811_command_dev_tx_power = b'tx_power:'
rak811_command_dev_eui = b'dev_eui:'
rak811_command_dev_join = b'join='

rak811_message_type_unconfirmed = b'0'
rak811_message_type_confirmed = b'1'

rak811_command_send = b'send='
rak811_command_send_skip = b','

rak811_command_signal = b'signal'


def rak811_send_msg(serial, msg_data):
    rak811_send_msg_tmp0 = rak811_command_start_code + rak811_command_send + rak811_message_type_unconfirmed + rak811_command_send_skip\
                           + rak811_message_port + rak811_command_send_skip + msg_data + rak811_command_cr + rak811_command_lf
    console_print(rak811_send_msg_tmp0)
    serial.write(rak811_send_msg_tmp0)
    rak811_wait(serial, b'at+recv=2,0,0\r\n')


def init_rak811(serial):
    if serial is not None:
        # restart
        rak811_restart(serial)
        # set mode
        rak811_set_mode(serial)
        # set config
        rak811_set_config(serial)
        # join
        rak811_join(serial)


def rak811_set_config(serial):
    if serial is not None:
        rak811_set_config_tmp0 = rak811_command_start_code + \
                                 rak811_command_set_config + rak811_command_dev_addr + rak811_dev_addr + \
                                 rak811_command_and + rak811_command_dev_nwks_key + rak811_dev_nwks_key + \
                                 rak811_command_and + rak811_command_dev_apps_key + rak811_dev_apps_key + \
                                 rak811_command_and + rak811_command_dev_tx_power + rak811_dev_tx_power + \
                                 rak811_command_and + rak811_command_dev_eui + rak811_dev_eui + \
                                 rak811_command_cr + rak811_command_lf
        console_print(rak811_set_config_tmp0)
        serial.write(rak811_set_config_tmp0)
        rak811_wait(serial, rak811_command_set_mode_lora_wan_resp_code + rak811_command_cr + rak811_command_lf)


def rak811_restart(serial):
    if serial is not None:
        rak811_restart_tmp0 = rak811_command_start_code + rak811_command_restart + rak811_command_cr + rak811_command_lf
        console_print(rak811_restart_tmp0)
        serial.write(rak811_restart_tmp0)
        rak811_wait(serial, rak811_command_restart_resp_code + rak811_command_cr + rak811_command_lf)


def rak811_set_mode(serial):
    if serial is not None:
        rak_811_set_mode_tmp0 = rak811_command_start_code + rak811_command_set_mode_lora_wan + rak811_command_cr + \
                                rak811_command_lf
        console_print(rak_811_set_mode_tmp0)
        serial.write(rak_811_set_mode_tmp0)
        rak811_wait(serial, rak811_command_set_mode_lora_wan_resp_code + rak811_command_cr + rak811_command_lf)


def rak811_join(serial):
    if serial is not None:
        rak811_join_tmp0 = rak811_command_start_code + rak811_command_dev_join + rak811_mode_abp + rak811_command_cr + \
                           rak811_command_lf
        console_print(rak811_join_tmp0)
        serial.write(rak811_join_tmp0)
        rak811_wait(serial, rak811_command_set_mode_lora_wan_resp_code + rak811_command_cr + rak811_command_lf)


def rak811_signal(serial):
    if serial is not None:
        rak811_signal_tmp0 = rak811_command_start_code + rak811_command_signal +rak811_command_cr + rak811_command_lf
        console_print(rak811_signal_tmp0)
        serial.write(rak811_signal_tmp0)
        rak811_wait(serial, b'OK')


def rak811_wait(serial, wait_string):
    rak811_wait_enabled = True
    while rak811_wait_enabled:
        rak811_read_line = serial.readline()
        print(rak811_read_line)
        if wait_string in rak811_read_line:
            return


def console_print(string):
    print("input:"+str(string))
