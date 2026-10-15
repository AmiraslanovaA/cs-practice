def read_rows(lines):
    lst =[]
    for i in lines:
        if lines[i] != []:
             counts = count(lines[i])
             break
    for i in lines:
        if lines[i] != [] and count(lines[i]) == counts:
            lst.append(dict(lines[i].strip().split(' ')))
    return lst
def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts
