# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: extract_pdf_to_txt.py
# @date: 2020/07/01
import PyPDF2


def convert(input_filename: str, output_filename: str):
    with open(output_filename, "w", encoding="utf-8") as f:
        res = []
        with open(input_filename, "rb") as pdf_file:
            # 创建一个pdf阅读器对象
            pdfReader = PyPDF2.PdfFileReader(pdf_file)
            for n in range(pdfReader.numPages):
                # 创建页面对象
                pageObj = pdfReader.getPage(n)
                # 提取页面内容
                content: str = pageObj.extractText()
                res.append(content)
        for x in res:
            f.write(x)
            f.write("\n\n")


if __name__ == "__main__":
    convert("./pdf_files/1.pdf", "./results/1.txt")
