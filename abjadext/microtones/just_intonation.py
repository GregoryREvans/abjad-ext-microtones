import fractions

import abjad


class HEJIVector:
    """
    HEJI vector.

    >>> from abjadext import microtones

    ..  container:: example

        >>> vector = microtones.HEJIVector(syntonic_commas_down=2)
        >>> vector.syntonic_commas_down
        2

        >>> vector = microtones.HEJIVector(syntonic_commas_down=2)
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
        seventeen_limit_skhismas_down=0,
        seventeen_limit_skhismas_up=0,
        nineteen_limit_skhismas_down=0,
        nineteen_limit_skhismas_up=0,
        twenty_three_limit_commas_down=0,
        twenty_three_limit_commas_up=0,
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
        self.seventeen_limit_skhismas_down = seventeen_limit_skhismas_down
        self.seventeen_limit_skhismas_up = seventeen_limit_skhismas_up
        self.nineteen_limit_skhismas_down = nineteen_limit_skhismas_down
        self.nineteen_limit_skhismas_up = nineteen_limit_skhismas_up
        self.twenty_three_limit_commas_down = twenty_three_limit_commas_down
        self.twenty_three_limit_commas_up = twenty_three_limit_commas_up

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.HEJIVector()
            HEJIVector(
                    diatonic_accidental="natural",
                    syntonic_commas_down=0,
                    syntonic_commas_up=0,
                    septimal_commas_down=0,
                    septimal_commas_up=0,
                    undecimal_quarter_tones_down=0,
                    undecimal_quarter_tones_up=0,
                    tridecimal_third_tones_down=0,
                    tridecimal_third_tones_up=0,
                    seventeen_limit_skhismas_down=0,
                    seventeen_limit_skhismas_up=0,
                    nineteen_limit_skhismas_down=0,
                    nineteen_limit_skhismas_up=0,
                    twenty_three_limit_commas_down=0,
                    twenty_three_limit_commas_up=0,
            )

        """

        return f"""{self.__class__.__name__}(
        diatonic_accidental="{self.diatonic_accidental}",
        syntonic_commas_down={self.syntonic_commas_down},
        syntonic_commas_up={self.syntonic_commas_up},
        septimal_commas_down={self.septimal_commas_down},
        septimal_commas_up={self.septimal_commas_up},
        undecimal_quarter_tones_down={self.undecimal_quarter_tones_down},
        undecimal_quarter_tones_up={self.undecimal_quarter_tones_up},
        tridecimal_third_tones_down={self.tridecimal_third_tones_down},
        tridecimal_third_tones_up={self.tridecimal_third_tones_up},
        seventeen_limit_skhismas_down={self.seventeen_limit_skhismas_down},
        seventeen_limit_skhismas_up={self.seventeen_limit_skhismas_up},
        nineteen_limit_skhismas_down={self.nineteen_limit_skhismas_down},
        nineteen_limit_skhismas_up={self.nineteen_limit_skhismas_up},
        twenty_three_limit_commas_down={self.twenty_three_limit_commas_down},
        twenty_three_limit_commas_up={self.twenty_three_limit_commas_up},\n)"""

    def has_just_accidentals(self):
        """
        Is true when vector has just accidentals.

        ..  container:: example

            >>> vector = microtones.HEJIVector()
            >>> vector.has_just_accidentals()
            False

            >>> vector = microtones.HEJIVector(syntonic_commas_down=1)
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
                self.seventeen_limit_skhismas_down,
                self.seventeen_limit_skhismas_up,
                self.nineteen_limit_skhismas_down,
                self.nineteen_limit_skhismas_up,
                self.twenty_three_limit_commas_down,
                self.twenty_three_limit_commas_up,
            ]
        )

    def calculate_heji_markup(self):
        r"""
        Calculates HEJI markup.

        ..  container:: example

            >>> vector = microtones.HEJIVector(syntonic_commas_down=1)
            >>> abjad.f(vector.calculate_heji_markup())
            \forced-natural-one-syntonic-comma-down

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
            string = fr"\forced-{self.diatonic_accidental}"
            accumulated_accidentals.append(string)
        elif self.syntonic_commas_down > self.syntonic_commas_up:
            self.syntonic_commas_down -= self.syntonic_commas_up
            self.syntonic_commas_up = 0
            string = fr"\forced-{self.diatonic_accidental}"
            string += f"-{int_to_word[str(self.syntonic_commas_down)]}"
            string += "-syntonic-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.syntonic_commas_up -= self.syntonic_commas_down
            self.syntonic_commas_down = 0
            string = fr"\forced-{self.diatonic_accidental}"
            string += f"-{int_to_word[str(self.syntonic_commas_up)]}"
            string += "-syntonic-comma-up"

            accumulated_accidentals.append(string)
        if self.septimal_commas_down == self.septimal_commas_up:
            self.septimal_commas_down = 0
            self.septimal_commas_up = 0
        elif self.septimal_commas_down > self.septimal_commas_up:
            self.septimal_commas_down -= self.septimal_commas_up
            self.septimal_commas_up = 0
            string = fr"\{int_to_word[str(self.septimal_commas_down)]}"
            string += "-septimal-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.septimal_commas_up -= self.septimal_commas_down
            self.septimal_commas_down = 0
            string = fr"\{int_to_word[str(self.septimal_commas_up)]}"
            string += "-septimal-comma-up"
            accumulated_accidentals.append(string)
        if self.undecimal_quarter_tones_down == self.undecimal_quarter_tones_up:
            self.undecimal_quarter_tones_down = 0
            self.undecimal_quarter_tones_up = 0
        elif self.undecimal_quarter_tones_down > self.undecimal_quarter_tones_up:
            self.undecimal_quarter_tones_down -= self.undecimal_quarter_tones_up
            self.undecimal_quarter_tones_up = 0
            string = fr"\{int_to_word[str(self.undecimal_quarter_tones_down)]}"
            string += "-undecimal-quarter-tone-down"
            accumulated_accidentals.append(string)
        else:
            self.undecimal_quarter_tones_up -= self.undecimal_quarter_tones_down
            self.undecimal_quarter_tones_down = 0
            string = fr"\{int_to_word[str(self.undecimal_quarter_tones_up)]}"
            string += "-undecimal-quarter-tone-up"
            accumulated_accidentals.append(string)
        if self.tridecimal_third_tones_down == self.tridecimal_third_tones_up:
            self.tridecimal_third_tones_down = 0
            self.tridecimal_third_tones_up = 0
        elif self.tridecimal_third_tones_down > self.tridecimal_third_tones_up:
            self.tridecimal_third_tones_down -= self.tridecimal_third_tones_up
            self.tridecimal_third_tones_up = 0
            string = fr"\{int_to_word[str(self.tridecimal_third_tones_down)]}"
            string += "-tridecimal-third-tone-down"
            accumulated_accidentals.append(string)
        else:
            self.tridecimal_third_tones_up -= self.tridecimal_third_tones_down
            self.tridecimal_third_tones_down = 0
            string = fr"\{int_to_word[str(self.tridecimal_third_tones_up)]}"
            string += "-tridecimal-third-tone-up"
            accumulated_accidentals.append(string)
        if self.seventeen_limit_skhismas_down == self.seventeen_limit_skhismas_up:
            self.seventeen_limit_skhismas_down = 0
            self.seventeen_limit_skhismas_up = 0
        elif self.seventeen_limit_skhismas_down > self.seventeen_limit_skhismas_up:
            self.seventeen_limit_skhismas_down -= self.seventeen_limit_skhismas_up
            self.seventeen_limit_skhismas_up = 0
            string = fr"\{int_to_word[str(self.seventeen_limit_skhismas_down)]}"
            string += "-seventeen-limit-skhisma-down"
            accumulated_accidentals.append(string)
        else:
            self.seventeen_limit_skhismas_up -= self.seventeen_limit_skhismas_down
            self.seventeen_limit_skhismas_down = 0
            string = fr"\{int_to_word[str(self.seventeen_limit_skhismas_up)]}"
            string += "-seventeen-limit-skhisma-up"
            accumulated_accidentals.append(string)
        if self.nineteen_limit_skhismas_down == self.nineteen_limit_skhismas_up:
            self.nineteen_limit_skhismas_down = 0
            self.nineteen_limit_skhismas_up = 0
        elif self.nineteen_limit_skhismas_down > self.nineteen_limit_skhismas_up:
            self.nineteen_limit_skhismas_down -= self.nineteen_limit_skhismas_up
            self.nineteen_limit_skhismas_up = 0
            string = fr"\{int_to_word[str(self.nineteen_limit_skhismas_down)]}"
            string += "-nineteen-limit-skhisma-down"
            accumulated_accidentals.append(string)
        else:
            self.nineteen_limit_skhismas_up -= self.nineteen_limit_skhismas_down
            self.nineteen_limit_skhismas_down = 0
            string = fr"\{int_to_word[str(self.nineteen_limit_skhismas_up)]}"
            string += "-nineteen-limit-skhisma-up"
            accumulated_accidentals.append(string)
        if self.twenty_three_limit_commas_down == self.twenty_three_limit_commas_up:
            self.twenty_three_limit_commas_down = 0
            self.twenty_three_limit_commas_up = 0
        elif self.twenty_three_limit_commas_down > self.twenty_three_limit_commas_up:
            self.twenty_three_limit_commas_down -= self.twenty_three_limit_commas_up
            self.twenty_three_limit_commas_up = 0
            string = fr"\{int_to_word[str(self.twenty_three_limit_commas_down)]}"
            string += "-twenty-three-limit-comma-down"
            accumulated_accidentals.append(string)
        else:
            self.twenty_three_limit_commas_up -= self.twenty_three_limit_commas_down
            self.twenty_three_limit_commas_down = 0
            string = fr"\{int_to_word[str(self.twenty_three_limit_commas_up)]}"
            string += "-twenty-three-limit-comma-up"
            accumulated_accidentals.append(string)
        if len(accumulated_accidentals):
            accumulated_accidentals.reverse()
            if accumulated_accidentals[-1] == r"\forced-natural":
                if self.has_just_accidentals():
                    accumulated_accidentals = [_ for _ in accumulated_accidentals[:-1]]
            literal_components = []
            for accidental_string in accumulated_accidentals:
                accidental_string = accidental_string + " "
                literal_components.append(accidental_string)
            if len(literal_components) == 1:
                literal = abjad.Markup(f"{literal_components[0]}", literal=True)
            else:
                literal = abjad.Markup(literal=True).concat(literal_components)
        else:
            literal = abjad.Markup(
                fr"  \forced-{self.diatonic_accidental}", literal=True
            )
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
        HEJIVector(
                diatonic_accidental="natural",
                syntonic_commas_down=0,
                syntonic_commas_up=0,
                septimal_commas_down=0,
                septimal_commas_up=0,
                undecimal_quarter_tones_down=0,
                undecimal_quarter_tones_up=0,
                tridecimal_third_tones_down=0,
                tridecimal_third_tones_up=0,
                seventeen_limit_skhismas_down=0,
                seventeen_limit_skhismas_up=0,
                nineteen_limit_skhismas_down=0,
                nineteen_limit_skhismas_up=0,
                twenty_three_limit_commas_down=0,
                twenty_three_limit_commas_up=0,
        )

    """

    def __init__(self, pitch="c'", vector=HEJIVector()):
        self.pitch = pitch
        self.vector = vector

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.JIBundle()
            JIBundle(
                pitch=c',
                vector=HEJIVector(
                    diatonic_accidental="natural",
                    syntonic_commas_down=0,
                    syntonic_commas_up=0,
                    septimal_commas_down=0,
                    septimal_commas_up=0,
                    undecimal_quarter_tones_down=0,
                    undecimal_quarter_tones_up=0,
                    tridecimal_third_tones_down=0,
                    tridecimal_third_tones_up=0,
                    seventeen_limit_skhismas_down=0,
                    seventeen_limit_skhismas_up=0,
                    nineteen_limit_skhismas_down=0,
                    nineteen_limit_skhismas_up=0,
                    twenty_three_limit_commas_down=0,
                    twenty_three_limit_commas_up=0,
                ),
            )

        """

        return f"""{self.__class__.__name__}(
        pitch={self.pitch},
        vector={repr(self.vector)},\n)"""


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
}

_numerator_factor_to_nudge = {
    5: "syntonic_commas_down",
    7: "septimal_commas_down",
    11: "undecimal_quarter_tones_up",
    13: "tridecimal_third_tones_down",
    17: "seventeen_limit_skhismas_down",
    19: "nineteen_limit_skhismas_up",
    23: "twenty_three_limit_commas_up",
}


def make_ji_bundle(pitch, ratio):
    r"""
    Makes JI bundle.

    ..  container:: example

        >>> bundle = microtones.make_ji_bundle(abjad.NamedPitch("c'"), "3/2")
        >>> bundle.pitch
        NamedPitch("g'")

        >>> bundle.vector
        HEJIVector(
                diatonic_accidental="natural",
                syntonic_commas_down=0,
                syntonic_commas_up=0,
                septimal_commas_down=0,
                septimal_commas_up=0,
                undecimal_quarter_tones_down=0,
                undecimal_quarter_tones_up=0,
                tridecimal_third_tones_down=0,
                tridecimal_third_tones_up=0,
                seventeen_limit_skhismas_down=0,
                seventeen_limit_skhismas_up=0,
                nineteen_limit_skhismas_down=0,
                nineteen_limit_skhismas_up=0,
                twenty_three_limit_commas_down=0,
                twenty_three_limit_commas_up=0,
                )

    """

    if isinstance(pitch, str):
        pitch = abjad.NamedPitch(pitch)
    elif isinstance(pitch, int):
        pitch = abjad.NumberedPitch(pitch)
    ratio = fractions.Fraction(ratio)
    numerator_factors = _prime_factors(ratio.numerator)
    denominator_factors = _prime_factors(ratio.denominator)
    accidental_vector = HEJIVector(diatonic_accidental=pitch.accidental.name)
    for prime in numerator_factors:
        assert prime < 23
        for string in _numerator_factor_to_intervals[prime]:
            pitch = abjad.NamedInterval(string).transpose(pitch)
        if prime in _numerator_factor_to_nudge:
            string = _numerator_factor_to_nudge[prime]
            value = getattr(accidental_vector, string)
            setattr(accidental_vector, string, value + 1)
    for prime in denominator_factors:
        assert prime < 23
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


def tune_to_ratio(note_head, ratio, add_accidental=True, tempered=False):
    r"""
    Transposes notehead in place and tweaks accidental stencil.

    ..  container:: example

        >>> note = abjad.Note()
        >>> microtones.tune_to_ratio(note.note_head, "3/1")
        >>> abjad.show(note) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \forced-natural
            g''4

    ..  container:: example

        >>> note = abjad.Note()
        >>> microtones.tune_to_ratio(note.note_head, "5/1")
        >>> abjad.show(note) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \forced-natural-one-syntonic-comma-down
            e'''4

    ..  container:: example

        >>> note = abjad.Note()
        >>> microtones.tune_to_ratio(note.note_head, "5/1", add_accidental=False)
        >>> abjad.show(note) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            e'''4

    ..  container:: example

        >>> ratios = [f"{_ + 1}/1" for _ in range(11)]
        >>> notes = [abjad.Note("a,,,32") for _ in ratios]
        >>> for note, ratio in zip(notes, ratios):
        ...     microtones.tune_to_ratio(note.note_head, ratio)
        >>> staff = abjad.Staff(notes)
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                a,,,32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                a,,32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                e,32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                a,32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-sharp-one-syntonic-comma-down
                cs32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                e32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-septimal-comma-down
                g32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                a32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-natural
                b32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \forced-sharp-one-syntonic-comma-down
                cs'32
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-undecimal-quarter-tone-up
                d'32
            }

    ..  container:: example

        >>> note = abjad.Note("c'4")
        >>> microtones.tune_to_ratio(note.note_head, "5/1", tempered=True)
        >>> abjad.show(note) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \tempered-natural
            e'''4

    ..  container:: example

        >>> note = abjad.Note("cqs'4")
        >>> microtones.tune_to_ratio(note.note_head, "tempered")
        >>> abjad.show(note) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \tempered-quarter-sharp
            cqs'4

    """

    if ratio == "tempered":
        tempered_accidental = note_head.written_pitch.accidental.name
        tempered_accidental = tempered_accidental.replace(" ", "-")
        abjad.tweak(
            note_head, literal=True
        ).Accidental.stencil = r"#ly:text-interface::print"
        abjad.tweak(
            note_head, literal=True
        ).Accidental.text = fr"\tempered-{tempered_accidental}"
    else:
        bundle = make_ji_bundle(note_head.written_pitch, ratio)
        note_head.written_pitch = bundle.pitch
        if add_accidental is True:
            if tempered is True:
                tempered_accidental = note_head.written_pitch.accidental.name
                tempered_accidental = tempered_accidental.replace(" ", "-")
                abjad.tweak(
                    note_head, literal=True
                ).Accidental.stencil = r"#ly:text-interface::print"
                abjad.tweak(
                    note_head, literal=True
                ).Accidental.text = fr"\tempered-{tempered_accidental}"
            else:
                markup = bundle.vector.calculate_heji_markup()
                abjad.tweak(
                    note_head, literal=True
                ).Accidental.stencil = r"#ly:text-interface::print"
                alteration_literal = markup
                abjad.tweak(
                    note_head, literal=False
                ).Accidental.text = alteration_literal
