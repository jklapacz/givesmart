from classes import *

charities = list()
categories = {'HEALTHCARE':list(),
	'GLOBAL POVERTY':list(),
	'ANIMALS':list(),}

AMF = Charity(name="Against Malaria Foundation", summary="\
	The Against Malaria Foundation protects people from malaria\
	 by distributing mosquito nets. Insecticide-Treated Bednets\
	  are one of the most effective ways to prevent transmission\
	   of malaria and have averted about 450 million cases since 2000.\
	    The Against Malaria Foundation can distribute bednets for between $5-7.50.",
	key_statistics="100% of public donations go directly to net purchases Malaria \
	killed 367-755 thousand people in 2013, most of them children, and there are about 200 million cases every year", 
	categories = ['HEALTHCARE', 'GLOBAL POVERTY'],
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

DWI = Charity(name="Deworm the Worm Initiative",
	summary="Deworm the World Initiative provides technical assistance and funds for programmes that treat people for parasitic worms. Intestinal worms like hookworm, roundworm, and whipworm are Neglected Tropical Diseases, which don't currently get the attention they deserve",
	key_statistics="875 million children require annual treatment. Deworm The World can help deworm children for around 50 cents / person / year",
	categories=['HEALTHCARE', 'GLOBAL POVERTY'],
	image_url="givesmartapp/Deworm-The-World-Initiative-Logo.png",
	initials="DWI",
	stats={
		'admin': 7,
		'impact': 85,
	})

categories['HEALTHCARE'].append(DWI)
categories['GLOBAL POVERTY'].append(DWI)

FAU = Charity(name="Faunalytics",
	summary="Faunalytics works to connect animal advocates with information. This mostly involves creating independent research, working directly with client organizations on various research projects, and providing resources for individual advocates through the content library they host on their website.",
	key_statistics="An estimated 2.8 animals are spared per dollar spent on Faunalytics' independent studies and 1.3 animals are spared per dollar spent on their pro bono consulting",
	categories=['ANIMALS'],
	image_url="givesmartapp/faunalytics-centered-logo.png",
	initials="FAU",
	stats={
		'admin': 30,
		'impact': 54,
	})
categories['ANIMALS'].append(FAU)

AEI = Charity(name="Animal Equality International",
	summary="Animal Equality advocates for animals by conducting undercover investigations and promoting them through media outlets. They also conduct grassroots outreach, including demonstrations, protests, leafleting, and video showings. Related to their undercover investigations, they also conduct some legal and corporate outreach efforts.",
	key_statistics="According to Animal Charity Evaluators, there is a $300K Funding Gap in 2016. A $1 Donation is estimated to spare 13.2 animals life in industrial agriculture",
	categories=['ANIMALS'],
	image_url="givesmartapp/aei_logo.png",
	initials="FAU",
	stats={
		'admin': 10,
		'impact': 74,
	})
categories['ANIMALS'].append(AEI)

MFA = Charity(name="Mercy For Animals",
	summary="Mercy For Animals (MFA) advocates for farmed animals by conducting undercover investigations, engaging in corporate and legal outreach, running online vegetarian ads, and organizing grassroots outreach events.",
	key_statistics="MFA has an estimated $300K funding gap in 2016. A $1 donation is estimated to spare 14 animals from lives in factory farms.",
	categories=['ANIMALS'],
	image_url="givesmartapp/mfa_logo.png",
	initials="MFA",
	stats={
		'admin': 9,
		'impact': 77,
	})
categories['ANIMALS'].append(MFA)

THL = Charity(name="The Humane League",
	summary="The Humane League (THL) works to reduce suffering of farmed animals through conducting online advertising, organizing grassroots outreach, instigating cage-free and Meatless Monday campaigns, giving presentations, and engaging in corporate outreach",
	key_statistics="The Humane League has an estimated $190K funding gap for the year 2016. A $1 donation is estimated to spare 13.4 animals from factory farms.",
	categories=['ANIMALS'],
	image_url="givesmartapp/thl_logo.png",
	initials="THL",
	stats={
		'admin': 10,
		'impact': 75,
	})
categories['ANIMALS'].append(THL)


charities.append(AMF)
charities.append(SCI)
charities.append(PHC)
charities.append(DWI)
charities.append(FAU)
charities.append(AEI)
charities.append(MFA)
charities.append(THL)
