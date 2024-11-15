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
pip install requests beautifulsoup4 arxiv
```
```python
from search_toolkit import PubMedSearcher, PlosSearcher, ArxivSearcher

# Initialize searchers
pmc = PubMedSearcher(max_results=10)
plos = PlosSearcher(max_results=10)
arxiv = ArxivSearcher(max_results=10)

# Perform searches
pmc_results = pmc.get_results("machine learning")
plos_results = plos.get_results("your_plos_api_url")
arxiv_results = arxiv.get_results("artificial intelligence")
```

## 🔧 Components

### PubMed Central Searcher
- Accesses the EuropePMC API for open access papers
- Retrieves full text and structured references
- Handles XML parsing for content extraction

### PLOS Searcher
- Interfaces with PLOS API
- Processes structured reference information
- Manages pagination and result limits

### arXiv Searcher
- Implements arXiv API integration
- Supports relevance-based sorting
- Includes automatic deduplication

## 📊 Data Format

All searchers return results in a consistent format optimized for AI processing:

The results are returned in a standardized format, making it easy to integrate with other AI systems.
```python
{
    "id": "10.1234/example.2023.123",  # Unique paper identifier (e.g., DOI)
    "title": "Deep Learning Applications in Natural Language Processing",
    "author": ["Jane Smith", "John Doe", "Alice Johnson"],  # List of authors
    "summary": "This paper explores recent advances in applying deep learning techniques to natural language processing tasks...", 
    "year": "2023",  # Publication year
    "url": "https://doi.org/10.1234/example.2023.123",  # Direct link to paper
    "reference": [  # List of cited papers
        {
            "title": "Attention Is All You Need",
            "author": ["Vaswani, A.", "Shazeer, N.", "Parmar, N."],
            "year": "2017",
            "journal": "NeurIPS"
        },
        {
            "title": "BERT: Pre-training of Deep Bidirectional Transformers",
            "author": ["Devlin, J.", "Chang, M.W."],
            "year": "2019", 
            "journal": "NAACL"
        }
    ]
}
```


## 🚀 Features

- **Unified Interface**: Consistent API across all search providers
- **Rich Metadata**: Comprehensive paper information including references
- **AI-Optimized**: Structured output format for easy parsing
- **Configurable**: Adjustable result limits and search criteria
- **Error Handling**: Robust error management for API failures
- **Rate Limiting**: Built-in rate limit compliance

## 🛠️ Technical Details

### Supported Metadata
- Paper titles and DOIs
- Author information
- Abstracts and summaries
- Publication dates
- Reference lists
- Direct URLs to papers

### Search Capabilities
- Full-text search
- Author-based search
- Date range filtering
- Relevance sorting
- Deduplication

## Limitations
- Arxiv does not provide references in the API, so it is not included in the reference list.

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Related Projects

- [arxiv.py](https://github.com/lukasschwab/arxiv.py)
- [europepmc](https://europepmc.org/RestfulWebService)
- [PLOS API](https://api.plos.org/)