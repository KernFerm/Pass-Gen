### PLEASE READ EVERYTHING ON THE README.MD INCLUDING THE LINKS BELOW TO THE .MD AND LICENSE FILE

# Secure Password Manager

This Secure Password Manager is a Python application designed to securely encrypt and store passwords using AES encryption. It provides functionalities to generate or load an existing AES encryption key, encrypt and save passwords with optional expiration dates, and decrypt passwords.

## how to download the repo first time users

  - click link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos)

## Features

- **AES Encryption**: Utilizes the cryptography library to encrypt passwords using AES encryption, ensuring secure storage.
- **Key Management**: Automatically generates a new AES encryption key if one does not exist or loads an existing key from a file.
- **Expiration Dates**: Allows setting expiration dates for passwords, adding an extra layer of security and management.
- **Logging**: Includes logging of operations, such as key generation, password encryption, and decryption, aiding in monitoring and debugging.

### Python 3.11.6 is Required:
- [Python-3.11.6](https://github.com/KernFerm/Py3.11.6installer/archive/refs/heads/main.zip)

## Installation

To use the Secure Password Manager, you need to have Python and pip installed on your system. It is recommended to use a virtual environment for Python projects to manage dependencies effectively. Follow these steps to set up your environment:

1. Install virtualenv if you haven't already:

```
pip install virtualenv
```
### Create a virtual environment in your project directory:
```
virtualenv venv
```
### Activate the virtual environment:

- On `Windows:`

```
.\venv\Scripts\activate
```

- On `Unix` or `MacOS:`

```
source venv/bin/activate
```

### Setup and Installation

1. **Clone the Repository**: First, clone the repository to your local machine using Git.

 ```
 git clone https://github.com/KernFerm/Pass-Gen
 cd Pass-Gen
 ```

2. **Create a Virtual Environment**: It's recommended to create a virtual environment for Python projects. This keeps dependencies required by different projects separate. If you're using `pipenv`, you can skip to step 3.

 ```
 python -m venv venv
 ```

 - Activate the virtual environment:
 - On Windows:
   ```
    .\venv\Scripts\activate
   ```
 - On Unix or MacOS:
   ```
   source venv/bin/activate
   ```

3. **Install Dependencies**: Install the `cryptography` library within your virtual environment.

  ```
  run the requirements.bat
  ```

 If you're using `pipenv`, you can install all dependencies by simply running:

  ```
  pipenv install
  ```

 Then, activate the `pipenv` shell:

   ```
   pipenv shell
   ```

### Usage

- **Generate or Load an AES Key**: The application will automatically generate a new AES encryption key if it does not exist or load an existing one from the `key.key` file.

- **Encrypt and Save Password**: Call the `encrypt_and_save_password(password, expiration_date=None)` function with the password you wish to encrypt. Optionally, you can provide an expiration date for the password.

- **Decrypt Password**: Use the `decrypt_and_load_password()` function to decrypt and load the password stored in `user.json`.

---

### Example

- **Encrypting and saving a password**:

    ```python
    from main import encrypt_and_save_password
    from datetime import datetime, timedelta

    # Encrypt and save password with an expiration date of 30 days from now
    encrypt_and_save_password("mySecurePassword123", datetime.now() + timedelta(days=30))
    ```

- **Decrypting and loading a password**:

    ```python
    from main import decrypt_and_load_password

    # Decrypt and load the password
    decrypt_and_load_password()
    ```

### Running the Application

After setting up the environment and installing the necessary dependencies, you can run the application by executing the Python script associated with the desired functionality. For example, to encrypt and save a password, you might run:

```bash
python main.py
```

Replace `main.py` with the appropriate script name if your entry point is different. Ensure you follow the usage examples provided above to interact with the application correctly.

----

## [CODE_OF_CONDUCT.md](https://github.com/KernFerm/Pass-Gen/blob/main/CODE_OF_CONDUCT.md)

## [LICENSE](https://github.com/KernFerm/Pass-Gen/blob/main/LICENSE)

## [CONTRIBUTING.md](https://github.com/KernFerm/Pass-Gen/blob/main/CONTRIBUTING.md)
