#!/usr/bin/python3

def extract_file_name(string):
    without_date = ''.join(reversed(''.join(reversed(string)).rsplit('_', 1)[0]))
    return ''.join(without_date.rsplit('.', 1)[0])

if __name__ == "__main__":
    print(extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))
    print(extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"))
