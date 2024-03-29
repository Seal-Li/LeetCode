def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    results = []
    for interval in intervals:
        if not results or interval[0] > results[-1][1]:
            results.append(interval)
        else:
            results[-1][1] = max(interval[1], results[-1][1])
    
    return results

intervals = [[1, 3], [2, 6], [7, 8], [10, 15], [12, 18]]
print(merge_intervals(intervals))