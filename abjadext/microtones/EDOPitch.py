from math import modf

import abjad


class EdoPitch:
    r"""
    >>> from abjadext import microtones
    >>> edo = microtones.EdoPitch(pitch=0.75)
    >>> edo(abjad.Note("c'4"))
    \three-eighths-sharp

    """

    def __init__(self, pitch=None):
        self.pitch = pitch

    def __call__(self, note):
        return self.apply_pitch(note)

    def substitution_from_remainder(self, default_accidental, remainder):
        accidental_to_value = {"sharp": 1, "natural": 0, "flat": -1}
        value_to_accidental = {
            "2": r"\double-sharp",
            "1.75": r"\seven-eighths-sharp",
            "1.5": r"\three-quarters-sharp",
            "1.25": r"\five-eighths-sharp",
            "1": r"\forced-sharp",
            "0.75": r"\three-eighths-sharp",
            "0.5": r"\quarter-sharp",
            "0.25": r"\eighth-sharp",
            "0": r"\forced-natural",
            "-0.25": r"\eighth-flat",
            "-0.5": r"\quarter-flat",
            "-0.75": r"\three-eighths-flat",
            "-1": r"\forced-flat",
            "-1.25": r"\five-eighths-flat",
            "-1.5": r"\three-quarters-flat",
            "-1.75": r"\seven-eighths-flat",
            "-2": r"\double-flat",
        }
        total_value = accidental_to_value[default_accidental.name] + remainder
        return value_to_accidental[f"{total_value}"]

    def apply_pitch(self, note):
        integer_part = modf(float(self.pitch))[1]
        float_remainder = modf(float(self.pitch))[0]
        pitch = abjad.NumberedPitch(integer_part)
        accidental = pitch.accidental
        alteration = self.substitution_from_remainder(
            default_accidental=accidental, remainder=float_remainder
        )
        return alteration
