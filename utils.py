import string

# The alphabet: 0-9, a-z, A-Z (62 characters)
BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase

def encode(num):
    """Converts an integer ID to a Base62 string."""
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

def decode(string_val):
    """Converts a Base62 string back to an integer ID."""
    base = len(BASE62)
    strlen = len(string_val)
    num = 0
    idx = 0
    for char in string_val:
        power = (strlen - (idx + 1))
        num += BASE62.index(char) * (base ** power)
        idx += 1
    return num