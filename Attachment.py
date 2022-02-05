from formats import image_prefix, audio_prefix
from PIL import Image as pImage
from setup_logger import logger
from  playsound import playsound
import datetime
import wave
import contextlib
import os


class Attachment:
    max_file_size = 50000000  # 50 mb

    def __init__(self, path, size=None):
        self.path = path
        self._size = self.validate_size(size)

    def validate_size(self, size):
        if not size:
            logger.info(f'getting size from {self.path}')
            size = os.path.getsize(self.path)
        if not 0 < size < self.max_file_size:
            raise Exception(f"The length of the file must be less than {self.max_file_size}, "
                            f"and greater than zero")
        return size

    def get_size(self):
        return self._size

    @staticmethod
    def valid_file_format(formats, f_type):
        if not f_type.lower().endswith(formats):
            raise ValueError(f"file type {f_type} is not supported.\n "
                             f"supported format/s: {formats}")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        format_type = value.split('/')[-1]
        if isinstance(self, Image):
            self.valid_file_format(image_prefix, format_type)
        elif isinstance(self, Audio):
            self.valid_file_format(audio_prefix, format_type)
        else:
            raise Exception(f'{self} is not valid child instance of {super()}')
        self._path = value


class Audio(Attachment):
    min_duration = 0.5
    max_duration = 480 # 480sec = 8min

    def __init__(self, path, size=None, duration=None):
        super().__init__(path, size)
        self._duration = self.validate_duration(duration)

    def validate_duration(self, duration):
        if not duration:
            duration = self.get_duration_from_path()
        if not self.min_duration < duration < self.max_duration:
            raise Exception(f"duration must be smaller than {self.max_duration}"
                            f" or bigger than {self.min_duration}")
        return str(datetime.timedelta(seconds=duration))

    def get_duration_from_path(self):
        print('getting audio duration from on local path')
        try:
            with contextlib.closing(wave.open(self.path, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                return frames / float(rate)
        except Exception as e:
            print(e)

    def get_duration(self):
        return self._duration

    def play_media(self):
        try:
            p = playsound(self.path)
        except Exception as e:
            print(f'Exception info {e} \n It may caused by invalid path')


class Image(Attachment):
    def __init__(self, path, size=None, resolution=None):
        super().__init__(path, size)
        self._resolution = self.set_resolution(resolution)

    @staticmethod
    def valid_resolution(res):
        width, height = res.split('X')
        if not int(width) > 0 and int(height) > 0:
            raise ValueError('width and height size mist be greater then 0')
        return res

    def set_resolution(self, res):
        if res:
            return self.valid_resolution(res)
        else:
            try:
                with pImage.open(self.path, mode='r') as im:
                    logger.info('get the resolution from local path')
                    width, height = im.size
            except Exception as e:
                print(e)
                return
            return self.valid_resolution(f"{width}X{height}")

    def get_resolution(self):
        return self._resolution

    def play_media(self):
        try:
            with pImage.open(self.path) as im:
                im.show()
        except Exception as e:
            print(e)







