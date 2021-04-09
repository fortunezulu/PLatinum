import numpy
import re
def cellphone(cell_number):
    cell_number=raw_input()
    x= re.sub("[^0-9]", "", cell_number)

    if x[0] != "0":
        x = "0" + x

        if len(x) != 10:
            raise Exception(
                "The number entered is not the lenth of 10,retry..."
            )

    return x
