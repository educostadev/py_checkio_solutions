from typing import List, Any

def solve(elements: List[Any], find) -> int:
   
    lower_bound = 0
    upper_bound = len(elements)-1
    
    while (lower_bound <= upper_bound):
        mid = (upper_bound - lower_bound) // 2
        mid = lower_bound + mid
        value = elements[mid]
        print(f"lower:{lower_bound} upper:{upper_bound} mid:{mid} value:{value}")
        if (value == find):
            return mid
        if (value > find): 
            upper_bound = mid-1 
        if (value < find):
            lower_bound = mid+1

    return -1

if __name__ == '__main__':    
    print("⚪ [1]")
    assert solve([1, 2, 3, 4, 5, 6, 7, 8], 2) == 1, "🔴 Failed"  
    print("⚪ [2]")
    assert solve([1, 2, 3, 4, 5, 6, 7, 8], 7) == 6, "🔴 Failed"  
    print("⚪ [3]")
    assert solve([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7, "🔴 Failed"  
    print("⚪ [4]")
    assert solve([1, 2, 3], 0) == -1, "Failed"  
    print("🟢 Success")
