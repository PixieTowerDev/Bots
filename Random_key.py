# librerías
import random
# variables


def gamepass(long):
    digits = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    long = 10

    key = ""
    # funcion de contraseña
    for i in range(long):
        key += random.choice(digits)

    return key
