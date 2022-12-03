from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_max_file_size_mb(image, size):
    size_in_bytes = size * 1024 ** 2
    if image.size > size_in_bytes:
        raise ValidationError(f'Maximum file size is {size}MB')


@deconstructible
class MaxSizeValidator:
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb

    def __call__(self, obj):
        size_in_bytes = self.max_size_mb * 1024 ** 2
        if obj.size > size_in_bytes:
            raise ValidationError(f'Maximum file size is {self.max_size_mb}MB')
