from classes import *

charities = list()

AMF = Charity(name="Against Malaria Foundation", summary="\
	The Against Malaria Foundation protects people from malaria\
	 by distributing mosquito nets. Insecticide-Treated Bednets\
	  are one of the most effective ways to prevent transmission\
	   of malaria and have averted about 450 million cases since 2000.\
	    The Against Malaria Foundation can distribute bednets for between $5-7.50.",
	key_statistics="100% of public donations go directly to net purchases Malaria \
	killed 367-755 thousand people in 2013, most of them children, and there are about 200 million cases every year", 
	categories = ['HEALTHCARE', 'GLOBAL POVERTY', 'ANIMALS'])

SCI = Charity(name="Schistomiasis Control Initiative", \
	summary="Schistosomiasis Control Initiative provides technical assistance and funds for programmes that treat people for parasitic worms. The WHO estimates that at least 261 million people required preventive treatment for schistosomiasis in 2013, but only 40 million were treated. The disease is widespread, but extremely cheap and easy to treat.", \
	key_statistics = "The recent Givewell report on SCI estimates that SCI has room for $3.8-8.3 million of additional funding over the next few years. SCI can distribute deworming tablets for around $2 / person / year.", 
categories = ['HEALTHCARE', 'GLOBAL POVERTY'])

charities.append(AMF)
charities.append(SCI)