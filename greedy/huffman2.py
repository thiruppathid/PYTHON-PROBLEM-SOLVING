def main():
    my_str = "BCCABBDDAECCBBAEDDCC"
    d = defaultdict(int)
    for i in my_str:
        d[i] += 1
    d_sorted = list(sorted(d.items(), key=lambda x: x[1]))
    print(d_sorted)