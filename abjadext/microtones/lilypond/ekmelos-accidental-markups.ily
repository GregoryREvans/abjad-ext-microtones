#(ly:set-option 'relative-includes #t)
font-name = "ekmelos"
\include "markup-functions.ily"

% tempered accidentals %
tempered-double-flat = \markup {
    \musicglyph #"accidentals.flatflat"
    \postscript #"gsave
    0.1 setlinewidth
    -1.75 1.8 moveto
    -1.2 1.8 lineto
    -1 1.8 lineto
    stroke grestore"
}

tempered-three-quarters-flat = \markup {
    \musicglyph #"accidentals.mirroredflat.flat"
    \postscript #"gsave
    0.1 setlinewidth
    -1.75 1.8 moveto
    -1.2 1.8 lineto
    -1 1.8 lineto
    stroke grestore"
}

tempered-flat = \markup {
    \musicglyph #"accidentals.flat"
    \postscript #"gsave
    0.1 setlinewidth
    -1.75 1.8 moveto
    -1.2 1.8 lineto
    -1 1.8 lineto
    stroke grestore"
}

tempered-quarter-flat = \markup {
    \musicglyph #"accidentals.mirroredflat"
    \postscript #"gsave
    0.1 setlinewidth
    -1.1 1.8 moveto
    -0.55 1.8 lineto
    -0.35 1.8 lineto
    stroke grestore"
}

tempered-natural = \markup {
    \musicglyph #"accidentals.natural"
    \postscript #"gsave
    0.1 setlinewidth
    -1.55 1.5 moveto
    -1.2 1.5 lineto
    -0.85 1.5 lineto
    stroke grestore"
}

tempered-quarter-sharp = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stem"
    \postscript #"gsave
    0.1 setlinewidth
    -1.3 1.3 moveto
    -0.95 1.3 lineto
    -0.6 1.3 lineto
    stroke grestore"
}

tempered-sharp = \markup {
    \musicglyph #"accidentals.sharp"
    \postscript #"gsave
    0.1 setlinewidth
    -1.25 1.45 moveto
    -0.9 1.45 lineto
    -0.55 1.45 lineto
    stroke grestore"
}

tempered-three-quarters-sharp = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stemstemstem"
    \postscript #"gsave
    0.1 setlinewidth
    -1.25 1.45 moveto
    -0.9 1.45 lineto
    -0.55 1.45 lineto
    stroke grestore"
}

tempered-double-sharp = \markup {
    \musicglyph #"accidentals.doublesharp"
    \postscript #"gsave
    0.17 setlinewidth
    -1.1 0 moveto
    -1.1 1.05 lineto
    stroke grestore
    gsave
    0.1 setlinewidth
    -1.45 1.05 moveto
    -1.1 1.05 lineto
    -0.75 1.05 lineto
    stroke grestore"
}
