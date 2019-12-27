# encoding=utf8
import codecs
import csv
import re
import sys
import os
import shutil
from collections import OrderedDict
import urllib.request
# import pdf_converter as pdf
import pdfkit


CHAPTERS_DIR = './chapters/'
BOOK_DIR = CHAPTERS_DIR
ACKNOWLEDGEMENT_PATH = './acknowledgement.md'

NO_PART_LIST = ['p{:02d}'.format(i) for i in range(0, 11)]
NO_CHAPTER_LIST = ['ch{:02d}'.format(i) for i in range(1, 59)]

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

def _convert_html_to_pdf(html_file, pdf_file):
    print("Convert html file {} to pdf file {}".format(html_file, pdf_file))
    pdfkit.from_file(html_file, pdf_file)


class Book(object):
    def __init__(self):
        self.en_vi_md_path = self._get_path('myl_en_vi.md')
        self.vi_md_path = self._get_path('myl_vi.md')
        self.en_vi_pdf_path = self._get_path('myl_en_vi.pdf')
        self.vi_pdf_path = self._get_path('myl_vi.pdf')

    @staticmethod
    def _get_path(filename):
        return os.path.join(BOOK_DIR, filename)

    def build_all(self):
        self.build_all_md(vn_only=True)
        self.build_all_md(vn_only=False)
        self.build_all_pdf(vn_only=True)
        # self.build_all_pdf(vn_only=False)

    def build_all_md(self, vn_only):
        output_filename = self.vi_md_path if vn_only else self.en_vi_md_path
        with codecs.open(output_filename, 'w', encoding='utf-8') as file_writer:
            # Cover.add_md(file_writer)
            TableOfContent().add_md(file_writer)
            MainContent(vn_only).add_md(file_writer)
            # Glossary.add_md(file_writer)
            # Acknowledgement().add_md(file_writer)
            file_writer.write('\n\n')

    def build_all_pdf(self, vn_only):
        md_file = self.vi_md_path if vn_only else self.en_vi_md_path
        # extract list of all part titles and chapter titles
        part_list = []
        path = md_file
        chapter_list = []
        html_file = md_file.replace('.md', '.html')
        pdf_file = md_file.replace('.md', '.pdf')

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
        os.system("python3 -m grip {} --export {}".format(md_file, html_file))

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

        _convert_html_to_pdf(html_file, pdf_file)
        # Remove the created html file
        # os.remove(html_file)
        print(html_file)


class BookPart(object):
    def __init__(self, vn_only=True):
        self.vn_only = vn_only

    def _get_content_lines_md(self):
        """a list of markdown lines to be written, must be implemented in subclasses"""
        raise NotImplementedError

    def _get_content_lines_html(self):
        """a list of markdown lines to be written, must be implemented in subclasses"""
        raise NotImplementedError

    def add_md(self, file_writer):
        for line in self._get_content_lines_md(): 
            file_writer.write(line)

    def add_html(self, file_writer):
        for line in self._get_content_lines_html(): 
            file_writer.write(line)


class TableOfContent(BookPart):
    def __init__(self, vn_only=True):
        super().__init__(vn_only=vn_only)

    def _get_content_lines_md(self):
        lines = []
        lines.append("**MỤC LỤC**\n")
        for part in PARTS:
            part_path = part['path']
            lines.append(self.get_toc_line(part_path, level=0))
            start_chapter, end_chatper = part['range']
            for chapter_number in range(start_chapter, end_chatper + 1):
                chapter_path = _chapter_path_from_chapter_number(chapter_number)
                lines.append(self.get_toc_line(chapter_path, level=1))
        # ack
        lines.append(Acknowledgement.toc_line())
        return lines

    def _get_content_lines_html(self):
        pass

    def get_toc_line(self, path, level):
        part_title = _get_title_from_file_path(path)
        filename = os.path.basename(path)
        link = _get_label_from_filename(filename)
        
        full_link = "[{display_text}]({link_to_chapter})".format(
            display_text=_remove_sharp(part_title),
            link_to_chapter=link
        )
        return '\t'*level + '* ' + full_link + '\n'


class MainContent(BookPart):
    def __init__(self, vn_only=True):
        super().__init__(vn_only=vn_only)

    def _get_content_lines_md(self):
        lines = []
        for part in PARTS:
            part_path = part['path']
            lines.extend(self._insert_content(part_path, heading=1))
            start_chapter, end_chatper = part['range']
            for chapter_number in range(start_chapter, end_chatper + 1):
                chapter_path = _chapter_path_from_chapter_number(chapter_number)
                lines.extend(self._insert_content(chapter_path, heading=2))
        return lines

    def _insert_content(self, file_path, heading):
        lines = []
        lines.append('<!-- ================= Insert {} ================= -->\n'.format(file_path))
        lines.append(
            '<!-- Please do not edit this file directly, edit in {} instead -->\n'.format(file_path)
        )
        
        filename = os.path.basename(file_path)
        lines.append('<a name="{}"></a>\n'.format(_get_label_from_filename(filename)))
        with codecs.open(file_path, 'r', encoding='utf-8') as one_file:
            for line in one_file:
                if self.vn_only and line.startswith('>'):
                    continue
                try:
                    if line.startswith('# '):
                        line = '#'*heading + ' ' + line[len('# '):]
                    elif line.startswith('> # '):
                        line = '> ' + '#'*heading + ' ' + line[len('> # '):]
                    lines.append(line)
                except UnicodeDecodeError as e:
                    print('Line with decode error:')
                    print(e)
        lines.append('\n')
        return lines


class Acknowledgement(BookPart):
    label = 'ack'

    def __init__(self, vn_only=True):
        super().__init__(vn_only=vn_only)

    @classmethod
    def toc_line(cls):
        return "* [Lời cảm ơn](#{})\n".format(cls.label)

    def _get_content_lines_md(self):
        lines = []
        lines.append('<a name="{}"></a>\n'.format(self.label))
        with codecs.open(ACKNOWLEDGEMENT_PATH, 'r', encoding='utf-8') as ack_file:
            for line in ack_file:
                lines.append(line)
        return lines




def _get_label_from_filename(chapter_or_part_filename):
    if chapter_or_part_filename.startswith('p'):
        return chapter_or_part_filename[:3]  # pxx
    elif chapter_or_part_filename.startswith('ch'):
        return chapter_or_part_filename[:4]  # chxx
    else:
        assert False, chapter_or_part_filename


# def main(vn_only=True):
#     if vn_only:
#         output_filename = os.path.join(CHAPTERS_DIR, ALL_CHAPTERS_VN_FILENAME)
#     else:
#         output_filename = os.path.join(CHAPTERS_DIR, ALL_CHAPTERS_FILENAME)
#     with codecs.open(output_filename, 'w', encoding='utf-8') as all_file_writer:
#         # table of content
#         all_file_writer.write("**MỤC LỤC**\n\n")
#         for part in PARTS:
#             part_path = part['path']
#             _insert_to_toc(all_file_writer, part_path, level=0)
#             start_chapter, end_chatper = part['range']
#             for chapter_number in range(start_chapter, end_chatper + 1):
#                 chapter_path = _chapter_path_from_chapter_number(chapter_number)
#                 _insert_to_toc(all_file_writer, chapter_path, level=1)

#         # main content
#         for part in PARTS:
#             part_path = part['path']
#             _insert_content(all_file_writer, part_path, vn_only, heading=1)
#             start_chapter, end_chatper = part['range']
#             for chapter_number in range(start_chapter, end_chatper + 1):
#                 chapter_path = _chapter_path_from_chapter_number(chapter_number)
#                 _insert_content(all_file_writer, chapter_path, vn_only, heading=2)


def _remove_sharp(title):
    assert title.startswith('# ')
    return title[len('# '):]


def _get_title_from_file_path(part_path):
    with codecs.open(part_path, 'r', encoding='utf-8') as one_file:
        for line in one_file:
            if line.startswith('# '):
                line = line.strip()
                return line
    assert False, part_path


def is_part(path_name):
    assert path_name[1] in ['p', 'c'], path_name
    return path_name[1] == "p"


def _insert_to_toc(all_file_writer, part_path, level):
    all_file_writer.write(TableOfContent().get_toc_line(part_path, level))


def _insert_content(all_file_writer, file_path, vn_only, heading):
    all_file_writer.write('<!-- ============================ Insert {} =================================== -->\n'.format(file_path))
    all_file_writer.write(
        '<!-- Please do not edit this file directly, edit in {} instead -->\n'.format(file_path)
    )
    
    # Create subsection link with number instead of vietnamese
    path_name = file_path[file_path.index("s")+1:]
    
    if is_part(path_name):
        all_file_writer.write('<a name="%s"></a>\n'%path_name[1:4])
    else:
        all_file_writer.write('<a name="%s"></a>\n'%path_name[3:5])
    with codecs.open(file_path, 'r', encoding='utf-8') as one_file:
        for line in one_file:
            if vn_only and line.startswith('>'):
                continue
            try:
                if line.startswith('# '):
                    line = '#'*heading + ' ' + line[len('# '):]
                elif line.startswith('> # '):
                    line = '> ' + '#'*heading + ' ' + line[len('> # '):]
                all_file_writer.write(line)
            except UnicodeDecodeError as e:
                print('Line with decode error:')
                print(e)
    all_file_writer.write('\n')


def _chapter_path_from_chapter_number(chapter_number):
    return os.path.join(CHAPTERS_DIR, 'ch{:02d}.md'.format(chapter_number))


def creat_pdf(vn_only=True):
    # extract list of all part titles and chapter titles
    part_list = []
    chapter_list = []
    path = Book().vi_md_path() if vn_only else Book().en_vi_md_path()
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
    os.system("python3 -m grip {} --export {}".format(md_file, html_file))

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

    _convert_html_to_pdf(html_file, pdf_file)
    # Remove the created html file
    # os.remove(html_file)

def create_pdfs():
    create_pdf(vn_only=False)
    create_pdf(vn_only=True)

    # Remove __pycache__ folder  
    shutil.rmtree("__pycache__")


if __name__ == '__main__':
    Book().build_all()
    # main(vn_only=False)
    # main(vn_only=True)
    # create_pdfs()
