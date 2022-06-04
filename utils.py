import pandas as pd

class my_utils:
    def row_id_validator(doc):
        int_error_list = []
        file = pd.read_excel(doc)
        for row, data in enumerate(file["row_id"]):
            validator = isinstance(data, int) #checks if is the data type, returns true or false
            if validator is True:
                x="El dato es entero"
            else:
                x="Fila: "+str(row)+" - Columna: 1 - "+"Valor: "+str(data)
                int_error_list.append(x)
                print(int_error_list)
            

    def email_validator(doc):
        email_error_list = []
        file = pd.read_excel(doc)
        for row, data in enumerate(file["email"]):
            validator = str(data).find("@") #returns the position of the required character
            if validator != -1:
                x="El correo es correcto"
            else:
                x="Fila: "+str(row)+" - Columna: 7 - "+"Valor: "+str(data)
                email_error_list.append(x)
                print(email_error_list)

    def sales_validator(doc):
        sales_error_list = []
        file = pd.read_excel(doc)
        for row, data in enumerate(file["sales"]):
            validator = str(data).isdecimal() #checks in a string if is decimal, returns true or false
            if validator == True:
                x="Es decimal"
            else:
                x="Fila: "+str(row)+" - Columna: 19 - "+"Valor: "+str(data)
                sales_error_list.append(x)
                print(sales_error_list)