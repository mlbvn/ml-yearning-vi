# encoding=utf8
import codecs
import csv
import re
import sys
import os

# reload(sys)
# sys.setdefaultencoding('utf8')


NUM_CHAPTERS = 58
NUM_CHAPTERS_PHASE_1 = 14
PENDING_CHAPTERS = [11, 13]

CHAPTERS_DIR = './chapters/'
ALL_CHAPTERS_FILENAME = 'all_chapters.md'


def main():
    with codecs.open(os.path.join(CHAPTERS_DIR, ALL_CHAPTERS_FILENAME), 'w', encoding='utf-8') as all_file:
        for i in range(1, NUM_CHAPTERS_PHASE_1 + 1):
            if i in PENDING_CHAPTERS:
                continue
            chapter_path = os.path.join(CHAPTERS_DIR, 'ch{:02d}.md'.format(i))
            with codecs.open(chapter_path, 'r', encoding='utf-8') as one_file:
                for line in one_file:
                    try:
                        all_file.write(line)
                    except UnicodeDecodeError as e:
                        print('Line with decode error:')
                        print(e)
            all_file.write('\n')
            all_file.write('------------------\n')


if __name__ == '__main__':
    main()


