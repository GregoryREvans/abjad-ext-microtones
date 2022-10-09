"""
Abjad's microtonal extension.

..  container:: example

    ET module models scales of twelfth, tenth, and eighth tones.

..  container:: example

    JI module models only 47-limit ratios and requires either the ekmelos or HEJI2 font.

..  container:: example

    Both modules require the Lilypond layout block to have the setting ``\\accidentalStyle "dodecaphonic"``. This forces accidental symbols to always be printed before each note head, allowing the symbol to be tweaked.

..  container:: example

    The fonts can be found at http://www.ekmelic-music.org/en/extra/ekmelos.htm and http://www.plainsound.org/ respectively and should be installed into the folders at ``/LilyPond.app/Contents/Resources/share/lilypond/current/fonts`` and the computer's font database such as `Font Book`.
"""
from ._version import __version__, __version_info__
from .et import (
    ETBundle,
    apply_alteration,
    get_accidental_value,
    get_alteration,
    get_value_sum,
)
from .ji import (
    JIBundle,
    JIVector,
    make_ji_bundle,
    return_cent_deviation_markup,
    tune_to_ratio,
)
from .utilities import (
    PitchClassSegment,
    PitchClassSet,
    PitchSegment,
    PitchSet,
    RatioClassSegment,
    RatioClassSet,
    RatioSegment,
    RatioSet,
)

__all__ = [
    "ETBundle",
    "JIBundle",
    "JIVector",
    "PitchClassSegment",
    "PitchClassSet",
    "PitchSegment",
    "PitchSet",
    "RatioClassSegment",
    "RatioClassSet",
    "RatioSegment",
    "RatioSet",
    "__version__",
    "__version_info__",
    "apply_alteration",
    "get_accidental_value",
    "get_alteration",
    "get_value_sum",
    "make_ji_bundle",
    "return_cent_deviation_markup",
    "tune_to_ratio",
]
