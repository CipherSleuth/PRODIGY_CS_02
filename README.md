Image Encryption Tool

This is a simple Python-based tool for encrypting and decrypting images using pixel manipulation. The tool works by performing basic mathematical operations on the pixel values of the image, such as inversion and addition of a key, along with swapping pixel values to obscure the original image. 

## Features:
- Encrypts an image by inverting pixel values and applying a key.
- Swaps pixels as part of the encryption process.
- Decrypts the image using the reverse of the encryption steps.
- Simple to use with basic Python libraries like `Pillow` and `NumPy`.

## Requirements:
- Python 3.x
- Pillow
- NumPy

## Installation:
To install the required libraries, run the following command:

pip install pillow numpy

## Usage:

### Encrypting an Image:
```python
encrypt_image("path_to_image.jpg", "encrypted_image.png", key=123)

Decrypting an Image:

decrypt_image("encrypted_image.png", "decrypted_image.jpg", key=123)

Functions:

encrypt_image(image_path, encrypted_path, key=100): Encrypts the image located at image_path and saves the encrypted version at encrypted_path using the given key.

decrypt_image(encrypted_path, decrypted_path, key=100): Decrypts the encrypted image and saves the original image at decrypted_path.


License:

This project is open-source and available under the MIT License.

Contributing:

Feel free to fork this project and submit pull requests with any improvements or bug fixes.

Disclaimer:

This tool is intended for educational purposes. Use it responsibly.
