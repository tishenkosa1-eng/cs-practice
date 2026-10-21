def parse_record(line: str) -> dict:
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")
    
    city, temp_str, date = fields
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()
    
    if not city or not date:
        raise ValueError("Город и дата не могут быть пустыми")
        
    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректное значение температуры: '{temp_str}'")
        
    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    city_totals = {}
    city_counts = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        city_totals[city] = city_totals.get(city, 0.0) + temp
        city_counts[city] = city_counts.get(city, 0) + 1
        
    averages = {}
    for city in city_totals:
        averages[city] = round(city_totals[city] / city_counts[city], 1)
    return averages


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    best_city = ""
    max_temp = float("-inf")
    for city in sorted(averages.keys()):
        if averages[city] > max_temp:
            max_temp = averages[city]
            best_city = city
    return best_city