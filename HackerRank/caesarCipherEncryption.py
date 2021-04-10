
if __name__ == '__main__':
    n = int(input())

    msg = input()

    shift = int(input())

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    output = ''

    for index, letter in enumerate(msg):
        if letter in alpha:
            output += alpha[(alpha.index(letter) + shift) % len(alpha)]

        elif letter in alpha_cap:
            output += alpha_cap[(alpha_cap.index(letter) + shift) % len(alpha_cap)]

        else:
            output += letter

    print(output)
