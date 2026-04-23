#!/usr/bin/env python3


def secure_archive(
    filename: str,
    mode: str = 'r',
    content: str = ''
) -> tuple[bool, str]:
    try:
        if mode == 'r':
            with open(filename, 'r') as file_ptr:
                data = file_ptr.read()
                return (True, data)
        elif mode == 'w':
            with open(filename, 'w') as file_ptr:
                file_ptr.write(content)
                return (True, content)
        return (False, f"Unknown mode: {mode}")
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    # onexistent file
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'r'))
    # Permission denied
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 'r'))
    # ok
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", 'r'))
    # write If the file doesn't exist, it creates it
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    result = secure_archive(
        "vault_test.txt",
        'w',
        "Content successfully written to file"
    )
    print(result)
