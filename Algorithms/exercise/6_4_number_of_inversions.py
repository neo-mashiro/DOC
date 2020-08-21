# Uses python3
import sys

def count_inversion(arr):
    """
    input: an unsorted array
    output: a tuple(the # of inversions, the sorted array in asc order)
    """
    if len(arr) == 1:
        return (0, arr)
    else:
        mid = len(arr) // 2
        count1, A = count_inversion(arr[:mid])  # count along the way as we sort
        count2, B = count_inversion(arr[mid:])  # count along the way as we sort
        count = count1 + count2

        # merge A,B(both sorted) into C(sorted), count along the way, and sum up counts
        i, j, C = 0, 0, []

        for _ in range(len(arr)):
            if i < len(A) and j < len(B):
                if (A[i] <= B[j]):
                    C.append(A[i])
                    i +=1
                else:
                    C.append(B[j])
                    j +=1
                    count += (len(A) - i)  # key point
            # if B is exhausted first, append A to C
            elif i < len(A):
                C.append(A[i])
                i +=1
            # if A is exhausted first, append B to C
            elif j < len(B):
                C.append(B[j])
                j +=1

        return (count, C)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(count_inversion(a)[0])
