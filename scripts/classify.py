# -*- coding: utf-8 -*-
"""Per-repo classifier for awesome-motion-prediction.

Rule order matters. Falls back to config default (Deterministic & Short-term).
"""
from lib_common import classify_by_rules

RULES = [
    ("Surveys", ["survey", "review of", "a review"]),
    ("Datasets & Benchmarks", ["dataset", "benchmark", "benchmarking"]),
    ("Trajectory & Multi-Agent Prediction",
     ["trajectory prediction", "multi-agent", "multi agent", "multi-person",
      "multi person", "multi-pedestrian", "crowd", "multi-human"]),
    ("Scene- & Interaction-Aware Prediction",
     ["scene", "interaction", "human-scene", "scene-aware", "scene aware",
      "context-aware", "context aware", "social", "human-scene interaction"]),
    ("Stochastic & Probabilistic Prediction",
     ["stochastic", "probabilistic", "diverse", "uncertainty", "diffusion",
      "generative", "gaussian", "distribution", "stochastic prediction"]),
    ("Deterministic & Short-term Prediction",
     ["deterministic", "short-term", "short term", "autoregressive",
      "recurrent", "graph convolution", "gan", "lstm", "deterministic prediction"]),
]

DEFAULT = "Deterministic & Short-term Prediction"


def classify(paper, config=None):
    return classify_by_rules(paper, RULES, DEFAULT)
