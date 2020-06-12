\version "2.19.84"
\language "english"


%%% one third up %%%
one-third-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 3
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% two thirds up %%%
two-thirds-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 2 3
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% one third down %%%
one-third-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 3
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% two thirds down %%%
two-thirds-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 2 3
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% one sixth up %%%
one-sixth-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 6
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% five sixths up %%%
five-sixths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 5 6
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% one sixth down %%%
one-sixth-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 6
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% five sixths down %%%
five-sixths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 5 6
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% one twelfth up %%%
one-twelfth-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 12
    \path #0.15
      #'(
          (moveto 0.8 1.85)
          (lineto 0.8 2.7)
          (moveto 0.5 1.9)
          (lineto 0.8 2.7)
          (lineto 1.1 1.9)
          )
}

%%% five twelfths up %%%
five-twelfths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 5 12
    \path #0.15
      #'(
          (moveto 0.8 1.85)
          (lineto 0.8 2.7)
          (moveto 0.5 1.9)
          (lineto 0.8 2.7)
          (lineto 1.1 1.9)
          )
}

%%% seven twelfths up %%%
seven-twelfths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 7 12
    \path #0.15
      #'(
          (moveto 0.8 1.85)
          (lineto 0.8 2.7)
          (moveto 0.5 1.9)
          (lineto 0.8 2.7)
          (lineto 1.1 1.9)
          )
}

%%% eleven twelfths up %%%
eleven-twelfths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 11 12
    \path #0.15
      #'(
          (moveto 0.8 1.85)
          (lineto 0.8 2.7)
          (moveto 0.5 1.9)
          (lineto 0.8 2.7)
          (lineto 1.1 1.9)
          )
}

%%% one twelfth down %%%
one-twelfth-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 12
    \path #0.15
      #'(
          (moveto 0.8 -0.95)
          (lineto 0.8 -1.7)
          (moveto 0.5 -1)
          (lineto 0.8 -1.78)
          (lineto 1.1 -1)
          )
}

%%% five twelfths down %%%
five-twelfths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 5 12
    \path #0.15
      #'(
          (moveto 0.8 -0.95)
          (lineto 0.8 -1.7)
          (moveto 0.5 -1)
          (lineto 0.8 -1.78)
          (lineto 1.1 -1)
          )
}

%%% seven twelfths down %%%
seven-twelfths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 7 12
    \path #0.15
      #'(
          (moveto 0.8 -0.95)
          (lineto 0.8 -1.7)
          (moveto 0.5 -1)
          (lineto 0.8 -1.78)
          (lineto 1.1 -1)
          )
}

%%% eleven twelfths down %%%
eleven-twelfths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 11 12
    \path #0.15
      #'(
          (moveto 0.8 -0.95)
          (lineto 0.8 -1.7)
          (moveto 0.5 -1)
          (lineto 0.8 -1.78)
          (lineto 1.1 -1)
          )
}

%%% one fifth up %%%
one-fifth-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 5
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% two fifths up %%%
two-fifths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 2 5
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% three fifths up %%%
three-fifths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 3 5
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% four fifths up %%%
four-fifths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 4 5
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
}

%%% one fifth down %%%
one-fifth-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 1 5
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% two fifths down %%%
two-fifths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 2 5
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% three fifths down %%%
three-fifths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 3 5
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}

%%% four fifths down %%%
four-fifths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction 4 5
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
}
