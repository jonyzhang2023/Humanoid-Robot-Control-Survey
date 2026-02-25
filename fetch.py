import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from arxiv_scraper import search_arxiv
import json

def fetch_and_save():
    query1 = 'all:"humanoid robot" AND (all:control OR all:locomotion OR all:reinforcement)'
    results1 = search_arxiv(query1, max_results=50)
    with open('papers_recent.json', 'w', encoding='utf-8') as f:
        json.dump(results1, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(results1)} recent papers.")

if __name__ == '__main__':
    fetch_and_save()
