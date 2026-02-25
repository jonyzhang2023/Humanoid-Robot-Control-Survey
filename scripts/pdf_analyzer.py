import os
import requests
import fitz  # PyMuPDF
import json
import argparse

def download_pdf(url, output_path):
    print(f"Downloading from {url}...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved to {output_path}")
        return True
    else:
        print(f"Failed to download. Status code: {response.status_code}")
        return False

def extract_text_from_pdf(pdf_path):
    print(f"Extracting text from {pdf_path}...")
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text() + "\n"
        return text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None

def analyze_paper_text(text):
    """Basic structural extraction to slice out abstract, methodology, and conclusion if possible."""
    sections = {
        "abstract": "",
        "method": "",
        "conclusion": ""
    }
    
    lines = text.split('\n')
    current_section = None
    
    for line in lines:
        line_lower = line.strip().lower()
        if "abstract" in line_lower and len(line_lower) < 20:
            current_section = "abstract"
            continue
        elif ("method" in line_lower or "approach" in line_lower) and len(line_lower) < 25:
            current_section = "method"
            continue
        elif "conclusion" in line_lower and len(line_lower) < 20:
            current_section = "conclusion"
            continue
        elif "references" in line_lower and len(line_lower) < 15:
            current_section = None
            
        if current_section:
            sections[current_section] += line + " "

    # Clean up excess whitespace
    for k in sections:
        sections[k] = sections[k].strip()
    
    # If abstract parsing failed (e.g. format issues), grab the first 1500 chars as a fallback
    if not sections["abstract"]:
        sections["abstract_fallback"] = text[:1500].replace('\n', ' ').strip()

    return sections

def main():
    parser = argparse.ArgumentParser(description="Download and analyze PDF papers.")
    parser.add_argument("--url", type=str, required=True, help="PDF URL to download")
    parser.add_argument("--id", type=str, required=True, help="Paper ID (used for filename)")
    parser.add_argument("--outdir", type=str, default="papers_pdf", help="Output directory for PDFs")
    
    args = parser.parse_args()
    
    os.makedirs(args.outdir, exist_ok=True)
    pdf_path = os.path.join(args.outdir, f"{args.id}.pdf")
    
    if not os.path.exists(pdf_path):
        success = download_pdf(args.url, pdf_path)
        if not success:
            return
    else:
        print(f"PDF {pdf_path} already exists. Skipping download.")
        
    text = extract_text_from_pdf(pdf_path)
    if text:
        analysis = analyze_paper_text(text)
        analysis['raw_length'] = len(text)
        
        info_path = os.path.join(args.outdir, f"{args.id}_info.json")
        with open(info_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)
        print(f"Analysis saved to {info_path}")
        print(f"Abstract preview: {analysis.get('abstract', analysis.get('abstract_fallback', ''))[:200]}...")

if __name__ == "__main__":
    main()
