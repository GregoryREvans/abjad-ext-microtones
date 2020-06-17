\version "2.19.84"


#(define-markup-command
    (thin-fraction-up-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
	\override #'(style . outline)
    \override #'(thickness . 0.8)
	\whiteout
    \fontsize #-4
	\translate #'(0 . -0.4)
	\bold
    \combine
	\translate #'(0.40 . 2.7)
	\musicglyph #"arrowheads.close.11"
    \fraction #num #den
    #}))

#(define-markup-command
    (thin-fraction-down-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
	\override #'(style . outline)
    \override #'(thickness . 0.8)
	\whiteout
    \fontsize #-4
	\translate #'(0 . -0.4)
	\bold
    \combine
    \fraction #num #den
	\translate #'(0.40 . -1.8)
	\musicglyph #"arrowheads.close.1M1"
    #}))

#(define-markup-command
    (wide-fraction-up-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
	\override #'(style . outline)
    \override #'(thickness . 0.8)
	\whiteout
    \fontsize #-4
	\translate #'(0 . -0.4)
	\bold
    \combine
	\translate #'(0.81 . 2.7)
	\musicglyph #"arrowheads.close.11"
    \fraction #num #den
    #}))

#(define-markup-command
    (wide-fraction-down-markup layout props num den)
    (markup? markup?)
    (interpret-markup layout props
    #{
    \markup
	\override #'(style . outline)
    \override #'(thickness . 0.8)
	\whiteout
    \fontsize #-4
    \translate #'(0 . -0.4)
	\bold
	\combine
    \fraction #num #den
	\translate #'(0.81 . -1.8)
	\musicglyph #"arrowheads.close.1M1"
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
one-tenth-sharp-markup = \markup \wide-fraction-up-markup 1 10
three-tenths-sharp-markup = \markup \wide-fraction-up-markup 3 10
seven-tenths-sharp-markup = \markup \wide-fraction-up-markup 7 10
one-tenth-flat-markup = \markup \wide-fraction-down-markup 1 10
three-tenths-flat-markup = \markup \wide-fraction-down-markup 3 10
seven-tenths-flat-markup = \markup \wide-fraction-down-markup 7 10
