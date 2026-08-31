#!/usr/bin/env python3
"""Extract content from Word document for blog conversion."""

from docx import Document
import sys

def extract_word_content(docx_path, output_path):
    """Extract text and image references from Word document."""
    
    try:
        doc = Document(docx_path)
        content = []
        
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                # Check if it's an image reference
                if text.startswith('[Image:') or text.startswith('[image:'):
                    content.append(text)
                else:
                    content.append(text)
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        
        print(f"Successfully extracted {len(content)} paragraphs")
        return True
    finally:
        # Ensure document object is cleaned up
        doc = None

if __name__ == "__main__":
    docx_file = r"C:\Users\nihal\0_Nihal - Personal Drive\Personal\Saum\Marketing\Website\_content-staging\Journey Guide - Ayodhya and Varanasi - V2.docx"
    output_file = r"C:\Users\nihal\0_Nihal - Personal Drive\Personal\Saum\Marketing\Website\_content-staging\extracted-content.txt"
    
    try:
        extract_word_content(docx_file, output_file)
        print(f"Content saved to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
