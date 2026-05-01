# ========== USAGE INSTRUCTIONS ==========
# This script generates a list of sRGB grayscale values (0-255) from
# evenly spaced L* (CIELAB lightness) values.
#
# Basic usage:
#   grays = lab_to_srgb_gray(n_colors=8)
#   print(grays)  # e.g. [0, 36, 68, 101, 137, 175, 214, 255]
#
# To also export an image (requires Pillow):
#   lab_to_srgb_gray(n_colors=8, output_path="my_palette.png")
#   --> saves a 8×1 pixel horizontal grayscale ramp.
#
# You can change the number of colors and the output file name.
# If Pillow is not installed, only the grayscale list is printed.
# ========================================

def single_lab_to_gray(L):
    """
    Convert a single L* value (0-100) to an sRGB grayscale value (0-255)
    """

    if L > 8:
        Y = ((L + 16) / 116) ** 3
    else:
        Y = L / 903.3
    linear_rgb = Y
    if linear_rgb <= 0.0031308:
        srgb = 12.92 * linear_rgb
    else:
        srgb = 1.055 * (linear_rgb ** (1/2.4)) - 0.055
    gray_val = int(round(srgb * 255))
    return max(0, min(255, gray_val))

def lab_to_srgb_gray(n_colors=8, output_path=None):
    """
    Generate equidistant L* values, convert to sRGB grayscale values,
    and try to export as a horizontal color bar palette.
    Returns a list of grayscale values (0-255).
    """

    # Generate n_colors equidistant L* values (0 to 100)
    step = 100 / (n_colors - 1) if n_colors > 1 else 0
    L_values = [i * step for i in range(n_colors)]
    grays = [single_lab_to_gray(L) for L in L_values]

    print("Grayscale values (0-255):", grays)

    # ---- Image generation (only executed if needed and Pillow is available) ----
    if output_path:
        try:
            from PIL import Image
            n = len(grays)
            data = bytes(grays)
            img = Image.frombytes('L', (n, 1), data)
            img.save(output_path)
            print(f"Image saved as {output_path} (size: {n}×1 pixels)")
        except ImportError:
            print("PIL (Pillow) library not installed, cannot generate image. Please install Pillow and try again.")
        except Exception as e:
            print(f"Error generating image: {e}")

    return grays

if __name__ == "__main__":
    # Example: generate 8 gray levels and save as an image
    lab_to_srgb_gray(n_colors=8, output_path="cielab_even_grayscale_8.png")
