import sys
import argparse

def main():
    parser = argparse.ArgumentParser(prog="audio_fingerprint")
    subparsers = parser.add_subparsers(dest="command")
    
    # build
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--dir", required=True)
    build_parser.add_argument("--db", required=True)
    
    # query
    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("--clip", required=True)
    query_parser.add_argument("--db", required=True)
    
    # test
    test_parser = subparsers.add_parser("test")
    test_parser.add_argument("--file", required=True)
    test_parser.add_argument("--db", required=True)
    
    args = parser.parse_args()
    
    if args.command == "build":
        print("BUILD FAILED") # Should be BUILD COMPLETE in golden patch
    elif args.command == "query":
        print("No match found")
    elif args.command == "test":
        print("FAIL")

if __name__ == "__main__":
    main()
