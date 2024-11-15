from typing import List
import arxiv
from .base_searcher import BaseSearcher, Article, Reference

class ArxivSearcher(BaseSearcher):
    def __init__(self, max_results: int = 10, criterion: arxiv.SortCriterion = arxiv.SortCriterion.Relevance):
        super().__init__(max_results)
        self.client = arxiv.Client()
        self.criterion = criterion

    def get_results(self, query: str) -> List[Article]:
        search = arxiv.Search(
            query=query,
            max_results=self.max_results,
            sort_by=self.criterion
        )
        
        results = list(self.client.results(search))
        articles = []
        seen_ids = set()
        
        for result in results:
            if result.entry_id in seen_ids:
                continue
                
            seen_ids.add(result.entry_id)
            articles.append(Article(
                title=result.title,
                authors=[author.name for author in result.authors],
                summary=result.summary,
                year=str(result.updated.year),
                url=result.entry_id,
                references=[],
                id=result.entry_id
            ))
            
        return articles