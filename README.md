# AI Search Toolkit

A comprehensive Python toolkit designed to enable AI agents to search and retrieve academic papers across multiple scholarly databases. This toolkit provides unified access to PubMed Central (PMC), PLOS, and arXiv, making it easier for AI systems to gather and process academic research.

## 🎯 Purpose

This toolkit addresses the need for AI agents to efficiently access and process academic literature by:
- Providing a standardized interface across multiple academic databases
- Handling authentication and API interactions
- Normalizing data formats for consistent processing
- Managing rate limits and API constraints
- Enabling efficient deduplication of results

## 👥 Team

| Role            | Name             | GitHub                                              |
|----------------|------------------|-----------------------------------------------------|
| Main Developer | Jared Orihuela   | [@JaocHatter](https://github.com/JaocHatter)       |
| Maintainer     | André Pacheco    | [@A-PachecoT](https://github.com/A-PachecoT)       |

## ⚡ Quick Start
```bash
pip install requests beautifulsoup4 arxiv lxml
```
Or install all dependencies:
```bash
pip install -r requirements.txt
```

```python
from tools.arxiv_search import ArxivSearcher
from tools.plos_search import PlosSearcher
from tools.pmc_search import PubMedSearcher

# Initialize searchers
pmc = PubMedSearcher(max_results=10)
plos = PlosSearcher(max_results=10)
arxiv = ArxivSearcher(max_results=10)

# Perform searches
query = "machine learning"
pmc_results = pmc.get_results(query)
plos_results = plos.get_results(query)
arxiv_results = arxiv.get_results(query)
```

## 🔧 Components

### Base Searcher
- Abstract base class defining the interface for all searchers
- Standardizes result format and search parameters
- Enforces consistent implementation across providers

### PubMed Central Searcher
- Accesses the EuropePMC API for open access papers
- Retrieves full text and structured references
- Handles XML parsing for content extraction
- Focuses on open access content with DOIs and PMCIDs

### PLOS Searcher
- Interfaces with PLOS API
- Processes structured reference information
- Provides title-based search functionality

### arXiv Searcher
- Implements arXiv API integration via arxiv.py
- Supports relevance-based sorting
- Includes automatic deduplication of results

## 📊 Data Structure

All searchers return results using these standardized dataclasses:

```python
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
```

## 🚀 Features

- **Unified Interface**: Common BaseSearcher abstract class
- **Rich Metadata**: Comprehensive paper information including references where available
- **Configurable**: Adjustable result limits and search criteria
- **Error Handling**: Built-in error management
- **Deduplication**: Automatic removal of duplicate results (implemented in ArXiv searcher)

## Limitations
- ArXiv API does not provide reference information
- PLOS search is currently limited to title-based queries
- PubMed Central searcher only retrieves open access articles

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
