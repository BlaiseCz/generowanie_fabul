
    (define (domain generowanie)
        (:predicates (at ?character ?location)
(at ?item ?location)
(has ?character ?item)
(safe ?location)
(cured ?character)
(fed ?character)
(healthy ?character)
(infected ?character)
   (:action go
	:parameters ( ?c ?l1 ?l2)
	:precondition (and (at ?c  ?l1 ) (alive ?c ) (hero ?c ) (open ?l1 ) (path ?l1  ?l2  ?c  ?l2  ?c  ?l1 ))
	:effect (and (at ?c  ?l1 ) (alive ?c ) (hero ?c ) (open ?l1 ) (path ?l1  ?l2  ?c  ?l2  ?c  ?l1 ))

   )
   (:action get
	:parameters ( ?c ?i ?l)
	:precondition (and (at ?c  ?l ) (alive ?c ) (hero ?c ) (at ?i  ?l ) (safe ?l  ?c  ?i  ?i  ?l ))
	:effect (and (at ?c  ?l ) (alive ?c ) (hero ?c ) (at ?i  ?l ) (safe ?l  ?c  ?i  ?i  ?l ))

   )
   (:action ask
	:parameters ( ?c1 ?c2 ?i ?l)
	:precondition (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (healthy ?c2 ) (at ?c2  ?l ) (has ?c2  ?i  ?c2  ?c1  ?i ))
	:effect (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (healthy ?c2 ) (at ?c2  ?l ) (has ?c2  ?i  ?c2  ?c1  ?i ))

   )
   (:action give
	:parameters ( ?c1 ?c2 ?i ?l)
	:precondition (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (healthy ?c2 ) (at ?c2  ?l ) (has ?c2  ?i ) (knowneed ?c2  ?c1  ?i  ?c2  ?i  ?c1  ?i ))
	:effect (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (healthy ?c2 ) (at ?c2  ?l ) (has ?c2  ?i ) (knowneed ?c2  ?c1  ?i  ?c2  ?i  ?c1  ?i ))

   )
   (:action fixbridge
	:parameters ( ?c ?i1 ?i2 ?l)
	:precondition (and (at ?c  ?l ) (alive ?c ) (hero ?c ) (isbridge ?l ) (istool ?i1 ) (iswood ?i2 ) (has ?c  ?i1 ) (has ?c  ?i2  ?l  ?c  ?i2 ))
	:effect (and (at ?c  ?l ) (alive ?c ) (hero ?c ) (isbridge ?l ) (istool ?i1 ) (iswood ?i2 ) (has ?c  ?i1 ) (has ?c  ?i2  ?l  ?c  ?i2 ))

   )
   (:action opendoor
	:parameters ( ?c ?i ?l)
	:precondition (and (at ?c  ?l ) (alive ?c ) (hero ?c ) (iskey ?i  ?l ) (has ?c  ?i  ?l  ?c  ?i ))
	:effect (and (at ?c  ?l ) (alive ?c ) (hero ?c ) (iskey ?i  ?l ) (has ?c  ?i  ?l  ?c  ?i ))

   )
   (:action attack
	:parameters ( ?e ?c ?l)
	:precondition (and (at ?c  ?l ) (alive ?c ) (healthy ?c  ?c  ?c ))
	:effect (and (at ?c  ?l ) (alive ?c ) (healthy ?c  ?c  ?c ))

   )
   (:action cure
	:parameters ( ?c1 ?c2 ?i ?l)
	:precondition (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (at ?c2  ?l ) (alive ?c2 ) (infected ?c2 ) (has ?c1  ?i ) (isantidote ?i ) (!= ?c1  ?c2  ?c2  ?c2  ?c2  ?c1  ?i ))
	:effect (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (at ?c2  ?l ) (alive ?c2 ) (infected ?c2 ) (has ?c1  ?i ) (isantidote ?i ) (!= ?c1  ?c2  ?c2  ?c2  ?c2  ?c1  ?i ))

   )
   (:action starve
	:parameters ( ?c ?l)
	:precondition (and (at ?c  ?l ) (alive ?c ) (healthy ?c  ?c  ?c ))
	:effect (and (at ?c  ?l ) (alive ?c ) (healthy ?c  ?c  ?c ))

   )
   (:action feed
	:parameters ( ?c1 ?c2 ?i ?l)
	:precondition (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (at ?c2  ?l ) (alive ?c2 ) (starving ?c2 ) (has ?c1  ?i ) (isfood ?i ) (!= ?c1  ?c2  ?c2  ?c2  ?c2  ?c1  ?i ))
	:effect (and (at ?c1  ?l ) (alive ?c1 ) (hero ?c1 ) (at ?c2  ?l ) (alive ?c2 ) (starving ?c2 ) (has ?c1  ?i ) (isfood ?i ) (!= ?c1  ?c2  ?c2  ?c2  ?c2  ?c1  ?i ))

   )
   (:action kill
	:parameters ( ?c ?e ?l)
	:precondition (and (at ?c  ?l ) (alive ?c ) (hero ?c  ?l ))
	:effect (and (at ?c  ?l ) (alive ?c ) (hero ?c  ?l ))

   )
)
