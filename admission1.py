"""
Image Processor Mini Project
"""

import numpy as np
from typing import Tuple, Optional


class ImageProcessor:
    """A modular class for basic image processing operations."""

    def __init__(self, image: np.ndarray):
        """
        Initialize with a 2D (grayscale) or 3D (color) image.
        """
        if image.ndim not in (2, 3):
            raise ValueError("Image must be 2D (grayscale) or 3D (color)")
        self.image = image.astype(np.float32)

    def get_shape(self) -> Tuple[int, ...]:
        """Return image dimensions."""
        return self.image.shape

    def normalize(self) -> np.ndarray:
        """Normalize pixel values to range [0, 1]."""
        min_val = np.min(self.image)
        max_val = np.max(self.image)
        if max_val == min_val:
            return np.zeros_like(self.image)
        return (self.image - min_val) / (max_val - min_val)

    def to_grayscale(self) -> np.ndarray:
        """Convert color image to grayscale."""
        if self.image.ndim == 2:
            return self.image
        return np.mean(self.image, axis=2)

    def flip_horizontal(self) -> np.ndarray:
        """Flip image horizontally."""
        return np.fliplr(self.image)

    def flip_vertical(self) -> np.ndarray:
        """Flip image vertically."""
        return np.flipud(self.image)

    def calculate_histogram(self) -> np.ndarray:
        """Calculate intensity histogram (for grayscale)."""
        gray = self.to_grayscale()
        hist, _ = np.histogram(gray.flatten(), bins=256, range=(0, 255))
        return hist

    def apply_threshold(self, threshold: float = 128.0) -> np.ndarray:
        """Simple binary thresholding."""
        gray = self.to_grayscale()
        return (gray > threshold).astype(np.float32) * 255


# Example usage
if __name__ == "__main__":
    # Create a sample 4x4 grayscale image
    sample_image = np.array([
        [50, 80, 120, 160],
        [60, 90, 130, 170],
        [70, 100, 140, 180],
        [80, 110, 150, 190]
    ], dtype=np.float32)

    processor = ImageProcessor(sample_image)

    print("Original shape:", processor.get_shape())
    print("Normalized image:\n", np.round(processor.normalize(), 3))
    print("Histogram (first 10 bins):", processor.calculate_histogram()[:10])
    print("Horizontally flipped:\n", processor.flip_horizontal())