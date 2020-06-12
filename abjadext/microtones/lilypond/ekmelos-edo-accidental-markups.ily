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
    \combine
    \char ##xe480
    \path #0.15
      #'(
          (moveto 0.74 -0.65)
          (lineto 0.74 -1.4)
          (moveto 0.44 -0.7)
          (lineto 0.74 -1.48)
          (lineto 1.04 -0.7)
          )
}

%%% seven eighth tones down %%%
seven-eighths-flat-markup = \markup {
    \fontsize #5
    \override #'(font-name . "ekmelos")
    \combine
    \char ##xe296
    \path #0.15
      #'(
          (moveto 0.77 -0.65)
          (lineto 0.77 -1.4)
          (moveto 0.47 -0.7)
          (lineto 0.77 -1.48)
          (lineto 1.07 -0.7)
          )
}
