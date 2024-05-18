import sys

def weird_algorithm(n: int) -> int:
    if n%2 == 0:
        n = n/2
    else:
        n = (n*3) + 1

    return int(n)

if __name__ == "__main__":
    try:
        if len(sys.argv) <= 1: 
            raise NameError("enter a number n")

        n = int(sys.argv[1])
        
        if n <= 0:
            raise NameError("enter a number > 0")

        result = []
        while n != 1:
            n = weird_algorithm(n)
            result.append(str(n))

        print(' '.join(result))

    except Exception as e:
        print(f"ERR: {e}")
        exit(-1)
