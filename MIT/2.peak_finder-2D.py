n, m = map(int, input("Enter rows and columns: ").strip().split(' '))
matrix = []
for i in range(n):
    row = list(map(int, input().strip().split(' ')))
    matrix.append(row)

def find_peak(matrix,n,m):
    start = 0
    end = m-1
    peak = [-9,-9]
    while(start <= end):
        mid = (start+end)//2
        maxInColm = matrix[0][mid]
        maxRow = 0
        for i in range(n):
            if maxInColm < matrix[i][mid]:
                maxInColm = matrix[i][mid]
                maxRow = i
        if((mid == 0 or matrix[maxRow][mid] > matrix[maxRow][mid-1])and(mid == m-1 or matrix[maxRow][mid] > matrix[maxRow][mid+1])):
            peak = [maxRow,mid]
            return peak
        elif matrix[maxRow][mid] < matrix[maxRow][mid-1]:
            end = mid-1
        else:
            start = mid+1

    return -999

peak = find_peak(matrix,n,m)
if peak is not -999:
    print(peak)
    print(matrix[peak[0]][peak[1]])
else:
    print("Peak not found")
