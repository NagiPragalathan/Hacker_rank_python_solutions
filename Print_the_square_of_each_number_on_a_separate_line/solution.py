def square_of_list(end):
    out=str()
    for i in range(end):
        out=out+str(i**2)+'\n'
    return out
if __name__ == '__main__':
    n = int(input())
    print(square_of_list(n))