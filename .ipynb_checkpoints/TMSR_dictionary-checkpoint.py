# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:27:36 2024

@author: Anna Knorr
"""

import re

#Manifestations of Radicalism

radicalism = ["\\bradical", "\\bextremi", "^violen.+(act|protest|political|movement)", "\\bextrem.+(pro.group.|political.)?(act|behaviou?r|ideolog|attitude)", "terror", "militan", "militia", "\\b(school|suicide).attack|bomb","\\b(illegal|extreme).+political.act", "\\bself.sacrific", "\\binsurgency\\b", "\\b(ideological|protest|political|religio).+(violen|aggress)", "\\bwill.+to.(fight|die)", "\\bpolitically.motivated.crim", "\\b(inter.)?group.violen", "\\bderadicali[zs]ation\\b", "^disengagement$", "^rve$"]

far_right = ["(far.|extreme.|alt.)?right(ist|wing)?\\b(?!.*brain)", "nazi", "\\bvox\\b", "\\bafd\\b", "\\bpegida\\b", "\\bgolden.dawn\\b", "\\bnpd\\b", "identitarian.movement", "fascis"]

far_left = ["(far.|extreme.)?left(ist|wing)?\\b(?!.*(brain|behind))"]

islamist = ["\\bsharia.govern", "islamis", "islamic.state", "\\bis(is|il)?\\b", "muslim.brotherhood", "jihad", "salafi", "al.?qaeda", "^daesh$", "^dabiq$", "al.?shabaa?b", "^jemaa?h.islamiyah?$", "h[ie]zb[uo]llah?", "boko.haram"]

lone_actor = ["\\blone.+(?:act|wol|terror|offender)"]

environmentalism = ["\\benvironmental.+(cause|extremi|radical|crimin)", "climate.protest", "ecology", "environment", "\\beco(?!n).*(radical|terror)","ecologically motivated violence"]

foreign_fighter = ["\\bforeign.(fight|terrorist.fight)", "isis?.foreign.fight", "white.jihad"]

animal_rights = ["\\banimal.rights?.+(extremis|terroris|radical)?"]

misogyny = ["\\b(misogyny|misogynistic.+extremism)\\b", "\\bgender.+based.+violence\\b", "\\bdigital.+misogyny\\b", "\\banti.+wom[ae]n\\b", "\\bviolence.+against.+wom[]aen\\b", "\\bincels?\\b", "^involuntary.celibat", "^male.supremacy$", "^red.pill"]

femcel = ["femcel"]


#Individual Differences

sex = ["boy", "girl", "\\bmale\\b", "\\bfemale\\b", "\\bgender\\b", "^sex$", "\\bwom[ae]n\\b(?!.*(rights|anti))", "\\bm[ae]n\\b(?!.*(rights|anti))"]

age = ["\\bage\\b", "\\bage.differences\\b", "school.+age", "\\bage.+child", "\\bage.+\\d", "\\bage.+(of|related) ", "age.+(diff|depend)", "aged.+\\d", "early age", "gestational.+age"]

status = ["(subjective|perceived|social).+(social|sociometric|economic|socio.?economic)?.*(status|class)", "socio.?economic", "economic.+(stress|background|condition)", "\\bses\\b", "^income\\b"]

employment = ["employ", "^welfare(.recipients?)?"]

urban = ["\\burban", "\\brural"]

adolescence = ["\\badolescen", "\\byouth", "\\bemerging.adult", "\\bpubert", "\\bchild", "\\bstudent\\b", "\\bteen", "\\bjuvenil", "\\bminor\\b", "\\bstudent", "\\byoung.people\\b", "\\b(early|young).adult"]

self_control = ["\\bself.control\\b", "\\bimpulsiv", "\\bself.regulat", "\\beffortful control\\b", "\\bexecutive function"]

law_abidance = ["\\blaw.(abidance|legitimacy)", "legal.(consciousness|awareness)", "policy legitimacy"]

digital_literacy = ["(digital|critical)? (medium|social media)? literacy"]

cognition = ["\\bcognit", "\\bknowledge\\b", "\\b(select.+|attribut.+)bias", "\\bperception\\b", "meta(.?awareness|cogniti)", "\\bconscious", "\\bthought", "\\bthink", "^memory$"]

nostalgia = ["nostalgi"]

anomia = ["anomi[ea]", "value.change", "normless"]

personality = ["temperament$", "^personality$", "^personality.+(trait|invento|questionn|dimensi|type|factor|character|assess|develop)", "5.(factor|personali)", "big.5", "personal.(feature|disposition)"]

empathy = ["empath", "perspective.+taking", "sympathy", "empathic concern", "theory.(of.)?mind", "\\btom\\b"]

hate = ["\\bhate", "\\bhatred\\b"]

sacred_values = ["\\bsacred.value", "\\b(obsessive.)?passion\\b", "\\bdevoted.act", "\\bsacred violence\\b", "fanaticism"]

honor = ["\\bhonou?r"]

masculinity = ["\\bmasculin", "^manosphere$"]

martyrdom = ["\\bmartyr", "\\bhero"]

white_race = ["\\bwhite"]

trust = ["trust"]

intolerance = ["tolerance\\b"]

significance_quest = ["significance.(quest|loss)", "\\bself.esteem\\b", "\\bqfs\\b", "(need|search|quest|loss).+(status|belong|meaning|significance)\\b", "meaning.+(life|existen", "^meaning$", "\\bstatus.seek", "\\bbelonging\\b"]

uncertainty = ["\\buncertain", "identity (in)?security"]

conspiracy = ["\\bconspira"]

immigration = ["migration", "migrant", "\\brefugee", "^diaspora$"]

pessimism = ["\\bpessimis"]

deviance = ["\\bdevia", "(illegal|destructive|illicit).act", "\\bsocial.adaptation", "\\bantisocial"]

morality = ["moral", "\\bprisoner.+dilemma\\b", "\\bethic", "\\bevil\\b", "^mfq$"]

deprivation = ["\\bdepriv", "\\bclass.struggles?\\b", "\\boppress", "\\bsuppress", "\\brepress", "\\bstrain", "\\bresource.loss\\b", "(economic|political).+(exclusion|discrimination)", "\\bethnic.exclsuion\\b", "\\bexclusionary.politics\\b"]
           
racism = ["\\b(?!ost)racis"]

poverty = ["\\bpoverty\\b", "\\blow.income\\b", "economic.+(hardship|stress)"]

conformity = ["conformity\\b", "complian", "loyal"]

superiority = ["superior", "\\bsdo\\b", "dominan", "group favoritism", "^power$"]

islamophobia = ["\\bislamophob", "\\banti.(muslim|islam)"]

system_justification = ["\\bsystem.justification\\b", "^legitimacy$"]

social_skills = ["social.skill", "social.(competenc|functioni)"]

rationality = ["\\b(ir)?rational"]

autonomy = ["self.?(determination|efficacy)", "autonomy"]

risk_taking = ["^risk.+(tak|behaviou?)", "(sensation|thrill).+seek", "reckless"]

political_agency = ["(political|civilian|\\bsocial).\\bagency", "\\bpolitical.(apath|access|effica)"]

political_engagement = ["(political|civic).+(engagement|participation|involvement)", "interest.(in.?)politics", "political.party.support", "participation.(in.)?decision.making"]

altruism = ["pro.{0,2}social.{0,2}(behav|response)?", "\\baltruis"]

apocalypticism = ["apocalyp"]

prejudice = ["\\bprejudice\\b", "\\bstereotyp", "\\bhalo.effect", "\\bxenophob"]

cynicism = ["\\bcynic"]

skepticism = ["s(k|c)epti"]

activism = ["^activis", "(^political|^non.?violent|^youth|^social|^community|^civi\w*)\\b.*?\\b(resist|acti)", "active.citizen", "^collective.act", "^demontrations?$", "^protest(ers?)?$", "^resistance$"]

authoritarianism = ["\\bauthorit"]

religiosity = ["^(extrinsic|intrinsic)?.*religiosity$", "^religion$", "spiritual", "^religious$", "^islam$", "^sufism$", "^shia$", "^sunni$","^jews?$", "^judaism$", "^christ", "^hindu(ism)?$", "^muslims?$", "^buddh(a|ists?)$", "^(catholic)?.*church$", "^religious.(belief|orientation|conversion|movement|cause|difference|experience|scripture|attitude|moderation|idea)"]

mobilization = ["^(?:(?!violent|radical|extremist|terror(ist)?|jihadi).)*mobili[sz]ation\\b", "social movement"]

mortality_salience = ["mortality.salience", "death.anxiety", "fear(of.)?death", "^terror.management.theory$" ]

emotion = ["regulati.+difficult", "(emoti|affect|anger).+(regulation|proble|adjustm|compete)", "dysregulation", "emotional.problems?", "psychological distress", "mood", "irritability", "emotio", "affect\\b", "^sad(ness)?$", "happy", "happiness", "affect.+intensity", "affect.+instab", "mood.+variab", "sham", "self.?consciou", "frustration", "feeling", "affective investment"]

dogmatism = ["dogmat", "\\brigid", "\\battitude certainty\\b", "\\bcertain"]

fundamentalism = ["fundamentali"]

nationalism = ["nationali", "ethnocentri", "\\bnational.(attitude|pride)\\b", "\\bnativis"]

patriotism = ["patriot"]

populism = ["populi"]

conservatism = ["conservati"]

liberalism = ["liberal"]

aggression = ["aggressive.behaviou?r", "\\baggression\\b", "\\breactive aggression\\b", "\\baggressiveness\\b", "\\bantagonis", "\\bhostil"]

violence = ["\\bviolen(ce|t)?\\b"]

criminality = ["^criminal(ity)?$", "crime\\b", "(?<!non)delinq", "\\bgangs?(.involvement)?\\b","\\bcriminolog", "^prison$", "^perpetration$", "^convicts?$"]

fusion = ["\\bfusion\\b", "\\bfused\\b", "\\bunified\\b", "\\bunification\\b"]

ideology = ["\\bideolog", "political.(attitude|orientation|preference)", "^partisanship$", "^worldview$"]

education = ["educat", "\\bacademic", "pedagogy"]

identity = ["identi(ty|ties|fication)", "^identity distress$", "emerging.+self", "representation.+self", "^affiliation$", "self.+(concept|construal|development|knowledge|representation|perception)", "self.+awareness"]

#Mental

resilience = ["\\bresilien", "\\bdifferential.susceptibility\\b"]

self_harm = ["\\bmutilation\\b", "self.injur", "self.harm", "^nssi$"]

suicide = ["^suicid(e|ality)$"]

substance_use = ["binge drinking", "^addiction$", "drug.(ab)?use", "subst.+use", "alcohol", "cannabis", "^drug$", "marijuana", "tobacco", "smoking", "^misuse$", "\\bsubstance use disorder\\b", "\\buse disorder\\b"]

depression = ["depressi.*", "^mdd$", "mood.disorder", "affective.disorder"]

anxiety = ["anxiety", "^panic", "^behaviou?ral.inhibition$", "\\bphobia"]

fear = ["fear"]

iq = ["\\biq\\b", "^intelligence$"]

wellbeing = ["\\bquality.+life\\b", "well.?being", "life.sat"]

anger = ["\\banger\\b"]

adhd = ["hyperactiv", "\\bcallous.unemotional trait\\b", "hyperactivity disorder", "\\badhd\\b"]

narcissism = ["narcissis"]

ptsd = ["ptsd", "trauma", "^survivors?"]

stress = ["\\b(di)?stress(?!\\sdisorder)"]

mental_health = ["psych.+symptom", "comorbid.+(?!anxiety)", "\\bmental.(disorders?|illness)\\b", "\\bdisorder.*\\b", "\\bmental.health", "\\bsymptom", "\\bpsychop.*\\b", "\\bpsychiatric.disorder.*\\b", "\\Bbpd\\b", "borderline personality", "\\b(psychological|somatic) symptom", "mental.disorder", "\\bsomatoform", "^bipolar$", "psychiatry"]

schizophrenia = ["schizo", "psychosis"]

therapy = ["\\bin.?patient\\b", "therapy"]

autism = ["\\basd\\b", "\\basperger.syndrome\\b", "autis", "pervasive developmental disorder", "\\bhigh(ly)?.functioning\\b", "spectrum disorder"]

hope = ["\\bhope"]

dark_triad = ["\\bdark.triad\\b", "\\bdark.personality\\b", "\\bdark.tetrad\\b"]


#Physical

health = ["^health$", "^chronic illness$", "^pain$", "^illness$", "diabetes", "cancer", "disease", "physical.+(illness|disorder)", "epilep", "health.related"]

neural = ["^neural\\b.+$", "^neuroscience.*$", "\\bf?mri\\b", "diffusion.tensor.imag", "brain", "hippocamp", "cortex", "cortica", "cingulate", "amygdala", "gyrus", "thalam", "limbic", "(gr[ea]y|white).+matter", "synap", "neuroimag", "functional.magnetic", "functional.connectivit"]

neurotransmitter = ["endocannabin", "glutam", "neurotrans", "catecholamin", "adrenalin", "dopamin"]

genes = ["gene(\\b|t)", "gene.+envi"]

sports = ["physical.+(fitness|activity)", "sport"]


#Environment

climate_change = ["\\bclimate.(change|shock|crisis|disruption|shift|conflict|protest)", "global.warming"]

globalization = ["\\bglobaliz"]

justice = ["justice", "\\bjust.world\\b", "\\bfreedom\\b(?!\\s(fighter|party))", "free.speech", "equal", "fair"]

economy = ["econom", "\\bgdp\\b", "\\bgini\\b", "\\bincome.+caput\\b", "\\bcaput.income\\b", "(\\beuro\\b|\\bfinancial\\b).crisis\\b", ]

competition = ["\\bcompetiti", "\\brival"]

security = ["\\b(?!(emotional|belief|identity).+)((in|cyber)?security|safety|(in)?stability)\\b", "\\bsecuritization\\b", "stabilization"]

satisfaction = ["satisfaction\\b", "\\bgrievances?\\b", "\\bgrudge\\b", " \\bdiscontent\\b"]

meritocracy = ["\\bmeritocra(tic|cy)\\b"]

corruption = ["\\bcorrupt"]

school = ["^schools?$"]

teachers = ["\\bteacher"]

state = ["^states?$", "^country$", "govern(ment|ance)", "^welfare.states?$"]  

police = ["\\bpolice$"] 

propaganda = ["\\bpropaganda\\b"]

threat = ["\\bthreat", "\\bdanger\\b"]

democracy = ["democra(tic|cy|cies|tization)"]

politics = ["\\bpolitics\\b", "^(political.)?part(y|ies)$"]



def compile_and_test_patterns(patterns, test_strings):
    matched = []
    unmatched = test_strings[:]

    for pattern_str in patterns:
        pattern = re.compile(pattern_str, re.IGNORECASE)  # Compile the pattern
        matched_for_pattern = []

        for string in unmatched[:]:
            if pattern.search(string):
                matched.append(string)
                matched_for_pattern.append(string)
                unmatched.remove(string)
                
    return matched, unmatched

# Using the function to test terms
test_strings = ['political party', 'party', 'parties', 'right wing party', 'party support']
# Compile and test patterns
matched, unmatched = compile_and_test_patterns(politics, test_strings)

print("Matched strings:", matched)
print("Unmatched strings:", unmatched)


social_media = ["^youtube$", "^facebook$", "^reddit$", "^tiktok$", "^instagram$", "^twitter$", "^telegram$", "\\bsocial.medi(a|um)", "online.(discussion|discourse|social|network|conversation|comment|debate)"]

internet = ["(?<!social )media\\b","internet", "\\bmeme\\b", "video.gam", "technology.use", "digital.+(technology|medium)", "cyberspace", "\\bonline\\b(?!\\s+(discussion|discourse|social|network|conversation|comment|debate))"]

norms = ["\\bnorms?\\b", "\\bnarrative", "\\bvalue", "\\bpublic.opinion\\b", "\\bhuman.rights?\\b"]

polarization = ["polariz", "polar.opinion"]

capitalism = ["capitali"]

violence_exposure = ["\\bviolence.exposure\\b", "\\bexpos(ed|ure).to.violen"]

language = ["language", "lingu", "rhetoric"]

elites = ["elite"]

elections = ["\\belection", "\\bvot[e|er|ing]", "\\belectoral\\b"]

peace = ["peace"]

conflict = ["\\bconflicts?\\b", "wars?\\b", "\\bunrests?\\b", "\\bshock.events?\\b", "^arab.spring$"]

crisis = ["covid", "cris[ie]s$"]




#Social

intergroup_contact = ["\\binter.?group.(contact|process)", "\\binter.?ethnic.contact", "\\bcontact.(hypothesis|theory)"]   

community = ["\\bcommunity\\b", "\\bcommunal"]

diversity = ["\\bdiversity\\b", "\\bheterogeneity\\b", "\\bheterogenous.environment\\b", "\\bmultinational", "\\bpluralis", "\\bmulticultural"]

consensus = ["\\bconsens", "\\bcommon.(understanding|consent)", "\\bagreement\\b"]

social_coherence = ["(social|local|group|commun|inclusion|peer).+(coherence|cohesion)", "social.(bond|contact|tie|connection)"]

neighborhood = ["neighbo"]

group_process = ["\\bgroup.(process|act|mechanism|dynamic|think|consens|interact)", "\\bsocial.(mechanism|dynamic)", "\\bcollective\\b.(dynamic|group)", "^groups?$"]

peers = ["^peer(s|.influences|.interactions|.relationships|.relations|.situations|.stress|.acceptance|.pressure)$", "^peer$", "^friends?$"]

society = ["\\bsociety\\b"]

culture = ["cultur", "civilization", "\\bsoci.+context", "socialization"]

social_exclusion = ["\\bexclu", "\\bostraci", "\\bmarginaliz", "(personal|peer|social).+reject", "^rejection$", "isola", "lonel", "social.(withdrawal|disconnectedness|disintegration)", "\\balienation\\b", "friendless"]

segregation = ["segregat", "fragmentation", "separatism", "ethnic.division"]

integration = ["integration", "inclusion"]

social_support = ["(social|peer|kin|parent|teacher).+support", "^social.(network|capital)"]

victimization = ["victimi[sz]ation"]

dehumanization = ["dehumani[sz]ation", "^contempt$"]

discrimination = ["bull[yi]", "discriminat", "harass", "humiliat"]

family = ["\\bparents?\\b", "\\bfamil(y|ies)", "intergenerational transmission", "mothe", "materna", "fathe", "paterna", "\\bsiblings?\\b", "\\bparenting\\b", "\\bparental (involvement|control)\\b", "parent.+style", "parent.+behav", "family.function"]

abuse = ["^abuse$", "maltreat", "(phys|sex|child|human.right|psycho).+(abuse|exploitation)"]

minority = ["minorit"]

misinformation = ["(mis|dis)infor", "^fake.news$", ]

discourse = ["discourse", "^dialogue$"]

social_change = ["soci(al|etal|opolitical).(change|shift|evolution|reform|progress|development|transformation)", "^revolution$", "^opinion.dynamics?$"]


# ========================================================================================================
## Building the dictionary

word_dict = {
    "radicalism": radicalism,
    "far right": far_right,
    "far left": far_left,
    "islamist": islamist,
    "lone actor": lone_actor,
    "environmentalism": environmentalism,
    "foreign fighter": foreign_fighter,
    "animal rights": animal_rights,
    "misogyny": misogyny,
    "femcel": femcel,
    "sex": sex,
    "age": age,
    "status": status,
    "employment": employment,
    "urban": urban,
    "adolescence": adolescence,
    "self control": self_control,
    "law abidance": law_abidance,
    "digital literacy": digital_literacy,
    "nostalgia": nostalgia,
    "anomia": anomia,
    "personality": personality,
    "emotion": emotion,
    "empathy": empathy,
    "hate": hate,
    "masculinity": masculinity,
    "white race": white_race,
    "trust": trust,
    "intolerance": intolerance,
    "significance quest": significance_quest,
    "uncertainty": uncertainty,
    "honor": honor,
    "martyrdom": martyrdom,
    "conspiracy": conspiracy,
    "cognition": cognition,
    "immigration": immigration,
    "pessimism": pessimism,
    "deviance": deviance,
    "morality": morality,
    "deprivation": deprivation,
    "racism": racism,
    "poverty": poverty,
    "conformity": conformity,
    "dogmatism": dogmatism,
    "authoritarianism": authoritarianism,
    "fundamentalism": fundamentalism,
    "nationalism": nationalism,
    "patriotism": patriotism,
    "populism": populism,
    "conservatism": conservatism,
    "liberalism": liberalism,
    "superiority": superiority,
    "islamophobia": islamophobia,
    "system justification": system_justification,
    "social skills": social_skills,
    "aggression": aggression,
    "violence": violence,
    "criminality": criminality,
    "sacred values": sacred_values,
    "identity": identity,
    "fusion": fusion,
    "ideology": ideology,
    "rationality": rationality,
    "autonomy": autonomy,
    "risk taking": risk_taking,
    "education": education,
    "political agency": political_agency,
    "altruism": altruism,
    "apocalypticism": apocalypticism,
    "prejudice": prejudice,
    "cynicism": cynicism,
    "skepticism": skepticism,
    "activism": activism,
    "religiosity": religiosity,
    "mobilization": mobilization,
    "mortality salience": mortality_salience,
    "political engagement": political_engagement,
    "resilience": resilience,
    "self harm": self_harm,
    "suicide": suicide,
    "substance use": substance_use,
    "depression": depression,
    "anxiety": anxiety,
    "fear": fear,
    "iq": iq,
    "wellbeing": wellbeing,
    "anger": anger,
    "adhd": adhd,
    "narcissism": narcissism,
    "ptsd": ptsd,
    "stress": stress,
    "mental health": mental_health,
    "schizophrenia": schizophrenia,
    "therapy": therapy,
    "autism": autism,
    "hope": hope,
    "dark triad": dark_triad,
    "health": health,
    "neural": neural,
    "neurotransmitter": neurotransmitter,
    "genes": genes,
    "sports": sports,
    "conflict": conflict,
    "crisis": crisis,
    "climate change": climate_change,
    "globalization": globalization,
    "justice": justice,
    "economy": economy,
    "competition": competition,
    "security": security,
    "satisfaction": satisfaction,
    "meritocracy": meritocracy,
    "corruption": corruption,
    "school": school,
    "teachers": teachers,
    "state": state,
    "police": police,
    "propaganda": propaganda,
    "threat": threat,
    "democracy": democracy,
    "politics": politics,
    "internet": internet,
    "social media": social_media,
    "norms": norms,
    "elections": elections,
    "polarization": polarization,
    "capitalism": capitalism,
    "violence exposure": violence_exposure,
    "language": language,
    "elites": elites,
    "peace": peace,
    "intergroup contact": intergroup_contact,
    "community": community,
    "minority": minority,
    "diversity": diversity,
    "consensus": consensus,
    "social coherence": social_coherence,
    "neighborhood": neighborhood,
    "peers": peers,
    "group process": group_process,
    "society": society,
    "culture": culture,
    "social exclusion": social_exclusion,
    "segregation": segregation,
    "integration": integration,
    "social support": social_support,
    "victimization": victimization,
    "dehumanization": dehumanization,
    "discrimination": discrimination,
    "family": family,
    "abuse": abuse,
    "misinformation": misinformation,
    "discourse": discourse,
    "social change": social_change}



# ===========================================================================================


