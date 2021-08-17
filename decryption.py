from random import randint

LIMIT = 100  # limit bits of random number
CHECKS_FOR_PRIME = 10  # random witnesses to check for prime number


def is_prime(num: int):
    for i in range(CHECKS_FOR_PRIME):
        if not rabin_miller(num, randint(1, num - 1)):
            return False
    return True


# rabin_miller check for prime number, even number = 2^r * s
def rabin_miller(num: int, witness: int):
    r = 0  # 2 ^ r
    s = num - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    x = pow(witness, s, num)  # 2^s
    for i in range(r):
        current = pow(x, 2, num)  # (witness ^s) ^ 2
        if current == 1:
            return x == num - 1 or x == 1
        x = current
    return False


def get_rand_prime(lim=LIMIT):
    from secrets import randbits
    num = None
    while True:
        num = randbits(lim)
        if num % 2 == 0 or not is_prime(num):  # check if num is prime
            continue
        break
    return num


def get_e_d_n():
    from math import gcd
    p = get_rand_prime()  # first prime
    q = get_rand_prime()  # second prime
    e = None
    phi = (p - 1) * (q - 1)  # calculate phi(n)
    while True:
        e = randint(1, phi)
        if gcd(phi, e) == 1:
            break
    d = pow(e, -1, phi)
    return e, d, p * q


def decrypt_message(d: int, n: int):
    return pow(int(input("Please enter message to decrypt: ")), d, n)


if __name__ == '__main__':
    e, d, n = get_e_d_n()
    print(f"Public Data = e:{e} n:{n}")  # public data
    print(f"Private Data = d:{d} n:{n}")  # private data
    while True:
        try:
            option = int(input(
                """1 to decrypt message
2 to exit
please choose an option:"""))
            if option == 1:
                print(f"Decrypted Message: {decrypt_message(d, n)}")
            elif option == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("You must enter option:")
