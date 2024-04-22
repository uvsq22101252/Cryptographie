def lfsr_17(seed):
    while True:
        yield seed
        
        b = seed[2] ^ seed[16]
        seed = [b] + seed[:-1]


def test_lfsr_17():
    s1 = [1] * 17  # Initialize the seed
    lfsr = lfsr_17(s1)  # Initialize the LFSR
    unique_states = set()  # Initialize the set of unique states

    for _ in range(2**17 - 1):
        state = next(lfsr)
        unique_states.add(tuple(state))  # Add the current state to the set of unique states

    print("Number of unique states:", len(unique_states))
    assert len(unique_states) == 2**17 - 1  # Check that all possible states were generated

    print("test_lfsr_17 passed successfully!")


test_lfsr_17()


def lfsr_25(seed):
    while True:
        yield seed
        
        b = seed[12] ^ seed[20] ^ seed[21] ^ seed[24]
        seed = [b] + seed[:-1]


def test_lfsr_25():
    s2 = [1] * 25  # Initialize the seed
    lfsr = lfsr_25(s2)  # Initialize the LFSR
    unique_states = set()  # Initialize the set of unique states

    for _ in range(2**25 - 1):
        state = next(lfsr)
        unique_states.add(tuple(state))  # Add the current state to the set of unique states

    print("Number of unique states:", len(unique_states))
    assert len(unique_states) == 2**25 - 1  # Check that all possible states were generated

    print("test_lfsr_25 passed successfully!")


test_lfsr_25()


def hex_to_binary(hex_num):
    binary_list = []
    hex_num = hex_num[2:]  # Remove the "0x" prefix
    for digit in hex_num:
        binary = bin(int(digit, 16))[2:].zfill(4)
        binary_list.extend(list(binary))
    return binary_list


def CSS(s):
    s1 = [1] + s[:16]
    s2 = [1] + s[16:]
    lfsr_17_state = lfsr_17(s1)  # Initialize lfsr_17
    lfsr_25_state = lfsr_25(s2)  # Initialize lfsr_25
    c = 0
    z_list = []  # Initialize the list of z
    for _ in range(5):
        x = [next(lfsr_17_state)[-1] for _ in range(8)]  # Generate x
        
        y = [next(lfsr_25_state)[-1] for _ in range(8)]  # Generate y
        

        x = int(''.join(map(str, x)), 2)  # Convert x to an integer
        
        y = int(''.join(map(str, y)), 2)  # Convert y to an integer
        

        z = (x + y + c) % 256  # Calculate z
        
        z_binary = bin(z)[2:].zfill(8)  # Convert z to binary
        z_list.insert(0, z_binary)  # Add z to the left of the list of z
        
        if x + y > 255:
            c = 1
        else:
            c = 0
        
    
    hex_result = hex(int(''.join(z_list), 2))  # Convert the binary list to hexadecimal
    print("hex_result:", hex_result)
    return hex_result


def encrypt_message(message, chiffre):
    message_binary = hex_to_binary(message)  # Convert message to binary
    chiffre_binary = hex_to_binary(chiffre)  # Convert chiffre to binary

    # Perform XOR bit-wise
    result_binary = [str(int(m) ^ int(c)) for m, c in zip(message_binary, chiffre_binary)]

    # Convert result to hexadecimal
    result_hex = hex(int(''.join(result_binary), 2))
    return result_hex


chiffre = encrypt_message('0xffffffffff', str(CSS([0]*40)))
print("le chiffre est:", chiffre)
dechiffre = encrypt_message('0x96366dffff', str(CSS([0]*40)))
print("le message est:", dechiffre)


def decrypt_message(message, key):
    chiffre_binary = hex_to_binary(message)  # Convert message to binary
    key_binary = hex_to_binary(key)  # Convert key to binary

    # Perform XOR bit-wise
    result_binary = [str(int(m) ^ int(k)) for m, k in zip(chiffre_binary, key_binary)]

    # Convert result to hexadecimal
    result_hex = hex(int(''.join(result_binary), 2))
    print("le message est:", result_hex)
    return result_hex


#decrypt_message('0x96366dffff', str(CSS([0]*40)))







 