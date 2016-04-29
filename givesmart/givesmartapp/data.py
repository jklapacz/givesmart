from classes import *

charities = list()
categories = {'HEALTHCARE':list(),
	'GLOBAL POVERTY':list(),
	'ANIMALS':list(),
	'LOCAL':list(),}

AMF = Charity(name="Against Malaria Foundation", summary="\
	The Against Malaria Foundation protects people from malaria\
	 by distributing mosquito nets. Insecticide-Treated Bednets\
	  are one of the most effective ways to prevent transmission\
	   of malaria and have averted about 450 million cases since 2000.\
	    The Against Malaria Foundation can distribute bednets for between $5-7.50.",
	key_statistics="100% of public donations go directly to net purchases Malaria \
	killed 367-755 thousand people in 2013, most of them children, and there are about 200 million cases every year", 
	categories = ['HEALTHCARE', 'GLOBAL POVERTY', 'ANIMALS'],
	image_url="givesmartapp/AMF_Logo.jpg",
	initials = "AMF",
	stats={
		'admin': 5,
		'impact': .95,
	},
	ratings=[4.1, 4.2, 4.0, 2.5, 3.0, 4.8, 4.9, 5.0, 4.3])

categories['HEALTHCARE'].append(AMF)
categories['GLOBAL POVERTY'].append(AMF)
categories['ANIMALS'].append(AMF)

SCI = Charity(name="Schistomiasis Control Initiative", 
	summary="Schistosomiasis Control Initiative provides technical assistance and funds for programmes that treat people for parasitic worms. The WHO estimates that at least 261 million people required preventive treatment for schistosomiasis in 2013, but only 40 million were treated. The disease is widespread, but extremely cheap and easy to treat.", 
	key_statistics = "The recent Givewell report on SCI estimates that SCI has room for $3.8-8.3 million of additional funding over the next few years. SCI can distribute deworming tablets for around $2 / person / year.", 
	categories = ['HEALTHCARE', 'GLOBAL POVERTY'],
	image_url="givesmartapp/SCI_Logo.jpg",
	initials = "SCI",
	stats={
		'admin': 12,
		'impact': .8,
	})

categories['HEALTHCARE'].append(SCI)
categories['GLOBAL POVERTY'].append(SCI)

PHC = Charity(name="Project Healthy Children",
	summary="Project Healthy Children works with governments in developing countries to fortify staple foods such as flour, sugar, rice and oil with vitamins and minerals. The body needs micronutrients like vitamins, iodine, and iron to function. Micronutrient deficiencies can lead to various health problems and may lead to serious cognitive impairment.",
	key_statistics="Millions of people are at risk of micronutrient deficiency worldwide By providing technical assistance to Governments in fortifying staple foods, Project Healthy Children helps to avert malnutrition and micronutrient deficiency for around 5 cents / person / year",
	categories=['HEALTHCARE', 'GLOBAL POVERTY'],
	image_url="givesmartapp/PHC_Logo.jpg",
	initials="PHC",
	stats={
		'admin': 19,
		'impact': 70,
	})

categories['HEALTHCARE'].append(PHC)
categories['GLOBAL POVERTY'].append(PHC)

charities.append(AMF)
charities.append(SCI)
charities.append(PHC)
