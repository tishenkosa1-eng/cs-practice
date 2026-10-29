VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line: str) -> dict:
    cleaned = line.strip()
    if not cleaned: raise ValueError("Empty")
    parts = cleaned.split(maxsplit=2)
    if len(parts) < 3: raise ValueError("Short")
    time, level, message = parts
    if level not in VALID_LEVELS: raise ValueError("Bad level")
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {"BROKEN": 0, "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        if not line.strip(): continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError: counts["BROKEN"] += 1
    return counts

def top_errors(lines, n: int) -> list:
    error_counts = {}
    for line in lines:
        if not line.strip(): continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError: continue
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return [list(item) for item in sorted_errors[:n]]

def format_report(counts: dict, errors: list) -> str:
    lines = ["Log report", ""]
    for lvl in sorted(counts.keys()): lines.append(f"{lvl}: {counts[lvl]}")
    lines.append("")
    lines.append("Frequent errors:")
    for msg, count in errors: lines.append(f" - {msg} - {count}")
    lines.append("")
    return "\n".join(lines)
