from PIL import Image

def xor_image(input_path, output_path, key):
    # Open and convert to RGB (important!)
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # XOR each RGB value with the key
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Saved: {output_path}")

# 🔐 Example usage:
key = 123

# Step 1: Encrypt
xor_image("original_image.jpg", "encrypted_image.jpg", key)

# Step 2: Decrypt
xor_image("encrypted_image.jpg", "decrypted_image.jpg", key)
