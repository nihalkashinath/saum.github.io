#!/usr/bin/env python3
"""Extract bold text and links from Word document."""

from docx import Document
import re

def extract_formatting(docx_path):
    """Extract text with formatting info."""
    
    doc = Document(docx_path)
    results = []
    
    for para in doc.paragraphs:
        for run in para.runs:
            text = run.text.strip()
            if text and run.bold:
                # Check if this looks like a link (contains URL-like text or is bracketed)
                if any(indicator in text.lower() for indicator in ['yatra', 'journey', 'guide', 'here', 'contact']):
                    results.append(f"BOLD: {text}")
    
    return results

if __name__ == "__main__":
    docx_file = r"C:\Users\nihal\0_Nihal - Personal Drive\Personal\Saum\Marketing\Website\_content-staging\Journey Guide - Ayodhya and Varanasi - V2.docx"
    
    try:
        bold_items = extract_formatting(docx_file)
        print("Found bold items that may be links:")
        for item in bold_items:
            print(item)
    except Exception as e:
        print(f"Error: {e}")
