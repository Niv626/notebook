from formats import image_prefix, audio_prefix


class Attachment:
    max_size = 1500

    def __init__(self, path, size):
        assert size < self.max_size, f"The length of the file must be less than {self.max_size}"
        self.path = path
        self.file_format = self.is_supported()
        self.size = size

    def is_supported(self):
        formatted = self.path.split('/')[-1]
        if not formatted.lower().endswith(image_prefix + audio_prefix):
            raise ValueError(f"file type {formatted} is not supported.\n "
                             f"supported format: {image_prefix + audio_prefix}")

    def display_media(self):
        pass


class Audio(Attachment):
    def __init__(self, media_type, size, duration):
        super().__init__(media_type, size)
        self.duration = duration

    # TODO: add function that check if duration is valid

    def display_media(self):
        # do something
        pass


class Image(Attachment):
    def __init__(self, media_type, size, resolution):
        super().__init__(media_type, size)
        self.resolution = resolution

    # TODO: add function that check if resolution is valid

    def display_media(self):
        # do something
        pass
