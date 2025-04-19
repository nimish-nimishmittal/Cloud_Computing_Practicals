# 🖼️ Image Resolution Reducer using Docker 🐳

## 🚀 Overview

This project demonstrates how to reduce the resolution of an image locally using Docker and Python. It's a great way to learn Docker containers, image processing with Python, and file mounting techniques.

---

## 📁 Project Structure

```
image-resizer/
├── images/
│   └── input.jpg         # High-res input image
├── output/               # Resized image will be saved here
├── resize.py             # Python script to resize the image
├── requirements.txt      # Python dependencies
└── Dockerfile            # Container instructions
```

---

## ⚙️ How It Works

1. A high-resolution image (`input.jpg`) is placed in the `images/` folder.
2. A Python script uses `Pillow` to reduce the image resolution (e.g., 25% of the original size).
3. The script is executed inside a Docker container.
4. The output is stored in the `output/` folder using Docker volume mapping.

---

## 🐍 Python Script: `resize.py`

```python
from PIL import Image
import os

input_path = 'images/input.jpg'
output_path = 'output/resized.jpg'

img = Image.open(input_path)
new_size = (img.width // 4, img.height // 4)
resized_img = img.resize(new_size)

os.makedirs(os.path.dirname(output_path), exist_ok=True)
resized_img.save(output_path)

print(f"Image resized to {new_size} and saved to {output_path}")
```

---

## 📦 requirements.txt

```
Pillow
```

---

## 🐳 Dockerfile

```Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "resize.py"]
```

---

## 🔧 Steps to Run

### 1. Clone the project (or create folders as above)

### 2. Place a high-resolution image in `images/input.jpg`

### 3. Build the Docker image

```bash
docker build -t image-resizer .
```

### 4. Run the Docker container

```bash
docker run -v $(pwd)/output:/app/output image-resizer
```

✅ Your resized image will be available in the `output/` folder.

---

## 📸 Before vs After

- **Original Image:** Full resolution from `images/input.jpg`
- **Resized Image:** Reduced resolution, saved as `output/resized.jpg`

You can open both and visually compare the change.

---

## 🎁 Bonus Ideas

- Accept custom dimensions as input parameters.
- Add a Streamlit UI for interactive usage.
- Extend to batch resize multiple images.

---

## 🤘 Happy Docking & Resizing!