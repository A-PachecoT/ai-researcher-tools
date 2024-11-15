import requests
import bs4 as bs

class PubMedSearcher:
    def __init__(self, query, max_results=10):
        self.ops_pmc = []
        self.max_results = max_results
    def get_results(self, query):
      url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
      params = {
          "query": query,
          "format": "json",
          "pageSize": self.max_results
      }
      response = requests.get(url, params=params)
      data = response.json()
      return self.get_cleaned_data(data)
    def get_cleaned_data(self, data):
      for result in data["resultList"]["result"]:
        if result.get("isOpenAccess") == "Y":
          # Skip if no DOI or PMCID
          if not (result.get("doi") and result.get("pmcid")):
              continue
              
          doi = result["doi"]
          pmcid = result["pmcid"]
          content_url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
          url_ref = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{result['source']}/{result['id']}/references?format=json"
          
          # Get references
          references = requests.get(url_ref).json()
          references_list = []
          if "referenceList" in references and "reference" in references["referenceList"]:
              for elem in references["referenceList"]["reference"]:
                  references_list.append({
                      "title": elem.get("title", ""),
                      "author": elem.get("authorString", ""),
                      "year": elem.get("pubYear", ""),
                      "journal": elem.get("journalAbbreviation", "")
                  })
          
          # Get content and abstract
          response = requests.get(content_url)
          content_xml = bs.BeautifulSoup(response.text, 'lxml')
          abstract_elem = content_xml.find('abstract')
          summary = abstract_elem.get_text() if abstract_elem else result.get("abstractText", "No abstract available")
          
          authors = result.get("authorString", "").split(", ")
          self.ops_pmc.append({
              "id": doi,
              "title": result.get("title", ""),
              "author": authors,
              "summary": summary,
              "year": result.get("pubYear", ""),
              "url": f"https://doi.org/{doi}",
              "reference": references_list
          })
      return self.ops_pmc