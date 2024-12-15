from rsa import rsa_encrypt

def encrypt_des_key(des_key, sender_private_key, receiver_public_key):
    # Encrypt DES key with sender's private key
    encrypted_with_sender_private = rsa_encrypt(des_key, sender_private_key)

    # Encrypt result with receiver's public key
    encrypted_with_receiver_public = rsa_encrypt(str(encrypted_with_sender_private), receiver_public_key)

    return encrypted_with_receiver_public
