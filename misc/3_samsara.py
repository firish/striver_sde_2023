def split_cases(code):
    # Returns a list of all split-cases for the given code
    return [(int(code[:i]), code[i:]) for i in range(1, len(code))]

def find_pattern(panel, codes):
    result = []
    for code in codes:
        for index, pattern in split_cases(code):
            print(index,pattern)
            if(index <= len(panel)):
                if panel[index:index+len(pattern)] == pattern:
                    result.append(pattern)
                    # continue
                else:
                    result.append("not found")
        # else:
        #     result.append("not found")
    print(len(result))
    return result

# Example
panel = "1"
codes = ["0001", "00111","00003","00000"]
print(find_pattern(panel, codes))
