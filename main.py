from cryptography.fernet import Fernet
import json
import os
import logging
from datetime import datetime, timedelta

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Generate AES encryption key or load existing key
def load_or_generate_key():
    key_file = 'key.key'
    if os.path.exists(key_file):
        # Load existing key
        with open(key_file, 'rb') as kf:
            key = kf.read()
    else:
        # Generate a new key and save it
        key = Fernet.generate_key()
        with open(key_file, 'wb') as kf:
            kf.write(key)
        logger.info("Generated new AES encryption key.")
    return key

# Encrypt password and save to JSON with expiration date
def encrypt_and_save_password(password, expiration_date=None):
    key = load_or_generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    if expiration_date:
        data = {"password": encrypted_password.decode(), "expiration_date": expiration_date.strftime('%Y-%m-%d')}
    else:
        data = {"password": encrypted_password.decode()}
    with open('user.json', 'w') as f:
        json.dump(data, f)
    logger.info(f"Password encrypted and saved to user.json. Expiration date: {expiration_date.strftime('%Y-%m-%d') if expiration_date else 'None'}")

# Decrypt password from JSON
def decrypt_and_load_password():
    key = load_or_generate_key()
    with open('user.json', 'r') as f:
        data = json.load(f)
        encrypted_password = data['password'].encode()
        cipher_suite = Fernet(key)
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    logger.info("Password decrypted from user.json.")
    return decrypted_password

# Check password expiration and prompt user to update if expired
def check_password_expiration():
    with open('user.json', 'r') as f:
        data = json.load(f)
        expiration_date_str = data.get('expiration_date')
        if expiration_date_str:
            expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d').date()
            if expiration_date <= datetime.now().date():
                logger.warning(f"Password expired on {expiration_date_str}. Prompting user to update password.")

# Print contents of user.json
def print_user_json():
    with open('user.json', 'r') as f:
        data = json.load(f)
    print("Contents of user.json:")
    print(json.dumps(data, indent=4))

# Main execution
if __name__ == "__main__":
    # Simulate password expiration after 30 days
    expiration_date = datetime.now().date() + timedelta(days=30)
    generated_password = "your_generated_password"

    # Encrypt password with expiration date
    encrypt_and_save_password(generated_password, expiration_date=expiration_date)

    # Decrypt password
    decrypted_password = decrypt_and_load_password()
    print(f"Decrypted Password: {decrypted_password}")

    # Check password expiration
    check_password_expiration()

    # Print user.json contents
    print_user_json()