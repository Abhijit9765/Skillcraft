def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():  # shift letters only
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # keep spaces/punctuation unchanged
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)  # reverse the shift

# --- Main Program ---
if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message (with known shift)")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            message = input("Enter your message: ")
            shift = int(input("Enter shift value (number): "))
            encrypted = encrypt(message, shift)
            print("\n✅ Encrypted Message:", encrypted)

        elif choice == "2":
            message = input("Enter your encrypted message: ")
            shift = int(input("Enter the shift value: "))
            decrypted = decrypt(message, shift)
            print("\n🔓 Decrypted Message:", decrypted)

        elif choice == "3":
            print("Exiting... Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")
