def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        values = line.split(",")
        for i in range(len(values)):
            values[i] = values[i].strip()
        if not header:
            header = values
            continue
        if len(values) != len(header):
            continue
        row = {}
        for i in range(len(header)):
            row[header[i]] = values[i]
        rows.append(row)
    return rows
def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts
def total_minutes(rows,kind):
    total = 0.0
    found = False
    for row in rows:
        if row.get("тип") == kind:
            found = True
            minutes_str = row.get("минуты","")
            try:
                minutes_val = float(minutes_str.replace(',','.'))
                total += minutes_val
            except (ValueError, TypeError):
                continue
    if not found:
        return 0.0
    return round(total,1)
    return total
def  to_csv(counts):
    lines = ["тип,количество"]
    for kind in sorted(counts.keys()):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
