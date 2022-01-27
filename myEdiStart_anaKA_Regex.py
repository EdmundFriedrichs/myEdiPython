# textfile Bearbeitung
# analyze Kontoauszug 2, mit regex

import re

def get_times(text):
#    pattern = re.compile(
#       r'(Mo|Di|Mi|Do|Fr|Sa|So)'  # Weekday
#       r'(\d{1,2}.\d{2})'         # Date
#       r'(\d{1,2}:\d{2})?'        # Start time
#       r'(\d{1,2}:\d{2})?'        # End time
#    )

    pattern = re.compile(
        r'/.07'
    )
    for match in re.findall(pattern, text):
        yield ' '.join(filter(bool, match))

def main():
    myFile = open(r"C:/Users/49157/myPython/testfiles/text/KontoAuszug_07_21.txt","r", encoding='utf8')
    lines = myFile.readlines()
    n = 0
    for line in lines:
        n += 1
        for time in get_times(line):
            print(f'{n} - {time}')
    print(f'{n} lines processed')
    myFile.close()

if __name__ == '__main__':
    main()

