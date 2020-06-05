#(define-markup-command
    (heji-accidental-markup layout props point-code)
    (number?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #5
    \override #'(font-name . "ekmelos")
    \char #point-code
    #}))

% tempered accidentals %
tempered-double-flat = \markup {\musicglyph #"accidentals.flatflat"
          \postscript #"gsave 0.1 setlinewidth -1.75 1.8 moveto -1.2 1.8 lineto -1 1.8 lineto
          stroke grestore"}

tempered-three-quarters-flat = \markup {\musicglyph #"accidentals.mirroredflat.flat"
       \postscript #"gsave 0.1 setlinewidth -1.75 1.8 moveto -1.2 1.8 lineto -1 1.8 lineto
       stroke grestore"}

tempered-flat = \markup {\musicglyph #"accidentals.flat"
          \postscript #"gsave 0.1 setlinewidth -1.75 1.8 moveto -1.2 1.8 lineto -1 1.8 lineto
          stroke grestore"}

tempered-quarter-flat = \markup {\musicglyph #"accidentals.mirroredflat"
       \postscript #"gsave 0.1 setlinewidth -1.1 1.8 moveto -0.55 1.8 lineto -0.35 1.8 lineto
       stroke grestore"}

tempered-natural = \markup {\musicglyph #"accidentals.natural"
          \postscript #"gsave 0.1 setlinewidth -1.55 1.5 moveto -1.2 1.5 lineto -0.85 1.5 lineto
          stroke grestore"}

tempered-quarter-sharp = \markup {\musicglyph #"accidentals.sharp.slashslash.stem"
       \postscript #"gsave 0.1 setlinewidth -1.3 1.3 moveto -0.95 1.3 lineto -0.6 1.3 lineto
       stroke grestore"}

tempered-sharp = \markup {\musicglyph #"accidentals.sharp"
          \postscript #"gsave 0.1 setlinewidth -1.25 1.45 moveto -0.9 1.45 lineto -0.55 1.45 lineto
          stroke grestore"}

tempered-three-quarters-sharp = \markup {\musicglyph #"accidentals.sharp.slashslash.stemstemstem"
          \postscript #"gsave 0.1 setlinewidth -1.25 1.45 moveto -0.9 1.45 lineto -0.55 1.45 lineto
          stroke grestore"}

tempered-double-sharp = \markup {\musicglyph #"accidentals.doublesharp"
          \postscript #"gsave 0.17 setlinewidth -1.1 0 moveto -1.1 1.05 lineto
          stroke grestore
          gsave 0.1 setlinewidth -1.45 1.05 moveto -1.1 1.05 lineto -0.75 1.05 lineto
          stroke grestore"}


% diatonic accidentals %
forced-natural = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##x266e
    }
}
forced-sharp = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe262
    }
}
forced-flat = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe260
    }
}
forced-double-sharp = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe263
    }
}
forced-double-flat = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe264
    }
}


% natural syntonic commas %
forced-natural-one-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c2
    }
}
forced-natural-two-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2cc
    }
}
forced-natural-three-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d6
    }
}
forced-natural-one-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c7
    }
}
forced-natural-two-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d1
    }
}
forced-natural-three-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2db
    }
}
% sharp syntonic commas %
forced-sharp-one-syntonic-comma-down = \markup \heji-accidental-markup ##xe2c3
forced-sharp-two-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2cd
    }
}
forced-sharp-three-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d7
    }
}
forced-sharp-one-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c8
    }
}
forced-sharp-two-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d2
    }
}
forced-sharp-three-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2dc
    }
}
% flat syntonic commas %
forced-flat-one-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c1
    }
}
forced-flat-two-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2cb
    }
}
forced-flat-three-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d5
    }
}
forced-flat-one-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c6
    }
}
forced-flat-two-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d0
    }
}
forced-flat-three-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2da
    }
}
% double sharp syntonic commas %
forced-double-sharp-one-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c4
    }
}
forced-double-sharp-two-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ce
    }
}
forced-double-sharp-three-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d8
    }
}
forced-double-sharp-one-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c9
    }
}
forced-double-sharp-two-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d3
    }
}
forced-double-sharp-three-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2dd
    }
}
% double flat syntonic commas %
forced-double-flat-one-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c0
    }
}
forced-double-flat-two-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ca
    }
}
forced-double-flat-three-syntonic-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d4
    }
}
forced-double-flat-one-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c5
    }
}
forced-double-flat-two-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2c5
    }
}
forced-double-flat-three-syntonic-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2d9
    }
}


% septimal commas %
one-septimal-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2de
    }
}
two-septimal-comma-down =
\markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e0
    }
}
three-septimal-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2de
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e0
    }
}
one-septimal-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2df
    }
}
two-septimal-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e1
    }
}
three-septimal-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2df
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e1
    }
}


% undecimal quarter tones %
one-undecimal-quarter-tone-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e2
    }
}
two-undecimal-quarter-tone-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e2
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e2
    }
}
three-undecimal-quarter-tone-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e2
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e2
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e2
    }
}
one-undecimal-quarter-tone-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e3
    }
}
two-undecimal-quarter-tone-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e3
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e3
    }
}
three-undecimal-quarter-tone-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e3
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e3
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e3
    }
}


% tridecimal third tones %
one-tridecimal-third-tone-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e4
    }
}
two-tridecimal-third-tone-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e4
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e4
    }
}
three-tridecimal-third-tone-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e4
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e4
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e4
    }
}
one-tridecimal-third-tone-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e5
    }
}
two-tridecimal-third-tone-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e5
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e5
    }
}
three-tridecimal-third-tone-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e5
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e5
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e5
    }
}


% seventeen-limit skhismas %
one-seventeen-limit-skhisma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e6
    }
}
two-seventeen-limit-skhisma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e6
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e6
    }
}
three-seventeen-limit-skhisma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e6
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e6
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e6
    }
}
one-seventeen-limit-skhisma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e7
    }
}
two-seventeen-limit-skhisma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e7
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e7
    }
}
three-seventeen-limit-skhisma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e7
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e7
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e7
    }
}


% nineteen-limit skhismas %
one-nineteen-limit-skhisma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e8
    }
}
two-nineteen-limit-skhisma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e8
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e8
    }
}
three-nineteen-limit-skhisma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e8
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e8
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e8
    }
}
one-nineteen-limit-skhisma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e9
    }
}
two-nineteen-limit-skhisma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e9
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e9
    }
}
three-nineteen-limit-skhisma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e9
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e9
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2e9
    }
}

one-twenty-three-limit-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2eb
    }
}
two-twenty-three-limit-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2eb
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2eb
    }
}
three-twenty-three-limit-comma-down = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2eb
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2eb
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2eb
    }
}
one-twenty-three-limit-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ea
    }
}
two-twenty-three-limit-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ea
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ea
    }
}
three-twenty-three-limit-comma-up = \markup {
    \concat {
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ea
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ea
        \fontsize #5
        \override #'(font-name . "ekmelos")
        \char ##xe2ea
    }
}
