import requests
from typing import List


class OpenAlexReader:
    """OpenAlex Reader.
    Gets a search query, returns a list of Documents of the top corresponding scientific papers on OpenAlex.
    """

    def __init__(self) -> None:
        """Initialize with parameters."""

    @staticmethod
    def _fetch_open_alex_results(search_query: str, max_results: int):
        """Fetch top scientific papers from OpenAlex based on search query."""
        base_url = "https://api.openalex.org/works"
        params = {"search": search_query, "per_page": max_results, "mailto": "your-email@example.com"}
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from OpenAlex. Status code: {response.status_code}")
        return response.json().get("results", [])

    def retrieve_from_open_alex(self, user_query: str, max_results=3) -> List[dict]:
        """
        Returns a list of dicts with document metadata extracted from OpenAlex.
        Title, authors, date, archive id and abstract.
        """
        papers = self._fetch_open_alex_results(user_query, max_results=max_results)
        results = []
        for i, paper in enumerate(papers):
            try:
                paper_metadata = {
                    'title': paper.get('title', 'No title'),
                    'author': ", ".join([author.get('author', {}).get('display_name', 'Unknown') for author in
                                         paper.get('authorships', [])]),
                    'creation_date': paper['publication_date'],
                    'text': self.extract_abstract(paper.get('abstract_inverted_index', "")),
                    'source_database': 'open_alex'
                }
                results.append(paper_metadata)
            except:
                print(i, paper.get('doi'))
        return results

    @staticmethod
    def extract_abstract(abstract_inverted_index):
        """Convert an abstract_inverted_index into a readable text format.

        Args:
            abstract_inverted_index (dict): The abstract inverted index from OpenAlex.

        Returns:
            str: The reconstructed abstract as a plain text string.
        """
        if not abstract_inverted_index:
            return "No abstract available"
        # Initialize a list to hold the words based on their positions
        abstract_length = max(max(pos) for pos in abstract_inverted_index.values()) + 1
        abstract_words = [""] * abstract_length

        # Place each word into the correct position
        for word, positions in abstract_inverted_index.items():
            for pos in positions:
                abstract_words[pos] = word

        # Join the words to form the complete abstract text
        return ' '.join(word for word in abstract_words if word)


# USAGE EXAMPLE
"""
r = OpenAlexReader()
metadata = r.retrieve_from_open_alex(user_query="Transformers", max_results=2)
"""
