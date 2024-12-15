import socket
import json
from rsa import rsa_decrypt, generate_rsa_keys, rsa_encrypt

def client():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))

    # Generate RSA keys for the client
    client_public, client_private = generate_rsa_keys()

    # Receive the encrypted PKA public key
    data = client_socket.recv(1024).decode()
    if not data:
        print("No data received.")
        client_socket.close()
        return
    print(f"Encrypted PKA Public Key Received: {data}")

    encrypted_pka_pub_key = json.loads(data)
    print(f"Encrypted PKA Public Key: {encrypted_pka_pub_key}")

    # Decrypt PKA's public key using the client's private key
    decrypted_bytes = rsa_decrypt(encrypted_pka_pub_key, client_private)

    if decrypted_bytes is None:
        print("Decryption failed.")
        client_socket.close()
        return

    print(f"Decrypted raw bytes: {decrypted_bytes}")
    print(f"Processed Decrypted Data: {decrypted_bytes}")

    # Client input loop for back-and-forth communication
    while True:
        # Send a message to the server
        message_to_send = input("Enter your message to the server: ")
        
        # Send the message to the server
        client_socket.sendall(message_to_send.encode())
        print(f"Sent to server: {message_to_send}")

        # If the message is "exit", close the connection
        if message_to_send.lower() == "exit":
            print("Exiting communication.")
            break

        # Wait for the server's response
        data = client_socket.recv(1024).decode()
        if data.lower() == "exit":
            print("Server requested to exit. Closing connection.")
            break
        print(f"Received from server: {data}")

    client_socket.close()

if __name__ == "__main__":
    client()
