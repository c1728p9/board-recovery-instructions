from pyOCD.board import MbedBoard

# dump application binary that is flashed on a board

#specific to board you are using for flashing by setting board_id = '<board id reported by mbedls command>'. If you set to None, then it will search for one and ask for confirmation.
board_id = None

with MbedBoard.chooseBoard(board_id=board_id) as board:
  memory_map = board.target.getMemoryMap()
  rom_region = memory_map.getBootMemory()  # application begins here in rom.

  addr = rom_region.start
  size = rom_region.length
  print("addr: %s, size: %s" % (addr, size))

  data = board.target.readBlockMemoryUnaligned8(addr, size)
  data = bytearray(data)
  with open("application.bin", 'wb') as f:
      f.write(data)

  print("Dump complete and named as application.bin")
