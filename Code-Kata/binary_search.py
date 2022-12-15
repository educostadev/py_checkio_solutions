from typing import List, Any

def solve(elements: List[Any], find: int) -> int:
    lower_bound = 0
    upper_bound = len(elements)-1
    while(lower_bound < upper_bound):
        mid_index = (upper_bound - lower_bound) // 2
        print(f"lower:{lower_bound} upper:{upper_bound} mid index:{mid_index}")
        if (elements[mid_index] == find):
            return mid_index
        
        if (elements[mid_index] > find):
            upper_bound = mid_index-1

        if (elements[mid_index] < find):
            lower_bound = mid_index+1
           
    return -1

if __name__ == '__main__':
    
    assert solve([1, 2, 3, 4, 5, 6, 7, 8], 2) == 1, "Failed"  
    print("---")
    assert solve([1, 2, 3], 0) == -1, "Failed"  
    print("Success!")