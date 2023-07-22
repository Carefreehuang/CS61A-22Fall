(define (vir-fib n)
    (if (<= n 1)
        n
        (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
)
(define (remove item lst)
  (cond ((null? lst) '())
        ((equal? item (car lst)) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst)))))
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))

(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)