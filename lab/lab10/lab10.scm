;   (define (over-or-under num1 num2) 
;    (if (> num1 num2 )
;    '1
;   (if (= num1 num2)
;   '0
;    '-1)
;    ))
(define (over-or-under num1 num2) 
(cond
((< num1 num2 ) -1)
((= num1 num2 ) 0)
(else 1)))

(define (make-adder num) 
(lambda(inc) (+ inc num)))

(define (composed f g) 
(lambda(x) (f 
    (g x))))  

(define lst 
(list '(1) 2 '(3 4) 5))

(define (duplicate lst)
   (if (null? lst)
       lst
       (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
)