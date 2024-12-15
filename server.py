import socket
import json
from rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt

def server():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 65432))
    server_socket.listen(1)
    print("Server listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Generate RSA keys for PKA
    pka_public, pka_private = generate_rsa_keys()

    # Serialize the public key to a JSON string
    pka_pub_key_str = json.dumps(pka_public)

    # Encrypt PKA public key string using PKA private key
    encrypted_pka_pub_key = rsa_encrypt(pka_pub_key_str, pka_private)
    print(f"Encrypted PKA Public Key: {encrypted_pka_pub_key}")

    # Send the encrypted public key to the client
    conn.sendall(json.dumps(encrypted_pka_pub_key).encode())
    print("Sent encrypted PKA public key.")

    # Server input loop for back-and-forth communication
    while True:
        # Wait for a message from the client
        data = conn.recv(1024).decode()
        if data.lower() == "exit":
            print("Client requested to exit. Closing connection.")
            break
        print(f"Received from client: {data}")

        # Process the received message (you can add logic here)
        response = input("Enter your message to send to the client: ")
        
        # Send the server's response to the client
        conn.sendall(response.encode())
        print(f"Sent to client: {response}")

    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    server()
