\version "2.19.84"
\language "english"



%%% natural %%%
forced-natural-markup = \markup {
    \musicglyph #"accidentals.natural"
}

%%% sharp %%%
forced-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp"
}

%%% flat %%%
forced-flat-markup = \markup {
    \musicglyph #"accidentals.flat"
}

%%% double sharp %%%
double-sharp-markup = \markup {
    \musicglyph #"accidentals.doublesharp"
}

%%% double flat %%%
double-flat-markup = \markup {
    \musicglyph #"accidentals.flatflat"
}

%%% one quarter tone up %%%
quarter-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stem"
}

%%% three quarter tones up %%%
three-quarters-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stemstemstem"
}

%%% one eighth tone up %%%
eighth-sharp-markup = \markup {
    \musicglyph #"accidentals.natural"
    \postscript #"gsave
        0.17 setlinewidth
        -1.2 1.25 moveto
        -1.2 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.5 1.4 moveto
        -1.2 2.18 lineto
        -0.9 1.4 lineto
        stroke grestore"
}

%%% three eighth tones up %%%
three-eighths-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stem"
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% five eighth tones up %%%
five-eighths-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp"
    \postscript #"gsave
        0.17 setlinewidth
        -0.91 1.25 moveto
        -0.91 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.21 1.4 moveto
        -0.91 2.18 lineto
        -0.61 1.4 lineto
        stroke grestore"
}

%%% seven eighth tones up %%%
seven-eighths-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stemstemstem"
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% one eighth tone down %%%
eighth-flat-markup = \markup {
    \musicglyph #"accidentals.natural"
    \postscript #"gsave
        0.15 setlinewidth
        -0.67 -1.35 moveto
        -0.67 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -0.97 -1.4 moveto
        -0.67 -2.18 lineto
        -0.37 -1.4 lineto
        stroke grestore"
}

%%% five eighth tones down %%%
five-eighths-flat-markup = \markup {
    \musicglyph #"accidentals.flat"
    \postscript #"gsave
        0.15 setlinewidth
        -1.38 -0.25 moveto
        -1.38 -1.4 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.68 -0.7 moveto
        -1.38 -1.48 lineto
        -1.08 -0.7 lineto
        stroke grestore"
}
