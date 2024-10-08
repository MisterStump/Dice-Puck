# -*- coding: utf-8 -*-
# Converted from UniversCondensed.ttf using:
#     font2bitmap.py UniversCondensed.ttf 32 -c 0x20-0x7f

MAP = (
    ' !\"#$%&\'()*+,-./0123456789:;<='
    '>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ['
    '\\]^_`abcdefghijklmnopqrstuvwxyz'
    '{|}~'
)

BPP = 1
HEIGHT = 32
MAX_WIDTH = 32
_WIDTHS = \
    b'\x07\x09\x0c\x0f\x0f\x15\x14\x07\x07\x07\x0f\x15\x07\x07\x07\x07'\
    b'\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x20\x15\x20\x0e'\
    b'\x15\x11\x10\x10\x11\x0e\x0d\x11\x11\x07\x0e\x10\x0c\x16\x11\x11'\
    b'\x0f\x11\x10\x10\x0f\x11\x0f\x16\x11\x0f\x0f\x07\x07\x07\x10\x10'\
    b'\x0f\x0d\x0d\x0c\x0d\x0d\x09\x0d\x0d\x06\x06\x0d\x06\x14\x0d\x0d'\
    b'\x0d\x0d\x09\x0c\x09\x0d\x0d\x15\x0c\x0d\x0b\x0e\x10\x0e\x20\x10'

OFFSET_WIDTH = 2
_OFFSETS = \
    b'\x00\x00\x00\xe0\x02\x00\x03\x80\x05\x60\x07\x40\x09\xe0\x0c\x60'\
    b'\x0d\x40\x0e\x20\x0f\x00\x10\xe0\x13\x80\x14\x60\x15\x40\x16\x20'\
    b'\x17\x00\x18\xe0\x1a\xc0\x1c\xa0\x1e\x80\x20\x60\x22\x40\x24\x20'\
    b'\x26\x00\x27\xe0\x29\xc0\x2a\xa0\x2b\x80\x2f\x80\x32\x20\x36\x20'\
    b'\x37\xe0\x3a\x80\x3c\xa0\x3e\xa0\x40\xa0\x42\xc0\x44\x80\x46\x20'\
    b'\x48\x40\x4a\x60\x4b\x40\x4d\x00\x4f\x00\x50\x80\x53\x40\x55\x60'\
    b'\x57\x80\x59\x60\x5b\x80\x5d\x80\x5f\x80\x61\x60\x63\x80\x65\x60'\
    b'\x68\x20\x6a\x40\x6c\x20\x6e\x00\x6e\xe0\x6f\xc0\x70\xa0\x72\xa0'\
    b'\x74\xa0\x76\x80\x78\x20\x79\xc0\x7b\x40\x7c\xe0\x7e\x80\x7f\xa0'\
    b'\x81\x40\x82\xe0\x83\xa0\x84\x60\x86\x00\x86\xc0\x89\x40\x8a\xe0'\
    b'\x8c\x80\x8e\x20\x8f\xc0\x90\xe0\x92\x60\x93\x80\x95\x20\x96\xc0'\
    b'\x99\x60\x9a\xe0\x9c\x80\x9d\xe0\x9f\xa0\xa1\xa0\xa3\x60\xa7\x60'

_BITMAPS =\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x03'\
    b'\x81\xc0\xe0\x70\x38\x1c\x0e\x07\x03\x81\xc0\xe0\x70\x38\x1c\x0e'\
    b'\x03\x00\x00\x00\xe0\x70\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x3b\x83\xb8\x31\x83\x18\x31\x83\x18\x31\x80\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x03\x18\x06\x30\x18\xc0\x31\x80\x63\x00\xc6\x03\x18\x1f'\
    b'\xfc\x3f\xf8\x18\xc0\x63\x00\xc6\x01\x8c\x03\x18\x0c\x60\x7f\xf0'\
    b'\xff\xe0\x63\x01\x8c\x03\x18\x06\x30\x0c\x60\x31\x80\x63\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x0e\x00\x1c\x00\x38\x00\x70\x01\xf8\x07\xf8\x1c\x70\x38\xe0\x71'\
    b'\xc0\x78\x00\x78\x00\x78\x00\x78\x00\x78\x1c\x70\x38\xe0\x71\xc0'\
    b'\x7f\x00\x7c\x00\x70\x00\xe0\x01\xc0\x03\x80\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x30\x0f\x81\x80'\
    b'\x6c\x0c\x07\x60\xc0\x3b\x86\x01\xdc\x20\x0e\xe3\x00\x77\x18\x03'\
    b'\xb1\x80\x0d\x8c\x00\x7c\x40\x03\xe6\x70\x00\x37\xc0\x03\x36\x00'\
    b'\x1b\xb0\x00\xd9\x80\x0c\xcc\x00\x66\x60\x02\x33\x00\x31\xd8\x01'\
    b'\x8e\xc0\x18\x3e\x00\xc1\xf0\x06\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x01\xf8\x00\x7f\xc0\x0f\x1e\x00\xe0\xe0\x0e\x0e\x00\xe0\xe0'\
    b'\x0f\x1c\x00\x73\xc0\x07\xf8\x00\x3e\x1c\x07\xc1\xc0\xfe\x1c\x1c'\
    b'\x71\xc3\xc7\x9c\x38\x3d\xc3\x81\xfc\x38\x0f\x83\x80\x78\x1c\x07'\
    b'\x81\xe1\xfc\x0f\xfd\xe0\x3f\x0f\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xc3'\
    b'\x87\x0e\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\xc3\x87\x0c\x18\x30'\
    b'\xe1\xc3\x87\x0e\x1c\x38\x70\xe1\xc3\x83\x06\x0c\x1c\x38\x30\x60'\
    b'\x00\x00\x00\x00\x00\x00\xc1\x83\x87\x06\x0c\x18\x38\x70\xe1\xc3'\
    b'\x87\x0e\x1c\x38\x70\xe1\x83\x06\x1c\x38\x60\xc0\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x12\x00\x66\x00\x78\x00\x60\x0f\xfc\x01\x80\x07'\
    b'\x80\x19\x80\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x01\x80\x00\x0c\x00\x00\x60\x00\x03\x00\x00\x18'\
    b'\x00\x1f\xfe\x00\xff\xf0\x00\x30\x00\x01\x80\x00\x0c\x00\x00\x60'\
    b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x01\xc7\x0e\x1c\x30\xe1\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x78\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0e\x1c\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x30\x60\xc1\x86\x0c\x18\x30\x60\xc1\x83'\
    b'\x04\x18\x30\x60\xc1\x83\x06\x0c\x30\x60\xc1\x80\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x1f\x80\xff\xc1\xc3\x87\x03\x8e\x07\x1c\x0e\x38'\
    b'\x1c\x70\x38\xe0\x71\xc0\xe3\x81\xc7\x03\x8e\x07\x1c\x0e\x38\x1c'\
    b'\x70\x38\xe0\x71\xc0\xe3\x83\xc3\x87\x03\xfc\x03\xf0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x07\x00\x1e\x00\xfc\x01\xf8\x02\x70\x00\xe0\x01\xc0\x03\x80\x07'\
    b'\x00\x0e\x00\x1c\x00\x38\x00\x70\x00\xe0\x01\xc0\x03\x80\x07\x00'\
    b'\x0e\x00\x1c\x00\x38\x00\x70\x00\xe0\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\xff\x83'\
    b'\xc7\x07\x07\x0e\x0e\x1c\x1c\x00\x38\x00\x70\x01\xc0\x03\x80\x0e'\
    b'\x00\x1c\x00\x70\x01\xe0\x03\x80\x0e\x00\x38\x00\xe0\x01\xc0\x07'\
    b'\x00\x0f\xfe\x1f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\xff\xc1\xc3\x87\x03\x8e'\
    b'\x07\x1c\x0e\x00\x1c\x00\x38\x00\xe0\x0f\xc0\x1f\x00\x07\x00\x07'\
    b'\x00\x0e\x00\x1c\x70\x38\xe0\x71\xc0\xe3\x83\xc3\x87\x03\xfc\x03'\
    b'\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x03\xc0\x0f\x80\x1f\x00\x7e\x00\xdc\x03\xb8\x06'\
    b'\x70\x1c\xe0\x31\xc0\xe3\x81\x87\x07\x0e\x0e\x1c\x38\x38\x70\x70'\
    b'\xff\xfd\xff\xf8\x03\x80\x07\x00\x0e\x00\x1c\x00\x38\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\xff\xc1\xff\x83\x80\x07\x00\x0e\x00\x1c\x00\x38\x00\x77\xc0\xff'\
    b'\xc1\xe3\xc3\x83\x87\x07\x00\x0e\x00\x1c\x00\x38\x00\x70\xe0\xe1'\
    b'\xc1\xc3\x83\x87\x8e\x07\xfc\x03\xe0\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x80\x7f\xc1'\
    b'\xc3\xc3\x83\x8e\x07\x1c\x0e\x38\x00\x70\x00\xef\xc1\xff\xc3\xc3'\
    b'\x87\x83\x8e\x07\x1c\x0e\x38\x1c\x70\x38\xe0\x71\xc0\xe3\x83\xc3'\
    b'\x87\x03\xfc\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xe1\xff\xc0\x03\x80\x07\x00'\
    b'\x0c\x00\x38\x00\x70\x01\xc0\x03\x80\x07\x00\x1c\x00\x38\x00\x70'\
    b'\x01\xc0\x03\x80\x0f\x00\x1c\x00\x38\x00\xf0\x01\xc0\x03\x80\x0f'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x1f\x80\x7f\xc1\xc3\x87\x03\x8e\x07\x1c\x0e\x38'\
    b'\x1c\x70\x38\x70\xe0\xff\x80\xff\x03\x87\x0f\x07\x1c\x0e\x38\x1c'\
    b'\x70\x38\xe0\x71\xc0\xe3\x81\xc3\x87\x03\xfc\x03\xf0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x1f\x80\x7f\x81\xc3\x87\x83\x8e\x07\x1c\x0e\x38\x1c\x70\x38\xe0'\
    b'\x71\xc0\xe3\x83\xc3\x87\x87\xf7\x07\xce\x00\x1c\x00\x38\xe0\x71'\
    b'\xc0\xe3\x83\x87\x87\x07\xfc\x03\xf0\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x70\xe1\xc0\x00\x00\x00\x00\x00\x00\x00\x07\x0e\x1c\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\xe1\xc0\x00'\
    b'\x00\x00\x00\x00\x00\x01\xc7\x0e\x1c\x30\xe1\x80\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x01\x80\x00\x00\x07\x80\x00\x00\x1f\x00\x00\x00\x7c\x00'\
    b'\x00\x01\xf0\x00\x00\x07\xc0\x00\x00\x1f\x00\x00\x00\x7c\x00\x00'\
    b'\x01\xf0\x00\x00\x03\xc0\x00\x00\x03\xc0\x00\x00\x01\xf0\x00\x00'\
    b'\x00\x7c\x00\x00\x00\x1f\x00\x00\x00\x07\xc0\x00\x00\x01\xf0\x00'\
    b'\x00\x00\x7c\x00\x00\x00\x1f\x00\x00\x00\x07\x80\x00\x00\x01\x80'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x03\xff\xc0\x1f\xfe\x00\x00\x00\x07\xff\x80\x3f\xfc\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x01\x80\x00\x00\x01\xe0\x00\x00\x00\xf8\x00\x00'\
    b'\x00\x3e\x00\x00\x00\x0f\x80\x00\x00\x03\xe0\x00\x00\x00\xf8\x00'\
    b'\x00\x00\x3e\x00\x00\x00\x0f\x80\x00\x00\x03\xc0\x00\x00\x03\xc0'\
    b'\x00\x00\x0f\x80\x00\x00\x3e\x00\x00\x00\xf8\x00\x00\x03\xe0\x00'\
    b'\x00\x0f\x80\x00\x00\x3e\x00\x00\x00\xf8\x00\x00\x01\xe0\x00\x00'\
    b'\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x07\xf8\x3c\xf0\xe1\xc3\x87'\
    b'\x0e\x1c\x00\x70\x01\xc0\x0e\x00\x38\x01\xc0\x0e\x00\x30\x00\xc0'\
    b'\x03\x00\x0c\x00\x30\x00\x00\x00\x00\x1c\x00\x70\x01\xc0\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x7f\x00\x0f\xfe\x00\xf0\x7c\x0e\x00\xe0\x70\x07\x87\x00'\
    b'\x1c\x38\x00\xe1\xc7\x77\x0e\x7f\xb8\x77\x9d\xc3\xb8\xee\x1d\xc7'\
    b'\x70\xee\x3b\x87\x71\xdc\x3b\x8e\xe1\xdc\x77\x0e\xe3\xb8\x77\x1d'\
    b'\xc3\x9f\x7e\x1c\x79\xe0\xe0\x00\x07\x80\x00\x1c\x00\x00\xf8\x10'\
    b'\x03\xff\x80\x07\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\xf0\x00\x78\x00\x7e\x00\x3f\x00\x1f\x80\x0d'\
    b'\xc0\x06\x60\x07\x38\x03\x9c\x01\xce\x00\xc7\x00\xe1\xc0\x70\xe0'\
    b'\x38\x70\x1c\x38\x1f\xfe\x0f\xff\x07\x03\x83\x81\xc1\x80\xe1\xc0'\
    b'\x78\xe0\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xc0\x3f\xf0\x38\x70\x38\x38'\
    b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x70\x3f\xe0\x3f\xf0\x38\x78'\
    b'\x38\x38\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x3c\x38\x38'\
    b'\x3f\xf8\x3f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x0f\xf8\x1c\x38\x38\x1c'\
    b'\x38\x1c\x38\x1c\x38\x1c\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
    b'\x38\x00\x38\x00\x38\x00\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x1c\x38'\
    b'\x1f\xf8\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x07\xff\x03\x83\xc1\xc0'\
    b'\xf0\xe0\x38\x70\x1c\x38\x0e\x1c\x07\x0e\x03\x87\x01\xc3\x80\xe1'\
    b'\xc0\x70\xe0\x38\x70\x1c\x38\x0e\x1c\x07\x0e\x03\x87\x01\xc3\x81'\
    b'\xe1\xc1\xe0\xff\xf0\x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\x0f\xfc\x38'\
    b'\x00\xe0\x03\x80\x0e\x00\x38\x00\xe0\x03\x80\x0f\xf8\x3f\xe0\xe0'\
    b'\x03\x80\x0e\x00\x38\x00\xe0\x03\x80\x0e\x00\x38\x00\xe0\x03\xff'\
    b'\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x0f\xfc\x7f\xe3\x80\x1c\x00\xe0\x07\x00\x38\x01\xc0'\
    b'\x0e\x00\x7f\xe3\xff\x1c\x00\xe0\x07\x00\x38\x01\xc0\x0e\x00\x70'\
    b'\x03\x80\x1c\x00\xe0\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xfc\x01\xff\x81\xe1\xc1\xe0'\
    b'\x70\xe0\x38\x70\x1c\x38\x00\x1c\x00\x0e\x00\x07\x00\x03\x87\xe1'\
    b'\xc3\xf0\xe0\x38\x70\x1c\x38\x0e\x1c\x07\x0e\x03\x87\x01\xc3\x80'\
    b'\xe0\xe0\xf0\x7f\xf8\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x07\x07\x03'\
    b'\x83\x81\xc1\xc0\xe0\xe0\x70\x70\x38\x38\x1c\x1c\x0e\x0e\x07\x07'\
    b'\xff\x83\xff\xc1\xc0\xe0\xe0\x70\x70\x38\x38\x1c\x1c\x0e\x0e\x07'\
    b'\x07\x03\x83\x81\xc1\xc0\xe0\xe0\x70\x70\x38\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1\xc3'\
    b'\x87\x0e\x1c\x38\x70\xe1\xc3\x87\x0e\x1c\x38\x70\xe1\xc3\x87\x0e'\
    b'\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x1c\x00'\
    b'\x70\x01\xc0\x07\x00\x1c\x00\x70\x01\xc0\x07\x00\x1c\x00\x70\x01'\
    b'\xc0\x07\x00\x1c\x00\x71\xc1\xc7\x07\x1c\x1c\x70\x70\xe3\x83\xfe'\
    b'\x03\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x38\x1e\x38\x1c\x38\x38\x38\x78\x38\x70\x38\xe0'\
    b'\x39\xe0\x39\xc0\x3b\x80\x3f\x80\x3f\x80\x3b\x80\x3b\xc0\x39\xc0'\
    b'\x39\xe0\x38\xe0\x38\x70\x38\x70\x38\x38\x38\x3c\x38\x1c\x38\x1e'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38'\
    b'\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03\x80\x38\x03'\
    b'\x80\x3f\xe3\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x03\xe0\x0f\x8f\x80\x3e\x3f\x01\xf8\xfc\x07'\
    b'\xe3\xf0\x1f\x8e\xc0\x6e\x3b\x83\xb8\xee\x0e\xe3\xb8\x3b\x8e\x60'\
    b'\xce\x39\xc7\x38\xe7\x1c\xe3\x9c\x73\x8e\x33\x8e\x38\xee\x38\xe3'\
    b'\xb8\xe3\x86\xc3\x8e\x1f\x0e\x38\x7c\x38\xe1\xf0\xe3\x83\x83\x8e'\
    b'\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x83\x87\xc1'\
    b'\xc3\xf0\xe1\xf8\x70\xfc\x38\x76\x1c\x3b\x8e\x1d\xc7\x0e\xe3\x87'\
    b'\x31\xc3\x9c\xe1\xce\x70\xe3\x38\x71\x9c\x38\xee\x1c\x77\x0e\x1b'\
    b'\x87\x0f\xc3\x87\xe1\xc3\xf0\xe0\xf8\x70\x7c\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\xf8\x01\xff\x01\xe1\xc1\xe0\xf0\xe0\x38\x70\x1c\x38\x0e\x1c'\
    b'\x07\x0e\x03\x87\x01\xc3\x80\xe1\xc0\x70\xe0\x38\x70\x1c\x38\x0e'\
    b'\x1c\x07\x0e\x03\x87\x01\xc3\xc1\xe0\xf1\xe0\x7f\xe0\x0f\xe0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\xff\x81\xff\xc3\x83\x87\x03\x8e\x07\x1c\x0e\x38'\
    b'\x1c\x70\x38\xe0\x71\xc1\xc3\xff\x07\xfc\x0e\x00\x1c\x00\x38\x00'\
    b'\x70\x00\xe0\x01\xc0\x03\x80\x07\x00\x0e\x00\x1c\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x01\xfc\x01\xff\x01\xc3\xc1\xc0\xf0\xe0\x38\x70\x1c\x38\x0e\x1c'\
    b'\x07\x0e\x03\x87\x01\xc3\x80\xe1\xc0\x70\xe0\x38\x70\x1c\x38\x0e'\
    b'\x1c\x07\x0e\x03\x87\x01\xc3\x81\xc0\xe1\xe0\x7f\xfe\x0f\xff\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x3f\xf0\x3f\xf8\x38\x38\x38\x1c\x38\x1c\x38\x1c'\
    b'\x38\x1c\x38\x1c\x38\x1c\x38\x38\x3f\xf0\x3f\xf0\x38\x78\x38\x38'\
    b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x1c\x38\x1c'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x07\xe0\x1f\xf8\x1c\x38\x38\x1c\x38\x1c\x38\x1c'\
    b'\x38\x1c\x3c\x00\x1e\x00\x1f\x80\x07\xe0\x03\xf0\x00\xf8\x00\x3c'\
    b'\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x1c\x38\x1f\xf0\x07\xe0'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x01\xff\xf3\xff\xe0\x38\x00\x70\x00\xe0\x01\xc0\x03'\
    b'\x80\x07\x00\x0e\x00\x1c\x00\x38\x00\x70\x00\xe0\x01\xc0\x03\x80'\
    b'\x07\x00\x0e\x00\x1c\x00\x38\x00\x70\x00\xe0\x01\xc0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x0e\x07\x07\x03\x83\x81\xc1\xc0\xe0\xe0\x70\x70\x38\x38\x1c\x1c'\
    b'\x0e\x0e\x07\x07\x03\x83\x81\xc1\xc0\xe0\xe0\x70\x70\x38\x38\x1c'\
    b'\x1c\x0e\x0e\x07\x07\x03\x83\x83\xc0\xe1\xc0\x7f\xc0\x0f\xc0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x01\xc0\x3b\x80\x73\x80\xc7\x03\x8e\x07\x1c\x0e\x3c'\
    b'\x1c\x38\x30\x70\xe0\xe1\xc1\xc3\x81\xc6\x03\x8c\x07\x38\x0e\x70'\
    b'\x0c\xc0\x1d\x80\x3b\x00\x7e\x00\xfc\x00\xf0\x01\xe0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x07\x07\x83\x9c\x1e\x0e\x70\x78\x38\xc3\xf0\xc3\x8f\xc7\x0e'\
    b'\x3f\x1c\x38\xcc\x70\xe3\x31\xc1\x8c\xc6\x06\x33\x18\x1d\xce\xe0'\
    b'\x77\x3b\x81\xd8\x6e\x07\x61\xb8\x0d\x86\xc0\x36\x1b\x00\xf8\x7c'\
    b'\x03\xe1\xf0\x0f\x87\xc0\x1c\x0e\x00\x70\x38\x01\xc0\xe0\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x03\x83\x83\x81\xc1\xc0\x71'\
    b'\xc0\x38\xe0\x1c\xe0\x07\x70\x03\xb0\x00\xf8\x00\x7c\x00\x1c\x00'\
    b'\x1e\x00\x0f\x80\x0f\xc0\x07\x70\x07\x38\x03\x8e\x03\x87\x01\xc3'\
    b'\x81\xc0\xe0\xe0\x70\xe0\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x71\xc1\xc3'\
    b'\x83\x87\x87\x07\x1c\x0e\x38\x1e\x70\x1d\xc0\x3b\x80\x36\x00\x7c'\
    b'\x00\xf8\x00\xe0\x01\xc0\x03\x80\x07\x00\x0e\x00\x1c\x00\x38\x00'\
    b'\x70\x00\xe0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x01\xff\xe3\xff\xc0\x03\x80\x0f\x00'\
    b'\x1c\x00\x78\x00\xe0\x03\xc0\x07\x00\x1e\x00\x38\x00\xe0\x01\xc0'\
    b'\x07\x00\x1e\x00\x38\x00\xf0\x01\xc0\x07\x80\x0e\x00\x1f\xfe\x3f'\
    b'\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x01\xe3\x06\x0c\x18\x30\x60\xc1\x83\x06\x0c\x18\x30\x60\xc1'\
    b'\x83\x06\x0c\x18\x30\x60\xc1\xe0\x00\x00\x00\x00\x00\x01\x83\x06'\
    b'\x0c\x0c\x18\x30\x60\xc1\x83\x06\x04\x0c\x18\x30\x60\xc1\x83\x06'\
    b'\x06\x0c\x18\x30\x00\x00\x00\x00\x00\x00\xf0\x60\xc1\x83\x06\x0c'\
    b'\x18\x30\x60\xc1\x83\x06\x0c\x18\x30\x60\xc1\x83\x06\x0c\x18\xf0'\
    b'\x00\x00\x00\x00\x01\x80\x03\xc0\x03\xc0\x07\xe0\x0e\x70\x1c\x38'\
    b'\x38\x1c\x60\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x3c\x00\x38\x00\x70\x00\x70\x00'\
    b'\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e'\
    b'\x07\xf8\x79\xe3\x87\x1c\x38\x01\xc0\xfe\x1f\xf1\xe3\x8e\x1c\x70'\
    b'\xe3\x87\x1c\x78\xff\xc1\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x70\x03\x80\x1c\x00\xe0\x07'\
    b'\x00\x38\x01\xde\x0f\xf8\x79\xe3\x87\x1c\x38\xe1\xc7\x0e\x38\x71'\
    b'\xc3\x8e\x1c\x70\xe3\x87\x1e\x78\xff\x87\x78\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\xfc\x1f\xe3\xcf\x38\x73\x87\x38\x03\x80'\
    b'\x38\x03\x80\x38\x03\x87\x38\x73\xcf\x1f\xe0\xfc\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\xe0\x07'\
    b'\x00\x38\x01\xc0\x0e\x00\x70\x7b\x87\xfc\x78\xe3\x87\x1c\x38\xe1'\
    b'\xc7\x0e\x38\x71\xc3\x8e\x1c\x70\xe3\x87\x1c\x78\x7f\xc1\xce\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x0f\xf0\xf3\xc7'\
    b'\x0e\x38\x71\xc3\x8f\xfc\x7f\xe3\x80\x1c\x00\xe1\xc7\x0e\x3c\xf0'\
    b'\xff\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x03\xe3\xf1\xe0\xe0\x70\x38\x1c\x3f\xdf\xe3\x81\xc0\xe0'\
    b'\x70\x38\x1c\x0e\x07\x03\x81\xc0\xe0\x70\x38\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\xf7\x0f\xf8\xf3\xc7\x0e\x38\x71\xc3\x8e\x1c\x70\xe3'\
    b'\x87\x1c\x38\xe1\xc7\x0e\x3c\xf0\xff\x83\xdc\x00\xe3\x07\x18\x38'\
    b'\xe3\xc3\xfc\x0f\x80\x00\x00\x00\x00\x00\x00\x0e\x00\x70\x03\x80'\
    b'\x1c\x00\xe0\x07\x00\x38\x01\xcf\x0f\xf8\x79\xe3\x87\x1c\x38\xe1'\
    b'\xc7\x0e\x38\x71\xc3\x8e\x1c\x70\xe3\x87\x1c\x38\xe1\xc7\x0e\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x8e\x38'\
    b'\x00\x00\x00\xe3\x8e\x38\xe3\x8e\x38\xe3\x8e\x38\xe3\x8e\x00\x00'\
    b'\x00\x00\x00\x00\x00\x03\x8e\x38\x00\x00\x00\xe3\x8e\x38\xe3\x8e'\
    b'\x38\xe3\x8e\x38\xe3\x8e\x38\xe3\x8e\xfb\xc0\x00\x00\x00\x00\x0e'\
    b'\x00\x70\x03\x80\x1c\x00\xe0\x07\x00\x38\x01\xc3\x8e\x38\x73\xc3'\
    b'\x9c\x1d\xc0\xee\x07\xe0\x3f\x01\xdc\x0e\xe0\x73\x83\x9c\x1c\x70'\
    b'\xe3\x87\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x03\x8e\x38\xe3\x8e\x38\xe3\x8e\x38\xe3\x8e\x38\xe3\x8e\x38'\
    b'\xe3\x8e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x3c'\
    b'\x70\x7f\xff\x87\x9f\x3c\x70\xe1\xc7\x0e\x1c\x70\xe1\xc7\x0e\x1c'\
    b'\x70\xe1\xc7\x0e\x1c\x70\xe1\xc7\x0e\x1c\x70\xe1\xc7\x0e\x1c\x70'\
    b'\xe1\xc7\x0e\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x01\xde\x0f\xfc\x79\xe3\x87\x1c\x38\xe1'\
    b'\xc7\x0e\x38\x71\xc3\x8e\x1c\x70\xe3\x87\x1c\x38\xe1\xc7\x0e\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x07\xf8\x79\xc3'\
    b'\x87\x1c\x38\xe1\xc7\x0e\x38\x71\xc3\x8e\x1c\x70\xe3\x87\x1e\x78'\
    b'\x7f\x81\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xde'\
    b'\x0f\xf8\x79\xe3\x87\x1c\x38\xe1\xc7\x0e\x38\x71\xc3\x8e\x1c\x70'\
    b'\xe3\x87\x1e\x78\xff\x87\x78\x38\x01\xc0\x0e\x00\x70\x03\x80\x1c'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\xe7\x0f\xf8\xf3\xc7\x0e\x38\x71\xc3\x8e\x1c\x70\xe3'\
    b'\x87\x1c\x38\xe1\xc7\x0e\x3c\xf0\xff\x83\xdc\x00\xe0\x07\x00\x38'\
    b'\x01\xc0\x0e\x00\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x1c\xcf\xe7\xf3\xc1\xc0\xe0\x70\x38\x1c\x0e\x07\x03\x81'\
    b'\xc0\xe0\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x1f\xc3\x8e\x38\xe3'\
    b'\x8e\x3c\x01\xf0\x07\x80\x3c\x01\xe3\x8e\x38\xe3\x8e\x1f\xc0\xf8'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x60\x70\x38\x1c\x3f\x9f\xc3\x81\xc0\xe0\x70\x38\x1c\x0e'\
    b'\x07\x03\x81\xc0\xe0\x7c\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc3'\
    b'\x8e\x1c\x70\xe3\x87\x1c\x38\xe1\xc7\x0e\x38\x71\xc3\x8e\x1c\x70'\
    b'\xe3\x87\x1c\x78\xff\xc1\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x03\x81\xdc\x0e\x70\xe3\x87\x1c\x38\xe1\xc3\x0c\x1c\xe0'\
    b'\xe7\x03\x30\x19\x80\xfc\x07\xe0\x1e\x00\xf0\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'\
    b'\x87\x87\x1c\x3c\x38\x61\xe1\xc3\x1f\x8c\x1c\xfc\x60\xe6\xe7\x07'\
    b'\x33\x38\x19\x99\xc0\xcc\xcc\x07\x67\x60\x3f\x3b\x01\xf9\xf8\x07'\
    b'\x87\xc0\x3c\x3c\x01\xe1\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0e\x38\xc3\x9c\x1d\x81'\
    b'\xf8\x0f\x80\xf0\x06\x00\xf0\x0f\x01\xf8\x19\x83\x9c\x39\xc7\x0e'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x81\xdc\x0e\x60\x63'\
    b'\x87\x1c\x38\xe1\x83\x1c\x1c\xe0\xe6\x03\x30\x1b\x80\xfc\x07\xc0'\
    b'\x1e\x00\xf0\x07\x00\x38\x01\xc0\x0c\x00\xe0\x07\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf1\xfe\x01'\
    b'\xc0\x70\x0e\x03\x80\x70\x0c\x03\x80\x60\x1c\x03\x00\xe0\x1f\xe3'\
    b'\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0'\
    b'\x1f\x00\x70\x03\x80\x0e\x00\x38\x00\xe0\x03\x80\x0e\x00\x38\x00'\
    b'\xe0\x03\x80\x0e\x00\xf0\x07\x80\x1e\x00\x3c\x00\x78\x00\xe0\x03'\
    b'\x80\x0e\x00\x38\x00\xe0\x03\x80\x0e\x00\x38\x00\xe0\x03\x80\x07'\
    b'\x00\x1f\x00\x3c\x00\x00\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
    b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
    b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
    b'\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'\
    b'\x01\x80\x01\x80\x00\x00\xe0\x03\xe0\x03\xc0\x07\x00\x1c\x00\x70'\
    b'\x01\xc0\x07\x00\x1c\x00\x70\x01\xc0\x07\x00\x0e\x00\x3c\x00\x78'\
    b'\x01\xe0\x0f\x00\x38\x01\xc0\x07\x00\x1c\x00\x70\x01\xc0\x07\x00'\
    b'\x1c\x00\x70\x01\xc0\x07\x00\x3c\x03\xe0\x0f\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x7e\x00\x80\x01\xff\xc1\xc0\x03\xc1\xff\x80\x01\x00\x3e\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x7f\xfe\x7f\xfe\x7f\xfe\x7f\xfe\x78\x1e\x78\x1e\x78\x1e\x78\x1e'\
    b'\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e\x78\x1e'\
    b'\x78\x1e\x78\x1e\x7f\xfe\x7f\xfe\x7f\xfe\x7f\xfe\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

WIDTHS = memoryview(_WIDTHS)
OFFSETS = memoryview(_OFFSETS)
BITMAPS = memoryview(_BITMAPS)

