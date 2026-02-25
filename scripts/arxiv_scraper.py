import requests
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time

def search_arxiv(query, max_results=50):
    """Searches arXiv for papers matching the given query."""
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'search_query={urllib.parse.quote(query)}'
    start = 0
    sort_by = "sortBy=lastUpdatedDate&sortOrder=descending"
    
    url = f"{base_url}{search_query}&start={start}&max_results={max_results}&{sort_by}"
    print(f"Fetching from: {url}")
    
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        xml_data = response.content
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
        
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    papers = []
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.replace('\n', ' ').strip()
        summary = entry.find('atom:summary', ns).text.replace('\n', ' ').strip()
        published = entry.find('atom:published', ns).text
        paper_id = entry.find('atom:id', ns).text.split('/abs/')[-1]
        
        authors = []
        for author in entry.findall('atom:author', ns):
            name = author.find('atom:name', ns).text
            authors.append(name)
            
        link = entry.find('atom:id', ns).text
        pdf_link = link.replace('abs', 'pdf')
        
        papers.append({
            'id': paper_id,
            'title': title,
            'authors': authors,
            'published': published,
            'summary': summary,
            'link': link,
            'pdf_link': pdf_link
        })
        
    return papers

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Scrape arXiv for humanoid robot control papers.")
    parser.add_argument("--query", type=str, default="all:\"humanoid robot\" AND (all:control OR all:locomotion)", help="ArXiv query string")
    parser.add_argument("--max", type=int, default=100, help="Max results to fetch")
    parser.add_argument("--out", type=str, default="arxiv_results.json", help="Output file path")
    
    args = parser.parse_args()
    
    print(f"Searching arXiv for: {args.query}")
    results = search_arxiv(args.query, args.max)
    print(f"Found {len(results)} papers.")
    
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {args.out}")
