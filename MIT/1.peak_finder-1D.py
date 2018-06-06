x = list(map(int, input().strip().split(' ')))
print(x)

def get_peak(arr):
    n = len(arr)
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        # print("start="+str(start) +" end="+str(end) +" mid="+str(mid))
        if((mid==0 or arr[mid] >= arr[mid-1]) and (mid == n-1 or arr[mid] >= arr[mid+1])):
            return arr[mid]
        elif arr[mid] < arr[mid-1]:
            end = mid-1
        else:
            start = mid+1

    return "no peak"

peak = get_peak(x)
print(peak)
