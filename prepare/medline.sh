#!/bin/sh
# This tool reads PubMed citation XML from STDIN, and extracts extracts abstract text.
grep '<AbstractText>' | sed -e 's/<AbstractText>//g' | sed -e 's/<\/AbstractText>//g'
