let katet1 = 0
let katet2 = 0
let hypotenusa = 0
function Pythagoras () {
    katet1 = input.rotation(Rotation.Pitch)
    katet2 = input.rotation(Rotation.Roll)
    hypotenusa = Math.sqrt(katet1 * katet1 + katet2 * katet2)
    basic.showNumber(hypotenusa)
}
