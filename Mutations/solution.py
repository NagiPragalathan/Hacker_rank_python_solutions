def mutate_string(string, position, character):
    str_lis = list(string)
    str_lis[position] = character
    return "".join(str_lis)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)