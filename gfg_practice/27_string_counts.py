# Good Math Problem
# Link: https://www.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints1135/1

def countStr(n):
    # All 'a's: 1 way
    count = 1

    # One 'b', rest 'a's: n ways
    count += n

    # One 'c', rest 'a's: n ways
    count += n

    # Two 'c's, rest 'a's: n choose 2 ways
    count += (n * (n - 1)) // 2

    # One 'b', one 'c', rest 'a's: n * (n - 1) ways
    count += n * (n - 1)

    # One 'b', two 'c's, rest 'a's: n * (n - 1) choose 2 ways
    count += n * ((n - 1) * (n - 2)) // 2

    return count

# Test the function with the given examples
countStr(1), countStr(3)
