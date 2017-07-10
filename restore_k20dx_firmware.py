from pyOCD.board import MbedBoard

#specific board used for OCD by setting board_id = '<board id of OCD reported by mbedls command>'. If you set to None, then it will search for one and ask for confirmation.
board_id = '10500000e062eef000000000000000000000000097969902'
#board_id = None

RECOVERY_FILE = "rom.bin"   # binary to write onto device

# to flash bootloader/interface firmware, set target_override='k20d50m'.  To flash application firmware to target, set target_override='<target board type>'.
with MbedBoard.chooseBoard(target_override='k20d50m', board_id=board_id, frequency=10000000) as board:
  print("Flashing " + RECOVERY_FILE + " to target")
  board.flash.flashBinary(RECOVERY_FILE)
  print("Recovery successful")
