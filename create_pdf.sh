#!/bin/bash
python3 run.py
gs -q -dPrinted=false -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=machine_learning_yearning.pdf book_cover.pdf all_chapters.pdf acknowledgement.pdf
gs -q -dPrinted=false -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=machine_learning_yearning_vietnamese.pdf book_cover.pdf all_chapters_vietnamese_only.pdf acknowledgement.pdf 
