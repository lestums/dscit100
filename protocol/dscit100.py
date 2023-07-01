#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# SPDX-License-Identifier: GPL-2.0

import itertools
from enum import Enum

class IT100PacketInvalid(Exception):
    """
    Indicates that the packet is invalid
    """

    pass

class IT100PacketInvalidChecksum(Exception):
    """
    Indicates that the checksum of a packet received from IT100 is invalid
    """

    pass

class StrEnum(str, Enum):
    """
    Provides a simple enum to string interface
    """

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return ".".join([self.__class__, self.name])

class IT100CmdID(StrEnum):
    """
    Lists identifiers that are used for sending requests to IT100
    """

    POLL = '000'
    STATUS_REQ = '001'
    LABELS_REQ = '002'
    SET_TIME_AND_DATE = '010'
    COMMAND_OUTPUT_CTRL = '020'
    PART_ARM_CTRL_AWAY = '030'
    PART_ARM_CTRL_STAY = '031'
    PART_ARM_CTRL_ARMED_NO_DELAY = '032'
    PART_ARM_CTRL_WITH_USERCODE = '033'
    PART_DISARM_CTRL_WITH_USERCODE = '040'
    TIMESTAMP_CTRL = '055'
    TIMEDATA_BROADCAST_CTRL = '056'
    TEMP_BROADCAST_CTRL = '057'
    VKEYPAD_CTRL = '058'
    TRIGGER_PANIC_ALARM = '060'
    VKEYPAD_KEY_PRESSED = '070'
    IT100_BAUDRATE_CHANGE = '080'
    ESCORT5580_GET_TEMP_SETPOINT = '095'
    ESCORT5580_CHANGE_TEMP = '096'
    ESCORT5580_SAVE_TEMP_SETTING = '097'
    CODE_SEND = '200'

class IT100ReplyID(StrEnum):
    """
    Lists identifiers that are used by IT100 for replies and event-driven notifications
    """

    ACK = '500'
    ERROR = '501'
    SYSTEM_ERROR = '502'
    TIMEDATE_BROADCAST = '550'
    ESCORT5580_RING_DETECTED = '560'
    INDOOR_TEMP_BROADCAST = '561'
    OUTDOOR_TEMP_BROADCAST = '562'
    THERMOSTAT_SETPOINTS = '563'
    LABELS_BROADCAST = '570'
    IT100_BAUDRATE_SET = '580'
    ZONE_ALARM = '601'
    ZONE_ALARM_RESTORE = '602'
    ZONE_TAMPER = '603'
    ZONE_TAMPER_RESTORE = '604'
    ZONE_FAULT = '605'
    ZONE_FAULT_RESTORE = '606'
    ZONE_OPEN = '609'
    ZONE_RESTORED = '610'
    DURESS_ALARM = '620'
    FIRE_ALARM_KEY = '621'
    FIRE_ALARM_KEY_RESTORED = '622'
    AUX_ALARM_KEY = '623'
    AUX_ALARM_KEY_RESTORED = '624'
    PANIC_ALARM_KEY = '625'
    PANIC_ALARM_KEY_RESTORED = '626'
    AUX_INPUT_ALARM = '631'
    AUX_INPUT_ALARM_RESTORED = '632'
    # Note here : v1.0 of the specification contains
    # an error on the command ID for PARTITION_READY.
    # Document mentions '626' on page 10, but example
    # provided on page 19 mentions '650'.
    # Stick with personal "real world" experiments,
    # document examples and plain logic.
    PART_READY = '650'
    PART_NOT_READY = '651'
    PART_ARMED_WITH_MODE = '652'
    PART_READY_FORCE_ARM = '653'
    PART_IN_ALARM = '654'
    PART_DISARMED = '655'
    EXIT_DELAY_IN_PROGRESS = '656'
    ENTRY_DELAY_IN_PROGRESS = '657'
    KEYPAD_LOCKOUT = '658'
    KEYPAD_BLANKING = '659'
    OUTPUT_IN_PROGRESS = '660'
    INVALID_ACCESS_CODE = '670'
    FUNCTION_NOT_AVAILABLE = '671'
    FAILED_TO_ARM = '672'
    PART_BUSY = '673'
    USER_CLOSING = '700'
    SPECIAL_CLOSING = '701'
    PARTIAL_CLOSING = '702'
    USER_OPENING = '750'
    SPECIAL_OPENING = '751'
    PANEL_BAT_TROUBLE = '800'
    PANEL_BAT_RESTORED = '801'
    PANEL_AC_TROUBLE = '802'
    PANEL_AC_RESTORED = '803'
    BELL_TROUBLE = '806'
    BELL_RESTORED = '807'
    TLM_LINE1_TROUBLE = '810'
    TLM_LINE1_RESTORED = '811'
    TLM_LINE2_TROUBLE = '812'
    TLM_LINE2_RESTORED = '813'
    FTC_TROUBLE = '814'
    BUFFER_75P_FULL = '816'
    WIRELESS_ZONE_LOW_BAT = '821'
    WIRELESS_ZONE_BAT_RESTORED = '822'
    WIRELESS_KEY_LOW_BAT = '825'
    WIRELESS_KEY_BAT_RESTORED = '826'
    HANDHELD_KEYPAD_LOW_BAT = '827'
    HANDHELD_KEYPAD_BAT_RESTORED = '828'
    GENERAL_SYSTEM_TEMPER = '829'
    GENERAL_SYSTEM_TEMPER_RESTORED = '830'
    ESCORT5580_HA_TROUBLE = '831'
    ESCORT5580_HA_TROUBE_RESTORED = '832'
    TROUBLE_STATUS_LED_ON = '840'
    TROUBLE_STATUS_LED_OFF = '841'
    FIRE_TROUBLE_ALARM = '842'
    CODE_REQUIRED = '900'
    VKEYPAD_LCD_UPDATE = '901'
    VKEYPAD_LCD_CURSOR = '902'
    VKEYPAD_LED_STATUS = '903'
    BEEP_STATUS = '904'
    TONE_STATUS = '905'
    BUZZER_STATUS = '906'
    DOOR_CHIME_STATUS = '907'
    SOFTWARE_VERSION = '908'

class IT100SysErrReason(StrEnum):
    """
    Lists error reasons issued along a SYSTEM_ERROR emitted by IT100
    """

    KEYBUS_BUSY = '017'
    PART_OUT_OF_RANGE = '021'
    PART_NOT_ARMED = '023'
    PART_NOT_READY = '024'
    USERCODE_NOT_REQUIRED = '026'
    VKEYPAD_DISABLED = '028'
    INVALID_PARAMETER = '029'
    VKEYPAD_NOT_OUT_OF_BLANK_MODE = '030'
    IT100_ALREADY_IN_THERMOSTAT_MENU = '031'
    IT100_NOT_IN_THERMOSTAT_MENU = '032'
    NO_FROM_THERMOSTAT_OR_ESCORT = '033'

class IT100SerialBaud(StrEnum):
    """
    Lists baudrates supported by IT100
    """

    RATE_9600 = "0"
    RATE_19200 = "1"
    RATE_38400 = "2"
    RATE_57600 = "3"
    RATE_115200 = "4"

class IT100VKeypadLCDLine(StrEnum):
    """
    Lists line identifier for the IT100 Virtual Keypad function
    """

    LINE1 = "0"
    LINE2 = "1"

class IT100VKeypadLCDColumn(StrEnum):
    """
    Lists column identifier for the IT100 Virtual Keypad function
    """

    COLUMN1 = "00"
    COLUMN2 = "01"
    COLUMN3 = "02"
    COLUMN4 = "03"
    COLUMN5 = "04"
    COLUMN6 = "05"
    COLUMN7 = "06"
    COLUMN8 = "07"
    COLUMN9 = "08"
    COLUMN10 = "09"
    COLUMN11 = "10"
    COLUMN12 = "11"
    COLUMN13 = "12"
    COLUMN14 = "13"
    COLUMN15 = "14"
    COLUMN16 = "16"

class IT100VKeypadLEDStatus(StrEnum):
    """
    Lists LEDs status available for the IT100 Virtual Keypad function
    """

    OFF = "0"
    ON = "1"
    FLASHING = "2"

class IT100VKeypadLED(StrEnum):
    """
    Lists LED indicators that are supported by the IT100 Virtual Keypad function
    """

    READY = "1"
    ARMED = "2"
    MEMORY = "3"
    BYPASS = "4"
    TROUBLE = "5"
    PROGRAM = "6"
    FIRE = "7"
    BACKLIGHT = "8"
    AC = "9"

class IT100VKeypadLCDCursor(StrEnum):
    """
    List LCD cursor state on the IT100 Virtual Keypad function
    """

    OFF = "0"
    UNDERSCORE = "1"
    BLOCK = "2"

class IT100PartitionArmedModeDesc(StrEnum):
    """
    List descriptions returned by IT100 after a PART_ARMED_WITH_MODE command
    has been issued
    """

    AWAY = "0"
    STAY = "1"
    AWAY_NO_DELAY = "2"
    STAY_NO_DELAY = "3"

class IT100LabelsBroadcastID(StrEnum):
    """
    List label identifiers returned by IT100 after a LABELS_BROADCAST command
    has been issued
    """

    ZONE1 = "001"
    ZONE2 = "002"
    ZONE3 = "003"
    ZONE4 = "004"
    ZONE5 = "005"
    ZONE5 = "006"
    ZONE6 = "007"
    ZONE7 = "008"
    ZONE8 = "009"
    ZONE9 = "010"
    ZONE10 = "010"
    ZONE11 = "011"
    ZONE12 = "012"
    ZONE13 = "013"
    ZONE14 = "014"
    ZONE15 = "015"
    ZONE16 = "016"
    ZONE17 = "017"
    ZONE18 = "018"
    ZONE19 = "019"
    ZONE20 = "020"
    ZONE21 = "021"
    ZONE22 = "022"
    ZONE23 = "023"
    ZONE24 = "024"
    ZONE25 = "025"
    ZONE26 = "026"
    ZONE27 = "027"
    ZONE28 = "028"
    ZONE29 = "029"
    ZONE30 = "030"
    ZONE31 = "031"
    ZONE32 = "032"
    ZONE33 = "033"
    ZONE34 = "034"
    ZONE35 = "035"
    ZONE36 = "036"
    ZONE37 = "037"
    ZONE38 = "038"
    ZONE39 = "039"
    ZONE40 = "040"
    ZONE41 = "041"
    ZONE42 = "042"
    ZONE43 = "043"
    ZONE44 = "044"
    ZONE45 = "045"
    ZONE46 = "046"
    ZONE47 = "047"
    ZONE48 = "048"
    ZONE49 = "049"
    ZONE50 = "050"
    ZONE51 = "051"
    ZONE52 = "052"
    ZONE53 = "053"
    ZONE54 = "054"
    ZONE55 = "055"
    ZONE56 = "056"
    ZONE57 = "057"
    ZONE58 = "058"
    ZONE59 = "059"
    ZONE60 = "060"
    ZONE61 = "061"
    ZONE62 = "062"
    ZONE63 = "063"
    ZONE64 = "064"
    FIRE_ALARM = "065"
    FAILED_ARM = "066"
    ALARM_ARMED = "067"
    PARTITION1 = "101"
    PARTITION2 = "102"
    PARTITION3 = "103"
    PARTITION4 = "104"
    PARTITION5 = "105"
    PARTITION6 = "106"
    PARTITION7 = "107"
    PARTITION8 = "108"
    CMDOUTPUT1 = "120"
    CMDOUTPUT2 = "121"
    CMDOUTPUT3 = "122"
    CMDOUTPUT4 = "123"
    CMDOUTPUT5 = "124"
    CMDOUTPUT5 = "125"
    CMDOUTPUT6 = "126"
    CMDOUTPUT7 = "127"
    CMDOUTPUT8 = "128"
    CMDOUTPUT9 = "129"
    CMDOUTPUT10 = "130"
    CMDOUTPUT11 = "131"
    CMDOUTPUT12 = "132"
    CMDOUTPUT13 = "133"
    CMDOUTPUT14 = "134"
    CMDOUTPUT15 = "135"
    CMDOUTPUT16 = "136"
    CMDOUTPUT17 = "137"
    CMDOUTPUT18 = "138"
    CMDOUTPUT19 = "139"
    CMDOUTPUT20 = "140"
    CMDOUTPUT21 = "141"
    CMDOUTPUT22 = "142"
    CMDOUTPUT23 = "143"
    CMDOUTPUT24 = "144"
    CMDOUTPUT25 = "145"
    CMDOUTPUT26 = "146"
    CMDOUTPUT27 = "147"
    CMDOUTPUT28 = "148"
    CMDOUTPUT29 = "149"
    CMDOUTPUT30 = "150"
    CMDOUTPUT31 = "151"

class IT100RawPacket:
    """
    Represents a raw packet that is sent to / received from a DSC IT-100 module.
    
    It implements the specification provided in DSC IT-100 Data Interface module v1.0
    developer's guide
    
    WARNING: No additional check is performed outside of checksum computation and
    basic minimal length check on decoding.
    Consequently, there is no guarantee that either the data nor the command exists
    and there's no additional verification on the reply / notifications received 
    from the module (data sanity, coherence, expected replies, etc...).
    """

    def __init__(self, command, data):
        self.cmd = command
        self.data = data
        self.checksum = self.compute_checksum()

    def encode(self):
        """
        See DSC IT-100 Data Interface Module v1.0 Developer's guide, p3
        """

        return ''.join([self.cmd, self.data, self.checksum, '\r\n']).encode('ascii')

    def compute_checksum(self):
        """
        See DSC IT-100 Data Interface Module v1.0 Developer's guide, p3, "CKS" field
        """

        return '{0:02X}'.format(sum(ord(char) for char in itertools.chain(self.cmd, self.data)) % 256)

    @classmethod
    def decode(cls, raw):
        """
        See DSC IT-100 Data Interface Module v1.0 Developer's guide, p3
        """

        # Shortest packets consist in CMD + CKS + EOP (like POLL),
        # so we expect at least 7 bytes in a valid packet.
        if len(raw) < 7:
            raise IT100PacketInvalid("Invalid packet")

        command = raw[0:3]
        data = raw[3:-4]
        checksum = raw[-4:-2]

        pktobj = cls(command, data)

        if pktobj.checksum != checksum:
            raise IT100PacketInvalidChecksum(f"Checksum error: expected {checksum}; got {pktobj.checksum}")

        return pktobj
