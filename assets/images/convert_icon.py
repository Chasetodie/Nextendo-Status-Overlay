import sys
from PIL import Image

SIZE = 256  # ancho y alto en píxeles del ícono final

def convert(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    raw = img.tobytes("raw", "RGBA")
    with open(output_path, "wb") as f:
        f.write(raw)
    print(f"Listo: {output_path} ({len(raw)} bytes, {SIZE}x{SIZE})")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python convert_icon.py entrada.png salida.bin")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])