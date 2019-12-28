#!/bin/bash
python3 run.py
cd chapters
echo "build vn version"
gs -q -dPrinted=false -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=book_mly_with_cover_vn.pdf book_cover.pdf book_vn.pdf
echo "build en-vn version"
gs -q -dPrinted=false -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=book_mly_with_cover_en_vn.pdf book_cover.pdf book_en_vn.pdf
