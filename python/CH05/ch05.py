def bin_to_str(double):
    import math

    integer = int(str(double)[2:])
    div = integer/math.pow(5, len(str(integer)))
    if div != int(div):
        return "ERROR"

    result = ""
    div = int(div)
    while div > 0:
        result += str(div % 2)
        div = div / 2
    return "0." + result[::-1]


def insertion(n, m, i, j):
    if i > j:
        return None
    mask = ((~0 << (j-i+1)) << i) | ~(~0 << i)
    return (n & mask)| (m << i)


def flip_bit_to_win(a):
    state = {'odd': {'len':0, 'start':0, 'parity':0}, 'even': {'len':0, 'start':0, 'parity':1}}
    if a in [0, ~0]:
        print "a is ", a, " all of it's bits are ", str(0 if a is 0 else 1)
        return 0

    def skip_zeros(n):
        idx = 0
        while n > 0 and (n & 1 is 0):
            n >>= 1
            idx += 1
        return idx

    def count_ones(n):
        idx = 0
        while n & 1:
            n >>= 1
            idx += 1
        return idx

    longest_seq = -1
    flip_idx = -1
    active_state = state[0]

    # skip trailing 0's at the left end
    idx = skip_zeros(a)

    while a > 0:
        if a & 1:
            active_state['start'] = idx
            active_state['len'] = count_ones(a)
            idx += active_state['len']

        if active_state == state[1]:
            seq_len = state[0]['len']+state[1]['len']+1
            if seq_len > longest_seq:
                longest_seq = seq_len
                flip_idx = state[1]['start'] -1
                
    return flip_idx


def next_number(n):

    if n in [0, ~0]:
        print "Can't find a numbers grater or smaller then ", n, "with the same number of bits turned on."
        return

    # look for next number
    mask = 1
    if n&1 and not n&2:
        print "Next number is ", (n & ~0<<1) | 2, "."
    else:
        while n & mask:
            mask <<= 1
        if mask & n is not 0:
            print "Prev number is ", (n & (~0 << count)) | ((mask >> 2) | mask), "."
        else:
            print "Prev number is ", (n & n-1) + 1, "."


    while n & next_mask:
        next_mask <<= 1

def conversion(a, b):
    x = a ^ b
    counter = 0
    while x:
        counter += x & 1
        x >> 1

    return counter


def pairwise_swap(n):
    m1 = 0x55555555
    m2 = 0xaaaaaaaa
    return ((n & m1) << 1) | ((n & m2) >> 1)


def draw_line(byte_screen, width, x1, x2, y):

    # first, lets write 0xff in all the bytes in the range between x1 and x2
    # then we handle the first and last byte

    # Also, we need to find the offset, in bytes,
    # from the top left of the screen to the y scan line
    offset = width * (y - 1)

    # bulk 0xffff
    byte_screen[offset + x1 / 8: offset + (x2 / 8) + 1] = 0xffff

    # first byte
    if x1 % 8 > 0:
        byte_screen[offset+x1/8] = ((8-(x1 % 8)) << 1)-1
    # else its 0xff and that value was set at the bulk  write

    # last byte
    if x2 % 8 > 0:
        byte_screen[offset + x2 / 8] = (~0) >> (x2 % 8)


print bin_to_str(0.625)
print bin_to_str(0.5)
print bin_to_str(0.5390625)

print pairwise_swap(0x55555555) == 0xaaaaaaaa
print pairwise_swap(0xaaaaaaaa) == 0x55555555
print 0xaaaaaaaa == pairwise_swap(pairwise_swap(0xaaaaaaaa))
print pairwise_swap(42)
print pairwise_swap(0)

print "insertion(0x400, 19, 2, 6) is ", insertion(0x400, 19, 2, 6)
print "insertion(0xff, 0x0, 0, 3) is ", insertion(0xff, 0, 4, 7)