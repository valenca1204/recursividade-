def inverter(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + inverter(str[:-1])
    
str = "pedro"
print(inverter(str))
