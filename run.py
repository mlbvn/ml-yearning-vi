# encoding=utf8
import codecs
import csv
import re
import sys
import os
from collections import OrderedDict

# reload(sys)
# sys.setdefaultencoding('utf8') 

NUM_CHAPTERS = 58
MAX_CHAPTER = 42
PENDING_CHAPTERS = []

CHAPTERS_DIR = './chapters/'
ALL_CHAPTERS_FILENAME = 'all_chapters.md'
ALL_CHAPTERS_VN_FILENAME = 'all_chapters_vietnames_only.md'
HEADER_TO_LINK_MAP = OrderedDict([(' ', '-'), ('#-', '#')])
HEADER_TO_LINK_MAP.update({a: '' for a in '.:?/'})

TRANSLATE_INDICATOR_STR = '--> _replace THIS LINE by your translation for the above line_'


def _create_header_link(line):
    for char, new_char in HEADER_TO_LINK_MAP.items():
        line = line.replace(char, new_char)
    return line.lower()


def main(vn_only=True):
    if vn_only:
        output_filename = os.path.join(CHAPTERS_DIR, ALL_CHAPTERS_VN_FILENAME)
    else:
        output_filename = os.path.join(CHAPTERS_DIR, ALL_CHAPTERS_FILENAME)
    with codecs.open(output_filename, 'w', encoding='utf-8') as all_file:
        # table of content
        all_file.write("**MỤC LỤC**\n\n")
        for i in range(1, MAX_CHAPTER + 1):
            if i in PENDING_CHAPTERS:
                continue
            chapter_path = _chapter_path_from_chapter_number(i)
            with codecs.open(chapter_path, 'r', encoding='utf-8') as one_file:
                for line in one_file:
                    if line.startswith('# '):
                        line=line.strip()
                        link = _create_header_link(line)

                        full_link = "[{display_text}]({link_to_chapter})".format(
                            display_text=line[len('# '):],
                            link_to_chapter=link
                        )

                        all_file.write('* ' + full_link + '\n')
                        break


        # main content
        for i in range(1, MAX_CHAPTER + 1):
            if i in PENDING_CHAPTERS:
                continue
            all_file.write('------------------\n')
            chapter_path = os.path.join(CHAPTERS_DIR, 'ch{:02d}.md'.format(i))
            with codecs.open(chapter_path, 'r', encoding='utf-8') as one_file:
                for line in one_file:
                    if vn_only and line.startswith('>'):
                        continue
                    try:
                        all_file.write(line)
                    except UnicodeDecodeError as e:
                        print('Line with decode error:')
                        print(e)
            all_file.write('\n')


def _chapter_path_from_chapter_number(chapter_number):
    return os.path.join(CHAPTERS_DIR, 'ch{:02d}.md'.format(chapter_number))


def reformat():
    min_chapter = 30
    for chapter in range(min_chapter, NUM_CHAPTERS + 1):
        chapter_path = _chapter_path_from_chapter_number(chapter)
        chapter_path_new = chapter_path.replace('.md', '_.md') 
        with codecs.open(chapter_path_new, 'w', encoding='utf-8') as new_file:
            with codecs.open(chapter_path, 'r', encoding='utf-8') as old_file:
                for line in old_file:
                    line = line.strip()
                    if line.startswith('!['):
                        new_file.write(line + '\n')
                    elif line == '':
                        new_file.write('\n')
                    elif line.startswith('>'):
                        new_file.write(line)
                    elif line == '->':
                        # add one more blankline
                        new_file.write('\n')
                        new_file.write(TRANSLATE_INDICATOR_STR + '\n')
                    else:
                        new_file.write('> ' + line + '\n')
        os.remove(chapter_path)
        os.rename(chapter_path_new, chapter_path)



if __name__ == '__main__':
    main(vn_only=False)
    main(vn_only=True)
    # reformat()
