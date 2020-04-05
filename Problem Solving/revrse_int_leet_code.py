def convert_bin_to_int(a):
    value=str(bin(a))[2:].zfill(32)
    new_value=value[::-1]
    if new_value=="00111001011110000010100101000000":
        print(True)
    print(new_value)
    new_value=int(new_value,2)
    return new_value

a=43261596 
convert_bin_to_int(a)       