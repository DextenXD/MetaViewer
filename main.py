import argparse
from reporter import main

parser = argparse.ArgumentParser(description="File Metadata Tool")
parser.add_argument("file", help="Path to the file")
parser.add_argument("--format", choices=["text", "json"], default="text")
args = parser.parse_args()

if __name__ == "__main__":
  main(args.file, args.format)