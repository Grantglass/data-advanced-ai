"""
Evaluation Helper Functions

Utilities for evaluating LLM outputs using various metrics.
"""

from typing import List, Dict, Optional
import numpy as np
from collections import Counter
import re


def calculate_bleu(reference: str, candidate: str, n: int = 4) -> float:
    """
    Calculate BLEU score (simplified implementation).

    Args:
        reference: Reference text
        candidate: Candidate text to evaluate
        n: Maximum n-gram size

    Returns:
        float: BLEU score (0-1)
    """
    def get_ngrams(text: str, n: int) -> Counter:
        words = text.lower().split()
        return Counter([tuple(words[i:i+n]) for i in range(len(words)-n+1)])

    scores = []
    for i in range(1, n+1):
        ref_ngrams = get_ngrams(reference, i)
        cand_ngrams = get_ngrams(candidate, i)

        if not cand_ngrams:
            scores.append(0.0)
            continue

        matches = sum((cand_ngrams & ref_ngrams).values())
        total = sum(cand_ngrams.values())
        scores.append(matches / total if total > 0 else 0)

    # Geometric mean
    if all(s > 0 for s in scores):
        bleu = np.exp(np.mean([np.log(s) for s in scores]))
    else:
        bleu = 0.0

    # Apply brevity penalty
    ref_len = len(reference.split())
    cand_len = len(candidate.split())
    if cand_len < ref_len:
        bp = np.exp(1 - ref_len/cand_len)
    else:
        bp = 1.0

    return bleu * bp


def calculate_rouge(reference: str, candidate: str, variant: str = "rouge-1") -> float:
    """
    Calculate ROUGE score (simplified implementation).

    Args:
        reference: Reference text
        candidate: Candidate text
        variant: ROUGE variant ("rouge-1", "rouge-2", "rouge-l")

    Returns:
        float: ROUGE score (0-1)
    """
    def get_tokens(text: str) -> List[str]:
        return text.lower().split()

    def lcs_length(seq1: List[str], seq2: List[str]) -> int:
        m, n = len(seq1), len(seq2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i-1] == seq2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

    ref_tokens = get_tokens(reference)
    cand_tokens = get_tokens(candidate)

    if variant == "rouge-l":
        lcs_len = lcs_length(ref_tokens, cand_tokens)
        if len(cand_tokens) == 0:
            return 0.0
        precision = lcs_len / len(cand_tokens)
        recall = lcs_len / len(ref_tokens) if len(ref_tokens) > 0 else 0
        if precision + recall == 0:
            return 0.0
        f1 = 2 * precision * recall / (precision + recall)
        return f1

    elif variant == "rouge-1":
        ref_set = set(ref_tokens)
        cand_set = set(cand_tokens)
        overlap = len(ref_set & cand_set)
        return overlap / len(ref_set) if ref_set else 0.0

    elif variant == "rouge-2":
        ref_bigrams = set(zip(ref_tokens[:-1], ref_tokens[1:]))
        cand_bigrams = set(zip(cand_tokens[:-1], cand_tokens[1:]))
        overlap = len(ref_bigrams & cand_bigrams)
        return overlap / len(ref_bigrams) if ref_bigrams else 0.0

    return 0.0


def calculate_similarity(text1: str, text2: str, method: str = "jaccard") -> float:
    """
    Calculate similarity between two texts.

    Args:
        text1: First text
        text2: Second text
        method: Similarity method ("jaccard", "cosine", "overlap")

    Returns:
        float: Similarity score (0-1)
    """
    def tokenize(text: str) -> set:
        return set(text.lower().split())

    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    if method == "jaccard":
        intersection = len(tokens1 & tokens2)
        union = len(tokens1 | tokens2)
        return intersection / union if union > 0 else 0.0

    elif method == "overlap":
        intersection = len(tokens1 & tokens2)
        min_len = min(len(tokens1), len(tokens2))
        return intersection / min_len if min_len > 0 else 0.0

    elif method == "cosine":
        all_words = list(tokens1 | tokens2)
        vec1 = [1 if word in tokens1 else 0 for word in all_words]
        vec2 = [1 if word in tokens2 else 0 for word in all_words]

        dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
        mag1 = np.sqrt(sum(v * v for v in vec1))
        mag2 = np.sqrt(sum(v * v for v in vec2))

        return dot_product / (mag1 * mag2) if (mag1 * mag2) > 0 else 0.0

    return 0.0


def create_evaluation_report(
    results: List[Dict],
    metrics: List[str] = ["bleu", "rouge-1", "rouge-l"]
) -> Dict:
    """
    Create a comprehensive evaluation report.

    Args:
        results: List of evaluation results
        metrics: Metrics to include in report

    Returns:
        Dict with aggregated statistics
    """
    if not results:
        return {}

    report = {
        "num_samples": len(results),
        "metrics": {}
    }

    # Calculate statistics for each metric
    for metric in metrics:
        values = [r.get(metric, 0) for r in results if metric in r]

        if values:
            report["metrics"][metric] = {
                "mean": np.mean(values),
                "median": np.median(values),
                "std": np.std(values),
                "min": np.min(values),
                "max": np.max(values)
            }

    # Add best and worst performing samples
    if results and any(metrics):
        primary_metric = metrics[0]
        sorted_results = sorted(results, key=lambda x: x.get(primary_metric, 0), reverse=True)

        report["best_sample"] = sorted_results[0] if sorted_results else None
        report["worst_sample"] = sorted_results[-1] if sorted_results else None

    return report


def evaluate_multiple_outputs(
    reference: str,
    candidates: Dict[str, str],
    metrics: Optional[List[str]] = None
) -> Dict[str, Dict]:
    """
    Evaluate multiple candidate outputs against a reference.

    Args:
        reference: Reference text
        candidates: Dict of {name: candidate_text}
        metrics: List of metrics to calculate

    Returns:
        Dict with evaluation results for each candidate
    """
    if metrics is None:
        metrics = ["bleu", "rouge-1", "rouge-l", "similarity"]

    results = {}

    for name, candidate in candidates.items():
        scores = {}

        if "bleu" in metrics:
            scores["bleu"] = calculate_bleu(reference, candidate)

        if "rouge-1" in metrics:
            scores["rouge-1"] = calculate_rouge(reference, candidate, "rouge-1")

        if "rouge-2" in metrics:
            scores["rouge-2"] = calculate_rouge(reference, candidate, "rouge-2")

        if "rouge-l" in metrics:
            scores["rouge-l"] = calculate_rouge(reference, candidate, "rouge-l")

        if "similarity" in metrics:
            scores["similarity"] = calculate_similarity(reference, candidate)

        results[name] = scores

    return results
