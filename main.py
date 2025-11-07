def mix_columns(state):
    for col in range(4):
        s0 = state[0][col]
        s1 = state[1][col]
        s2 = state[2][col]
        s3 = state[3][col]
        
        # Mul by 2: (x << 1) ^ (0x1b if high bit set)
        mul2_0 = ((s0 << 1) ^ (0x1b if s0 & 0x80 else 0)) & 0xff
        mul2_1 = ((s1 << 1) ^ (0x1b if s1 & 0x80 else 0)) & 0xff
        mul2_2 = ((s2 << 1) ^ (0x1b if s2 & 0x80 else 0)) & 0xff
        mul2_3 = ((s3 << 1) ^ (0x1b if s3 & 0x80 else 0)) & 0xff
        
        # Mul by 3: mul2 ^ x
        mul3_0 = mul2_0 ^ s0
        mul3_1 = mul2_1 ^ s1
        mul3_2 = mul2_2 ^ s2
        mul3_3 = mul2_3 ^ s3
        
        state[0][col] = mul2_0 ^ mul3_1 ^ s2 ^ s3
        state[1][col] = s0 ^ mul2_1 ^ mul3_2 ^ s3
        state[2][col] = s0 ^ s1 ^ mul2_2 ^ mul3_3
        state[3][col] = mul3_0 ^ s1 ^ s2 ^ mul2_3

# Example:
state = [
    [0x87, 0xf2, 0x4d, 0x97],
    [0x6e, 0x4c, 0x90, 0xec],
    [0x46, 0xe7, 0x4a, 0xc3],
    [0xa6, 0x8c, 0xd8, 0x95]
]
mix_columns(state)
for row in state:
    print([hex(x) for x in row])