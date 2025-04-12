"""
This code will combine multiple PDF files into a single PDF.
The pdf files that are to be combined are expected to be in a common folder.
The folder of the files to be combined is an argument to this module.
The output file name of the combined file is an argument to this module.
It is expected that the naming convention of each pdf file is consistent with
a naming style that is case-sensitive and increments numerically sequentially per page.
"""

from pypdf import PdfReader, PdfWriter
import os
import argparse


def merge_pdfs(pdf_list, output_path):
    """
    This function will take a list of pdfs
    and combine them into a single pdf
    at the defined output path.

    Parameters
    ----------
    pdf_list : list
        This is a list of PDF files.
    output_path : string
        This is the path of the combined final PDF.
    """
    writer = PdfWriter()

    for pdf_file in pdf_list:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Merged PDF saved to: {output_path}")


def main():
    """
    This is the main driver of the python file.
    """
    parser = argparse.ArgumentParser(description="Merge multiple PDFs into one.")
    parser.add_argument(
        "-f", "--folder", required=True, help="Path to the folder containing PDF files"
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output file path for the merged PDF"
    )
    args = parser.parse_args()

    folder_path = args.folder
    output_file = args.output

    pdf_files = [
        os.path.join(folder_path, f)
        for f in sorted(os.listdir(folder_path))
        if f.endswith(".pdf")
    ]

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()
