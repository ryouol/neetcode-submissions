from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    
    if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])):
        return False
    return True



# take in a 2d Grid and ints r and c where r is index row and c is index coloumn it should return True of R and C are in the bounds of the gird and False otherwise. 

# thus we check if R > len(rows) AND if C > len(C) return false else return true


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
