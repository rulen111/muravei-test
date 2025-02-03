from __future__ import division
from collections import deque

# Dict for caching digit sums
digit_sum_cache = dict()

def digit_sum(n):
    """
    Calculate sum of the given number's digits
    :param n: input number (int)
    :return: sum of digits (int)
    """
    n_abs = abs(n)
    if n_abs in digit_sum_cache:
        return digit_sum_cache[n_abs]
    
    s = 0
    num = n_abs
    while num > 0:
        s += num % 10
        num = num // 10
    digit_sum_cache[n_abs] = s
    
    return s

def count_accessible_cells(start = (1000, 1000)):
    """
    Count cells which are accessible for the ant
    :param start: starting coordinates (tuple)
    :return: number of cells (int)
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                sum_x = digit_sum(nx)
                sum_y = digit_sum(ny)
                if sum_x + sum_y <= 25:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return len(visited)

if __name__ == "__main__":
    result = count_accessible_cells()
    print "Number of accessible cells: ", result
