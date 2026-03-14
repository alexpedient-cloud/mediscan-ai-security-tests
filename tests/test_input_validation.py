import pytest
import numpy as np

def validate_image(image):

    if image is None:
        raise ValueError("Image cannot be None")

    if len(image.shape) != 3:
        raise ValueError("Invalid image dimensions")

    if image.max() > 255 or image.min() < 0:
        raise ValueError("Pixel values out of range")

    return True


def test_malformed_image_dimensions():

    malformed = np.array([1,2,3])

    with pytest.raises(ValueError):
        validate_image(malformed)


def test_corrupt_image():

    corrupt = None

    with pytest.raises(ValueError):
        validate_image(corrupt)


def test_extreme_pixel_values():

    extreme = np.array([[[500]]])

    with pytest.raises(ValueError):
        validate_image(extreme)