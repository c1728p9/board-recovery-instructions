from pyOCD.board import MbedBoard

#specific board used for OCD by setting board_id = '<board id of OCD reported by mbedls command>'. If you set to None, then it will search for one and ask for confirmation.
board_id = '10500000e062eef000000000000000000000000097969902'

with MbedBoard.chooseBoard(target_override='k20d50m', board_id=board_id) as board:
  addr = 0x00000000
  size = 128 * 1024   # K20 has 128 KB of flash. 1024 converts to KB
  data = board.target.readBlockMemoryUnaligned8(addr, size)
  data = bytearray(data)
  with open("rom.bin", 'wb') as f:
      f.write(data)
  print("Dump success. File rom.bin created")
