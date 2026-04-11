import sys
import argparse
from audio_fingerprint.database import build_database, query
from audio_fingerprint.matcher import test_mode

def main():
    parser = argparse.ArgumentParser(prog="audio_fingerprint")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")
    
    # build --dir <wav_dir> --db <db_path>
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--dir", required=True, help="Directory containing WAV files")
    build_parser.add_argument("--db", required=True, help="Path to SQLite database")
    
    # query --clip <wav_path> --db <db_path>
    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("--clip", required=True, help="Path to audio clip")
    query_parser.add_argument("--db", required=True, help="Path to SQLite database")
    
    # test --file <wav_path> --db <db_path>
    test_parser = subparsers.add_parser("test")
    test_parser.add_argument("--file", required=True, help="Path to audio file for test")
    test_parser.add_argument("--db", required=True, help="Path to SQLite database")
    
    args = parser.parse_args()
    
    if args.command == "build":
        build_database(args.dir, args.db)
        print("BUILD COMPLETE")
    elif args.command == "query":
        song_name, confidence = query(args.clip, args.db)
        if song_name != "no_match":
            print(f"Match: {song_name} (confidence: {confidence})")
        else:
            print("No match found")
    elif args.command == "test":
        success = test_mode(args.file, args.db)
        if success:
            print("PASS")
        else:
            print("FAIL")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
