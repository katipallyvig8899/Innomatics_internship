def solve(s):
    a=[]
    a=s.split(" ")
    for i in range(0,len(a)):
        a[i]=a[i].capitalize()
    a=' '.join(a)
    return(a)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
