"""
Data Analyzer Mini Project
"""

from typing import List, Dict, Any
import numpy as np
from collections import Counter


class DataAnalyzer:
    """Reusable class for analyzing tabular data."""

    def __init__(self, records: List[Dict[str, Any]]):
        if not records:
            raise ValueError("Records list cannot be empty")
        self.records = records

    def get_numeric_statistics(self, key: str) -> Dict[str, float]:
        """Return statistics for a numeric column."""
        values = [r[key] for r in self.records if isinstance(r.get(key), (int, float))]
        if not values:
            return {"count": 0}
        
        return {
            "count": len(values),
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
            "min": float(np.min(values)),
            "max": float(np.max(values)),
            "median": float(np.median(values))
        }

    def remove_outliers(self, key: str, threshold: float = 2.0) -> List[Dict[str, Any]]:
        """Remove outliers using z-score method."""
        values = np.array([r[key] for r in self.records if isinstance(r.get(key), (int, float))])
        if len(values) == 0:
            return self.records[:]
        
        mean = np.mean(values)
        std = np.std(values)
        if std == 0:
            return self.records[:]
        
        z_scores = np.abs((values - mean) / std)
        mask = z_scores <= threshold
        return [self.records[i] for i in range(len(self.records)) if mask[i]]

    def most_frequent(self, key: str, top_n: int = 5) -> List[tuple]:
        """Return most frequent values for a field."""
        values = [r[key] for r in self.records if key in r]
        return Counter(values).most_common(top_n)


# Example usage
if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": 25, "score": 85},
        {"name": "Bob", "age": 30, "score": 92},
        {"name": "Charlie", "age": 25, "score": 78},
        {"name": "Diana", "age": 35, "score": 95},
        {"name": "Eve", "age": 28, "score": 88},
        {"name": "Frank", "age": 40, "score": 110},
    ]

    analyzer = DataAnalyzer(sample_data)

    print("Age statistics:", analyzer.get_numeric_statistics("age"))
    print("Score statistics:", analyzer.get_numeric_statistics("score"))
    print("Most frequent ages:", analyzer.most_frequent("age"))
    print("Data without outliers (score):", analyzer.remove_outliers("score", threshold=1.5))