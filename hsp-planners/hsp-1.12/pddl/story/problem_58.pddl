
    (define  (problem projekcik)
        (:domain generowanie)
        (:objects
    		john anne maggie rick bob matt robin 		forest vilage johnhouse neighborhouse hospital hospitaldoor store vilageislandbridge island islandwest islandeast islandmountainbridge mountain mountainwest mountaineast 		antidote1 antidote2 antidote3 antidote4 antidote5 wood1 wood2 wood3 wood4 hospitalkey toolkit1 toolkit2 food1 food2 food3 food4 food5 		zombie 		bigzombie 
        )
        (:init
    		(path johnhouse vilage)
		(path vilage johnhouse)
		(path forest vilage)
		(path vilage forest)
		(path neighborhouse vilage)
		(path vilage neighborhouse)
		(path hospitaldoor vilage)
		(path vilage hospitaldoor)
		(path hospitaldoor hospital)
		(path hospital hospitaldoor)
		(path store vilage)
		(path vilage store)
		(path vilageislandbridge vilage)
		(path vilage vilageislandbridge)
		(path vilageislandbridge island)
		(path island vilageislandbridge)
		(path island islandwest)
		(path islandwest island)
		(path island islandeast)
		(path islandeast island)
		(path island islandmountainbridge)
		(path islandmountainbridge island)
		(path mountain islandmountainbridge)
		(path islandmountainbridge mountain)
		(path mountain mountainwest)
		(path mountainwest mountain)
		(path mountain mountaineast)
		(path mountaineast mountain)
		(open forest)
		(open vilage)
		(open johnhouse)
		(open neighborhouse)
		(open hospital)
		(open store)
		(open island)
		(open islandwest)
		(open islandeast)
		(open mountain)
		(open mountainwest)
		(open mountaineast)
		(safe johnhouse)
		(safe neighborhouse)
		(safe hospital)
		(safe store)
		(hero john)
		(alive john)
		(alive anne)
		(alive maggie)
		(alive rick)
		(alive bob)
		(alive matt)
		(alive robin)
		(healthy john)
		(healthy anne)
		(healthy maggie)
		(healthy rick)
		(healthy bob)
		(healthy matt)
		(healthy robin)
		(at john johnhouse)
		(at anne johnhouse)
		(at maggie johnhouse)
		(at rick store)
		(at bob hospital)
		(at matt islandeast)
		(at robin mountainwest)
		(istool toolkit1)
		(istool toolkit2)
		(iswood wood1)
		(iswood wood2)
		(iswood wood3)
		(iswood wood4)
		(isbridge vilageislandbridge)
		(isbridge islandmountainbridge)
		(isantidote antidote1)
		(isantidote antidote2)
		(isantidote antidote3)
		(isantidote antidote4)
		(isantidote antidote5)
		(isfood food1)
		(isfood food2)
		(isfood food3)
		(isfood food4)
		(isfood food5)
		(iskey hospitalkey hospitaldoor)
		(at food1 mountainwest)
		(at wood1 forest)
		(at hospitalkey forest)
		(at antidote2 hospital)
		(has bob antidote3)
		(has rick food2)
		(at food3 hospital)
		(at wood2 islandeast)

        )
        (:goal
    		(healthy bob)

        )
    )
    