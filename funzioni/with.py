#aprire e quidere i file 
file = open("CIAOO.txt","w")

with file:
    file.write("CIAOOOPROVAWITH")

import pathlib
import logging
file_path = pathlib.Path("hello.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("hello,World!")
except OSError as error:
    logging.error("Writing to file %s failed due to: %s")
