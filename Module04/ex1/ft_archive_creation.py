#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <filename>")
    else:
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")
        # is everything OK ?
        success = False
        file_ptr = None
        lines = []
        try:
            file_ptr = open(filename, 'r')
            lines = file_ptr.readlines()
            # reading OK
            success = True
            print("---")
            for line in lines:
                print(line, end="")
            print("")
            print("---")
        except Exception as e:
            print(f"Error opening file '{filename}': {e}")
        finally:
            if file_ptr is not None:
                file_ptr.close()
                print(f"File '{filename}' closed.")
        # TRANSFORMATION if only is everything OK
        if success:
            new_data = ""
            for line in lines:
                # line[:-1] all but the last character (\n)
                new_data += line[:-1] + "#\n"
            print("Transform data:")
            print("---")
            print(new_data)
            print("---")
            destination = input("Enter new file name (or empty): ")
            # Not save nothing
            if len(destination) > 0:
                print("Saving data to", destination)
                # in case we dont have permission
                destination_ptr = None
                try:
                    destination_ptr = open(destination, 'w')
                    destination_ptr.write(new_data)
                    print(f"Data saved in file '{destination}'.")
                except Exception as e:
                    print(f"Error saving data: {e}")
                finally:
                    if destination_ptr is not None:
                        destination_ptr.close()
            else:
                print("Not saving data.")
