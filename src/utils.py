"""Shared helpers for the cleaning notebooks."""
import re
import unicodedata


def homogenize_text(text: str) -> str:
    """Normalize product descriptions and search terms.

    Lower-cases the text, strips Spanish accents, removes non-alphanumeric
    characters and collapses repeated whitespace, so the same product is
    matched across days even when the retailer changes its formatting.
    """
    text = text.lower()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
