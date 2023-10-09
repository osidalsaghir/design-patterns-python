# Subject interface
class Image:
    def display(self):
        pass

# Real subject
class RealImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self._load_image()

    def _load_image(self):
        print(f"Loading image from file: {self._filename}")

    def display(self):
        print(f"Displaying image: {self._filename}")

# Proxy
class ImageProxy(Image):
    def __init__(self, filename):
        self._filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()

# Client code
if __name__ == "__main__":
    # Creating a proxy to load and display the image
    image_proxy = ImageProxy("example.jpg")

    # The image is not loaded until display is called
    image_proxy.display()

    # Subsequent display calls use the already loaded image
    image_proxy.display()
