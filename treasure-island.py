# 100 Days of Python
# Day 3 - Treasure Island/Choose Your Own Adventure Game
# Sarah Vigstol
# 4/21/21


print('''
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
.............................................,,,,,,,,,,,................................................................
.........................................,,,,,=======~,,,,,,,,,,........................................................
.......................................,,,~==================~,,,,,,,,,,................................................
.....................................,,,=============================,,,,,,,,,,.........................................
....................................,,:======================================:,,,,,,,,,.................................
..................................,,,,:~============================================~:,,,,,,,,,.........................
...................................,,,,,,,,,,,,,~==================================:,,,,,:~~~,,,,,......................
....................................,,~~~~~~~:,,,,,,,,,,,~=======================,,,:===========~,,,....................
.....................................,,~~~~~~~~~~~~~~:,,,,,,,,,,,:============:,,,=~===========~==:,,...................
......................................,,~~~~~~~~~~~~~~~~~~~,,:::,,,,,,,,,,,~,,,~===================:,,..................
.......................................,,~~~~~~~~~~~~~~~~~,,:::::::::::::,,,,,======================,,..................
........................................,,~~~~~~~~~~~~~~~,,::::::::::::::::::,,====================~~,,.................
..........................++.............,,~~~~~~~~~~~~:,,::::::::::::::::::::,,:====================,,.................
...........................++.............,,~~~~~~~~~~,,,::::::::::::::::::::::,,,===================,,.................
............................++.............,,~~~~~~~,,,::::::::::::::::::::::::::,,================~=,,.................
............................,++.............,,~~~~,,,:::::::::::::::::::::::::::::,,~~==~============,,.................
.............................,+,.............,,:,,,::::::::::::::::::::::::::::::::,,:==========~====,,.................
................+++:..........................,,,,,:::::::::::::::::::::::::::::::::,,,=============~,,.................
..................++++,............,,,...........,,,,,,,,:::,,,,,,,,,,,:::::::::::::::,,===========~,,..................
.....................++:........,,,:+,,,,,,,,,,,,,,,:++=,,,,,+++++++++,:,,:::::::::::::,,,==========,,..................
..............................,,,~++:,,,,++++++++++~,,=:,,+++++++++++++++,,:::::::::::::,,,========,,...................
.............................,,~+++=,,=,,+++++++++=,,,,,,,+++++++++++++++,,:::::::::::::::,,======~,,...................
..........................,,,,++++,,,=,,,,,,,,,,,,,,,,:,,,,:,:++++++=:,,,,,,,,,,,::::::::::,,~====,,....................
......................,,,,,,=++++,,,=,,,===========:,,:,,+=:,,,,,,,,,,,:=:,...,,,,,,,,,:::::,,:==,,.....................
...................,,,,::,:++++:,,==:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,++=,,,,,,,,,,,,,......................
...................,,:,,,,,:+=,,,=:,,++++++===+++:,,,,++++,,,~,,:===~,,,,+++++++=,,,,,......,,,,,.......................
...................,,=====,,,,,,~,,,:,,,,,,,,,,,,,,+~,,+~,,~+==:,,~~,,=~,,++++++++:,,,,,,,..............................
...................,,==========,,,,,,~===~:,,,:~,,,,,,,,,,,,,,,,,,,,,,,,,,,++++++,,,:::::,,,,,,,........................
...................,,~=============,,,,,,,:::::,,,,::::,,:::::::::,,::::,,,,,,,,,,:,::::::,,,,,,........................
....................,:=============,,+++:,,,,,,,,:,,===:,:=======,,~=~:,,,,,:~+===,,,,,,,,,~~~,,........................
....................,,=============,,=+++++++~,,,,,,,:==,,======,,:~=,,:=======,,,,,,,:~~~~~~~,,........................
....................,,=============,,++++++++=,,==,,,,,,:,,=====,,~~,,,,,,,,,,,77I:~~~~~~~~~~~,,........................
....................,,=============~,+++:,+++=,,=======,,,,,,~=,,~:,777:,,,,,:~II+~~~~~~~~~~~~,,........................
....................,,==============,~++:,~++=,,============,,,,,,,,~II,,:~~~~~I7I~~~~~~~~~~~~,,........................
....................,,==============,:++~,:++=,,================:,,,,77I~~~~~~~777~~~~~~~~~~~~,,........................
....................,,==============,,+++:+++=,,==================,,~77I~~~~~~~+I~~~~~~~~~~~~~,,........................
.....................,~=============,,+++++++=,,==================,,~~I7?~~~~~~I7I~~~~~~~~~~~:,,........................
.....................,,=============,,,,:++++=,,==================,,~~77I~~~~~~~~~~~~~~~~~~~~:,,........................
.....................,,~===============,,,,,:+,,==================,,~~II?~~~~~~III~~~~~~~~~~~:,,........................
......................,,~=================~,,,,,==================,,~~I77~~~~~~II+~~~~~~~~~~~:,.........................
........................,,,~======================================,,~~~II~~~~~+77?~~~~~~~~~~~:,.........................
..........................,,,,,===================================,,~~?I7I~~~~~77~~~~~~~~~~~~,,.........................
..............................,,,,:===============================,,~~~~?=~~~~7I+~~~~~~~~~~~:,,.........................
.................................,,,,:============================,,~~~III?77~I77~~~~~~~~~~,,,..........................
..................,,,,,,,,,,,,,,,...,,,,,~========================,,~~~~?+=7II~~~~~~~~~~~,,,............................
................,,++++++++++++++,,......,,,,,=====================,,~~~~~~~~~~~~~~~~~:,,,,..............................
................,,,,,~++++++~,,,,,..........,,,,~=================,,~~~~~~~~~~~~~~:,,,,.................................
................,,=,,,,,,,,,,,:=,,.............,,,,:==============,,~~~~~~~~~~~:,,,,....................................
................,,,,,::~~~~::,,,,,.................,,,,~==========,,~~~~~~~~:,,,,.....,,,,,,,,,,,,,.....................
....................,,,,,,,,,,........................,,,,,=======,:~~~~~:,,,,.....,,,~+++++++++++,,,...................
..........................................................,,,,:===,:~~,,,,.........,,,,++++++++++~,,,,..................
.............................................................,,,,,,,,,,............,,:,,,,,,,,,,,,,:,,..................
....................................................................................,,,==========:,,,...................
......................................................................................,,,,,,,,,,,,,.....................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
........................................................................................................................
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('''After a long journey, you come to a fork in the road.
The path to the left is overgrown with foliage and appears to have been untraveled in quite some time,
while the path to the right is paved with well-worn cobblestone.
''')
left_or_right = input("Do you choose to go left or right? \n").lower()
if left_or_right == "left":
	print('''
	You stumble and hack your way along the path until you reach a wide, lazy river.
	There is a dock nearby with a sign that reads, "FERRY, 5 SILVER"
	''')
	swim_or_wait = input("Do you decide to wait for the next boat, or try to swim across? \n").lower()
	if swim_or_wait == "wait":
		print('''
		You take off your pack and sit down beside it on the dock, hoping you won't have to wait too long.
		Soon, you spot an impossibly old man rowing toward you from the opposite side of the river.
		"Five silver!" he barks as his boat reaches the dock with a small bump.
		You quickly withdraw the silver pieces from the purse at your belt, drop them into his outstretched hand,
		and clumsily clamber into the boat along with your belongings before he changes his mind.
		''')
		print('''
		Once you are safely across, you spy a small cottage with three doors:
		one red, one blue, and one yellow.
		''')
		door_choice = input("Which door do you choose?  \n").lower()
		if door_choice == "red":
			print('''
			The moment your hand touches the knob, a blast of magical flame incinerates you on the spot.
			Game over!
			''')
		elif door_choice == "blue":
			print('''
			The moment your hand touches the knob, a blast of frigid magical wind encases you in a solid block of ice.
			Game over!
			''')
		else:
			print('''
			You grip the knob and slowly open the door. Peering into the darkness, a glimmer of light catches your eye,
			and you catiously step inside. Magical torches along the walls ignite at your presence, fully illuminating the room
			and revealing the vast piles of treasure that have been awaiting you all this time.
			You win!
			''')
	else:
		print('''
		You abandon any uncessessary items on the shore and attempt to swim across the river.
		As you get about halfway across, you feel something suddenly wrap tightly around your right leg.
		You panic and struggle against it for a moment, but the appendage quickly overpowers your feeble efforts and drags you under.
		You are never seen again. Game over!
		''')
else:
	print('''
	As you turn to the right, your foot slips on a loose stone and you faceplant into the ground, knocking yourself out cold."
	While you are unconcious, a hungry troll wanders by and spots your lifeless body sprawled across the stony path.
	"What luck!" he cries whilst rubbing his grubby hands together gleefully, and quickly drags you back to his cave to begin
	preparing his dinner. Game over!
	''')
