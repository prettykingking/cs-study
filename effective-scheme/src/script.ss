;;; script.ss

;;; Command line arguments processing

#!chezscheme
; print command line arguments
(for-each
 (lambda (x) (display x) (newline))
 (cdr (command-line)))

