def address_decoder(cpu_address):
    # Extract relevant bits from CPU address
    a0_to_a8 = cpu_address & 0b111111111
    a9 = (cpu_address >> 9) & 1

    # Use a 4-to-16 binary decoder
    decoder_outputs = [0] * 16
    for i in range(16):
        # Connect A0 to A8 for RAM
        if i < 9:
            decoder_outputs[i] = a0_to_a8 & (1 << i)
        # Connect A9 for ROM
        elif i == 9:
            decoder_outputs[i] = a9 << 9

    # Connect two most significant outputs to chip select lines for both RAM and ROM
    ram_chip_select = decoder_outputs[14] | decoder_outputs[15]
    rom_chip_select = decoder_outputs[14] | decoder_outputs[15]

    return ram_chip_select, rom_chip_select


# Example usage:
cpu_address_bus = 0b11011010101110  # Replace this with the actual CPU address
ram_cs, rom_cs = address_decoder(cpu_address_bus)

print(f"RAM Chip Select: {ram_cs}")
print(f"ROM Chip Select: {rom_cs}")
