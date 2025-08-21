import os
from PIL import Image

# 支援的圖片副檔名
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp'}

# 遞迴搜尋所有圖片
for root, _, files in os.walk('assets'):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in IMAGE_EXTENSIONS:
            img_path = os.path.join(root, file)
            try:
                with Image.open(img_path) as im:
                    # 檢查是否為RGBA
                    if im.mode == 'RGBA':
                        # 建立黑色背景
                        bg = Image.new('RGB', im.size, (0, 0, 0))
                        # 合成: 透明處為黑色
                        bg.paste(im, mask=im.split()[3])
                        # 覆蓋原始檔案
                        bg.save(img_path)
            except Exception as e:
                print(f'Error processing {img_path}: {e}')
