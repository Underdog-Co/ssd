#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

def convert_png_to_jpg():
    current_dir = Path.cwd()
    png_files = list(current_dir.glob("*.png"))
    
    if not png_files:
        print("PNG файлы не найдены в текущей директории")
        return
    
    print(f"Найдено {len(png_files)} PNG файл(ов)")
    
    for png_file in png_files:
        try:
            jpg_file = png_file.with_suffix(".jpg")
            with Image.open(png_file) as img:
                # Конвертируем в RGB (JPG не поддерживает прозрачность)
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                img.save(jpg_file, "JPEG", quality=95)
            print(f"✓ {png_file.name} → {jpg_file.name}")
        except Exception as e:
            print(f"✗ Ошибка конвертации {png_file.name}: {e}")
    
    print("Готово!")

if __name__ == "__main__":
    convert_png_to_jpg()
