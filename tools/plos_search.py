from typing import List, Dict, Any
import requests
from .base_searcher import BaseSearcher, Article, Reference

class PlosSearcher(BaseSearcher):
    def get_results(self, query: str) -> List[Article]:
        response = requests.get(query, headers={"User-Agent": "Research Buddy"})
        docs = response.json()['response']['docs']
        return self._process_documents(docs)
    
    def _process_documents(self, docs: List[Dict[str, Any]]) -> List[Article]:
        articles = []
        
        for doc in docs:
            references = []
            if "reference" in doc:
                references = self._process_references(doc["reference"])
                
            articles.append(Article(
                id=doc["id"],
                title=doc.get("title_display", doc.get("title", "")),
                authors=doc.get("author_display", []),
                summary=doc.get("abstract", [""])[0],
                year=doc.get("publication_date", "")[:4],
                url=f"https://doi.org/{doc['id']}",
                references=references
            ))
            
        return articles
    
    def _process_references(self, raw_references: List[str]) -> List[Reference]:
        references = []
        
        for ref in raw_references:
            if ref.strip() == '|  |  |':
                continue
                
            parts = ref.split('|')
            if len(parts) < 3:
                continue
                
            authors = [author.strip() for author in parts[0].replace("\n", "").split(",") if author.strip()]
            year = parts[1].strip()
            title = parts[2].strip() or parts[3].strip() if len(parts) > 3 else ""
            
            references.append(Reference(
                title=title,
                authors=authors,
                year=year,
                journal=parts[3].strip() if len(parts) > 3 else ""
            ))
            
        return references
