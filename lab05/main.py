import sys
from logstats import count_levels, top_errors, format_report

def main():
    filename = sys.stdin.readline().strip()
    if not filename: return
    with open(filename, "r", encoding="utf-8") as f: counts = count_levels(f)
    with open(filename, "r", encoding="utf-8") as f: errors = top_errors(f, 3)
    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as rf: rf.write(report_text)

if __name__ == "__main__": main()
