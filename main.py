import argparse
from reporter import main

parser = argparse.ArgumentParser(description="File Metadata Tool")
parser.add_argument("file", help="Path to the file")
parser.add_argument("--format", choices=["text", "json"], default="text")
args = parser.parse_args()
main(args.file)

print(args.file)
print(args.format)