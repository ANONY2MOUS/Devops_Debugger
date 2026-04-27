import sys
from parser import parse_log
from rules import detect_issue

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <logfile>")
        return

    with open(sys.argv[1], 'r') as f:
        log = f.read()

    parsed = parse_log(log)
    result = detect_issue(parsed)

    print("\n=== Analysis Result ===")
    print(f"Problem: {result['problem']}")
    print(f"Cause: {result['cause']}")
    print(f"Fix: {result['fix']}")

if __name__ == "__main__":
    main()
