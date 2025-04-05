@echo off

set file_path="C:\Users~\csvdata_extraction_tool"

set file_name="list.csv"

py csvdata_extraction_tool.py %file_path% %file_name% 2 "C" >> result.txt
