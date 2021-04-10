
def cipher(k, s):
    shifts = k

    encoded = [int(x) for x in s]
    iter_list = []
    one_count = 0
    decoded = ''

    for i in range(len(encoded))[::-1]:
        curr_iteration = len(encoded) - i - 1

        # turtle and shift chase, we add everything we see but remove the last element in the shift as we move along
        if curr_iteration > 0:
            one_count += iter_list[-1]

            if curr_iteration >= shifts:
                one_count -= iter_list[curr_iteration - shifts]

        # if our current value is a 1, we must match the ones we seen so far
        if encoded[i] == 1:
            iter_list.append(1 if one_count % 2 == 0 else 0)
            decoded += '1' if one_count % 2 == 0 else '0'
        else:
            iter_list.append(0 if one_count % 2 == 0 else 1)
            decoded += '0' if one_count % 2 == 0 else '1'

    return decoded[::-1][shifts-1:]
