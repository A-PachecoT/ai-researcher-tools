from typing import List, Dict, Any
import requests
import bs4 as bs
from .base_searcher import BaseSearcher, Article, Reference

class PubMedSearcher(BaseSearcher):
    def get_results(self, query: str) -> List[Article]:
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        params = {
            "query": query,
            "format": "json",
            "pageSize": self.max_results
        }
        response = requests.get(url, params=params)
        data = response.json()
        return self._process_results(data)
    
    def _process_results(self, data: Dict[str, Any]) -> List[Article]:
        articles = []
        
        for result in data["resultList"]["result"]:
            if not (result.get("isOpenAccess") == "Y" and result.get("doi") and result.get("pmcid")):
                continue
                
            doi = result["doi"]
            pmcid = result["pmcid"]
            
            summary = self._get_article_content(pmcid)
            references = self._get_article_references(result['source'], result['id'])
            
            articles.append(Article(
                id=doi,
                title=result.get("title", ""),
                authors=result.get("authorString", "").split(", "),
                summary=summary,
                year=result.get("pubYear", ""),
                url=f"https://doi.org/{doi}",
                references=references
            ))
            
        return articles
    
    def _get_article_content(self, pmcid: str) -> str:
        content_url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
        response = requests.get(content_url)
        content_xml = bs.BeautifulSoup(response.text, 'lxml')
        abstract_elem = content_xml.find('abstract')
        return abstract_elem.get_text() if abstract_elem else "No abstract available"
    
    def _get_article_references(self, source: str, article_id: str) -> List[Reference]:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{source}/{article_id}/references?format=json"
        response = requests.get(url)
        data = response.json()
        
        references = []
        if "referenceList" in data and "reference" in data["referenceList"]:
            for ref in data["referenceList"]["reference"]:
                references.append(Reference(
                    title=ref.get("title", ""),
                    authors=ref.get("authorString", "").split(", "),
                    year=ref.get("pubYear", ""),
                    journal=ref.get("journalAbbreviation", "")
                ))
                
        return references