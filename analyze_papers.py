import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from pdf_analyzer import download_pdf, extract_text_from_pdf, analyze_paper_text

def process_papers(json_file, limit=None):
    if not os.path.exists(json_file):
        return
    with open(json_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)
        
    # Example heuristic: sort by published date or select specific ones
    if limit:
        papers = papers[:limit]
        
    for p in papers:
        # Check if it's humanoid related (basic filter for the missed papers list which might have false positives)
        if "humanoid" not in p['title'].lower() and "robot" not in p['title'].lower() and "embodied" not in p['title'].lower():
            if "humanoid" not in p['summary'].lower():
                continue
                
        print(f"\nProcessing: {p['title']}")
        pdf_url = p['pdf_link'].replace('http://', 'https://')
        paper_id = p['id'].replace('/', '_')
        
        pdf_path = os.path.join('papers_pdf', f"{paper_id}.pdf")
        os.makedirs('papers_pdf', exist_ok=True)
        
        if not os.path.exists(pdf_path):
            download_pdf(pdf_url, pdf_path)
            
        if os.path.exists(pdf_path):
            text = extract_text_from_pdf(pdf_path)
            if text:
                analysis = analyze_paper_text(text)
                
                # Save markdown summary
                md_path = os.path.join('papers_pdf', f"{paper_id}_summary.md")
                with open(md_path, 'w', encoding='utf-8') as mf:
                    mf.write(f"# {p['title']}\n\n")
                    mf.write(f"**Authors:** {', '.join(p['authors'])}\n")
                    mf.write(f"**Link:** {p['link']}\n\n")
                    mf.write(f"## Abstract (from PDF parsing)\n{analysis.get('abstract', analysis.get('abstract_fallback',''))[:1500]}...\n\n")
                    mf.write(f"## Method / Approach (Snippets)\n{analysis.get('method', '')[:1500]}...\n\n")
                    mf.write(f"## Conclusion (Snippets)\n{analysis.get('conclusion', '')[:1000]}...\n")
                print(f"-> Saved summary to {md_path}")

if __name__ == '__main__':
    print("Processing Missed Papers (BeyondMimic, ZEST)...")
    process_papers('papers_missed.json', limit=5)
    
    print("\nProcessing Recent Papers (Top 10 max)...")
    process_papers('papers_recent.json', limit=10)
