# FAQ

## Why are you doing this? 
Because, as this lovely [video from the channel Machine Thinking](https://www.youtube.com/watch?v=djB9oK6pkbA) eloquently expresses, the cost and accessability of the machine that makes the machine is paramount to expanding creative possibilities for everyone and can induce an explosion of other previously unrealizable possibilities. 
If the means of production can be brought freely (or very cheaply) to all, then a world of real abundance greater than the one we presently find ourselves in could be realized and the cost of creating anything and everything can approach zero.  A world of abundance where anyone and everyone can have what they want and what they need. 
Better, stronger, faster, cheaper, and from earth, to the stars. 

## Why should I care about metal printing when I can just SLS/SLM a part? 
SLS and SLM are incredible processes for precision components in a limited number of alloys. But, the underlying cost of optics, lasers, gas, and the relatively finely processed powder feedstocks and supporting facilities and equipment to safely handle and recycle / dispose of them drive high capital costs and operational costs for SLS and SLM parts. [Typical costs of SLS aluminum parts can easily exceed $100/Kg](https://pmc.ncbi.nlm.nih.gov/articles/PMC11173345/). The resulting microstructure of the SLS/SLM parts tends to be as cast, limiting mechanical and thermal performance. With Rotoforge, you can print parts with tuneable microstructure comparable to forged parts, from bulk wire ($3/Kg) or powder as you desire,with no gas, no lasers, no metal fumes, with minimal limitations on multimaterial combinations and with an potentially unlimited accessible build volume for a total cost of <$700. 100X cheaper than some of the [lowest cost SLS/SLM machines.](https://3dprintingindustry.com/news/xact-metal-launches-affordable-new-sub-90k-metal-3d-printers-technical-specifications-and-pricing-199638/) 

## Do you melt the wire? 
No. We do not melt the wire. We use heat from friction, and plastic deformation to decrease the [flow stress](https://en.wikipedia.org/wiki/Flow_stress) of the metal to the point it can be stirred and spread like peanut butter or clay mortar and thus readily mixed with the underlying layer to bond and build up thickness. We also take advantage of shear thinning, ([thixotropy](https://en.wikipedia.org/wiki/Thixotropy)) at high shear rates to keep the viscosity change sharp, and minimize the total temperature rise required to achieve a given spread/mix at the deposition region/wheel contact patch.  The typical deposition temperature 5054 aluminum is ~450 C at the contact patch generated entirely locally by friction and deformation heating of the metal by contact with the wheel. While it is not neccessary for aluminum, as in [low force friction welding](https://www.mtiwelding.com/blog/low-force-friction-welding-what-is-it/) we can preheat the wire as high as 600 C, through a hot block to reduce deposition forces, increase print speeds, and enable printing of copper alloys, and soon, steels. 
Because we never melt the material, the oxygen solubility and diffusion rate in the metal remains near room temperature, solid state values and thus, oxidation in air is greatly inhibited and does not pose a problem for printing many materials, even aluminum. Also, because we do not require bed heating, or chamber heating, and the wheel can grind and mix through surface contaminants, printing outdoors, and in relatively adverse conditions is possible, allowing for potentially very large prints. 

## Why use an ender?
Its cheap, available, and has plenty of low cost open source community mods. Everyone has one, and probably has little use for it these days. Rotoforge does not have to go on an ender, but the ender is a representative printer frame to demonstrate that this friction welding process can be done with forces, temperatures and speeds, tolerable by a minimally modified ender 3 and thus, likely any other well built 3D printer or low force precision motion system. 

## Why not use high torque at lower spindle speed? 
For a simple machine like the wheel, the power dissipated at the contact patch "P" goes as, [P = Fv](https://en.wikipedia.org/wiki/Wheel_and_axle) F being force of friction, and v the rolling velocity of the wheel. Machinists will know that, higher [spindle speeds](https://en.wikipedia.org/wiki/Speeds_and_feeds#Spindle_speed) typically correspond to lower cutting forces all else being equal. This is typically attributed to thermal softening of the worked material by the dissipated power of the cutter sliding against/through it. The phenomenon is [well documented in many systems of many sizes](https://pmc.ncbi.nlm.nih.gov/articles/PMC10456406/). Motion systems that achieve precision over a relatively large working volume, at low cost, typically must be built for relatively low forces. Thus to keep costs as low as possible and allow for easy expansion of the system to arbitraily large working volumes, it is neccessary to work at the highest available spindle speed to keep [deposition forces](https://discord.com/channels/1028060441273958510/1342730788608671796/1432168894612770837) minimal. 

## Is it loud / can it be made quieter? 
Yes it is about as loud as a desktop milling machine or table saw but, a low cost acoustic foam lined enclosure (~$50-$100) can greatly muffle the machine, and in future, use of a brushless FOC controlled close loop spindle drive may greatly reduce the [table saw like noise centered on 500 Hz](https://discord.com/channels/1028060441273958510/1342730788608671796/1429659095337668728) the printer makes. 

## Can you only print aluminum? 
No, though we are currently focused on printing aluminum and all its alloys, because they are the most readily printable and offer an excellent combination of strength, weight, stiffness, corrossion resistance and cost. They are like our metal printer's version of PLA. We are currently working on copper alloys, steels, and titanium and nickel alloys as well. Parameters will be released in future videos and documented online for anyone to use. 

## Can you only go in straight lines? 
No, we can currently print at up to +-30 degree angles to the X axis. This is limiting, but we are currently working on a 4th axis which will allow 360 degree circles and smooth curves of greater angles without the deposition efficiency losses and printing process stability challenges of printing at steep  drift angles. 

## Do you want fries with that? 
no. I prefer [wafflehouse](https://www.wafflehouse.com/) hashbrowns, but they are delicious. 

## Can I buy one? 
Yes! you can buy the parts from [the BOM](https://github.com/Sindry-Manufacturing/rotoforge/tree/main/docs/billsofmaterials) and build it yourself.
The community is willing to help you build one for your specs, providing advice, helpful links and resources, and parts. This is worthwhile as long as all of us can learn and explore together. 
If you really just want someone to build it for you, and make it work, you can find us on [discord](https://discord.gg/tprMSEd4wA), or send an email to sindrymanufacturing@gmail.com
We can do this case by case. But we are still very much in "alpha" at the moment. In future we hope to provide a fully supported, and extremely smooth and easy user experience to make it possible for anyone to get great metal prints at home on their desktop(or in your yard/garage for you big printer types). 

## Can this be used to print X? 
Anything printable with 1 to 2mm line width resolution, and that can be made of materials that can be bonded/worked/printed by friction welding are viable applications. 

## "Have you tried induction heating or approach X"
Take a look at our [list of methods we're considering](a-list-of-methods.md)
