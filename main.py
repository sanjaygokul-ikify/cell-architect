import argparse
import json
from src.core import CellArchitect

def main():
    parser = argparse.ArgumentParser(description='Cell Architect')
    parser.add_argument('--input', help='Input file')
    parser.add_argument('--output', help='Output file')
    args = parser.parse_args()
    architect = CellArchitect()
    architect.generate(args.input, args.output)
if __name__ == '__main__':
    main()