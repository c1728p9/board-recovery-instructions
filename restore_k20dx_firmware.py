from pyOCD.board import MbedBoard

RECOVERY_FILE = "rom.bin"
with MbedBoard.chooseBoard(target_override='k20d50m', frequency=10000000) as board:
    print("Starting flashing")
    board.flash.flashBinary(RECOVERY_FILE)
    print("Recovery successful")
