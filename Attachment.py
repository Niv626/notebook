from abc import abstractmethod


class Attachment:
    max_size = 1500

    def __init__(self, media_type, size):
        assert size < self.max_size, (
            f"The length of the file must be less than {self.max_size}")
        self.media_type = media_type
        self.size = size

    @abstractmethod
    def display_media(self):
        pass


class Audio(Attachment):
    def __init__(self, media_type, size, duration):
        super().__init__(media_type, size)

        self.duration = duration

    def display_media(self):
        # do something
        pass


class Image(Attachment):
    def __init__(self, media_type, size, resolution):
        super().__init__(media_type, size)

        self.resolution = resolution

    def display_media(self):
        # do something
        pass
