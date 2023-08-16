from itertools import product

# Define the number of channels and the range of values for each channel
num_channels = 32  # 32 channels of 8 bits each gives a 256-bit color code
channel_range = 256

# Generate all possible color codes for the given number of channels and range
all_color_codes = product(range(channel_range), repeat=num_channels)

# Define a function to map a 256-bit color code to a unique value in the range 0 to 4,294,967,295
def map_color_code(color_code):
    mapped_value = 0
    for i, value in enumerate(color_code):
        mapped_value += value << (8 * i)  # Shift each 8-bit value into position
    return mapped_value % 4294967296  # Take the remainder to fit into the target range

# Map all color codes to the target range
mapped_color_codes = [map_color_code(code) for code in all_color_codes]

# Do something with the mapped color codes...
