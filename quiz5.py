#Katherine O'Roark

#problem 1
def tire_pressure(pres):
    if pres < 28:
        return "Tire Pressure is Low."
    else:
        return None

print(tire_pressure(2))
print(tire_pressure(29))

#problem 2
def thermostat(temp):
    if temp <= 52:
        return "The heater is on."
    elif temp >= 71:
        return "The AC is on."
    else:
        return "The heater and AC are off."

print(thermostat(50))
print(thermostat(65))
print(thermostat(78))

#problem 3
def fruit_message(fruit):
    if fruit == "banana":
        return "Banana it is!"
    elif fruit == "cherry":
        return "I cherish you!"
    elif fruit == "apple":
        return "I applesolutely like you!"
    elif fruit == "orange":
        return "Orange you glad to see me?"
    elif fruit == "melon":
        return "You are one in a Melon!"
    else:
        return None

print(fruit_message("banana"))
print(fruit_message("cherry"))
print(fruit_message("apple"))
print(fruit_message("orange"))
print(fruit_message("melon"))
print(fruit_message("grapes"))
