def F_to_K(temperature_F):
    temperature_K = (5/9) * (temperature_F - 32) + 273.15
    return temperature_K

def C_to_R(temperature_C):
    temperature_R = temperature_C * 1.8 + 32 + 459.67
    return temperature_R

def C_to_F(temperature_C):
    temperature_F = temperature_C * 1.8 + 32
    return temperature_F
