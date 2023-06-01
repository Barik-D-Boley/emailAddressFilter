import sys
import re


def main(infile, outfile):
    with open(infile, 'r') as file:
        file_read = file.read()

    # This finds every email address using Regex, gets rid of duplicates with set, and sorts it alphabetically
    emails = sorted([*set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', file_read))])
    
    with open(outfile, 'w') as file:
        file.writelines(',\n'.join(emails))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])