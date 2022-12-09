[[ Installation Directions ]]
In the Terminal enter:

-   pip install -U -r requirements.txt

This will install all the required programs needed to start the pipBoy. Then enter:

-   python ui_redo.py

This will start the pip-boy screen, giving you the ability to interact with our different features.



[[ Program Description ]]

[Radio Program]
The Radio Program, creates a tab that displays the different channels, as well as their
descriptions and a Pseudo radio-frequency line for aesthetics.

How does it work?
[Playing Music]
The Radio Works by creating channels that are linked to specific folders containing the
mp3 files. These files are then loaded to a list and are then shuffled inorder to simulate
how a radio would play its songs. This is done through the load_music function.

By pressing the button to start the radio, the play_music function will be called to started
mixer function imported from pygame. The play_music function takes plays the songs based on the
order of them in the shuffled song list.

The user has the ability to open up other tabs, while the radio continues to play. They can
also switch between radio channels.

Once the user presses the Turn-Off button, it with end the mixer thus putting an end to the Radio.

[Radio Frequency]
Inorder to simulate radio frequency lines, we turned to using cosine. By using the draw function
in pygame, the squiggle function calculates the position of each point on the cosing graph based on
what is calculated using the amplitude, frequency, overallY. In order to create different frequency lines,
a number is inserted into the function that will modify the x variable - which increases or decreases the number
of peaks in the line.

The final_dance_ultra function is then used to call multiple iterations of the squiggle function, simulating that
moving animation.

[Display Radio Description]
The Program reads from a txt file that matches with the Radio Channel selected by the user.


[Inventory Program]
The Inventory Program, creates a tab that displays a Inventory meant to simulate one that belongs in a video game.

How does it work?
[Inventory Interactions]
The Inventory is filled with items that the user is able to interact with. Based on the users current level, the number
of items available in their inventory will change. At a higher level, the number of items available will continue to
increase.

Since their no real way to do item collection, to simulate this we made it so that the items would refresh in the
Inventory every 30 minutes. The type of items available is different each time, however the user is guaranteed to have
at least one of each type.

[Types]
The items can fall into three categories that will affect the stats of the Virtual Pet. These categories are Fun,
Hygiene and Food. Each item has the ability to either add or remove stats from the Virtual Pet. The number of points the
items as contribute is randomly decided on based on the users level. At a hgigher level the range will shift
upwards, guaranteeing higher numbers.



[Data Program]
The Data Program creates a tab that displays data from a set of given files.

How does it work?

[Data Collection]
While the Collection and General data doesn't change, the data within the Health and Level category is directly linked
to the users actual health (on the Pip-Boy) and their current level. In order to do this, the program reads the
information the Level Program has stored in a file, as well as the information the Health Program has stored. This is
then formatted to the tab inorder to be displayed.


[Virtual Pet Program]
The Virtual Pet Program displays a small character that the user has to take care of.

How does it Work?

[Increasing Stats]
The virtual pet gives you a character to take care of with three stats (hunger, fun, and radiation). To take care of
these stats the user must use items (Which they can find under the Inventory tab) to randomly increase the current
stats (depending on which type of item the user chooses). The higher the user’s level, the more the stats can increase
by.

By walking the user can level up, which will randomly increase the max stats the virtual pet can reach. The cap
doesn’t always increase, and each stat has a certain random chance to increase with each level up.

[Decreasing Stats]

Over time the virtual pet’s stats will decrease, the amount it decreases by lowering the higher the user’s level is.
The virtual pet’s mood changes with the stats, and is determined by taking the total of the current stats and dividing
it by the maximum stats it can have.


[Health Program]

The Health Program simulates how much health the user has as the day goes on.

How does it work?

[Health System]
In video games, health is decreased as the player takes damage. Since figuring out how to monitor a user's
health based on their bodily damage would be difficult. So, we decided to base their health on the idea of exhaustion.
So as the day goes on, the user's health will decrease, and then refresh at 8AM, as though they had gone to bed.


[Level Program]

The Level Program creates a leveling bar that shows the user's current level based on how long they’ve walked.

How does it work?

[Leveling System]
When the user presses the Walk button on the Stat tab they will begin to gain experience (aka exp). When they gain
enough exp they will level up, increasing the max stats their Virtual Pet can have and the amount of exp needed for
the next level up.

[Display]
The level bar is created by taking the width of the rectangular bar, and dividing it up based on the necessary exp
needed for the user to reach the next level.

The amount of the bar that is filled is then based on how far the user has progressed.
