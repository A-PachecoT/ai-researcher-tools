import requests

class PlosSearcher:
  def __init__(self, max_results=10):
    self.ops_plos = []
  def get_results(self, query):
    # The query is the URL
    plos_response = requests.get(query, headers = {"User-Agent":"Research Buddy"})
    docs_ = plos_response.json()['response']['docs']
    return self.get_cleaned_data(docs_)
  def get_cleaned_data(self, docs_):
    for elem in docs_:
      content = {}
      content["id"] = elem["id"] # doi
      content["title"] = elem["title_display"] if "title_display" in elem else elem["title"]
      content["author"] = elem["author_display"] if "author_display" in elem else []
      content["summary"] = elem["abstract"][0] if "abstract" in elem else ""
      content["year"] = elem["publication_date"][:4] if "publication_date" in elem else ""
      content["url"] = "https://doi.org/"+elem["id"]
      content["reference"] = []  # Initialize empty references list
      
      # Only process references if they exist
      if "reference" in elem:
        cleaned_data = [item for item in elem["reference"] if item.strip() != '|  |  |']
        for paper in cleaned_data:
          parts = paper.split('|')
          authors = [author.strip() for author in parts[0].replace("\n", "").split(",") if author.strip()]
          year = parts[1].strip() if len(parts) > 1 else None
          title = parts[2].strip() if len(parts) > 2 else None
          topic = parts[3].strip() if len(parts) > 3 else None
          if title == "":
            title = topic
          paper_dict = {
              'title': title,
              'author': authors,
              'year': year,
              'journal': topic
          }
          content["reference"].append(paper_dict)
          
      self.ops_plos.append(content)
    return self.ops_plos
