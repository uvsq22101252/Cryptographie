"""Question 1: LFSR 17 et test LFSR 17"""


def lfsr_17(seed):
    while True:
        yield seed
        b = seed[2] ^ seed[16]  # calcul valeur de retroaction, 2 et 16 correspondent aux coefficients de retroaction non nuls {14,0}
        seed = [b] + seed[:-1]  # decalage de la seed


def test_lfsr_17():
    s1 = [1] * 17  # initialisation de la seed
    lfsr = lfsr_17(s1)  # Initialisation du lfsr de taille 17
    unique_states = set()  # Initialisation du set des états uniques

    for _ in range(2**17 - 1):
        state = next(lfsr) # Générer l'état suivant
        unique_states.add(tuple(state))  # Ajout de l'état courant au set des états uniques

    if len(unique_states) == 2**17 - 1:  # Vérifier que tous les états possibles ont été générés
        print("l'état prend bien 2^17-1 valeurs différentes")
    else:
        print("l'état ne prend pas 2^17-1 valeurs différentes,tess_lfsr_17 failed!")


#test_lfsr_17()


"""Question 2: LFSR 25 et test LFSR 25"""


def lfsr_25(seed):
    while True:
        yield seed
        b = seed[12] ^ seed[20] ^ seed[21] ^ seed[24]  # calcul valeur de retroaction, 12, 20, 21, 24 correspondent aux coefficients de retroaction non nuls {12,4,3,0}
        seed = [b] + seed[:-1]


def test_lfsr_25():
    s2 = [1] * 25           # initialisation de la seed
    lfsr = lfsr_25(s2)      # Initialisation du lfsr de taille 25
    unique_states = set()   # Initialisation du set des états uniques

    for _ in range(2**25 - 1):
        state = next(lfsr)
        unique_states.add(tuple(state))  # Ajout de l'état courant au set des états uniques

    if len(unique_states) == 2**25 - 1:  # verifier que tous les états possibles ont été générés
        print("l'état prend bien 2^25-1 valeurs différentes")
    else:
        print("l'état ne prend pas 2^17-1 valeurs différentes,tess_lfsr_17 failed!")

#test_lfsr_25()


def hex_to_binary(hex_num):
    binary_list = []
    hex_num = hex_num[2:]  # retirer le préfixe "0x"
    for digit in hex_num:
        binary = bin(int(digit, 16))[2:].zfill(4)
        binary_list.extend(list(binary))
    return binary_list


def binary_to_hex(binary_list):
    return hex(int(''.join(binary_list), 2))


def binary_to_int(binary_list):
    return int(''.join(map(str, binary_list)), 2)


"""Question 3: CSS et chiffrement et dechiffrement d'un message"""


def CSS(s):
    s1 = [1] + s[:16]  # ajout de 1 au début de la seed
    s2 = [1] + s[16:]  # ajout de 1 au début de la seed
    lfsr_17_state = lfsr_17(s1)  # Initialisation lfsr_17
    lfsr_25_state = lfsr_25(s2)  # Initialisation lfsr_25
    c = 0
    z_list = ""
    str_z_list = []
    for _ in range(len(s)//8):
        x = [next(lfsr_17_state)[-1] for _ in range(8)]  # generer x
        x.reverse()

        y = [next(lfsr_25_state)[-1] for _ in range(8)]  # generer y
        y.reverse()

        x = binary_to_int(x)  # convertis x en entier
        y = binary_to_int(y)  # convertis y en entier

        z = (x + y + c) % 256  # calcule de z

        z_binary = bin(z)[2:].zfill(8)  # convertis z en binaire
        z_list += (z_binary)  # ajout de z en binaire à la liste z_list
        
        if x + y > 255:  # calcul de la retenue
            c = 1
        else:
            c = 0

    for i in range(0, len(z_list)):  # convertis z_list en liste de string
        str_z_list.append(str(z_list[i]))

    return list(str_z_list)


def encrypt_message(message, chiffre):  # fonction de chiffrement et dechiffrement d'un message
    message_binary = hex_to_binary(message)  # convertis le message en binaire
    result_binary = []  # initialisation de la liste du resultat en binaire

    for m in range(0, len(message_binary)):
        xor = int(message_binary[m]) ^ int(chiffre[m]) # xor entre le message et le chiffre
        result_binary.append(str(xor))

    # Convert result to hexadecimal
    result_hex = binary_to_hex(result_binary)  # convertis le resultat en hexadecimal
    print("le chiffre/message est : ", result_hex)
    return result_hex


def main():
    choice = input("Choisissez une option:\n1. Test LFSR 17\n2. Test LFSR 25\n3. Chiffré un message\n4. Déchiffrer unmessage\n")

    if choice == "1":
        test_lfsr_17()
    elif choice == "2":
        test_lfsr_25()
    elif choice == "3":
        encrypt_message("0xffffffffff", CSS([0]*40))
    elif choice == "4":
        encrypt_message("0xffffb66c39", CSS([0]*40))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
