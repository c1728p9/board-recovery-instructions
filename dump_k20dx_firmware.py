from pyOCD.board import MbedBoard

#board_id = '0240000033514e45001c500585d40025e981000097969900'  #specific to board you are using for flashing. can check with "pyocd-gdbserver -l" command. If you set to None, then it will search for one.

board_id = None

with MbedBoard.chooseBoard(target_override='k20d50m', board_id=board_id) as board:
    addr = 0x00000000
    size = 128 * 1024   # K20 has 128 is size of flash. 1024 converts to KB
    data = board.target.readBlockMemoryUnaligned8(addr, size)
    data = bytearray(data)
    with open("rom.bin", 'wb') as f:
        f.write(data)
