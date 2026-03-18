"""
similarity.py
--------------
Utility functions for computing similarity scores between
numeric vectors or feature lists.

Used for:
- Comparing soil profiles
- Matching crop requirements
- Recommendation ranking
"""

from typing import List
import numpy as np


def similarity_score(a: List[float], b: List[float]) -> float:
    """
    Computes cosine similarity between two numeric vectors.

    Parameters
    ----------
    a : List[float]
        First feature vector
    b : List[float]
        Second feature vector

    Returns
    -------
    float
        Similarity score between 0 and 1
        (1 = identical, 0 = completely different)

    Raises
    ------
    ValueError
        If input vectors are empty or have different lengths
    """

    if not a or not b:
        raise ValueError("Input vectors must not be empty")

    if len(a) != len(b):
        raise ValueError("Input vectors must have the same length")

    vec_a = np.array(a, dtype=float)
    vec_b = np.array(b, dtype=float)

    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    similarity = np.dot(vec_a, vec_b) / (norm_a * norm_b)

    # Numerical safety
    return float(np.clip(similarity, 0.0, 1.0))