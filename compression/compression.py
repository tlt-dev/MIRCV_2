def variable_byte_encode(number):
    """Encodes a number using variable byte encoding."""
    if number == 0:
        return [0]

    bytes_list = []
    while number > 0:
        bytes_list.insert(0, number % 128)
        number >>= 7

    # Set the most significant bit to 1 for all but the last byte
    for i in range(len(bytes_list) - 1):
        bytes_list[i] |= 0x80
    bytes_list[-1] |= 0x00  # Ensure the last byte is in the range 0-127

    return bytes_list

def variable_byte_decode(encoded_bytes):
    """ Decodes a sequence of bytes using variable byte encoding.    """
    decoded_numbers = []
    current_number = 0
    for byte in encoded_bytes:
        # Add the 7 least significant bits of the byte to the current number
        current_number = (current_number << 7) | (byte & 0x7F)
        # Check if this is the last byte in the number
        if (byte & 0x80) == 0:  # If the most significant bit is not set
            decoded_numbers.append(current_number)
            current_number = 0  # Reset for the next number
    return decoded_numbers