def opposite_rotations(rot1, rot2):
    return len(rot1) != len(rot2) and rot1[0] == rot2[0]

def shorten1(seq):
    for n in range(len(seq) - 1):
        if opposite_rotations(seq[n], seq[n + 1]):
            return shorten1(seq[:n] + seq[n + 2:])
    return seq

def shorten2(seq):
    for n in range(len(seq) - 2):
        if seq[n] == seq[n + 1] == seq[n + 2] and len(seq[n]) == 1:
            return shorten2(seq[:n] + [seq[n] + 'i'] + seq[n + 3:])
        if seq[n] == seq[n + 1] == seq[n + 2] and len(seq[n]) == 2:
            return shorten2(seq[:n] + [seq[n][0]] + seq[n + 3:])
    return seq

def shorten(seq): return shorten1(shorten2(seq))
