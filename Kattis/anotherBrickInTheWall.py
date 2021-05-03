h,w,n = map(int, input().split())

bricks = list(map(int, input().split()))


def find_possible():
    height = h
    width = w

    for brick in bricks:
        if height == 0:
            return 'YES'

        width -= brick

        if width == 0:
            width = w
            height -= 1

        elif width < 0:
            return 'NO'

    return 'YES' if height == 0 else 'NO'


print(find_possible())
