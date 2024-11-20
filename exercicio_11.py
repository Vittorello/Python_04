dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dic_fund = {**dicionario1,**dicionario2}

        # ou

dic_fund = dicionario1 | dicionario2


print(dic_fund)