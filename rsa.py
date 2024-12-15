def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x3 == 1:
        d = x2 % phi
    return d

def generate_rsa_keys():
    p, q = 61, 53  # Simple primes for demonstration
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))  # Public key, Private key

def rsa_encrypt(message, public_key):
    e, n = public_key
    message_int = int.from_bytes(message.encode('utf-8'), byteorder='big')
    return pow(message_int, e, n)

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_int = pow(ciphertext, d, n)
    
    byte_len = (decrypted_int.bit_length() + 7) // 8
    decrypted_bytes = decrypted_int.to_bytes(byte_len, 'big')

    return decrypted_bytes
    """
    # Convert the decrypted integer back to bytes and return it as a string (not UTF-8 directly)
    try:
        # Convert integer to byte sequence (equivalent to original encryption) 
        byte_len = (decrypted_int.bit_length() + 7) // 8  # Calculate how many bytes are needed to store the integer
        decrypted_bytes = decrypted_int.to_bytes(byte_len, 'big')
        
        # If the decrypted value is a string, it will be stored in a byte array
        return decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError as e:
        # If there’s a problem decoding, you can try to return the raw bytes or handle accordingly
        print(f"Error decoding the decrypted message: {e}")
        return None
    """
