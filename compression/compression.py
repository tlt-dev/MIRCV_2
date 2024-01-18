def variable_byte_encode(number):
    if number == 0:
        return [0]

    bytes_list = []
    while number > 0:
        bytes_list.insert(0, number % 128)
        number >>= 7

    for i in range(len(bytes_list) - 1):
        bytes_list[i] |= 0x80
    bytes_list[-1] |= 0x00

    return bytes_list

def variable_byte_decode(encoded_bytes):
    decoded_numbers = []
    current_number = 0
    for byte in encoded_bytes:
        # Current number = 7 least significant bit
        current_number = (current_number << 7) | (byte & 0x7F)
        # If most significant bit == 0 : last byte of the number
        if (byte & 0x80) == 0:
            decoded_numbers.append(current_number)
            current_number = 0
    return decoded_numbers