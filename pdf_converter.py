# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:48:01 2019

@author: Quang
"""

import codecs
from run import _get_title_from_file_path, _chapter_path_from_chapter_number
import os
import shutil
import pdfkit

WIN_USE = 0
LINUX_USE = 1

# PLEASE CHANGE THIS FLAG DEPENDING ON WHAT OS YOU ARE USING
usage_flag = LINUX_USE

# For windows user, please first install wkhtmltopdf to the directory below
if usage_flag == WIN_USE:
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

PARTS = [
    {'path': './chapters/p00_01_04.md', 'range': [1, 4]},
    {'path': './chapters/p01_05_12.md', 'range': [5, 12]},
    {'path': './chapters/p02_13_19.md', 'range': [13, 19]},
    {'path': './chapters/p03_20_27.md', 'range': [20, 27]},
    {'path': './chapters/p04_28_32.md', 'range': [28, 32]},
    {'path': './chapters/p05_33_35.md', 'range': [33, 35]},
    {'path': './chapters/p06_36_43.md', 'range': [36, 43]},
    {'path': './chapters/p07_44_46.md', 'range': [44, 46]},
    {'path': './chapters/p08_47_52.md', 'range': [47, 52]},
    {'path': './chapters/p09_53_57.md', 'range': [53, 57]},
    {'path': './chapters/p10_58.md', 'range': [58, 58]},
]


def _convert_title_to_link(title):
    title = title.lower()
    title = title.replace(" ", "-")
    title = title.replace(".", "")
    title = title.replace(":", "")
    title = title.replace("/", "")
    title = title.replace("?", "")
    title = title.replace(",", "")
    title = title.replace("#-", "#user-content-")
    return title


NO_PART_LIST = ['p{:02d}'.format(i) for i in range(0, 11)]
NO_CHAPTER_LIST = ['{:02d}'.format(i) for i in range(1, 59)]
ALL_CHAPTERS = "./chapters/all_chapters"
ALL_CHAPTERS_VN = "./chapters/all_chapters_vietnamese_only"


def main(vn_only=True):
    # extract list of all part titles and chapter titles
    part_list = []
    chapter_list = []
    path = ALL_CHAPTERS_VN if vn_only else ALL_CHAPTERS
    html_file = path + '.html'
    md_file = path + '.md'
    pdf_file = path[11:] + '.pdf'

    for part in PARTS:
        part_path = part['path']
        # Extract the original parth title
        part_title = _get_title_from_file_path(part_path)

        # Convert to the html link syntax
        part_list.append(_convert_title_to_link(part_title))

        start_chapter, end_chatper = part['range']
        for chapter_number in range(start_chapter, end_chatper + 1):
            chapter_path = _chapter_path_from_chapter_number(chapter_number)

            # Extract the original chapter title
            chapter_title = _get_title_from_file_path(chapter_path)
            # Convert to html link syntax
            chapter_list.append(_convert_title_to_link(chapter_title))

    # export mardown file to html file
    os.system("grip {} --export {}".format(md_file, html_file))

    f = codecs.open(html_file, "r", "utf-8", "html.parser")

    filedata = f.read()
    f.close()
     
    # Add an html code for new page before each part
    for part_name in NO_PART_LIST:
        filedata = filedata.replace(
            '<p><a name="user-content-%s"></a></p>' % part_name,
            '<div style="page-break-after: always;"></div>\r\n<p><a name="%s"></a></p>' % part_name
        )

    # Add an html code for new page before each chapter
    for chapter_name in NO_CHAPTER_LIST:
        filedata = filedata.replace(
            '<p><a name="user-content-%s"></a></p>' % chapter_name,
            '<div style="page-break-after: always;"></div>\r\n<p><a name="%s"></a></p>' % chapter_name
        )

    # Replace the correct link subsection of each part
    for order, part_name in enumerate(NO_PART_LIST):
        filedata = filedata.replace('#%s' % part_name, '%s' % part_list[order])

    # Replace the correct link subsection of each chapter
    for order, chapter_name in enumerate(NO_CHAPTER_LIST):
        filedata = filedata.replace('#%s' % chapter_name, '%s'% chapter_list[order])
    # Remove the ".md" title bar at begining
    filedata = filedata.replace(
        '<h3>\r\n                  <span class="octicon octicon-book"></span>\r\n                  %s.md\r\n                </h3>'%path[11:],
        ""
    )

    # Centering images in html_file by replace <p> with <p align="center"> for lines that have
    # <img> tag

    for line in filedata.splitlines():
        if "<img " in line:
            new_line = line.replace("<p>","<p align=\"center\">")
            filedata = filedata.replace(line, new_line)

    f = codecs.open(html_file, "w", "utf-8", "html.parser")

    f.write(filedata)
    f.close()

    # Convert html to pdf file
    if usage_flag == WIN_USE:
        pdfkit.from_file(html_file, pdf_file, configuration=config) 
    else:
        pdfkit.from_file(html_file, pdf_file)
    # Remove the created html file
    os.remove(html_file)


if __name__ == '__main__':
    main(vn_only=False)
    main(vn_only=True)

    # Remove the created __pycache__ folder
    shutil.rmtree("__pycache__")
