def init_state():
    flag = open("flag", "rb").read().strip()
    assert len(flag) == 38
    assert flag.startswith("flag{")
    assert flag.endswith("}")
    return int(flag[5:37], 16)


def lfsr(R, mask):
    degree = 128
    f_skr = (1 << degree) - 1
    tmp = ((R << 1) & mask)
    lastbit = 0
    while tmp != 0:
        lastbit ^= (tmp & 1)
        tmp = tmp >> 1
    return ((R << 1) ^ lastbit) & f_skr


def feedforward(r):
    x = [int(i) for i in list('{0:0b}'.format(r))][::-1]
    x += [0] * (128 - len(x))
    box = [78, 65, 90, 99, 117, 113, 87, 119, 64, 69, 114, 86, 72, 123, 91, 103, 124, 93, 79, 82, 76, 84, 106, 73, 110,
           92, 118, 63, 109, 101, 67, 122, 98, 111, 80, 105, 108, 107, 100, 81, 125, 71, 96, 83, 75, 68, 95, 74, 104,
           112, 121, 115, 77, 89, 85, 97, 70, 120, 88, 66, 94, 102, 116]
    out = x[127]
    for i in range(0, 63):
        out ^= (x[i] ^ x[box[i]]) & 1
    out ^= x[11] & x[22] & x[33] & x[53] & 1
    out ^= x[1] & x[9] & x[12] & x[18] & x[20] & x[23] & x[25] & x[26] & x[28] & x[33] & x[38] & x[41] & x[42] & x[51] & \
           x[53] & x[59] & 1
    tmp = 1
    for i in range(0, 63):
        tmp &= x[i]
    out ^= tmp & 1
    return out


mask = 79357851974096019130801167812430455523505
r = init_state()

s = ""
for i in range(2048):
    tmp = 0
    for j in range(8):
        r = lfsr(r, mask)
        tmp = (tmp << 1) ^ feedforward(r)
    s += chr(tmp)
open("output", "wb").write(s)
