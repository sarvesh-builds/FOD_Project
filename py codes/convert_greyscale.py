import cv2
from pathlib import Path

# ==========================
# CHANGE THESE PATHS
# ==========================

INPUT_DATASET = Path(r"D:\PROJECTS\ML_projects\FOD_Project\dataset")

OUTPUT_DATASET = Path(r"D:\PROJECTS\ML_projects\FOD_Project\dataset_grayscale")

# ==========================

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp"}

total_images = 0

for image_path in INPUT_DATASET.rglob("*"):

    if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
        continue

    # Preserve folder structure
    relative_path = image_path.relative_to(INPUT_DATASET)
    output_path = OUTPUT_DATASET / relative_path

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Read image
    img = cv2.imread(str(image_path))

    if img is None:
        print(f"Couldn't read: {image_path}")
        continue

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save image
    cv2.imwrite(str(output_path), gray)

    total_images += 1

print("=" * 40)
print("Conversion Completed")
print(f"Total Images Converted : {total_images}")
print(f"Saved to : {OUTPUT_DATASET}")
print("=" * 40)