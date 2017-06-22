from pyOCD.board import MbedBoard

RECOVERY_FILE = "rom.bin"   # binary to write onto device

# to flash bootloader/interface firmware, set target_override='k20d50m'.  To flash application firmware to target, set target_override='<target board type>'.
with MbedBoard.chooseBoard(target_override='k20d50m', frequency=10000000) as board:
  print("Starting flashing")
  board.flash.flashBinary(RECOVERY_FILE)
  print("Recovery successful")
