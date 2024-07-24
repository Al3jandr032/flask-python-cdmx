from abc import ABC, abstractmethod
import io
from PIL import Image, ImageFilter

class ImageProcessor(ABC):
    """
    Abstract class for image processing with filter application.
    """

    @abstractmethod
    def load_image(self, image_path: str) -> None:
        """
        Load the image from the given path.
        """
        pass

    @abstractmethod
    def apply_filter(self, filter_type: str) -> None:
        """
        Apply the specified filter to the loaded image.
        """
        pass

    @abstractmethod
    def save_image(self, output_path: str) -> None:
        """
        Save the processed image to the specified output path.
        """
        pass


class PillowImageProcessor(ImageProcessor):
     
    def __init__(self) -> None:
          self.image = None
          self.format = 'JPEG'

    def load_image(self, image_path: str) -> None:
        self.image = Image.open(image_path)

    def apply_filter(self, filter_type: str) -> None:
        if filter_type == "blur":
            self.image = self.image.filter(ImageFilter.BLUR)
        elif filter_type == "grayscale":
            self.image = self.image.convert("L")
        elif filter_type == "kernel":
            self.image = self.image.filter(ImageFilter.Kernel(size=(3,3),kernel=(-1, -1, -1, -1, 11, -2, -2, -2, -2)))

    def save_image(self) -> bytes:
        buf = io.BytesIO()
        self.image.save(buf, format=self.format)
        return buf.getvalue()




def main():
    infile = "/Users/atomic/Desktop/steve-johnson-3Sf_G9m0gcQ-unsplash.jpg"
    outfile = '/Users/atomic/Desktop/processed_image.png'
    with Image.open(infile) as im:
            # Apply a filter (e.g., Gaussian blur)
            # filtered_image = im.filter(ImageFilter.GaussianBlur(radius=5))
            # Apply Kernel
            filtered_image = im.filter(ImageFilter.Kernel(size=(3,3),kernel=(-1, -1, -1, -1, 11, -2, -2, -2, -2)))
            filtered_image.save(outfile)

if __name__ == "__main__":
    main()

