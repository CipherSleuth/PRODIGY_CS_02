from PIL import Image
import numpy as np

def swap_pixels(img_array):
    # Swapping pixels: Swap top-left with bottom-right corners, for example.
    h, w, _ = img_array.shape
    img_array[0, 0], img_array[h-1, w-1] = img_array[h-1, w-1], img_array[0, 0]
    return img_array

def encrypt_image(image_path, encrypted_path, key=100):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Swap pixels and apply basic operation (invert + add key)
    img_array = swap_pixels(img_array)
    encrypted_array = (255 - img_array + key) % 256

    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(encrypted_path)
    print(f"Encrypted image saved as {encrypted_path}")

def decrypt_image(encrypted_path, decrypted_path, key=100):
    img = Image.open(encrypted_path)
    img_array = np.array(img)

    # Reverse the operation: swap pixels back and subtract the key
    img_array = swap_pixels(img_array)  # Swap pixels back
    decrypted_array = (255 - img_array - key) % 256

    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(decrypted_path)
    print(f"Decrypted image saved as {decrypted_path}")

# Example usage:
# encrypt_image("original.jpg", "encrypted.png", key=123)
# decrypt_image("encrypted.png", "decrypted.jpg", key=123)
