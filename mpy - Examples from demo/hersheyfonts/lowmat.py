WIDTH = 78
HEIGHT = 78
FIRST = 0x20
LAST = 0x7f

_font =\
b'\x00\x4a\x5a\x08\x46\x5e\x52\x4a\x52\x5b\x20\x52\x4a\x52\x5a'\
b'\x52\x20\x52\x4a\x5b\x5a\x5b\x08\x46\x5e\x52\x4a\x52\x5b\x20'\
b'\x52\x4a\x4a\x5a\x4a\x20\x52\x4a\x52\x5a\x52\x05\x47\x5d\x4b'\
b'\x4b\x59\x59\x20\x52\x59\x4b\x4b\x59\x05\x50\x55\x52\x51\x52'\
b'\x52\x53\x52\x53\x51\x52\x51\x1f\x46\x5e\x5b\x46\x49\x5b\x20'\
b'\x52\x4e\x46\x50\x48\x50\x4a\x4f\x4c\x4d\x4d\x4b\x4d\x49\x4b'\
b'\x49\x49\x4a\x47\x4c\x46\x4e\x46\x50\x47\x53\x48\x56\x48\x59'\
b'\x47\x5b\x46\x20\x52\x57\x54\x55\x55\x54\x57\x54\x59\x56\x5b'\
b'\x58\x5b\x5a\x5a\x5b\x58\x5b\x56\x59\x54\x57\x54\x09\x46\x5e'\
b'\x5a\x46\x4a\x4d\x5a\x54\x20\x52\x4a\x56\x5a\x56\x20\x52\x4a'\
b'\x5b\x5a\x5b\x09\x46\x5e\x4a\x46\x5a\x4d\x4a\x54\x20\x52\x4a'\
b'\x56\x5a\x56\x20\x52\x4a\x5b\x5a\x5b\x13\x4b\x59\x56\x42\x54'\
b'\x44\x52\x47\x50\x4b\x4f\x50\x4f\x54\x50\x59\x52\x5d\x54\x60'\
b'\x56\x62\x20\x52\x54\x44\x52\x48\x51\x4b\x50\x50\x50\x54\x51'\
b'\x59\x52\x5c\x54\x60\x13\x4b\x59\x4e\x42\x50\x44\x52\x47\x54'\
b'\x4b\x55\x50\x55\x54\x54\x59\x52\x5d\x50\x60\x4e\x62\x20\x52'\
b'\x50\x44\x52\x48\x53\x4b\x54\x50\x54\x54\x53\x59\x52\x5c\x50'\
b'\x60\x08\x4a\x5a\x52\x4c\x52\x58\x20\x52\x4d\x4f\x57\x55\x20'\
b'\x52\x57\x4f\x4d\x55\x05\x45\x5f\x52\x49\x52\x5b\x20\x52\x49'\
b'\x52\x5b\x52\x07\x4e\x56\x53\x57\x52\x58\x51\x57\x52\x56\x53'\
b'\x57\x53\x59\x51\x5b\x02\x45\x5f\x49\x52\x5b\x52\x05\x4e\x56'\
b'\x52\x56\x51\x57\x52\x58\x53\x57\x52\x56\x02\x47\x5d\x5b\x42'\
b'\x49\x62\x11\x48\x5c\x51\x46\x4e\x47\x4c\x4a\x4b\x4f\x4b\x52'\
b'\x4c\x57\x4e\x5a\x51\x5b\x53\x5b\x56\x5a\x58\x57\x59\x52\x59'\
b'\x4f\x58\x4a\x56\x47\x53\x46\x51\x46\x04\x48\x5c\x4e\x4a\x50'\
b'\x49\x53\x46\x53\x5b\x0e\x48\x5c\x4c\x4b\x4c\x4a\x4d\x48\x4e'\
b'\x47\x50\x46\x54\x46\x56\x47\x57\x48\x58\x4a\x58\x4c\x57\x4e'\
b'\x55\x51\x4b\x5b\x59\x5b\x0f\x48\x5c\x4d\x46\x58\x46\x52\x4e'\
b'\x55\x4e\x57\x4f\x58\x50\x59\x53\x59\x55\x58\x58\x56\x5a\x53'\
b'\x5b\x50\x5b\x4d\x5a\x4c\x59\x4b\x57\x06\x48\x5c\x55\x46\x4b'\
b'\x54\x5a\x54\x20\x52\x55\x46\x55\x5b\x11\x48\x5c\x57\x46\x4d'\
b'\x46\x4c\x4f\x4d\x4e\x50\x4d\x53\x4d\x56\x4e\x58\x50\x59\x53'\
b'\x59\x55\x58\x58\x56\x5a\x53\x5b\x50\x5b\x4d\x5a\x4c\x59\x4b'\
b'\x57\x17\x48\x5c\x58\x49\x57\x47\x54\x46\x52\x46\x4f\x47\x4d'\
b'\x4a\x4c\x4f\x4c\x54\x4d\x58\x4f\x5a\x52\x5b\x53\x5b\x56\x5a'\
b'\x58\x58\x59\x55\x59\x54\x58\x51\x56\x4f\x53\x4e\x52\x4e\x4f'\
b'\x4f\x4d\x51\x4c\x54\x05\x48\x5c\x59\x46\x4f\x5b\x20\x52\x4b'\
b'\x46\x59\x46\x1d\x48\x5c\x50\x46\x4d\x47\x4c\x49\x4c\x4b\x4d'\
b'\x4d\x4f\x4e\x53\x4f\x56\x50\x58\x52\x59\x54\x59\x57\x58\x59'\
b'\x57\x5a\x54\x5b\x50\x5b\x4d\x5a\x4c\x59\x4b\x57\x4b\x54\x4c'\
b'\x52\x4e\x50\x51\x4f\x55\x4e\x57\x4d\x58\x4b\x58\x49\x57\x47'\
b'\x54\x46\x50\x46\x17\x48\x5c\x58\x4d\x57\x50\x55\x52\x52\x53'\
b'\x51\x53\x4e\x52\x4c\x50\x4b\x4d\x4b\x4c\x4c\x49\x4e\x47\x51'\
b'\x46\x52\x46\x55\x47\x57\x49\x58\x4d\x58\x52\x57\x57\x55\x5a'\
b'\x52\x5b\x50\x5b\x4d\x5a\x4c\x58\x14\x41\x63\x48\x42\x48\x62'\
b'\x20\x52\x49\x42\x49\x62\x20\x52\x5b\x42\x5b\x62\x20\x52\x5c'\
b'\x42\x5c\x62\x20\x52\x44\x42\x60\x42\x20\x52\x44\x62\x4d\x62'\
b'\x20\x52\x57\x62\x60\x62\x16\x42\x61\x47\x42\x51\x50\x46\x62'\
b'\x20\x52\x46\x42\x50\x50\x20\x52\x45\x42\x50\x51\x20\x52\x45'\
b'\x42\x5c\x42\x5e\x49\x5b\x42\x20\x52\x47\x61\x5c\x61\x20\x52'\
b'\x46\x62\x5c\x62\x5e\x5b\x5b\x62\x03\x46\x5e\x5a\x49\x4a\x52'\
b'\x5a\x5b\x05\x45\x5f\x49\x4f\x5b\x4f\x20\x52\x49\x55\x5b\x55'\
b'\x03\x46\x5e\x4a\x49\x5a\x52\x4a\x5b\x08\x45\x5f\x59\x49\x4b'\
b'\x5b\x20\x52\x49\x4f\x5b\x4f\x20\x52\x49\x55\x5b\x55\x08\x45'\
b'\x5f\x49\x4d\x5b\x4d\x20\x52\x49\x52\x5b\x52\x20\x52\x49\x57'\
b'\x5b\x57\x11\x49\x5c\x58\x4d\x58\x5b\x20\x52\x58\x50\x56\x4e'\
b'\x54\x4d\x51\x4d\x4f\x4e\x4d\x50\x4c\x53\x4c\x55\x4d\x58\x4f'\
b'\x5a\x51\x5b\x54\x5b\x56\x5a\x58\x58\x11\x48\x5b\x4c\x46\x4c'\
b'\x5b\x20\x52\x4c\x50\x4e\x4e\x50\x4d\x53\x4d\x55\x4e\x57\x50'\
b'\x58\x53\x58\x55\x57\x58\x55\x5a\x53\x5b\x50\x5b\x4e\x5a\x4c'\
b'\x58\x0e\x49\x5b\x58\x50\x56\x4e\x54\x4d\x51\x4d\x4f\x4e\x4d'\
b'\x50\x4c\x53\x4c\x55\x4d\x58\x4f\x5a\x51\x5b\x54\x5b\x56\x5a'\
b'\x58\x58\x11\x49\x5c\x58\x46\x58\x5b\x20\x52\x58\x50\x56\x4e'\
b'\x54\x4d\x51\x4d\x4f\x4e\x4d\x50\x4c\x53\x4c\x55\x4d\x58\x4f'\
b'\x5a\x51\x5b\x54\x5b\x56\x5a\x58\x58\x11\x49\x5b\x4c\x53\x58'\
b'\x53\x58\x51\x57\x4f\x56\x4e\x54\x4d\x51\x4d\x4f\x4e\x4d\x50'\
b'\x4c\x53\x4c\x55\x4d\x58\x4f\x5a\x51\x5b\x54\x5b\x56\x5a\x58'\
b'\x58\x08\x4d\x59\x57\x46\x55\x46\x53\x47\x52\x4a\x52\x5b\x20'\
b'\x52\x4f\x4d\x56\x4d\x16\x49\x5c\x58\x4d\x58\x5d\x57\x60\x56'\
b'\x61\x54\x62\x51\x62\x4f\x61\x20\x52\x58\x50\x56\x4e\x54\x4d'\
b'\x51\x4d\x4f\x4e\x4d\x50\x4c\x53\x4c\x55\x4d\x58\x4f\x5a\x51'\
b'\x5b\x54\x5b\x56\x5a\x58\x58\x0a\x49\x5c\x4d\x46\x4d\x5b\x20'\
b'\x52\x4d\x51\x50\x4e\x52\x4d\x55\x4d\x57\x4e\x58\x51\x58\x5b'\
b'\x08\x4e\x56\x51\x46\x52\x47\x53\x46\x52\x45\x51\x46\x20\x52'\
b'\x52\x4d\x52\x5b\x0b\x4d\x57\x52\x46\x53\x47\x54\x46\x53\x45'\
b'\x52\x46\x20\x52\x53\x4d\x53\x5e\x52\x61\x50\x62\x4e\x62\x08'\
b'\x49\x5a\x4d\x46\x4d\x5b\x20\x52\x57\x4d\x4d\x57\x20\x52\x51'\
b'\x53\x58\x5b\x02\x4e\x56\x52\x46\x52\x5b\x12\x43\x61\x47\x4d'\
b'\x47\x5b\x20\x52\x47\x51\x4a\x4e\x4c\x4d\x4f\x4d\x51\x4e\x52'\
b'\x51\x52\x5b\x20\x52\x52\x51\x55\x4e\x57\x4d\x5a\x4d\x5c\x4e'\
b'\x5d\x51\x5d\x5b\x0a\x49\x5c\x4d\x4d\x4d\x5b\x20\x52\x4d\x51'\
b'\x50\x4e\x52\x4d\x55\x4d\x57\x4e\x58\x51\x58\x5b\x11\x49\x5c'\
b'\x51\x4d\x4f\x4e\x4d\x50\x4c\x53\x4c\x55\x4d\x58\x4f\x5a\x51'\
b'\x5b\x54\x5b\x56\x5a\x58\x58\x59\x55\x59\x53\x58\x50\x56\x4e'\
b'\x54\x4d\x51\x4d\x11\x48\x5b\x4c\x4d\x4c\x62\x20\x52\x4c\x50'\
b'\x4e\x4e\x50\x4d\x53\x4d\x55\x4e\x57\x50\x58\x53\x58\x55\x57'\
b'\x58\x55\x5a\x53\x5b\x50\x5b\x4e\x5a\x4c\x58\x11\x49\x5c\x58'\
b'\x4d\x58\x62\x20\x52\x58\x50\x56\x4e\x54\x4d\x51\x4d\x4f\x4e'\
b'\x4d\x50\x4c\x53\x4c\x55\x4d\x58\x4f\x5a\x51\x5b\x54\x5b\x56'\
b'\x5a\x58\x58\x08\x4b\x58\x4f\x4d\x4f\x5b\x20\x52\x4f\x53\x50'\
b'\x50\x52\x4e\x54\x4d\x57\x4d\x11\x4a\x5b\x58\x50\x57\x4e\x54'\
b'\x4d\x51\x4d\x4e\x4e\x4d\x50\x4e\x52\x50\x53\x55\x54\x57\x55'\
b'\x58\x57\x58\x58\x57\x5a\x54\x5b\x51\x5b\x4e\x5a\x4d\x58\x08'\
b'\x4d\x59\x52\x46\x52\x57\x53\x5a\x55\x5b\x57\x5b\x20\x52\x4f'\
b'\x4d\x56\x4d\x0a\x49\x5c\x4d\x4d\x4d\x57\x4e\x5a\x50\x5b\x53'\
b'\x5b\x55\x5a\x58\x57\x20\x52\x58\x4d\x58\x5b\x05\x4a\x5a\x4c'\
b'\x4d\x52\x5b\x20\x52\x58\x4d\x52\x5b\x0b\x47\x5d\x4a\x4d\x4e'\
b'\x5b\x20\x52\x52\x4d\x4e\x5b\x20\x52\x52\x4d\x56\x5b\x20\x52'\
b'\x5a\x4d\x56\x5b\x05\x4a\x5b\x4d\x4d\x58\x5b\x20\x52\x58\x4d'\
b'\x4d\x5b\x09\x4a\x5a\x4c\x4d\x52\x5b\x20\x52\x58\x4d\x52\x5b'\
b'\x50\x5f\x4e\x61\x4c\x62\x4b\x62\x08\x4a\x5b\x58\x4d\x4d\x5b'\
b'\x20\x52\x4d\x4d\x58\x4d\x20\x52\x4d\x5b\x58\x5b\x0b\x4b\x59'\
b'\x4f\x42\x4f\x62\x20\x52\x50\x42\x50\x62\x20\x52\x4f\x42\x56'\
b'\x42\x20\x52\x4f\x62\x56\x62\x02\x4b\x59\x4b\x46\x59\x5e\x0b'\
b'\x4b\x59\x54\x42\x54\x62\x20\x52\x55\x42\x55\x62\x20\x52\x4e'\
b'\x42\x55\x42\x20\x52\x4e\x62\x55\x62\x14\x46\x5f\x5b\x57\x59'\
b'\x57\x57\x56\x55\x54\x52\x50\x51\x4f\x4f\x4e\x4d\x4e\x4b\x4f'\
b'\x4a\x51\x4a\x53\x4b\x55\x4d\x56\x4f\x56\x51\x55\x52\x54\x55'\
b'\x50\x57\x4e\x59\x4d\x5b\x4d\x19\x46\x5f\x5c\x53\x5b\x55\x59'\
b'\x56\x57\x56\x55\x55\x54\x54\x51\x50\x50\x4f\x4e\x4e\x4c\x4e'\
b'\x4a\x4f\x49\x51\x49\x53\x4a\x55\x4c\x56\x4e\x56\x50\x55\x51'\
b'\x54\x54\x50\x55\x4f\x57\x4e\x59\x4e\x5b\x4f\x5c\x51\x5c\x53'\
b'\x0d\x4b\x59\x51\x46\x4f\x47\x4e\x49\x4e\x4b\x4f\x4d\x51\x4e'\
b'\x53\x4e\x55\x4d\x56\x4b\x56\x49\x55\x47\x53\x46\x51\x46\x1a'\
b'\x48\x5c\x50\x42\x50\x5f\x20\x52\x54\x42\x54\x5f\x20\x52\x59'\
b'\x49\x57\x47\x54\x46\x50\x46\x4d\x47\x4b\x49\x4b\x4b\x4c\x4d'\
b'\x4d\x4e\x4f\x4f\x55\x51\x57\x52\x58\x53\x59\x55\x59\x58\x57'\
b'\x5a\x54\x5b\x50\x5b\x4d\x5a\x4b\x58\x09\x45\x5b\x48\x4d\x4c'\
b'\x4d\x52\x59\x20\x52\x4b\x4d\x52\x5b\x20\x52\x5b\x42\x52\x5b'\
b'\x09\x41\x62\x44\x4d\x49\x4d\x52\x59\x20\x52\x48\x4e\x52\x5b'\
b'\x20\x52\x62\x3a\x52\x5b\x0c\x46\x5e\x5a\x4a\x53\x4a\x4f\x4b'\
b'\x4d\x4c\x4b\x4e\x4a\x51\x4a\x53\x4b\x56\x4d\x58\x4f\x59\x53'\
b'\x5a\x5a\x5a\x0c\x46\x5e\x4a\x4a\x4a\x51\x4b\x55\x4c\x57\x4e'\
b'\x59\x51\x5a\x53\x5a\x56\x59\x58\x57\x59\x55\x5a\x51\x5a\x4a'\
b'\x0c\x46\x5e\x4a\x4a\x51\x4a\x55\x4b\x57\x4c\x59\x4e\x5a\x51'\
b'\x5a\x53\x59\x56\x57\x58\x55\x59\x51\x5a\x4a\x5a\x0c\x46\x5e'\
b'\x4a\x5a\x4a\x53\x4b\x4f\x4c\x4d\x4e\x4b\x51\x4a\x53\x4a\x56'\
b'\x4b\x58\x4d\x59\x4f\x5a\x53\x5a\x5a\x0f\x46\x5e\x5a\x4a\x53'\
b'\x4a\x4f\x4b\x4d\x4c\x4b\x4e\x4a\x51\x4a\x53\x4b\x56\x4d\x58'\
b'\x4f\x59\x53\x5a\x5a\x5a\x20\x52\x4a\x52\x56\x52\x0a\x45\x5f'\
b'\x58\x50\x5b\x52\x58\x54\x20\x52\x55\x4d\x5a\x52\x55\x57\x20'\
b'\x52\x49\x52\x5a\x52\x0a\x4a\x5a\x50\x4c\x52\x49\x54\x4c\x20'\
b'\x52\x4d\x4f\x52\x4a\x57\x4f\x20\x52\x52\x4a\x52\x5b\x0a\x45'\
b'\x5f\x4c\x50\x49\x52\x4c\x54\x20\x52\x4f\x4d\x4a\x52\x4f\x57'\
b'\x20\x52\x4a\x52\x5b\x52\x0a\x4a\x5a\x50\x58\x52\x5b\x54\x58'\
b'\x20\x52\x4d\x55\x52\x5a\x57\x55\x20\x52\x52\x49\x52\x5a\x2b'\
b'\x49\x5c\x58\x52\x57\x4f\x56\x4e\x54\x4d\x52\x4d\x4f\x4e\x4d'\
b'\x51\x4c\x54\x4c\x57\x4d\x59\x4e\x5a\x50\x5b\x52\x5b\x55\x5a'\
b'\x57\x58\x58\x55\x59\x50\x59\x4b\x58\x48\x57\x47\x55\x46\x52'\
b'\x46\x50\x47\x4f\x48\x4f\x49\x50\x49\x50\x48\x20\x52\x52\x4d'\
b'\x50\x4e\x4e\x51\x4d\x54\x4d\x58\x4e\x5a\x20\x52\x52\x5b\x54'\
b'\x5a\x56\x58\x57\x55\x58\x50\x58\x4b\x57\x48\x55\x46\x0e\x48'\
b'\x5c\x4a\x46\x52\x5b\x20\x52\x4b\x46\x52\x59\x20\x52\x5a\x46'\
b'\x52\x5b\x20\x52\x4a\x46\x5a\x46\x20\x52\x4b\x47\x59\x47\x09'\
b'\x41\x62\x44\x4d\x49\x4d\x52\x59\x20\x52\x48\x4e\x52\x5b\x20'\
b'\x52\x62\x3a\x52\x5b\x1f\x46\x5e\x5b\x43\x5a\x44\x5b\x45\x5c'\
b'\x44\x5c\x43\x5b\x42\x59\x42\x57\x43\x55\x45\x54\x47\x53\x4a'\
b'\x52\x4e\x50\x5a\x4f\x5e\x4e\x60\x20\x52\x56\x44\x55\x46\x54'\
b'\x4a\x52\x56\x51\x5a\x50\x5d\x4f\x5f\x4d\x61\x4b\x62\x49\x62'\
b'\x48\x61\x48\x60\x49\x5f\x4a\x60\x49\x61\x38\x43\x61\x5d\x2e'\
b'\x5c\x2e\x5b\x2f\x5b\x30\x5c\x31\x5d\x31\x5e\x30\x5e\x2e\x5d'\
b'\x2c\x5b\x2b\x59\x2b\x57\x2c\x55\x2e\x54\x30\x53\x33\x52\x3a'\
b'\x51\x4a\x51\x6a\x50\x73\x4f\x76\x20\x52\x5c\x2f\x5c\x30\x5d'\
b'\x30\x5d\x2f\x5c\x2f\x20\x52\x52\x3a\x52\x6a\x20\x52\x55\x2e'\
b'\x54\x31\x53\x3a\x53\x5a\x52\x6a\x51\x71\x50\x74\x4f\x76\x4d'\
b'\x78\x4b\x79\x49\x79\x47\x78\x46\x76\x46\x74\x47\x73\x48\x73'\
b'\x49\x74\x49\x75\x48\x76\x47\x76\x20\x52\x47\x74\x47\x75\x48'\
b'\x75\x48\x74\x47\x74\x1b\x49\x5b\x58\x2b\x55\x31\x52\x38\x50'\
b'\x3d\x4f\x41\x4e\x46\x4d\x4e\x4d\x56\x4e\x5e\x4f\x63\x50\x67'\
b'\x52\x6c\x55\x73\x58\x79\x20\x52\x55\x31\x53\x36\x51\x3c\x50'\
b'\x40\x4f\x46\x4e\x4e\x4e\x56\x4f\x5e\x50\x64\x51\x68\x53\x6e'\
b'\x55\x73\x1b\x49\x5b\x4c\x2b\x4f\x31\x52\x38\x54\x3d\x55\x41'\
b'\x56\x46\x57\x4e\x57\x56\x56\x5e\x55\x63\x54\x67\x52\x6c\x4f'\
b'\x73\x4c\x79\x20\x52\x4f\x31\x51\x36\x53\x3c\x54\x40\x55\x46'\
b'\x56\x4e\x56\x56\x55\x5e\x54\x64\x53\x68\x51\x6e\x4f\x73\x0d'\
b'\x49\x5b\x4d\x2b\x4d\x52\x4d\x79\x20\x52\x4e\x2b\x4e\x52\x4e'\
b'\x79\x20\x52\x4d\x2b\x58\x2b\x20\x52\x4d\x79\x58\x79\x0d\x49'\
b'\x5b\x56\x2b\x56\x52\x56\x79\x20\x52\x57\x2b\x57\x52\x57\x79'\
b'\x20\x52\x4c\x2b\x57\x2b\x20\x52\x4c\x79\x57\x79\x0b\x49\x5c'\
b'\x58\x46\x58\x5b\x20\x52\x4b\x46\x58\x46\x20\x52\x50\x50\x58'\
b'\x50\x20\x52\x4b\x5b\x58\x5b\x2d\x48\x5c\x4b\x49\x4c\x4b\x58'\
b'\x57\x59\x59\x59\x5b\x20\x52\x4c\x4c\x58\x58\x20\x52\x4b\x49'\
b'\x4b\x4b\x4c\x4d\x58\x59\x59\x5b\x20\x52\x50\x50\x4c\x54\x4b'\
b'\x56\x4b\x58\x4c\x5a\x4b\x5b\x20\x52\x4b\x56\x4d\x5a\x20\x52'\
b'\x4c\x54\x4c\x56\x4d\x58\x4d\x5a\x4b\x5b\x20\x52\x53\x53\x58'\
b'\x4e\x20\x52\x56\x49\x56\x4c\x57\x4e\x59\x4e\x59\x4c\x57\x4b'\
b'\x56\x49\x20\x52\x56\x49\x57\x4c\x59\x4e\x0e\x45\x5f\x52\x49'\
b'\x51\x4a\x52\x4b\x53\x4a\x52\x49\x20\x52\x49\x52\x5b\x52\x20'\
b'\x52\x52\x59\x51\x5a\x52\x5b\x53\x5a\x52\x59\x05\x4b\x59\x4f'\
b'\x42\x4f\x62\x20\x52\x55\x42\x55\x62\x05\x46\x5e\x52\x42\x52'\
b'\x5b\x20\x52\x49\x5b\x5b\x5b\x27\x4b\x59\x54\x42\x52\x43\x51'\
b'\x44\x50\x46\x50\x48\x51\x4a\x52\x4b\x53\x4d\x53\x4f\x51\x51'\
b'\x20\x52\x52\x43\x51\x45\x51\x47\x52\x49\x53\x4a\x54\x4c\x54'\
b'\x4e\x53\x50\x4f\x52\x53\x54\x54\x56\x54\x58\x53\x5a\x52\x5b'\
b'\x51\x5d\x51\x5f\x52\x61\x20\x52\x51\x53\x53\x55\x53\x57\x52'\
b'\x59\x51\x5a\x50\x5c\x50\x5e\x51\x60\x52\x61\x54\x62\x03\x46'\
b'\x5e\x5b\x42\x49\x5b\x5b\x5b\x27\x4b\x59\x50\x42\x52\x43\x53'\
b'\x44\x54\x46\x54\x48\x53\x4a\x52\x4b\x51\x4d\x51\x4f\x53\x51'\
b'\x20\x52\x52\x43\x53\x45\x53\x47\x52\x49\x51\x4a\x50\x4c\x50'\
b'\x4e\x51\x50\x55\x52\x51\x54\x50\x56\x50\x58\x51\x5a\x52\x5b'\
b'\x53\x5d\x53\x5f\x52\x61\x20\x52\x53\x53\x51\x55\x51\x57\x52'\
b'\x59\x53\x5a\x54\x5c\x54\x5e\x53\x60\x52\x61\x50\x62\x11\x45'\
b'\x5f\x52\x49\x51\x4a\x52\x4b\x53\x4a\x52\x49\x20\x52\x49\x59'\
b'\x48\x5a\x49\x5b\x4a\x5a\x49\x59\x20\x52\x5b\x59\x5a\x5a\x5b'\
b'\x5b\x5c\x5a\x5b\x59\x17\x46\x5e\x49\x55\x49\x53\x4a\x50\x4c'\
b'\x4f\x4e\x4f\x50\x50\x54\x53\x56\x54\x58\x54\x5a\x53\x5b\x51'\
b'\x20\x52\x49\x53\x4a\x51\x4c\x50\x4e\x50\x50\x51\x54\x54\x56'\
b'\x55\x58\x55\x5a\x54\x5b\x51\x5b\x4f'

_index =\
b'\x00\x00\x03\x00\x16\x00\x29\x00\x36\x00\x43\x00\x84\x00\x99'\
b'\x00\xae\x00\xd7\x00\x00\x01\x13\x01\x20\x01\x31\x01\x38\x01'\
b'\x45\x01\x4c\x01\x71\x01\x7c\x01\x9b\x01\xbc\x01\xcb\x01\xf0'\
b'\x01\x21\x02\x2e\x02\x6b\x02\x9c\x02\xc7\x02\xf6\x02\xff\x02'\
b'\x0c\x03\x15\x03\x28\x03\x3b\x03\x60\x03\x85\x03\xa4\x03\xc9'\
b'\x03\xee\x03\x01\x04\x30\x04\x47\x04\x5a\x04\x73\x04\x86\x04'\
b'\x8d\x04\xb4\x04\xcb\x04\xf0\x04\x15\x05\x3a\x05\x4d\x05\x72'\
b'\x05\x85\x05\x9c\x05\xa9\x05\xc2\x05\xcf\x05\xe4\x05\xf7\x05'\
b'\x10\x06\x17\x06\x30\x06\x5b\x06\x90\x06\xad\x06\xe4\x06\xf9'\
b'\x06\x0e\x07\x29\x07\x44\x07\x5f\x07\x7a\x07\x9b\x07\xb2\x07'\
b'\xc9\x07\xe0\x07\xf7\x07\x50\x08\x6f\x08\x84\x08\xc5\x08\x38'\
b'\x09\x71\x09\xaa\x09\xc7\x09\xe4\x09\xfd\x09\x5a\x0a\x79\x0a'\
b'\x86\x0a\x93\x0a\xe4\x0a\xed\x0a\x3e\x0b\x63\x0b'

INDEX = memoryview(_index)
FONT = memoryview(_font)
