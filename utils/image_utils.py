def is_valid_image(filename: str) -> bool:
    return filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
