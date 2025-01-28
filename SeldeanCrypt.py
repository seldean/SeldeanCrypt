import argparse
from cryptography.fernet import Fernet

# Function to generate a key
def generate_key(output_file):
    key = Fernet.generate_key()
    with open(output_file, "wb") as key_file:
        key_file.write(key)
        print(f"Key generated and saved to {output_file}")

# Function to load a key
def load_key(input_file):
    with open(input_file, "rb") as key_file:
        return key_file.read()

# Function to encrypt a file
def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(output_file, "wb") as file:
        file.write(encrypted_data)
        print(f"File '{input_file}' encrypted and saved to '{output_file}'.")

def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, "wb") as file:
        file.write(decrypted_data)
    
    print(f"File '{input_file}' decrypted and saved to '{output_file}'.")

def main():
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt files using a generated key.")
    parser.add_argument("operation", choices=["generate-key", "encrypt", "decrypt"], help="Operation to perform: generate a key, encrypt or decrypt")
    parser.add_argument("--input", "-i", type=str, help="Input file (for encryption or decryption)")
    parser.add_argument("--output", "-o", type=str, help="Output file (for encryption or decryption)")
    parser.add_argument("--key", "-k", type=str, help="Key file to use with program.")

    args = parser.parse_args()

    if args.operation == "generate-key":
        if not args.output:
            print("Error: --output must be specified for generating a key file.")
            return
        generate_key(args.output)
    elif args.operation == "encrypt":
        if not args.input or not args.output or not args.key:
            print("Error: --input, --output and --key must be specified for encryption.")
            return
        key = load_key(args.key)
        encrypt_file(args.input, args.output, key)
    elif args.operation == "decrypt":
        if not args.input or not args.output or not args.key:
            print("Error: --input, --output and --key must be specified for decryption.")
            return
        key = load_key(args.key)
        decrypt_file(args.input, args.output, key)

if __name__ == "__main__":
    main()