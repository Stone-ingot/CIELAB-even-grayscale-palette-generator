# CIELAB Even Grayscale Palette Generator

This script generates perceptually uniform grayscale palettes by sampling evenly spaced lightness values (L*) in the CIELAB color space and converting them to sRGB.

Unlike traditional RGB‑even grayscale sampling (e.g., `[0, 36, 73, 109, 146, 182, 219, 255]`), this approach produces steps that appear evenly spaced to the human eye, making it ideal for **pixel art shading**, value studies, and any application where balanced contrast is required.

## Requirements

- Python 3.x
- Pillow (optional – only needed for image export)

```bash
pip install Pillow

## Usage

### As a function

```python
from cielab_even_grayscale import lab_to_srgb_gray

# Generate a list of 8 grayscale values
grays = lab_to_srgb_gray(n_colors=8)
# Output: [0, 36, 68, 101, 137, 175, 214, 255]

# Generate a palette and also save it as a PNG image
lab_to_srgb_gray(n_colors=8, output_path="my_palette.png")
```

### Command line

Run the script directly:

```bash
python cielab_even_grayscale.py

## Output

- **List of integers**: sRGB grayscale values in the range 0–255  
  Example: `[0, 36, 68, 101, 137, 175, 214, 255]`

- **Image file** (if `output_path` is provided): A horizontal PNG strip of `n_colors` pixels (height 1), suitable for use as a pixel art palette reference.

## License

MIT License. See the [LICENSE](LICENSE) file for details.
