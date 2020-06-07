"""
Abjad's microtonal extension.
"""
from ._version import __version__, __version_info__
from .equal_temperament import (
    EDOBundle,
    apply_alteration,
    get_accidental_value,
    get_alteration,
    get_value_sum,
)
from .et_utilities import PitchClassSegment, PitchClassSet, PitchSegment, PitchSet
from .just_intonation import HEJIVector, JIBundle, make_ji_bundle, tune_to_ratio

__all__ = [
    "__version__",
    "__version_info__",
    "EDOBundle",
    "HEJIVector",
    "JIBundle",
    "PitchClassSet",
    "PitchSet",
    "PitchClassSegment",
    "PitchSegment",
    "apply_alteration",
    "get_accidental_value",
    "get_alteration",
    "get_value_sum",
    "is_prime",
    "prime_factors",
    "make_ji_bundle",
    "tune_to_ratio",
]
