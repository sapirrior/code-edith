from ddgs import DDGS

def execute(query: str) -> str:
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(f"Title: {r.get('title')}\nURL: {r.get('href')}\nSnippet: {r.get('body')}")
        return "\n---\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search error: {e}"
