import pandas as pd

if __name__ == "__main__":

    correo = 'jose@gmail.com'
    x = correo.find("@")
    print(x)

    if x != -1:
        print("True")
    else:
        print("False")