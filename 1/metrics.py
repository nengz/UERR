import numpy as np
from typing import List


def precision_at_k(rel_scores: List[int], k: int) -> float:
    """
    Calculate Pre@k.
    """
    relevant_count = sum(1 for score in rel_scores[:k] if score >= 3)
    return relevant_count / float(k) if k > 0 else 0.0

def mrr_at_k(rel_scores: List[int], k: int) -> float:
    """
    Calculate MRR@K (Mean Reciprocal Rank).
    """
    for rank, score in enumerate(rel_scores[:k], 1):
        if score >= 3:
            return 1.0 / rank
    return 0.0

def ap_at_k(rel_scores: List[int], k: int) -> float:
    """
    Calculate Average Precision@K for a single query.
    """
    precisions = []
    relevant_count = 0
    for i, score in enumerate(rel_scores[:k], 1):
        if score >= 3:
            relevant_count += 1
            precisions.append(relevant_count / float(i))

    if not precisions:
        return 0.0

    return sum(precisions) / len(precisions)

def map_at_k(mulQ_rel_scores: List[List[int]], k: int) -> float:
    """
    Calculate MAP@K (Mean Average Precision) for multiple queries.
    """
    ap_k_scores = []
    for rel_scores in mulQ_rel_scores:
        ap_k_scores.append(ap_at_k(rel_scores, k))
    return np.mean(ap_k_scores) if ap_k_scores else 0.0

def dcg_at_k(rel_scores: List[int], k: int) -> float:
    """
    Calculate DCG@K (Discounted Cumulative Gain).
    """
    dcg = 0.0
    for i, score in enumerate(rel_scores[:k], 1):
        dcg += score / np.log2(i + 1)
    return dcg

def ndcg_at_k(mulM_rel_scores: List[int], rel_scores: List[int], k: int) -> float:
    """
    Calculate NDCG@K (Normalized Discounted Cumulative Gain).
    """
    dcg = dcg_at_k(rel_scores, k)
    idcg = 0.0
    ideal_sorted = sorted(mulM_rel_scores, reverse=True)[:k]
    for i, score in enumerate(ideal_sorted, 1):
        idcg += score / np.log2(i + 1)
    return dcg / idcg if idcg > 0.0 else 0.0
