;;; socket.ss

#!chezscheme
(define listener (listen-tcp "::" 5300 self))
(printf "Waiting for connection on port ~a~%"
        (listener-port-number listener))
(receive
    [#(accept-tcp ,_ ,ip ,op)
     (printf "Handling new connection~%")
     (put-bytevector op (string->utf8 (format "Heihei~%")))
     (flush-output-port op)
     (close-port op)]
    [#(accept-tcp-failed ,_ ,_ ,_)
     (printf "Bye-bye~%")])
