"""
Package for Just Intonation.
"""
import math

import abjad
import black
import quicktions


class JIVector:
    """
    JI vector.

    >>> from abjadext import microtones

    ..  container:: example

        >>> vector = microtones.JIVector(syntonic_commas_down=2)
        >>> vector.syntonic_commas_down
        2

        >>> vector = microtones.JIVector(syntonic_commas_down=2)
        >>> vector.syntonic_commas_up
        0

    """

    def __init__(
        self,
        diatonic_accidental="natural",
        syntonic_commas_down=0,
        syntonic_commas_up=0,
        septimal_commas_down=0,
        septimal_commas_up=0,
        undecimal_quarter_tones_down=0,
        undecimal_quarter_tones_up=0,
        tridecimal_third_tones_down=0,
        tridecimal_third_tones_up=0,
        seventeen_limit_schismas_down=0,
        seventeen_limit_schismas_up=0,
        nineteen_limit_schismas_down=0,
        nineteen_limit_schismas_up=0,
        twenty_three_limit_commas_down=0,
        twenty_three_limit_commas_up=0,
        twenty_nine_limit_commas_down=0,
        twenty_nine_limit_commas_up=0,
        thirty_one_limit_schismas_down=0,
        thirty_one_limit_schismas_up=0,
        thirty_seven_limit_quarter_tones_down=0,
        thirty_seven_limit_quarter_tones_up=0,
        forty_one_limit_commas_down=0,
        forty_one_limit_commas_up=0,
        forty_three_limit_commas_down=0,
        forty_three_limit_commas_up=0,
        forty_seven_limit_quarter_tones_down=0,
        forty_seven_limit_quarter_tones_up=0,
    ):
        self.diatonic_accidental = diatonic_accidental
        self.syntonic_commas_down = syntonic_commas_down
        self.syntonic_commas_up = syntonic_commas_up
        self.septimal_commas_down = septimal_commas_down
        self.septimal_commas_up = septimal_commas_up
        self.undecimal_quarter_tones_down = undecimal_quarter_tones_down
        self.undecimal_quarter_tones_up = undecimal_quarter_tones_up
        self.tridecimal_third_tones_down = tridecimal_third_tones_down
        self.tridecimal_third_tones_up = tridecimal_third_tones_up
        self.seventeen_limit_schismas_down = seventeen_limit_schismas_down
        self.seventeen_limit_schismas_up = seventeen_limit_schismas_up
        self.nineteen_limit_schismas_down = nineteen_limit_schismas_down
        self.nineteen_limit_schismas_up = nineteen_limit_schismas_up
        self.twenty_three_limit_commas_down = twenty_three_limit_commas_down
        self.twenty_three_limit_commas_up = twenty_three_limit_commas_up
        self.twenty_nine_limit_commas_down = twenty_nine_limit_commas_down
        self.twenty_nine_limit_commas_up = twenty_nine_limit_commas_up
        self.thirty_one_limit_schismas_down = thirty_one_limit_schismas_down
        self.thirty_one_limit_schismas_up = thirty_one_limit_schismas_up
        self.thirty_seven_limit_quarter_tones_down = (
            thirty_seven_limit_quarter_tones_down
        )
        self.thirty_seven_limit_quarter_tones_up = thirty_seven_limit_quarter_tones_up
        self.forty_one_limit_commas_down = forty_one_limit_commas_down
        self.forty_one_limit_commas_up = forty_one_limit_commas_up
        self.forty_three_limit_commas_down = forty_three_limit_commas_down
        self.forty_three_limit_commas_up = forty_three_limit_commas_up
        self.forty_seven_limit_quarter_tones_down = forty_seven_limit_quarter_tones_down
        self.forty_seven_limit_quarter_tones_up = forty_seven_limit_quarter_tones_up

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.JIVector()
            repr not yet defined

        """
        return "repr not yet defined"

    def __str__(self):
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

    def has_just_accidentals(self):
        """
        Is true when vector has just accidentals.

        ..  container:: example

            >>> vector = microtones.JIVector()
            >>> vector.has_just_accidentals()
            False

            >>> vector = microtones.JIVector(syntonic_commas_down=1)
            >>> vector.has_just_accidentals()
            True

        """
        return any(
            [
                self.syntonic_commas_down,
                self.syntonic_commas_up,
                self.septimal_commas_down,
                self.septimal_commas_up,
                self.undecimal_quarter_tones_down,
                self.undecimal_quarter_tones_up,
                self.tridecimal_third_tones_down,
                self.tridecimal_third_tones_up,
                self.seventeen_limit_schismas_down,
                self.seventeen_limit_schismas_up,
                self.nineteen_limit_schismas_down,
                self.nineteen_limit_schismas_up,
                self.twenty_three_limit_commas_down,
                self.twenty_three_limit_commas_up,
                self.twenty_nine_limit_commas_down,
                self.twenty_nine_limit_commas_up,
                self.thirty_one_limit_schismas_down,
                self.thirty_one_limit_schismas_up,
                self.thirty_seven_limit_quarter_tones_down,
                self.thirty_seven_limit_quarter_tones_up,
                self.forty_one_limit_commas_down,
                self.forty_one_limit_commas_up,
                self.forty_three_limit_commas_down,
                self.forty_three_limit_commas_up,
                self.forty_seven_limit_quarter_tones_down,
                self.forty_seven_limit_quarter_tones_up,
            ]
        )

    def calculate_ji_markup(self):
        r"""
        Calculates JI markup.

        ..  container:: example

            >>> vector = microtones.JIVector(syntonic_commas_down=1)
            >>> print(abjad.lilypond(vector.calculate_ji_markup()))
            \markup { \natural-one-syntonic-comma-down  }

        """
        int_to_word = {"1": "one", "2": "two", "3": "three"}
        accumulated_accidentals = []
        if self.diatonic_accidental == "double sharp":
            self.diatonic_accidental = "double-sharp"
        if self.diatonic_accidental == "double flat":
            self.diatonic_accidental = "double-flat"
        if self.syntonic_commas_down == self.syntonic_commas_up:
            self.syntonic_commas_down = 0
            self.syntonic_commas_up = 0
            string = rf"\{self.diatonic_accidental}"
            accumulated_accidentals.append(string)
        elif self.syntonic_commas_down > self.syntonic_commas_up:
            self.syntonic_commas_down -= self.syntonic_commas_up
            self.syntonic_commas_up = 0
            string = rf"\{self.diatonic_accidental}"
            string += f"-{int_to_word[str(self.syntonic_commas_down)]}"
            string += "-syntonic-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.syntonic_commas_up -= self.syntonic_commas_down
            self.syntonic_commas_down = 0
            string = rf"\{self.diatonic_accidental}"
            string += f"-{int_to_word[str(self.syntonic_commas_up)]}"
            string += "-syntonic-comma-up"

            accumulated_accidentals.append(string)
        if self.septimal_commas_down == self.septimal_commas_up:
            self.septimal_commas_down = 0
            self.septimal_commas_up = 0
        elif self.septimal_commas_down > self.septimal_commas_up:
            self.septimal_commas_down -= self.septimal_commas_up
            self.septimal_commas_up = 0
            string = rf"\{int_to_word[str(self.septimal_commas_down)]}"
            string += "-septimal-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.septimal_commas_up -= self.septimal_commas_down
            self.septimal_commas_down = 0
            string = rf"\{int_to_word[str(self.septimal_commas_up)]}"
            string += "-septimal-comma-up"
            accumulated_accidentals.append(string)
        if self.undecimal_quarter_tones_down == self.undecimal_quarter_tones_up:
            self.undecimal_quarter_tones_down = 0
            self.undecimal_quarter_tones_up = 0
        elif self.undecimal_quarter_tones_down > self.undecimal_quarter_tones_up:
            self.undecimal_quarter_tones_down -= self.undecimal_quarter_tones_up
            self.undecimal_quarter_tones_up = 0
            string = rf"\{int_to_word[str(self.undecimal_quarter_tones_down)]}"
            string += "-undecimal-quarter-tone-down"
            accumulated_accidentals.append(string)
        else:
            self.undecimal_quarter_tones_up -= self.undecimal_quarter_tones_down
            self.undecimal_quarter_tones_down = 0
            string = rf"\{int_to_word[str(self.undecimal_quarter_tones_up)]}"
            string += "-undecimal-quarter-tone-up"
            accumulated_accidentals.append(string)
        if self.tridecimal_third_tones_down == self.tridecimal_third_tones_up:
            self.tridecimal_third_tones_down = 0
            self.tridecimal_third_tones_up = 0
        elif self.tridecimal_third_tones_down > self.tridecimal_third_tones_up:
            self.tridecimal_third_tones_down -= self.tridecimal_third_tones_up
            self.tridecimal_third_tones_up = 0
            string = rf"\{int_to_word[str(self.tridecimal_third_tones_down)]}"
            string += "-tridecimal-third-tone-down"
            accumulated_accidentals.append(string)
        else:
            self.tridecimal_third_tones_up -= self.tridecimal_third_tones_down
            self.tridecimal_third_tones_down = 0
            string = rf"\{int_to_word[str(self.tridecimal_third_tones_up)]}"
            string += "-tridecimal-third-tone-up"
            accumulated_accidentals.append(string)
        if self.seventeen_limit_schismas_down == self.seventeen_limit_schismas_up:
            self.seventeen_limit_schismas_down = 0
            self.seventeen_limit_schismas_up = 0
        elif self.seventeen_limit_schismas_down > self.seventeen_limit_schismas_up:
            self.seventeen_limit_schismas_down -= self.seventeen_limit_schismas_up
            self.seventeen_limit_schismas_up = 0
            string = rf"\{int_to_word[str(self.seventeen_limit_schismas_down)]}"
            string += "-seventeen-limit-schisma-down"
            accumulated_accidentals.append(string)
        else:
            self.seventeen_limit_schismas_up -= self.seventeen_limit_schismas_down
            self.seventeen_limit_schismas_down = 0
            string = rf"\{int_to_word[str(self.seventeen_limit_schismas_up)]}"
            string += "-seventeen-limit-schisma-up"
            accumulated_accidentals.append(string)
        if self.nineteen_limit_schismas_down == self.nineteen_limit_schismas_up:
            self.nineteen_limit_schismas_down = 0
            self.nineteen_limit_schismas_up = 0
        elif self.nineteen_limit_schismas_down > self.nineteen_limit_schismas_up:
            self.nineteen_limit_schismas_down -= self.nineteen_limit_schismas_up
            self.nineteen_limit_schismas_up = 0
            string = rf"\{int_to_word[str(self.nineteen_limit_schismas_down)]}"
            string += "-nineteen-limit-schisma-down"
            accumulated_accidentals.append(string)
        else:
            self.nineteen_limit_schismas_up -= self.nineteen_limit_schismas_down
            self.nineteen_limit_schismas_down = 0
            string = rf"\{int_to_word[str(self.nineteen_limit_schismas_up)]}"
            string += "-nineteen-limit-schisma-up"
            accumulated_accidentals.append(string)
        if self.twenty_three_limit_commas_down == self.twenty_three_limit_commas_up:
            self.twenty_three_limit_commas_down = 0
            self.twenty_three_limit_commas_up = 0
        elif self.twenty_three_limit_commas_down > self.twenty_three_limit_commas_up:
            self.twenty_three_limit_commas_down -= self.twenty_three_limit_commas_up
            self.twenty_three_limit_commas_up = 0
            string = rf"\{int_to_word[str(self.twenty_three_limit_commas_down)]}"
            string += "-twenty-three-limit-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.twenty_three_limit_commas_up -= self.twenty_three_limit_commas_down
            self.twenty_three_limit_commas_down = 0
            string = rf"\{int_to_word[str(self.twenty_three_limit_commas_up)]}"
            string += "-twenty-three-limit-comma-up"
            accumulated_accidentals.append(string)
        if self.twenty_nine_limit_commas_down == self.twenty_nine_limit_commas_up:
            self.twenty_nine_limit_commas_down = 0
            self.twenty_nine_limit_commas_up = 0
        elif self.twenty_nine_limit_commas_down > self.twenty_nine_limit_commas_up:
            self.twenty_nine_limit_commas_down -= self.twenty_nine_limit_commas_up
            self.twenty_nine_limit_commas_up = 0
            string = rf"\{int_to_word[str(self.twenty_nine_limit_commas_down)]}"
            string += "-twenty-nine-limit-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.twenty_nine_limit_commas_up -= self.twenty_nine_limit_commas_down
            self.twenty_nine_limit_commas_down = 0
            string = rf"\{int_to_word[str(self.twenty_nine_limit_commas_up)]}"
            string += "-twenty-nine-limit-comma-up"
            accumulated_accidentals.append(string)
        if self.thirty_one_limit_schismas_down == self.thirty_one_limit_schismas_up:
            self.thirty_one_limit_schismas_down = 0
            self.thirty_one_limit_schismas_up = 0
        elif self.thirty_one_limit_schismas_down > self.thirty_one_limit_schismas_up:
            self.thirty_one_limit_schismas_down -= self.thirty_one_limit_schismas_up
            self.thirty_one_limit_schismas_up = 0
            string = rf"\{int_to_word[str(self.thirty_one_limit_schismas_down)]}"
            string += "-thirty-one-limit-schisma-down"
            accumulated_accidentals.append(string)
        else:
            self.thirty_one_limit_schismas_up -= self.thirty_one_limit_schismas_down
            self.thirty_one_limit_schismas_down = 0
            string = rf"\{int_to_word[str(self.thirty_one_limit_schismas_up)]}"
            string += "-thirty-one-limit-schisma-up"
            accumulated_accidentals.append(string)
        if (
            self.thirty_seven_limit_quarter_tones_down
            == self.thirty_seven_limit_quarter_tones_up
        ):
            self.thirty_seven_limit_quarter_tones_down = 0
            self.thirty_seven_limit_quarter_tones_up = 0
        elif (
            self.thirty_seven_limit_quarter_tones_down
            > self.thirty_seven_limit_quarter_tones_up
        ):
            self.thirty_seven_limit_quarter_tones_down -= (
                self.thirty_seven_limit_quarter_tones_up
            )
            self.thirty_seven_limit_quarter_tones_up = 0
            string = rf"\{int_to_word[str(self.thirty_seven_limit_quarter_tones_down)]}"
            string += "-thirty-seven-limit-quarter-tone-down"
            accumulated_accidentals.append(string)
        else:
            self.thirty_seven_limit_quarter_tones_up -= (
                self.thirty_seven_limit_quarter_tones_down
            )
            self.thirty_seven_limit_quarter_tones_down = 0
            string = rf"\{int_to_word[str(self.thirty_seven_limit_quarter_tones_up)]}"
            string += "-thirty-seven-limit-quarter-tone-up"
            accumulated_accidentals.append(string)
        if self.forty_one_limit_commas_down == self.forty_one_limit_commas_up:
            self.forty_one_limit_commas_down = 0
            self.forty_one_limit_commas_up = 0
        elif self.forty_one_limit_commas_down > self.forty_one_limit_commas_up:
            self.forty_one_limit_commas_down -= self.forty_one_limit_commas_up
            self.forty_one_limit_commas_up = 0
            string = rf"\{int_to_word[str(self.forty_one_limit_commas_down)]}"
            string += "-forty-one-limit-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.forty_one_limit_commas_up -= self.forty_one_limit_commas_down
            self.forty_one_limit_commas_down = 0
            string = rf"\{int_to_word[str(self.forty_one_limit_commas_up)]}"
            string += "-forty-one-limit-comma-up"
            accumulated_accidentals.append(string)
        if self.forty_three_limit_commas_down == self.forty_three_limit_commas_up:
            self.forty_three_limit_commas_down = 0
            self.forty_three_limit_commas_up = 0
        elif self.forty_three_limit_commas_down > self.forty_three_limit_commas_up:
            self.forty_three_limit_commas_down -= self.forty_three_limit_commas_up
            self.forty_three_limit_commas_up = 0
            string = rf"\{int_to_word[str(self.forty_three_limit_commas_down)]}"
            string += "-forty-three-limit-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.forty_three_limit_commas_up -= self.forty_three_limit_commas_down
            self.forty_three_limit_commas_down = 0
            string = rf"\{int_to_word[str(self.forty_three_limit_commas_up)]}"
            string += "-forty-three-limit-comma-up"
            accumulated_accidentals.append(string)

        if (
            self.forty_seven_limit_quarter_tones_down
            == self.forty_seven_limit_quarter_tones_up
        ):
            self.forty_seven_limit_quarter_tones_down = 0
            self.forty_seven_limit_quarter_tones_up = 0
        elif (
            self.forty_seven_limit_quarter_tones_down
            > self.forty_seven_limit_quarter_tones_up
        ):
            self.forty_seven_limit_quarter_tones_down -= (
                self.forty_seven_limit_quarter_tones_up
            )
            self.forty_seven_limit_quarter_tones_up = 0
            string = rf"\{int_to_word[str(self.forty_seven_limit_quarter_tones_down)]}"
            string += "-forty-seven-limit-quarter-tone-down"
            accumulated_accidentals.append(string)
        else:
            self.forty_seven_limit_quarter_tones_up -= (
                self.forty_seven_limit_quarter_tones_down
            )
            self.forty_seven_limit_quarter_tones_down = 0
            string = rf"\{int_to_word[str(self.forty_seven_limit_quarter_tones_up)]}"
            string += "-forty-seven-limit-quarter-tone-up"
            accumulated_accidentals.append(string)

        if len(accumulated_accidentals):
            accumulated_accidentals.reverse()
            if accumulated_accidentals[-1] == r"\natural":
                if self.has_just_accidentals():
                    accumulated_accidentals = [_ for _ in accumulated_accidentals[:-1]]
            for i, s in enumerate(accumulated_accidentals):
                if s == r"\natural":
                    accumulated_accidentals[i] = r"\abjad-natural"
                if s == r"\sharp":
                    accumulated_accidentals[i] = r"\abjad-sharp"
                if s == r"\flat":
                    accumulated_accidentals[i] = r"\abjad-flat"
            literal_components = []
            for accidental_string in accumulated_accidentals:
                accidental_string = accidental_string + " "
                literal_components.append(accidental_string)
            if len(literal_components) == 1:
                literal = abjad.Markup(rf"\markup {{ {literal_components[0]} }}")
            else:
                kerned_components = []
                for i, item in enumerate(literal_components):
                    kerned_components.append(item)
                    if i != len(literal_components) - 1:
                        kerned_components.append(r"\hspace #0.125 ")
                kerned_components_string = ""
                for kerned_component in kerned_components:
                    kerned_components_string += kerned_component
                literal = abjad.Markup(
                    rf"\markup \concat {{ {kerned_components_string} }}"
                )
        else:
            literal = abjad.Markup(rf" \markup {{ \abjad-{self.diatonic_accidental} }}")
        self.accidental_literal = literal
        return literal


class JIBundle:
    """
    JI bundle.

    ..  container:: example

        >>> bundle = microtones.JIBundle()
        >>> bundle.pitch
        "c'"

        >>> bundle.vector
        repr not yet defined

    """

    def __init__(self, pitch="c'", vector=JIVector()):
        self.pitch = pitch
        self.vector = vector

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.JIBundle()
            repr not yet defined

        """
        return "repr not yet defined"

    def __str__(self):
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string


def _is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def _prime_factors(n):
    prime_factor_list = []
    while not n % 2:
        prime_factor_list.append(2)
        n //= 2
    while not n % 3:
        prime_factor_list.append(3)
        n //= 3
    i = 5
    while n != 1:
        if _is_prime(i):
            while not n % i:
                prime_factor_list.append(i)
                n //= i
        i += 2
    return prime_factor_list


_numerator_factor_to_intervals = {
    2: ("+P8",),
    3: ("+P8", "+P5"),
    5: ("+P8", "+P8", "+M3"),
    7: ("+P8", "+P8", "+m7"),
    11: ("+P8", "+P8", "+P8", "+P4"),
    13: ("+P8", "+P8", "+P8", "+M6"),
    17: ("+P8", "+P8", "+P8", "+P8", "+A1"),
    19: ("+P8", "+P8", "+P8", "+P8", "+m3"),
    23: ("+P8", "+P8", "+P8", "+P8", "+A4"),
    29: ("+P8", "+P8", "+P8", "+P8", "+m7"),
    31: ("+P8", "+P8", "+P8", "+P8", "+P8"),
    37: ("+P8", "+P8", "+P8", "+P8", "+P8", "+M2"),
    41: ("+P8", "+P8", "+P8", "+P8", "+P8", "+M3"),
    43: ("+P8", "+P8", "+P8", "+P8", "+P8", "+P4"),
    47: ("+P8", "+P8", "+P8", "+P8", "+P8", "+A4"),
}

_numerator_factor_to_nudge = {
    5: "syntonic_commas_down",
    7: "septimal_commas_down",
    11: "undecimal_quarter_tones_up",
    13: "tridecimal_third_tones_down",
    17: "seventeen_limit_schismas_down",
    19: "nineteen_limit_schismas_up",
    23: "twenty_three_limit_commas_up",
    29: "twenty_nine_limit_commas_up",
    31: "thirty_one_limit_schismas_down",
    37: "thirty_seven_limit_quarter_tones_up",
    41: "forty_one_limit_commas_up",
    43: "forty_three_limit_commas_up",
    47: "forty_seven_limit_quarter_tones_up",
}


def make_ji_bundle(pitch, ratio):
    r"""
    Makes JI bundle.

    ..  container:: example

        >>> bundle = microtones.make_ji_bundle(abjad.NamedPitch("c'"), "3/2")
        >>> bundle.pitch
        NamedPitch("g'")

        >>> bundle.vector
        repr not yet defined

    """
    if isinstance(pitch, str):
        pitch = abjad.NamedPitch(pitch)
    elif isinstance(pitch, int):
        pitch = abjad.NumberedPitch(pitch)
    ratio = quicktions.Fraction(ratio)
    numerator_factors = _prime_factors(ratio.numerator)
    denominator_factors = _prime_factors(ratio.denominator)
    accidental_vector = JIVector(diatonic_accidental=pitch.accidental.name)
    for prime in numerator_factors:
        assert prime <= 47
        for string in _numerator_factor_to_intervals[prime]:
            pitch = abjad.NamedInterval(string).transpose(pitch)
        if prime in _numerator_factor_to_nudge:
            string = _numerator_factor_to_nudge[prime]
            value = getattr(accidental_vector, string)
            setattr(accidental_vector, string, value + 1)
    for prime in denominator_factors:
        assert prime <= 47
        for string in _numerator_factor_to_intervals[prime]:
            string = string.replace("+", "-")
            pitch = abjad.NamedInterval(string).transpose(pitch)
        if prime in _numerator_factor_to_nudge:
            string = _numerator_factor_to_nudge[prime]
            if string.endswith("_up"):
                string = string.replace("_up", "_down")
            else:
                string = string.replace("_down", "_up")
            value = getattr(accidental_vector, string)
            setattr(accidental_vector, string, value + 1)
    accidental_vector.diatonic_accidental = pitch.accidental.name
    return JIBundle(pitch, accidental_vector)


def return_cent_deviation_markup(
    ratio=1, fundamental="a'", chris=False
):  # chris values are temp.
    pitch = None
    ratio = quicktions.Fraction(ratio)
    tonic_cent_difference = abjad.NamedPitch(fundamental).number * 100
    log_ratio = quicktions.Fraction(math.log10(ratio))
    log_2 = quicktions.Fraction(1200 / math.log10(2))
    ji_cents = quicktions.Fraction(log_ratio * log_2)
    et_cents = (
        make_ji_bundle(fundamental, ratio).pitch.number * 100
    ) - tonic_cent_difference
    cent_difference = ji_cents - et_cents
    final_cents = round(float(cent_difference))
    if chris is True:
        final_cents = round(float(cent_difference), 2)
    if chris is True:
        p_string = f"{fundamental.name}4"
        demo_note = abjad.Note(p_string)
        demo_head = demo_note.note_head
        # tune_to_ratio(demo_head, quicktions.Fraction(ratio) * quicktions.Fraction(9, 8)) # for Rag'sma only
        tune_to_ratio(demo_head, quicktions.Fraction(ratio))
        pitch = abjad.NumberedPitch(demo_head.written_pitch)
    if 50 < abs(final_cents):
        if chris is False:
            p_string = f"{fundamental.name}4"
            # raise Exception(p_string)
            demo_note = abjad.Note(p_string)
            demo_head = demo_note.note_head
            tune_to_ratio(demo_head, ratio)
            pitch = abjad.NumberedPitch(demo_head.written_pitch)
        semitones = final_cents / 100
        parts = math.modf(semitones)
        pitch += parts[1]
        remainder = round(parts[0] * 100)
        if 50 < abs(remainder):
            if 0 < remainder:
                pitch += 1
                remainder = -100 + remainder
            else:
                pitch -= 1
                remainder = 100 + remainder
        final_cents = remainder
    if final_cents < 0:
        cent_string = f"{final_cents}"
        if chris is True:
            if not cent_string[0].isalpha():
                pitch_string = str(abjad.NamedPitchClass(pitch).name)
                pos, acc = pitch_string[0], pitch_string[1:]
                pos = pos.capitalize()
                acc = acc.replace(
                    "s",
                    r"\raise #0.75 { \teeny \smaller \sharp } ",
                )
                acc = acc.replace(
                    "f", r"\raise #0.5 { \teeny \flat } "
                )
                cent_string = pos + acc + cent_string
                cent_string = cent_string.replace(
                    r"A\raise #0.5 { \teeny \flat } ",
                    r"G\raise #0.75 { \teeny \smaller \sharp } ",
                )
        if chris is False:
            if pitch is not None:
                pitch_string = str(abjad.NamedPitchClass(pitch).name)
                pos, acc = pitch_string[0], pitch_string[1:]
                pos = pos.capitalize()
                acc = acc.replace(
                    "s",
                    r"\raise #0.75 { \teeny \smaller \sharp } ",
                )
                acc = acc.replace(
                    "f", r"\raise #0.5 { \teeny \flat } "
                )
                cent_string = pos + acc + cent_string
    else:
        cent_string = f"+{final_cents}"
        if chris is True:
            if not cent_string[0].isalpha():
                pitch_string = str(abjad.NamedPitchClass(pitch).name)
                pos, acc = pitch_string[0], pitch_string[1:]
                pos = pos.capitalize()
                acc = acc.replace(
                    "s",
                    r"\raise #0.75 { \teeny \smaller \sharp } ",
                )
                acc = acc.replace(
                    "f", r"\raise #0.5 { \teeny \flat } "
                )
                cent_string = pos + acc + cent_string
                cent_string = cent_string.replace(
                    r"A\raise #0.5 { \teeny \flat } ",
                    r"G\raise #0.75 { \teeny \smaller \sharp } ",
                )
        if chris is False:
            if pitch is not None:
                pitch_string = str(abjad.NamedPitchClass(pitch).name)
                pos, acc = pitch_string[0], pitch_string[1:]
                pos = pos.capitalize()
                acc = acc.replace(
                    "s",
                    r"\raise #0.75 { \teeny \smaller \sharp } ",
                )
                acc = acc.replace(
                    "f", r"\raise #0.5 { \teeny \flat } "
                )
                cent_string = pos + acc + cent_string
    mark = abjad.Markup(rf"\markup \center-align {{ \concat {{ {cent_string} }} }}")
    return mark


def tune_to_ratio(
    note_head,
    ratio,
    *,
    omit_just_accidental=False,
    tempered=False,
):
    r"""
    Transposes notehead in place and tweaks accidental stencil.

    ..  container:: example

        All implemented accidentals are available for both stylesheets:

        >>> note = abjad.Note("c'4")
        >>> microtones.tune_to_ratio(note.note_head, "7/4")
        >>> staff = abjad.Staff([note])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/abjad/scm/abjad.ily\'",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/ekmelos-ji-accidental-markups.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        >>> note = abjad.Note("c'4")
        >>> microtones.tune_to_ratio(note.note_head, "7/4")
        >>> staff = abjad.Staff([note])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/abjad/scm/abjad.ily\'",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/HEJI2-ji-accidental-markups.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        Tweaks accidentals when ``omit_just_accidental=False``:

        >>> note = abjad.Note("c'4")
        >>> microtones.tune_to_ratio(note.note_head, "5/1", omit_just_accidental=False)
        >>> print(abjad.lilypond(note)) # doctest: +SKIP

        Does not tweak accidentals when ``omit_just_accidental=True``:

        >>> note = abjad.Note("c'4")
        >>> microtones.tune_to_ratio(note.note_head, "5/1", omit_just_accidental=True)
        >>> print(abjad.lilypond(note)) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.lilypond(note))
            e'''4

    ..  container:: example

        A harmonic series with the ekmelos font.

        >>> ratios = [f"{_ + 1}/1" for _ in range(23)]
        >>> notes = [abjad.Note("a,,,8") for _ in ratios]
        >>> for note, ratio in zip(notes, ratios):
        ...     microtones.tune_to_ratio(note.note_head, ratio)
        ...
        >>> staff = abjad.Staff()
        >>> staff.extend(notes)
        >>> abjad.attach(abjad.Clef("bass"), staff[0])
        >>> abjad.attach(abjad.Clef("treble"), staff[6])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/abjad/scm/abjad.ily\'",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/ekmelos-ji-accidental-markups.ily\'",
        ...         "\\include \'harmonic-series-layout.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.lilypond(staff))
            \new Staff
            {
                \clef "bass"
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                a,,,8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                a,,8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                e,8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                a,8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \sharp-one-syntonic-comma-down  }
                cs8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                e8
                \clef "treble"
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \one-septimal-comma-down  }
                g8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                a8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                b8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \sharp-one-syntonic-comma-down  }
                cs'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \one-undecimal-quarter-tone-up  }
                d'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                e'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup \concat { \one-tridecimal-third-tone-down \hspace #0.125 \abjad-sharp  }
                fs'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \one-septimal-comma-down  }
                g'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \sharp-one-syntonic-comma-down  }
                gs'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                a'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup \concat { \one-seventeen-limit-schisma-down \hspace #0.125 \abjad-sharp  }
                as'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \abjad-natural  }
                b'8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \one-nineteen-limit-schisma-up  }
                c''8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \sharp-one-syntonic-comma-down  }
                cs''8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \one-septimal-comma-down  }
                d''8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup { \one-undecimal-quarter-tone-up  }
                d''8
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \markup \concat { \one-twenty-three-limit-comma-up \hspace #0.125 \abjad-sharp  }
                ds''8
            }

        A harmonic series with the HEJI2 font.

        >>> ratios = [f"{_ + 1}/1" for _ in range(23)]
        >>> notes = [abjad.Note("a,,,8") for _ in ratios]
        >>> for note, ratio in zip(notes, ratios):
        ...     microtones.tune_to_ratio(note.note_head, ratio)
        ...
        >>> staff = abjad.Staff()
        >>> staff.extend(notes)
        >>> abjad.attach(abjad.Clef("bass"), staff[0])
        >>> abjad.attach(abjad.Clef("treble"), staff[6])
        >>> abjad.attach(abjad.TimeSignature((24, 32)), staff[0])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/abjad/scm/abjad.ily\'",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/HEJI2-ji-accidental-markups.ily\'",
        ...         "\\include \'harmonic-series-layout.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        Prints tempered accidentals when ``tempered=True``:

        >>> note = abjad.Note("c'4")
        >>> microtones.tune_to_ratio(note.note_head, "5/1", tempered=True)
        >>> staff = abjad.Staff([note])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/abjad/scm/abjad.ily\'",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/ekmelos-ji-accidental-markups.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ]
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.lilypond(note))
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \tempered-natural
            e'''4

    """
    bundle = make_ji_bundle(note_head.written_pitch, ratio)
    note_head.written_pitch = bundle.pitch
    if omit_just_accidental:
        return
    if tempered is True:
        tempered_accidental = note_head.written_pitch.accidental.name
        tempered_accidental = tempered_accidental.replace(" ", "-")
        # manager = abjad.tweak(note_head, literal=True)
        # manager.Accidental.stencil = r"#ly:text-interface::print"
        abjad.tweak(note_head, r"\tweak Accidental.stencil #ly:text-interface::print")
        # manager.Accidental.text = rf"\tempered-{tempered_accidental}"
        abjad.tweak(
            note_head, rf"\tweak Accidental.text \tempered-{tempered_accidental}"
        )
    else:
        markup = bundle.vector.calculate_ji_markup()
        # manager = abjad.tweak(note_head, literal=True)
        # manager.Accidental.stencil = r"#ly:text-interface::print"
        abjad.tweak(note_head, r"\tweak Accidental.stencil #ly:text-interface::print")
        alteration_literal = markup
        # manager.Accidental.text = alteration_literal
        abjad.tweak(note_head, rf"\tweak Accidental.text {alteration_literal.string}")
