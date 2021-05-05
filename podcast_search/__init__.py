from dataclasses import dataclass

SEARCH_URL = "https://itunes.apple.com/search"

@dataclass
class Podcast:
    """Podcast metadata."""
    id: str
    name: str
    author: str
    url: str
    feed: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None


def search(name: str, limit: int = 5) -> List[Podcast]:
    """Search podcast by name."""
    params = {"term": name, "limit": limit, "media": "podcast"}
    response = _get(url=SEARCH_URL, params=params)
    return _parse(response)