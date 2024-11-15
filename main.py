from tools.arxiv_search import ArxivSearcher
from tools.plos_search import PlosSearcher 
from tools.pmc_search import PubMedSearcher

def main():
    # Initialize searchers with max results
    arxiv = ArxivSearcher(max_results=10)
    plos = PlosSearcher(max_results=10)
    pmc = PubMedSearcher(max_results=10)

    # Define query
    query = "ReAct for LLMs"
    # Example searches
    arxiv_results = arxiv.get_results(query)
    
    # PLOS requires a specific API URL format
    plos_url = f"https://api.plos.org/search?q=title:{query}&fl=id,abstract,title,author,publication_date,reference&wt=json"
    plos_results = plos.get_results(plos_url)
    
    pmc_results = pmc.get_results(query)

    # Print sample results
    print("\nArXiv Results:")
    for paper in arxiv_results[:2]:
        print(f"\nTitle: {paper.title}")
        print(f"Authors: {', '.join(paper.authors)}")
        print(f"Year: {paper.year}")

    print("\nPLOS Results:")
    for paper in plos_results[:2]:
        print(f"\nTitle: {paper.title}")
        print(f"Authors: {', '.join(paper.authors)}")
        print(f"Year: {paper.year}")

    print("\nPubMed Results:")
    for paper in pmc_results[:2]:
        print(f"\nTitle: {paper.title}")
        print(f"Authors: {', '.join(paper.authors)}")
        print(f"Year: {paper.year}")

if __name__ == "__main__":
    main() 