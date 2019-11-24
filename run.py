# encoding=utf8
import codecs
import csv
import re
import sys
import os
from collections import OrderedDict
import urllib.request

# reload(sys)
# sys.setdefaultencoding('utf8') 

NUM_CHAPTERS = 58
# TODO: get rid of max chapter, auto infer from CONTRIBUTIONS
MAX_CHAPTER = 45
PENDING_CHAPTERS = []

CHAPTERS_DIR = './chapters/'
ALL_CHAPTERS_FILENAME = 'all_chapters.md'
ALL_CHAPTERS_VN_FILENAME = 'all_chapters_vietnames_only.md'
HEADER_TO_LINK_MAP = OrderedDict([(' ', '-'), ('#-', '#')])
HEADER_TO_LINK_MAP.update({a: '' for a in '.:?/'})
README_PREFIX = './readme_prefix.md'
README = './README.md'
PR_PREFIX = 'https://github.com/aivivn/Machine-Learning-Yearning-Vietnamese-Translation/pull/'
TRANSLATE_INDICATOR_STR = '--> _replace THIS LINE by your translation for the above line_'

CONTRIBUTIONS = {
    1: [40],
    2: [54],
    3: [90],
    4: [83],
    5: [82],
    6: [91],
    7: [70],
    8: [80],
    9: [77],
    10: [117],
    11: [150],
    12: [113],
    13: [160],
    14: [140],
    15: [161],
    16: [164],
    17: [168],
    18: [156],
    19: [169],
    20: [172],
    21: [173],
    22: [181],
    23: [175],
    24: [192],
    25: [195],
    26: [193],
    27: [211],
    28: [234],
    29: [225],
    30: [228],
    31: [248],
    32: [251],
    33: [247],
    34: [254],
    35: [276],
    36: [273],
    37: [279],
    38: [302],
    39: [258],
    40: [282],
    41: [278],
    42: [298],
    43: [296],
    44: [301, 312],
    45: [304],
    46: [329],
    47: [333, 336],
    48: [],
    49: [340],
    50: [342],
    51: [349],
    52: [],
    53: [355],
    54: [352],
    58: [317]
}


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
            chapter_title = _get_chapter_title(i)
            link = _create_header_link(chapter_title)
            full_link = "[{display_text}]({link_to_chapter})".format(
                display_text=_remove_sharp(chapter_title),
                link_to_chapter=link
            )
            all_file.write('* ' + full_link + '\n')

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


def _remove_sharp(title):
    assert title.startswith('# ')
    return title[len('# '):]


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


def _create_header_link(line):
    for char, new_char in HEADER_TO_LINK_MAP.items():
        line = line.replace(char, new_char)
    return line.lower()


def _get_chapter_title(chapter_number):
    chapter_path = _chapter_path_from_chapter_number(chapter_number)
    with codecs.open(chapter_path, 'r', encoding='utf-8') as one_file:
        for line in one_file:
            if line.startswith('# '):
                line = line.strip()
                return line
    return '# {:02d}. chưa có tên'.format(chapter_number)


def _chapter_path_from_chapter_number(chapter_number):
    return os.path.join(CHAPTERS_DIR, 'ch{:02d}.md'.format(chapter_number))


def shorten_url(long_url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + long_url).read()
    return tinyurl.decode("utf-8")


def _get_markdown_link_to_pr(pr):
    assert isinstance(pr, int)
    pr_link = PR_PREFIX + str(pr)
    tiny_url = shorten_url(pr_link)
    res = '[#{}]({})'.format(pr, tiny_url)
    return res


def _gen_progress_table():
    header = '| Chương | Đóng góp |\n'
    spliter = '| --- | --- |\n'
    res = header + spliter
    for chapter_number in range(1, NUM_CHAPTERS + 1):
        chapter_path = _chapter_path_from_chapter_number(chapter_number)
        prs = CONTRIBUTIONS.get(chapter_number, [])
        title = _get_chapter_title(chapter_number)
        pr_links = ', '.join(_get_markdown_link_to_pr(pr) for pr in sorted(prs))
        markdown_table_row = '| [{}]({}) | {} |\n'.format(_remove_sharp(title), chapter_path, pr_links)
        res += markdown_table_row

    return res


def gen_readme():
    with codecs.open(README, 'w', encoding='utf-8') as readme:
        with codecs.open(README_PREFIX, 'r', encoding='utf-8') as readme_prefix:
            for line in readme_prefix:
                readme.write(line)
        readme.write(_gen_progress_table())


if __name__ == '__main__':
    main(vn_only=False)
    main(vn_only=True)
    gen_readme()
