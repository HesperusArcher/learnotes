(defun NAME ARGLIST
  [DOCSTRING]
  BODY...)
(defvar SYMBOL &optional INITVALUE
  DOCSTRING)
(setq SYM VAL
      SYM VAL ...)
(let VARLIST
  BODY...)
(let* VARLIST
  BODY...)
(lambda ARGS
  [DOCSTRING]
  [INTERACTIVE]
  BODY)
(progn
  BODY ...)
(if COND
    THEN
  ELSE...)
(cond CLAUSES...)
(when COND
  BODY ...)
(unless COND
  BODY ...)
(when COND
  BODY ...)
(or CONDITIONS ...)
(and CONDITIONS ...)
(not OBJECT)


;; test function
(integerp OBJECT)
(floatp OBJECT)
(numberp OBJECT)
(zerop NUMBER)
(wholenump OBJECT)
;; compare function
(> NUM1 NUM2)
(< NUM1 NUM2)
(>= NUM1 NUM2)
(<= NUM1 NUM2)
(= NUM1 NUM2)
(eql OBJ1 OBJ2)
(/= NUM1 NUM2)
;; transform function
(float ARG)
(truncate ARG &optional DIVISOR)
(floor ARG &optional DIVISOR)
(ceiling ARG &optional DIVISOR)
(round ARG &optional DIVISOR)
;; calculate
(+ &rest NUMBERS-OR-MARKERS)
(- &optional NUMBER-OR-MARKER &rest MORE-NUMBERS-OR-MARKERS)
(* &rest NUMBERS-OR-MARKERS)
(/ DIVIDEND DIVISOR &rest DIVISORS)
(1+ NUMBER)
(1- NUMBER)
(abs ARG)
(% X Y)
(mod X Y)
(sin ARG)
(cos ARG)
(tan ARG)
(asin ARG)
(acos ARG)
(atan Y &optional X)
(sqrt ARG)
(exp ARG)
(expt ARG1 ARG2)
(log ARG &optional BASE)
(log10 ARG)
(logb ARG)
;; random
(random &optional N)
