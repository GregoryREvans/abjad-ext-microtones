\version "2.19.84"


#(define-markup-command
    (thin-fraction-up-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction #num #den
    \path #0.15
      #'(
          (moveto 0.4 1.85)
          (lineto 0.4 2.7)
          (moveto 0.1 1.9)
          (lineto 0.4 2.7)
          (lineto 0.7 1.9)
          )
    #}))

#(define-markup-command
    (thin-fraction-down-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction #num #den
    \path #0.15
      #'(
          (moveto 0.4 -0.95)
          (lineto 0.4 -1.7)
          (moveto 0.1 -1)
          (lineto 0.4 -1.78)
          (lineto 0.7 -1)
          )
    #}))

#(define-markup-command
    (wide-fraction-up-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction #num #den
    \path #0.15
      #'(
          (moveto 0.8 1.85)
          (lineto 0.8 2.7)
          (moveto 0.5 1.9)
          (lineto 0.8 2.7)
          (lineto 1.1 1.9)
          )
    #}))

#(define-markup-command
    (wide-fraction-down-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #-4
    \translate #'(0 . -0.5)
    \combine
    \fraction #num #den
    \path #0.15
      #'(
          (moveto 0.8 -0.95)
          (lineto 0.8 -1.7)
          (moveto 0.5 -1)
          (lineto 0.8 -1.78)
          (lineto 1.1 -1)
          )
    #}))



one-third-sharp-markup = \markup \thin-fraction-up-markup 1 3
two-thirds-sharp-markup = \markup \thin-fraction-up-markup 2 3
one-third-flat-markup = \markup \thin-fraction-down-markup 1 3
two-thirds-flat-markup = \markup \thin-fraction-down-markup 2 3
one-sixth-sharp-markup = \markup \thin-fraction-up-markup 1 6
five-sixths-sharp-markup = \markup \thin-fraction-up-markup 5 6
one-sixth-flat-markup = \markup \thin-fraction-down-markup 1 6
five-sixths-flat-markup = \markup \thin-fraction-down-markup 5 6
one-twelfth-sharp-markup = \markup \wide-fraction-up-markup 1 12
five-twelfths-sharp-markup = \markup \wide-fraction-up-markup 5 12
seven-twelfths-sharp-markup = \markup \wide-fraction-up-markup 7 12
eleven-twelfths-sharp-markup = \markup \wide-fraction-up-markup 11 12
one-twelfth-flat-markup = \markup \wide-fraction-down-markup 1 12
five-twelfths-flat-markup = \markup \wide-fraction-down-markup 5 12
seven-twelfths-flat-markup = \markup \wide-fraction-down-markup 7 12
eleven-twelfths-flat-markup = \markup \wide-fraction-down-markup 11 12
one-fifth-sharp-markup = \markup \thin-fraction-up-markup 1 5
two-fifths-sharp-markup = \markup \thin-fraction-up-markup 2 5
three-fifths-sharp-markup = \markup \thin-fraction-up-markup 3 5
four-fifths-sharp-markup = \markup \thin-fraction-up-markup 4 5
one-fifth-flat-markup = \markup \thin-fraction-down-markup 1 5
two-fifths-flat-markup = \markup \thin-fraction-down-markup 2 5
three-fifths-flat-markup = \markup \thin-fraction-down-markup 3 5
four-fifths-flat-markup = \markup \thin-fraction-down-markup 4 5
