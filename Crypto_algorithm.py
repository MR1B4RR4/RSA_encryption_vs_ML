
def map_string_to_numbers(input_string):
    # Define the ASCII printable characters
    ascii_printable = ' ' + ''.join(chr(i) for i in range(33, 127))  # From space to tilde
    # Create a mapping from each character to a unique double-digit number
    char_to_num_map = {char: f"{i+10:02}" for i, char in enumerate(ascii_printable)}
    
    # Transform each character in the input string
    transformed_string = ''.join(char_to_num_map[char] for char in input_string if char in char_to_num_map)
    
    return transformed_string

def map_numbers_to_string(input_numbers):
    # Define the ASCII printable characters
    ascii_printable = ' ' + ''.join(chr(i) for i in range(33, 127))  # From space to tilde
    # Create a reverse mapping from each unique double-digit number to its character
    num_to_char_map = {f"{i+10:02}": char for i, char in enumerate(ascii_printable)}
    
    # Transform each pair of digits in the input numbers to characters
    transformed_string = ''.join(num_to_char_map[input_numbers[i:i+2]] for i in range(0, len(input_numbers), 2) if input_numbers[i:i+2] in num_to_char_map)
    
    return transformed_string

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

def extended_euclidean(k, z):
    if k == 0:
        return (z, 0, 1)
    else:
        gcd, x1, y1 = extended_euclidean(z % k, k)
        x = y1 - (z // k) * x1
        y = x1
        return (gcd, x, y)

def find_a_b(k, z):
    gcd, a, b = extended_euclidean(k, z)
    if gcd != 1:
        return "No solution exists because k and z are not coprime."
    else:
        return a, b

def RSA_generate(p,q):
    n = p*q
    k_aux = (p-1)*(q-1)
    k = k_aux -1 
    for i in range(k_aux):
        if compute_hcf(k,k_aux) == 1:
            a, b = find_a_b(k, k_aux)
            if a > 0: 
                break
            k -= 1
        else:
            k -= 1
    
    public_key = (a,n)
    private_key = k
    return public_key, private_key

def separate_number_into_pairs(number):
    # Convert the number to a string
    number_str = str(number)
    # Split the string into pairs of digits
    pairs = [int(number_str[i:i+2]) for i in range(0, len(number_str), 2)]
    return pairs

def separate_number_into_groups_of_four(number):
    # Convert the number to a string
    number_str = str(number)
    # Calculate the number of zeros needed to make the last group have four digits
    padding_needed = (4 - len(number_str) % 4) % 4
    # Pad the string with zeros at the end if necessary
    number_str_padded = number_str + '0' * padding_needed
    # Split the padded string into groups of four digits
    groups_of_four = [int(number_str_padded[i:i+4]) for i in range(0, len(number_str_padded), 4)]
    return groups_of_four


def RSA_encryption(message, public_key):
    #message = input('Insertar mensaje: ')
    a = public_key[0]
    n = public_key[1]

    message_number = map_string_to_numbers(message)
    pairs = separate_number_into_groups_of_four(message_number)
    encryption_list = []
    for i in pairs:
        i = int(i)
        encryption = i**a % n
        encryption_list.append(encryption)
    return encryption_list


def RSA_open(encryption_list, private_key, public_key):
    a = public_key[0]
    n = public_key[1]
    digits = []
    for i in encryption_list:
        digit = i**private_key % n
        digits.append(digit)
    open_number = ''.join(str(number) for number in digits)
    open_string = map_numbers_to_string(open_number)
    return open_string

prime_1 = 227
prime_2 = 229

# # ej_public_key, ej_private_key =  RSA_generate(int(input('Primer primo: ')),int(input('Segundo primo: ')))
# ej_public_key, ej_private_key =  RSA_generate(prime_1,prime_2)
# print('Llave publica: ',ej_public_key, '\nLlave privada: ',ej_private_key)

# # # ej_message = input('\nMensaje a encriptar: ')
# ej_message = 'mistake'

# ej_crypt = RSA_encryption(ej_message, ej_public_key)

# print('\nMensaje numero: ', map_string_to_numbers(ej_message))
# print('\nMensaje numero cut: ', separate_number_into_groups_of_four(map_string_to_numbers(ej_message)))
# print('\nMensaje encriptado: ',ej_crypt)

# ej_open = RSA_open(ej_crypt, ej_private_key, ej_public_key)

# print('\nMensaje desencriptado: ', ej_open)
