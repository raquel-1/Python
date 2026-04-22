#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <filename>")
    else:
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{filename}'")
        file_ptr = None
        try:
            # Open the file in read-only mode 'r'
            file_ptr = open(filename, 'r')
            conten = file_ptr.read()
            print("---")
            print(conten)
            print("---")
        except Exception as e:
            print(f"Error opening file '{filename}': {e}")
        finally:
            if file_ptr is not None:
                file_ptr.close()
                print(f"File '{filename}' closed.")
