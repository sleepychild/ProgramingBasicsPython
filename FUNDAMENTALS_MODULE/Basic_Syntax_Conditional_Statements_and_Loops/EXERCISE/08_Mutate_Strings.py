start_str: str = input()
end_str: str = input()
for c in range(len(start_str)):
    if start_str[c] == end_str[c]:
        continue
    print(end_str[:c+1] + start_str[c+1:])
