# Part of LuaUI.
from psutil import virtual_memory # Get memory.


MEMORY = (0x401 - 0x1) # Memory. (1024)

with open("RAM", "w") as WRITE_RAM: # Opening file with data.
    WRITE_RAM.write(str(int(virtual_memory().total / MEMORY / MEMORY / MEMORY) + 0x1)) # Send memory.
    WRITE_RAM.close() # Closing.
