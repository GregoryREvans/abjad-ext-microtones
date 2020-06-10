\version "2.19.84"
\language "english"
\include "fraction-accidental-markups.ily"
\include "general-edo-accidental-markups.ily"


%%% one quarter tone down %%%
quarter-flat-markup = \markup {
    \fontsize #5
    \override #'(font-name . "ekmelos")
    \char ##xe480
}

%%% three quarter tones down %%%
three-quarters-flat-markup = \markup {
    \fontsize #5
    \override #'(font-name . "ekmelos")
    \char ##xe296
}

%%% three eighth tones down %%%
three-eighths-flat-markup = \markup {
    \fontsize #5
    \override #'(font-name . "ekmelos")
    \char ##xe480
    \postscript #"gsave
        0.15 setlinewidth
        -0.73 -0.25 moveto
        -0.73 -1.4 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.03 -0.7 moveto
        -0.73 -1.48 lineto
        -0.43 -0.7 lineto
        stroke grestore"
}

%%% seven eighth tones down %%%
seven-eighths-flat-markup = \markup {
    \fontsize #5
    \override #'(font-name . "ekmelos")
    \char ##xe296
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -0.25 moveto
        -1.40 -1.4 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -0.7 moveto
        -1.40 -1.48 lineto
        -1.10 -0.7 lineto
        stroke grestore"
}
