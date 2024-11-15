from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Reference:
    title: str
    authors: List[str]
    year: str
    journal: str = ""

@dataclass
class Article:
    title: str
    authors: List[str]
    summary: str
    year: str
    url: str
    references: List[Reference]
    id: str = ""

class BaseSearcher(ABC):
    def __init__(self, max_results: int = 10):
        self.max_results = max_results
        
    @abstractmethod
    def get_results(self, query: str) -> List[Article]:
        """Search and return articles matching the query"""
        pass 