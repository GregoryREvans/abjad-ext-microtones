%%% natural %%%
forced-natural =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \forced-natural-markup
        $note #})

%%% sharp %%%
forced-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \forced-sharp-markup
        $note #})

%%% flat %%%
forced-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \forced-flat-markup
        $note #})

%%% double sharp %%%
double-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \double-sharp-markup
        $note #})

%%% double flat %%%
double-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \double-flat-markup
        $note #})

%%% one quarter tone up %%%
quarter-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \quarter-sharp-markup
        $note #})

%%% one quarter tone up %%%
three-quarters-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \three-quarters-sharp-markup
        $note #})

%%% one quarter tone down %%%
quarter-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \quarter-flat-markup
        $note #})

%%% one quarter tone down %%%
three-quarters-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \three-quarters-flat-markup
        $note #})

%%% one eighth tone up %%%
one-eighth-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \eighth-sharp-markup
        $note #})

%%% three eighth tones up %%%
three-eighths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \three-eighths-sharp-markup
        $note #})

%%% five eighth tones up %%%
five-eighths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \five-eighths-sharp-markup
        $note #})

%%% seven eighth tones up %%%
seven-eighths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \seven-eighths-sharp-markup
        $note #})

%%% one eighth tone down %%%
one-eighth-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \eighth-flat-markup
        $note #})

%%% three eighth tones down %%%
three-eighths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \three-eighths-flat-markup
        $note #})

%%% five eighth tones down %%%
five-eighths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \five-eighths-flat-markup
        $note #})

%%% seven eighth tones down %%%
seven-eighths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \seven-eighths-flat-markup
        $note #})

%%% one third up %%%
one-third-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-third-sharp-markup
        $note #})

%%% two thirds up %%%
two-thirds-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \two-thirds-sharp-markup
        $note #})

%%% one third down %%%
one-third-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-third-flat-markup
        $note #})

%%% two thirds down %%%
two-thirds-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \two-thirds-flat-markup
        $note #})

%%% one sixth up %%%
one-sixth-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-sixth-sharp-markup
        $note #})

%%% five sixths up %%%
five-sixths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \five-sixths-sharp-markup
        $note #})

%%% one sixth down %%%
one-sixth-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-sixth-flat-markup
        $note #})

%%% five sixths down %%%
five-sixths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \five-sixths-flat-markup
        $note #})

%%% one twelfth up %%%
one-twelfth-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-twelfth-sharp-markup
        $note #})

%%% five twelfths up %%%
five-twelfths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \five-twelfths-sharp-markup
        $note #})

%%% seven twelfths up %%%
seven-twelfths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \seven-twelfths-sharp-markup
        $note #})

%%% eleven twelfths up %%%
eleven-twelfths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \eleven-twelfths-sharp-markup
        $note #})

%%% one twelfth down %%%
one-twelfth-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-twelfth-flat-markup
        $note #})

%%% five twelfths down %%%
five-twelfths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \five-twelfths-flat-markup
        $note #})

%%% seven twelfths down %%%
seven-twelfths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \seven-twelfths-flat-markup
        $note #})

%%% eleven twelfths down %%%
eleven-twelfths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \eleven-twelfths-flat-markup
        $note #})

%%% one fifth up %%%
one-fifth-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-fifth-sharp-markup
        $note #})

%%% two fifths up %%%
two-fifths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \two-fifths-sharp-markup
        $note #})

%%% three fifths up %%%
three-fifths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \three-fifths-sharp-markup
        $note #})

%%% four fifths up %%%
four-fifths-sharp =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \four-fifths-sharp-markup
        $note #})

%%% one fifth down %%%
one-fifth-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \one-fifth-flat-markup
        $note #})

%%% two fifths down %%%
two-fifths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \two-fifths-flat-markup
        $note #})

%%% three fifths down %%%
three-fifths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \three-fifths-flat-markup
        $note #})

%%% four fifths down %%%
four-fifths-flat =
#(define-music-function (parser location note)   (ly:music?)
 #{ \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \four-fifths-flat-markup
        $note #})
