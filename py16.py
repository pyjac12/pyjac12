cel=int(input("write your temprture here"))


def fahenit(cel):
    return round ((cel*1.8 + 32), 1)


print("the temprature in farenhit is "  + str(fahenit(cel)) + ".")
