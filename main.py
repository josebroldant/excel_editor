import pandas as pd
from utils import my_utils

# if __name__ == "__main__":
#     sales_error_list = []
#     file = pd.read_excel("C://Users//roldanto//Documents//Curso de python//Actividad 6//datos.xls")
#     for row, data in enumerate(file["sales"]):
#         validator = str(data).isdecimal() #checks in a string if is decimal, returns true or false
#         if validator == True:
#             x="Es decimal"
#         else:
#             x="Fila: "+str(row)+" - Columna: 19 - "+"Valor: "+str(data)
#             sales_error_list.append(x)
#             print(sales_error_list)     

print("Inserte la direccion donde se encuentra el archivo y seguido del nombre del archivo y su extension ")
# C://Users//roldanto//Documents//Curso de python//Actividad 6//datos.xls
direc = input()
file = pd.read_excel(direc)

my_utils.row_id_validator(direc)
my_utils.email_validator(direc)
my_utils.sales_validator(direc)