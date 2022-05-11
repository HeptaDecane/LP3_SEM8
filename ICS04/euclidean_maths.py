def power_mod(base, exponent, modulus):
    result = 1
    while exponent:
        if (exponent % 2) == 1:
            result = (result * base) % modulus

        base = (base * base) % modulus
        exponent = int(exponent/2)

    return result
