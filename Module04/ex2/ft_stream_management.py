#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # add \n
        sys.stdout.write(f"Usage: {sys.argv[0]} <filename>\n")
        sys.stdout.flush()
    else:
        filename = sys.argv[1]
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
        sys.stdout.write(f"Accessing file '{filename}'\n")
        sys.stdout.flush()
        # is everything OK ?
        success = False
        file_ptr = None
        lines = []
        try:
            file_ptr = open(filename, 'r')
            # saves \n
            lines = file_ptr.readlines()
            # reading OK
            success = True
            sys.stdout.write("---\n")
            for line in lines:
                # contains \n
                sys.stdout.write(line)
            sys.stdout.write("\n---\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(
                f"[STDERR] Error opening file '{filename}': {e}\n"
                )
            sys.stderr.flush()
        finally:
            if file_ptr is not None:
                file_ptr.close()
                sys.stdout.write(f"File '{filename}' closed.\n")
                sys.stdout.flush()
        # TRANSFORMATION if only is everything OK
        if success:
            new_data = ""
            for line in lines:
                # new_data += line.rstrip('\n') + "#\n"
                new_data += line[:-1] + "#\n"
            sys.stdout.write("Transform data:\n---\n")
            sys.stdout.write(new_data)
            sys.stdout.write("---\n")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            # READ and CLEAR (crucial for the next if)
            raw_input = sys.stdin.readline()
            # destination = raw_input.rstrip('\n')
            destination = raw_input[:-1]
            # Save?
            if len(destination) > 0:
                sys.stdout.write(f"Saving data to '{destination}'\n")
                sys.stdout.flush()
                destination_ptr = None
                try:
                    destination_ptr = open(destination, 'w')
                    destination_ptr.write(new_data)
                    sys.stdout.write(f"Data saved in file '{destination}'.\n")
                except Exception as e:
                    sys.stderr.write(
                        f"[STDERR] Error opening file '{destination}': {e}\n"
                        )
                    sys.stderr.flush()
                    sys.stdout.write("Data not saved.\n")
                finally:
                    if destination_ptr is not None:
                        destination_ptr.close()
            else:
                sys.stdout.write("Not saving data.\n")
                sys.stdout.flush()
