# 🖼️ Image Encryptor & Decryptor

A simple, secure Python GUI application that encrypts and decrypts image files using **Fernet (AES-128)** symmetric encryption. This tool allows users to protect sensitive visual data with a password-like key.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features
- Encrypt image files securely
- Decrypt images using a generated key
- Simple graphical user interface
- Automatic encryption key generation

## 🛠️ Requirements
- Python 3.x
- `cryptography` library

# 🚀 Installation
1. **Clone the repository**
```bash
git clone https://github.com/AmirmasoudCS/Image-Encryptor.git
cd Image-Encryptor
```
2. **Install dependencies**
```
pip install -r requirements.txt
```
3. **Run the program**
```bash
python ImageEncryptor.py
```
## 📖 How to Use
### 🔐 Encrypt an Image
1. Click **Encrypt (Generate Key)** button.
2. Select an image file you want to protect.
3. Choose a location to save the encrypted file (it will have a `.enc` extension).
4. **Important:** Copy the generated key from the text box and save it securely. You cannot decrypt the image without this key!
### 🔓 Decrypt an Image
1. Paste your key into the **Encryption Key** field.
2. Click the **Decrypt** button.
3. Select the .enc file you wish to decrypt.
4. Choose where to save the restored image (e.g., as a `.png` or `.jpg`).
# 📁 Project Structure
```
.
├── 🚫 .gitignore          # Files to ignore in Git
├── 🐍 ImageEncryptor.py   # Main source code
├── ⚖️ LICENSE             # MIT License file
├── 📖 README.md           # Project documentation
└── 📝 requirements.txt    # List of Python dependencies
```
# ⚖️ License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.