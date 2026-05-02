from PIL import Image

src = "change.jpg"
img = Image.open(src).convert("RGBA")

sizes = {
    "icons/icon-512.png": (512, 512),
    "icons/icon-512-maskable.png": (512, 512),
    "icons/icon-192.png": (192, 192),
    "icons/apple-touch-icon.png": (180, 180),
}

for path, size in sizes.items():
    resized = img.resize(size, Image.LANCZOS)
    resized.save(path)
    print(f"已建立 {path}")

favicon = img.resize((32, 32), Image.LANCZOS)
favicon.save("favicon.ico")
print("已建立 favicon.ico")

print("完成！所有 icon 已取代。")
