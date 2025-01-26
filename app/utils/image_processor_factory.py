from app.utils.image_filter import ImageProcessor, PillowImageProcessor


class ImageProcessorFactory:
    """
    Image Processor Factory
    Creates an instance of ImageProcessor class
    that implements its abstract methods

    @abstractmethod
    def load_image(self, image_path: str) -> None:

    @abstractmethod
    def apply_filter(self, filter_type: str) -> None:

    @abstractmethod
    def save_image(self, output_path: str) -> None:

    """

    @staticmethod
    def create_processor(processor_type: str) -> ImageProcessor:
        if processor_type == "PIL":
            return PillowImageProcessor()
        raise ValueError("Tipo de procesador no válido")

    @staticmethod
    def get_filters():
        return ["blur", "grayscale", "kernel"]
