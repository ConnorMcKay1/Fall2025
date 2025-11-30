from ListReader import TxtReader

# print('\n' + "Going for the password match!!!@!@")

# TxtReader()


# def Detection():
#     print('\n' + "found!")


# Detection()

import gzip
import shutil

input_path = "crackstation-human-only.txt.gz"  # .gz file
output_path = "crackstation.txt"          # output .txt file

with gzip.open(input_path, "rb") as f_in:
    with open(output_path, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Decompression complete!")

