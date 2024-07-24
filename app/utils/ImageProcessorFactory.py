

from app.utils.ImageFilter import ImageProcessor, PillowImageProcessor


class ImageProcessorFactory:
    @staticmethod
    def create_processor(processor_type: str) -> ImageProcessor:
        if processor_type == "PIL":
            return PillowImageProcessor()
        # Puedes agregar más tipos de procesadores según tus necesidades
        else:
            raise ValueError("Tipo de procesador no válido")
        
    @staticmethod
    def get_filters():
        return ["blur","grayscale","kernel"]