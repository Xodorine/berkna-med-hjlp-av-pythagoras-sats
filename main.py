katet1 = 0
katet2 = 0
hypotenusa = 0
def Pythagoras():
    global katet1, katet2, hypotenusa
    katet1 = input.rotation(Rotation.PITCH)
    katet2 = input.rotation(Rotation.ROLL)
    hypotenusa = Math.sqrt(katet1 * katet1 + katet2 * katet2)
    basic.show_number(hypotenusa)