# senior_project

Development of a Methodology to Exploit Predictable Behavior in the World of Warcraft Virtual Auction House

Abstract
Virtual markets are everywhere. In massively-multiplayer online (MMO) video games, it takes the shape of an “Auction House,” an eBay-like auction board, where players can exchange items and materials with other players, in exchange for in-game currency. Studies have shown that These virtual markets mimic real market behavior so closely, that they can be studied for real world application [1]. MMO players are some of the most engaged video game players out there. Studies have shown that highly engaged video game players exhibit predictable, and ultimately risky behavior [2]–[5]. Predictability in markets is bad, because it creates an opportunity to exploit the market, and damage it as a result. As a long-time player of the MMO “World of Warcraft,” I have observed a troubling behavior within the Warcraft auction house, namely, that auction house prices are more elastic on the weekend. I Intend to investigate.

1. Background/Significance
World of Warcraft (WoW) is the world’s most popular massively multiplayer online role-playing game. [6] In this game, you go on quests, defeat monsters, and craft items alongside millions of other players in real time. Completing these activities rewards the player with an in-game currency referred to as gold. Players can use this gold to purchase items from characters and vendors that the designers placed in the game, or you can use it to purchase items and materials from other players.
Websites exist that sell in-game currency for real money [7]. Groups of people determine the most efficient way to produce gold, and replicate that process on multiple accounts, to then trade the gold to a discerning player once a Paypal transaction has been completed. 
Blizzard also offers a conversion system to trade in-game currency for game time (which is valued at .50dollars/day [7].) This was Blizzard’s answer to the illegitimate gold trade. When this was announced, price of gold-per-dollar plummeted [8]. It took another nose dive when it was announced that gold could be used to purchase account balance for other Blizzard games.
Studies like this are critical. If the behavior that is manifesting itself in this virtual market is causational, then it stands to reason that a system can be created to take advantage of it. If the illegal gold traders were to develop such a system, they could corner entire markets and cause massive inflation. This would have real business consequences for Blizzard Entertainment. What’s more, the hedonistic pricing behavior of such a system could then give clues into real insider trading behavior, or other behavior involving illegal information.

2. Methodology
I the coming weeks, I will develop a program in python that analyzes the raw auction house data served by the World of Warcraft API. This will be completed in time for me to begin collecting data on March 14th. From then, every Wednesday, from 12pm-12am I will run this program, and capture all sold auctions for the item “Leystone Ore,” a commodity that moves quickly on the auction house. I will Capture the same data from the Saturday following, and repeat this process for 3 weeks. Once all the data has been collected, I will determine the percent average and standard deviation for the difference between each Wednesday, and its subsequent Saturday. I will apply this data to the auction house that resides on the High-Population US Server “Blackrock.” Beginning the Wednesday after the data has been collected, I will purchase 3000 gold worth of “Leystone Ore,” and record the average price. The following Saturday, I will sell 1/3rd of the ore based on the percent difference applied to the Average price on Wednesday, with the other 2/3rds being sold at a relative -2% and +2%, respectively. I will record metrics for percent sold for each price, each week. I will also track the percent of the “Leystone Ore” market that I own, as the experiment progresses. This procedure should wrap up in time to analyze my findings, and produce a research paper in late April, with a presentation to follow in May.

3. Statement of Qualification
My associates degree in Computer Science, and my coursework for my Bachelors will allow me to use the tools required to collect data on this scale. Courses I’ve taken in marketing and statistics will play a key role in the analysis of the information that the program I create will produce. I have played World of Warcraft for 9 years, which has granted me insight into the game’s myriad of mechanics, and an understanding enough to create a methodology that will work within the rules of the game.

4. Expected Outcomes
The expected outcome of this experiment is a little hard to pin down, since the question is not “does this trend exist?” but rather “can it be exploited?” The significant metric here will be the percent of the “Leystone Ore” market that I control at the end of the experiment. I predict 70% control of the market following this methodology. What’s more, I believe this experiment will produce a trend that will allow me to predict how long it would take to corner an entire market with this method.
I intend to record my findings in a report in late April. I intend to present my findings at Eastern Connecticut State University in early May.

Bibliography
[1]	E. Marks, “Price Dynamics in Virtual World Auctions.”
[2]	M. Pawlikowski and M. Brand, “Excessive Internet gaming and decision making: Do excessive World of Warcraft players have problems in decision making under risky conditions?,” Psychiatry Res., vol. 188, no. 3, pp. 428–433, Aug. 2011.
[3]	Y. Guo and S. J. Barnes, “Explaining Purchasing Behavior within World of Warcraft,” J. Comput. Inf. Syst., vol. 52, no. 3, pp. 18–30, Mar. 2012.
[4]	Y. Guo and S. Barnes, “Virtual item purchase behavior in virtual worlds: an exploratory investigation,” Electron. Commer. Res., vol. 9, no. 1–2, pp. 77–96, Jun. 2009.
[5]	C. S. Peters and L. A. Malesky, “Problematic Usage Among Highly-Engaged Players of Massively Multiplayer Online Role Playing Games,” Cyberpsychol. Behav., vol. 11, no. 4, pp. 481–484, Aug. 2008.
[6]	P. Svoboda, W. Karner, and M. Rupp, “Traffic Analysis and Modeling for World of Warcraft,” in 2007 IEEE International Conference on Communications, 2007, pp. 1612–1617.
[7]	“WoW Gold Price research: A World of Warcraft Gold study.” [Online]. Available: http://www.gamerprice.com/wow-gold-study.html. [Accessed: 26-Feb-2018].
[8]	D. Friedman, “World of Warcraft’s gold rush has upended Blizzard’s economy,” Polygon, 20-Feb-2017. [Online]. Available: https://www.polygon.com/2017/2/20/14667728/world-of-warcraft-tokens-blizzard-hearthstone-overwatch. [Accessed: 26-Feb-2018].


A program that pulls and parses information from the World of Warcraft Auction House and Item Repository APIs.
