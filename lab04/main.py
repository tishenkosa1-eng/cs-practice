import sys
from stats import parse_record, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    success_count = 0
    error_count = 0
    valid_records = []
    
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
            success_count += 1
        except ValueError:
            error_count += 1
            
    best_city = warmest_city(valid_records)
    if best_city:
        averages = average_by_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0

    print(success_count)
    print(error_count)
    print(f"{best_temp:.1f}")

if __name__ == "__main__":
    main()