from PIL import Image

def extract_image(filepath):
  data = {}

  img = Image.open(filepath)
  data["Format"] = img.format
  data["Mode"] = img.mode
  data["Size"] = f"{img.width}X{img.height}"
  data["Width"] = img.width
  data["Height"] = img.height
  data["Megapixels"] = round((img.width * img.height) / 1_000_000, 2)
  data["Is Animated"] = getattr(img, "is_animated", False)
  data["Frames"] = getattr(img, "n_frames", 1)
  data.update(img.info)

  try: 
    with open(filepath, "rb") as f:
      return data
  except FileNotFoundError:
    print(f"File not found: {filepath}")
    return None
  except Exception as e:
    print(f"How did you even manage to do this??? {e}")
    return None