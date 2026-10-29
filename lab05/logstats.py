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
    counts = {}
    for line in lines:
        if not line.strip(): continue
        try:
            event = parse_event(line)
            lvl = event["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
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
    title = chr(1054)+chr(1090)+chr(1095)+chr(1105)+chr(1090)+" "+chr(1087)+chr(1086)+" "+chr(1078)+chr(1103)+chr(1088)+chr(1085)+chr(1072)+chr(1083)+chr(1091)
    err_label = chr(1063)+chr(1072)+chr(1089)+chr(1090)+chr(1099)+chr(1077)+" "+chr(1086)+chr(1096)+chr(1080)+chr(1073)+chr(1082)+chr(1080)+":"
    lines = [title, ""]
    for lvl in sorted(counts.keys()):
        lines.append(f"{lvl}: {counts[lvl]}")
    lines.append("")
    lines.append(err_label)
    for msg, count in errors:
        lines.append(f"- {msg} - {count}")
    lines.append("")
    return "\n".join(lines)
