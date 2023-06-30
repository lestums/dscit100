#!/usr/bin/env python3

# Packet format

## Bytes as ASCII Hex.
## CMD + DATA + CRC + EOP

## CMD : Command : 3 bytes
## DATA : N bytes (related to CMD)
## CRC : (CMD + DATA) mod 256
## EOP : CR + LF => 0x0D0A

COMMAND_POLL = "000"
COMMAND_STATUS_REQ = "001"
COMMAND_LABELS_REQ = "002"
COMMAND_SET_TIME_AND_DATE = "010"
COMMAND_COMMAND_OUTPUT_CTRL = "020"
COMMAND_PART_ARM_CTRL_AWAY = "030"
COMMAND_PART_ARM_CTRL_STAY = "031"
COMMAND_PART_ARM_CTRL_ARMED_NO_DELAY = "032"
COMMAND_PART_ARM_CTRL_WITH_USERCODE = "033"
COMMAND_PART_DISARM_CTRL_WITH_USERCODE = "040"
COMMAND_TIMESTAMP_CTRL = "055"
COMMAND_TIMEDATA_BROADCAST_CTRL = "056"
COMMAND_TEMP_BROADCAST_CTRL = "057"
COMMAND_VKEYPAD_CTRL = "058"
COMMAND_TRIGGER_PANIC_ALARM = "060"
COMMAND_VKEYPAD_KEY_PRESSED = "070"
COMMAND_IT100_BAUDRATE_CHANGE = "080"
COMMAND_ESCORT_GET_TEMP_SETPOINT = "095"
COMMAND_ESCORT_CHANGE_TEMP = "096"
COMMAND_ESCORT_SAVE_TEMP_SETTING = "097"
COMMAND_CODE_SEND = "200"


REPLY_COMMAND_ACK = "500"
REPLY_COMMAND_ERROR = "501"
REPLY_SYSTEM_ERROR = "502"
  SYSTEM_ERROR_KEYBUS_BUSY = "017"
  SYSTEM_ERROR_PART_OUT_OF_RANGE = "021"
  SYSTEM_ERROR_PART_NOT_ARMED = "023"
  SYSTEM_ERROR_PART_NOT_READY = "024"
  SYSTEM_ERROR_USERCODE_NOT_REQUIRED = "026"
  SYSTEM_ERROR_VKEYPAD_DISABLED = "028"
  SYSTEM_ERROR_INVALID_PARAMETER = "029"
  SYSTEM_ERROR_VKEYPAD_NOT_OUT_OF_BLANK_MODE = "030"
  SYSTEM_ERROR_IT100_ALREADY_IN_THERMOSTAT_MENU = "031"
  SYSTEM_ERROR_IT100_NOT_IN_THERMOSTAT_MENU = "032"
  SYSTEM_ERROR_NO_REPLY_FROM_THERMOSTAT_OR_ESCORT = "033"
REPLY_TIMEDATE_BROADCAST = "550"
REPLY_ESCORT_RING_DETECTED = "560"
REPLY_INDOOR_TEMP_BROADCAST = "561"
REPLY_OUTDOOR_TEMP_BROADCAST = "562"
REPLY_THERMOSTAT_SETPOINTS = "563"
REPLY_LABELS_BROADCAST = "570"
  # Labels are space padded up to 32 bytes
  LABELS_BROADCAST_ZONE1 = "001"
  LABELS_BROADCAST_ZONE2 = "002" 
  LABELS_BROADCAST_ZONE3 = "003"
  LABELS_BROADCAST_ZONE4 = "004"
  LABELS_BROADCAST_ZONE5 = "005"
  LABELS_BROADCAST_ZONE5 = "006"
  LABELS_BROADCAST_ZONE6 = "007"
  LABELS_BROADCAST_ZONE7 = "008"
  LABELS_BROADCAST_ZONE8 = "009"
  LABELS_BROADCAST_ZONE9 = "010"
  LABELS_BROADCAST_ZONE10 = "010"
  LABELS_BROADCAST_ZONE11 = "011"
  LABELS_BROADCAST_ZONE12 = "012"
  LABELS_BROADCAST_ZONE13 = "013" 
  LABELS_BROADCAST_ZONE14 = "014" 
  LABELS_BROADCAST_ZONE15 = "015" 
  LABELS_BROADCAST_ZONE16 = "016" 
  LABELS_BROADCAST_ZONE17 = "017" 
  LABELS_BROADCAST_ZONE18 = "018" 
  LABELS_BROADCAST_ZONE19 = "019" 
  LABELS_BROADCAST_ZONE20 = "020" 
  LABELS_BROADCAST_ZONE21 = "021" 
  LABELS_BROADCAST_ZONE22 = "022" 
  LABELS_BROADCAST_ZONE23 = "023" 
  LABELS_BROADCAST_ZONE24 = "024" 
  LABELS_BROADCAST_ZONE25 = "025" 
  LABELS_BROADCAST_ZONE26 = "026" 
  LABELS_BROADCAST_ZONE27 = "027" 
  LABELS_BROADCAST_ZONE28 = "028" 
  LABELS_BROADCAST_ZONE29 = "029" 
  LABELS_BROADCAST_ZONE30 = "030" 
  LABELS_BROADCAST_ZONE31 = "031" 
  LABELS_BROADCAST_ZONE32 = "032" 
  LABELS_BROADCAST_ZONE33 = "033" 
  LABELS_BROADCAST_ZONE34 = "034" 
  LABELS_BROADCAST_ZONE35 = "035" 
  LABELS_BROADCAST_ZONE36 = "036" 
  LABELS_BROADCAST_ZONE37 = "037" 
  LABELS_BROADCAST_ZONE38 = "038" 
  LABELS_BROADCAST_ZONE39 = "039" 
  LABELS_BROADCAST_ZONE40 = "040" 
  LABELS_BROADCAST_ZONE41 = "041" 
  LABELS_BROADCAST_ZONE42 = "042" 
  LABELS_BROADCAST_ZONE43 = "043" 
  LABELS_BROADCAST_ZONE44 = "044" 
  LABELS_BROADCAST_ZONE45 = "045" 
  LABELS_BROADCAST_ZONE46 = "046" 
  LABELS_BROADCAST_ZONE47 = "047" 
  LABELS_BROADCAST_ZONE48 = "048" 
  LABELS_BROADCAST_ZONE49 = "049" 
  LABELS_BROADCAST_ZONE50 = "050" 
  LABELS_BROADCAST_ZONE51 = "051" 
  LABELS_BROADCAST_ZONE52 = "052" 
  LABELS_BROADCAST_ZONE53 = "053" 
  LABELS_BROADCAST_ZONE54 = "054" 
  LABELS_BROADCAST_ZONE55 = "055" 
  LABELS_BROADCAST_ZONE56 = "056" 
  LABELS_BROADCAST_ZONE57 = "057" 
  LABELS_BROADCAST_ZONE58 = "058" 
  LABELS_BROADCAST_ZONE59 = "059" 
  LABELS_BROADCAST_ZONE60 = "060" 
  LABELS_BROADCAST_ZONE61 = "061" 
  LABELS_BROADCAST_ZONE62 = "062" 
  LABELS_BROADCAST_ZONE63 = "063" 
  LABELS_BROADCAST_ZONE64 = "064" 
  LABELS_BROADCAST_FIRE_ALARM = "065"
  LABELS_BROADCAST_FAILED_ARM = "066"
  LABELS_BROADCAST_ALARM_ARMED = "067"
  LABELS_BROADCAST_PARTITION1 = "101"
  LABELS_BROADCAST_PARTITION2 = "102"
  LABELS_BROADCAST_PARTITION3 = "103"
  LABELS_BROADCAST_PARTITION4 = "104"
  LABELS_BROADCAST_PARTITION5 = "105"
  LABELS_BROADCAST_PARTITION6 = "106"
  LABELS_BROADCAST_PARTITION7 = "107"
  LABELS_BROADCAST_PARTITION8 = "108"
  LABELS_BROADCAST_CMDOUTPUT1 = "120"
  LABELS_BROADCAST_CMDOUTPUT2 = "121" 
  LABELS_BROADCAST_CMDOUTPUT3 = "122"
  LABELS_BROADCAST_CMDOUTPUT4 = "123"
  LABELS_BROADCAST_CMDOUTPUT5 = "124"
  LABELS_BROADCAST_CMDOUTPUT5 = "125"
  LABELS_BROADCAST_CMDOUTPUT6 = "126"
  LABELS_BROADCAST_CMDOUTPUT7 = "127"
  LABELS_BROADCAST_CMDOUTPUT8 = "128"
  LABELS_BROADCAST_CMDOUTPUT9 = "129"
  LABELS_BROADCAST_CMDOUTPUT10 = "130"
  LABELS_BROADCAST_CMDOUTPUT11 = "131"
  LABELS_BROADCAST_CMDOUTPUT12 = "132"
  LABELS_BROADCAST_CMDOUTPUT13 = "133" 
  LABELS_BROADCAST_CMDOUTPUT14 = "134" 
  LABELS_BROADCAST_CMDOUTPUT15 = "135" 
  LABELS_BROADCAST_CMDOUTPUT16 = "136" 
  LABELS_BROADCAST_CMDOUTPUT17 = "137" 
  LABELS_BROADCAST_CMDOUTPUT18 = "138" 
  LABELS_BROADCAST_CMDOUTPUT19 = "139" 
  LABELS_BROADCAST_CMDOUTPUT20 = "140" 
  LABELS_BROADCAST_CMDOUTPUT21 = "141" 
  LABELS_BROADCAST_CMDOUTPUT22 = "142" 
  LABELS_BROADCAST_CMDOUTPUT23 = "143" 
  LABELS_BROADCAST_CMDOUTPUT24 = "144" 
  LABELS_BROADCAST_CMDOUTPUT25 = "145" 
  LABELS_BROADCAST_CMDOUTPUT26 = "146" 
  LABELS_BROADCAST_CMDOUTPUT27 = "147" 
  LABELS_BROADCAST_CMDOUTPUT28 = "148" 
  LABELS_BROADCAST_CMDOUTPUT29 = "149" 
  LABELS_BROADCAST_CMDOUTPUT30 = "150" 
  LABELS_BROADCAST_CMDOUTPUT31 = "151" 
REPLY_IT100_BAUDRATE_SET = "580"
  IT100_BAUDRATE_9600 = "0"
  IT100_BAUDRATE_19200 = "1"
  IT100_BAUDRATE_38400 = "2"
  IT100_BAUDRATE_57600 = "3"
  IT100_BAUDRATE_115200 = "4"
REPLY_ZONE_ALARM = "601"
REPLY_ZONE_ALARM_RESTORE = "602"
REPLY_ZONE_TAMPER = "603"
REPLY_ZONE_TAMPER_RESTORE = "604"
REPLY_ZONE_FAULT = "605"
REPLY_ZONE_FAULT_RESTORE = "606"
REPLY_ZONE_OPEN = "609"
REPLY_ZONE_RESTORED = "610"
REPLY_DURESS_ALARM = "620"
REPLY_FIRE_ALARM_KEY = "621"
REPLY_FIRE_ALARM_KEY_RESTORED = "622"
REPLY_AUX_ALARM_KEY = "623"
REPLY_AUX_ALARM_KEY_RESTORED = "624"
REPLY_PANIC_ALARM_KEY = "625"
REPLY_PANIC_ALARM_KEY_RESTORED = "626"
REPLY_AUX_INPUT_ALARM = "631"
REPLY_AUX_INPUT_ALARM_RESTORED = "632"
REPLY_PART_READY = "650"
REPLY_PART_NOT_READY = "651"
REPLY_PART_ARMED_WITH_MODE = "652"
  PART_ARMED_MODE_AWAY = "0"
  PART_ARMED_MODE_STAY = "1"
  PART_ARMED_MODE_AWAY_NO_DELAY = "2"
  PART_ARMED_MODE_STAY_NO_DELAY = "3"
REPLY_PART_READY_FORCE_ARM = "653"
REPLY_PART_IN_ALARM = "654"
REPLY_PART_DISARMED = "655"
REPLY_EXIT_DELAY_IN_PROGRESS = "656"
REPLY_ENTRY_DELAY_IN_PROGRESS = "657"
REPLY_KEYPAD_LOCKOUT = "658"
REPLY_KEYPAD_BLANKING = "659"
REPLY_COMMAND_OUTPUT_IN_PROGRESS = "660"
REPLY_INVALID_ACCESS_CODE = "670"
REPLY_FUNCTION_NOT_AVAILABLE = "671"
REPLY_FAILED_TO_ARM = "672"
REPLY_PART_BUSY = "673"
REPLY_USER_CLOSING = "700"
REPLY_SPECIAL_CLOSING = "701"
REPLY_PARTIAL_CLOSING = "702"
REPLY_USER_OPENING = "750"
REPLY_SPECIAL_OPENING = "751"
REPLY_PANEL_BAT_TROUBLE = "800"
REPLY_PANEL_BAT_RESTORED = "801"
REPLY_PANEL_AC_TROUBLE = "802"
REPLY_PANEL_AC_RESTORED = "803"
REPLY_BELL_TROUBLE = "806"
REPLY_BELL_RESTORED = "807"
REPLY_TLM_LINE1_TROUBLE = "810"
REPLY_TLM_LINE1_RESTORED = "811"
REPLY_TLM_LINE2_TROUBLE = "812"
REPLY_TLM_LINE2_RESTORED = "813"
REPLY_FTC_TROUBLE = "814"
REPLY_BUFFER_75P_FULL = "816"
REPLY_WIRELESS_ZONE_LOW_BAT = "821"
REPLY_WIRELESS_ZONE_BAT_RESTORED = "822"
REPLY_WIRELESS_KEY_LOW_BAT = "825"
REPLY_WIRELESS_KEY_BAT_RESTORED = "826"
REPLY_HANDHELD_KEYPAD_LOW_BAT = "827"
REPLY_HANDHELD_KEYPAD_BAT_RESTORED = "828"
REPLY_GENERAL_SYSTEM_TEMPER = "829"
REPLY_GENERAL_SYSTEM_TEMPER_RESTORED = "830"
REPLY_ESCORT5580_HA_TROUBLE = "831"
REPLY_ESCORT5580_HA_TROUBE_RESTORED = "832"
REPLY_TROUBLE_STATUS_LED_ON = "840"
REPLY_TROUBLE_STATUS_LED_OFF = "841"
REPLY_FIRE_TROUBLE_ALARM = "842"
REPLY_CODE_REQUIRED = "900"
REPLY_VKEYPAD_LCD_UPDATE = "901"
  # Number of character to display == Ascii data length
  # Ascii data can contain special ASCII chars (0-7)
  VKEYPAD_LCD_LINE1 = "0"
  VKEYPAD_LCD_LINE2 = "1"
  VKEYPAD_LCD_COLUMN1 = "00"
  VKEYPAD_LCD_COLUMN2 = "01"
  VKEYPAD_LCD_COLUMN3 = "02"
  VKEYPAD_LCD_COLUMN4 = "03"
  VKEYPAD_LCD_COLUMN5 = "04"
  VKEYPAD_LCD_COLUMN6 = "05"
  VKEYPAD_LCD_COLUMN7 = "06"
  VKEYPAD_LCD_COLUMN8 = "07"
  VKEYPAD_LCD_COLUMN9 = "08"
  VKEYPAD_LCD_COLUMN10 = "09"
  VKEYPAD_LCD_COLUMN11 = "10"
  VKEYPAD_LCD_COLUMN12 = "11"
  VKEYPAD_LCD_COLUMN13 = "12"
  VKEYPAD_LCD_COLUMN14 = "13"
  VKEYPAD_LCD_COLUMN15 = "14"
  VKEYPAD_LCD_COLUMN16 = "16"
REPLY_VKEYPAD_LCD_CURSOR = "902"
  VKEYPAD_LCD_CURSOR_OFF = "0"
  VKEYPAD_LCD_CURSOR_UNDERSCORE = "1"
  VKEYPAD_LCD_CURSOR_BLOCK = "2"
REPLY_VKEYPAD_LED_STATUS = "903"
  VKEYPAD_LED_STATUS_OFF = "0"
  VKEYPAD_LED_STATUS_ON = "1"
  VKEYPAD_LED_STATUS_FLASHING = "2"
  VKEYPAD_LED_READY = "1"
  VKEYPAD_LED_ARMED = "2"
  VKEYPAD_LED_MEMORY = "3"
  VKEYPAD_LED_BYPASS = "4"
  VKEYPAD_LED_TROUBLE = "5"
  VKEYPAD_LED_PROGRAM = "6"
  VKEYPAD_LED_FIRE = "7"
  VKEYPAD_LED_BACKLIGHT = "8"
  VKEYPAD_LED_AC = "9"
REPLY_BEEP_STATUS = "904"
REPLY_TONE_STATUS = "905"
  TONE_CTRL_OFF = "0"
  TONE_CTRL_ON = "1"
REPLY_BUZZER_STATUS = "906"
REPLY_DOOR_CHIME_STATUS = "907"
REPLY_SOFTWARE_VERSION = "908"


