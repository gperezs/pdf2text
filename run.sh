# Script for converting pdf news files to text
# [GPS - 05/13/2019]

mkdir -p pdfs/images
mkdir -p converted_text/
cd pdfs

find . -type f -name '*.pdf' -print0 |
  while IFS= read -r -d '' file
    do convert -density 300 -resize 100% "${file}" "images/${file%.*}.png"
  done
cd ..

python extract_text.py
