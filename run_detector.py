# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from detector.core import DeadCodeDetector

def main():
    parser = argparse.ArgumentParser(description="Basic Dead Code Detector")
    parser.add_argument("path", help="Directory or file to scan (defaults to current dir)", nargs='?', default=".")
    
    args = parser.parse_args()
    path = os.path.abspath(args.path)
    
    issues = []
    
    if os.path.isfile(path):
        issues = DeadCodeDetector.scan_file(path)
    elif os.path.isdir(path):
        issues = DeadCodeDetector.scan_directory(path)
    else:
        print(f"Error: Path '{path}' not found.")
        sys.exit(1)
        
    if not issues:
        print("Clean! No obvious unreachable code found.")
        sys.exit(0)
        
    print(f"Found {len(issues)} dead code blocks:\n")
    for issue in issues:
        print(f"[{issue['file']}:{issue['line']}] {issue['msg']}: {issue['content']}")
        
    sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
