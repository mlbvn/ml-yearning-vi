import pdfkit
import os

os.system("grip chapters/all_chapters.md --export chapters/all_chapters.html;grip chapters/all_chapters_vietnamese_only.md --export chapters/all_chapters_vietnamese_only.html")

# Convert all_chapters.md to all_chapters.pdf
pdfkit.from_file('chapters/all_chapters.html', 'all_chapters.pdf')

# Convert all_chapters_vietnamese_only.md to all_chapters_vietnamese_only.pdf
pdfkit.from_file('chapters/all_chapters_vietnamese_only.html', 'all_chapters_vietnamese_only.pdf')

os.system("rm chapters/all_chapters_vietnamese_only.html;rm chapters/all_chapters.html;rm missfont.log")
