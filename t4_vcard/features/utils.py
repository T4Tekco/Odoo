import base64
import io

from PIL import Image

__all__ = ["ImageExtractor"]


class ImageExtractor:
    """Helper for vCard"""

    def __init__(self, data: bytes = b""):
        self.__data = data

    def load(self, data: bytes):
        """data: Odoo b64 image"""
        self.__data = data

    def _extract(self):
        if not self.__data:
            raise ValueError("data is empty...")

        raw = base64.b64decode(self.__data)
        image_raw = io.BytesIO(raw)
        im = Image.open(image_raw, "r")
        format_type = im.format
        im.close()
        image_raw.close()

        return base64.b64encode(raw).decode(), format_type, "BASE64"

    def extract(self):
        b64_data, _format_type, encoding = self._extract()
        if not _format_type:
            raise ValueError("Can't determine format type...")

        return b64_data, _format_type, encoding
