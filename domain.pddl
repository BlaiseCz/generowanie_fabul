
(define (domain castles-witches)
   (:requirements :strips :typing)
   (:types character location item enemy bigenemy)
   (:action go
	:parameters (?c - character ?l1 - location ?l2 - location )
	:precondition (and (at?c ?l1 ) (alive?c ) (hero?c ) (open?l1 ) (path?l1 ?l2 ?c ?l2 ?c ?l1 ))
	:effect (and (at?c ?l1 ) (alive?c ) (hero?c ) (open?l1 ) (path?l1 ?l2 ?c ?l2 ?c ?l1 )
   )
   (:action get
	:parameters (?c - character ?i - item ?l - location )
	:precondition (and (at?c ?l ) (alive?c ) (hero?c ) (at?i ?l ) (safe?l ?c ?i ?i ?l ))
	:effect (and (at?c ?l ) (alive?c ) (hero?c ) (at?i ?l ) (safe?l ?c ?i ?i ?l )
   )
   (:action ask
	:parameters (?c1 - character ?c2 - character ?i - item ?l - location )
	:precondition (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (healthy?c2 ) (at?c2 ?l ) (has?c2 ?i ?c2 ?c1 ?i ))
	:effect (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (healthy?c2 ) (at?c2 ?l ) (has?c2 ?i ?c2 ?c1 ?i )
   )
   (:action give
	:parameters (?c1 - character ?c2 - character ?i - item ?l - location )
	:precondition (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (healthy?c2 ) (at?c2 ?l ) (has?c2 ?i ) (knowneed?c2 ?c1 ?i ?c2 ?i ?c1 ?i ))
	:effect (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (healthy?c2 ) (at?c2 ?l ) (has?c2 ?i ) (knowneed?c2 ?c1 ?i ?c2 ?i ?c1 ?i )
   )
   (:action fixbridge
	:parameters (?c - character ?i1 - item ?i2 - item ?l - location )
	:precondition (and (at?c ?l ) (alive?c ) (hero?c ) (isbridge?l ) (istool?i1 ) (iswood?i2 ) (has?c ?i1 ) (has?c ?i2 ?l ?c ?i2 ))
	:effect (and (at?c ?l ) (alive?c ) (hero?c ) (isbridge?l ) (istool?i1 ) (iswood?i2 ) (has?c ?i1 ) (has?c ?i2 ?l ?c ?i2 )
   )
   (:action opendoor
	:parameters (?c - character ?i - item ?l - location )
	:precondition (and (at?c ?l ) (alive?c ) (hero?c ) (iskey?i ?l ) (has?c ?i ?l ?c ?i ))
	:effect (and (at?c ?l ) (alive?c ) (hero?c ) (iskey?i ?l ) (has?c ?i ?l ?c ?i )
   )
   (:action attack
	:parameters (?e - enemy ?c - character ?l - location )
	:precondition (and (at?c ?l ) (alive?c ) (healthy?c ?c ?c ))
	:effect (and (at?c ?l ) (alive?c ) (healthy?c ?c ?c )
   )
   (:action cure
	:parameters (?c1 - character ?c2 - character ?i - item ?l - location )
	:precondition (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (at?c2 ?l ) (alive?c2 ) (infected?c2 ) (has?c1 ?i ) (isantidote?i ) (!=?c1 ?c2 ?c2 ?c2 ?c2 ?c1 ?i ))
	:effect (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (at?c2 ?l ) (alive?c2 ) (infected?c2 ) (has?c1 ?i ) (isantidote?i ) (!=?c1 ?c2 ?c2 ?c2 ?c2 ?c1 ?i )
   )
   (:action starve
	:parameters (?c - character ?l - location )
	:precondition (and (at?c ?l ) (alive?c ) (healthy?c ?c ?c ))
	:effect (and (at?c ?l ) (alive?c ) (healthy?c ?c ?c )
   )
   (:action feed
	:parameters (?c1 - character ?c2 - character ?i - item ?l - location )
	:precondition (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (at?c2 ?l ) (alive?c2 ) (starving?c2 ) (has?c1 ?i ) (isfood?i ) (!=?c1 ?c2 ?c2 ?c2 ?c2 ?c1 ?i ))
	:effect (and (at?c1 ?l ) (alive?c1 ) (hero?c1 ) (at?c2 ?l ) (alive?c2 ) (starving?c2 ) (has?c1 ?i ) (isfood?i ) (!=?c1 ?c2 ?c2 ?c2 ?c2 ?c1 ?i )
   )
   (:action kill
	:parameters (?c - character ?e - bigenemy ?l - location )
	:precondition (and (at?c ?l ) (alive?c ) (hero?c ?l ))
	:effect (and (at?c ?l ) (alive?c ) (hero?c ?l )
   )
