# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:27:36 2024

@author: Anna Knorr
"""

#import re

#Manifestations of Radicalism

radicalism = ["\\bradical", "\\bextremi", "^violen.+(act|protest|political|movement)", "\\bextrem.+(pro.group.|political.)?(act|behaviou?r|ideolog|attitude)", "terror", "militan", "militia", "\\b(school|suicide).attack|bomb","\\b(illegal|extreme).+political.act", "\\bself.sacrific", "\\binsurgency\\b", "\\b(ideological|protest|political|religio).+(violen|aggress)", "\\bwill.+(fight|die)", "\\bpolitically.motivated.crim", "\\b(inter.)?group.violen", "\\bderadicali[zs]ation\\b", "^attack$", "^disengagement$", "^rve$"]

far_right = ["far.right(?!.part)|ultra.right|extreme.right|^radical.right$", "^right.wing.(extremi|radicali|terror)",
             "nazi", "^pegida$", "identitarian.movement", "^fascis", "^golden.dawn$", "^vox$"]

# far_left = ["left.*\\b(?!.*(brain|behind))", "meinhof", "^red.army$", "^black.panther"]

far_left = [
    "\\b(?<!\\bright wing )(?<!\\bright radical )left(ist)?\\b(?!.*(brain|behind))", 
    "\\bmeinhof\\b", 
    "^red.army$", 
    "^black.panther$"
]




#def compile_and_test_patterns(patterns, test_strings):
#    matched = []
#    unmatched = test_strings[:]
#    for pattern_str in patterns:
#        pattern = re.compile(pattern_str, re.IGNORECASE)  # Compile the pattern
#        matched_for_pattern = []
#        for string in unmatched[:]:
#            if pattern.search(string):
#                matched.append(string)
#                matched_for_pattern.append(string)
#                unmatched.remove(string)
#              
#    return matched, unmatched

## Using the function to test terms
#test_strings = ['left', 'left wing', 'leftist', 'radical left', 'left brain', 'radical left party', 'right wing left', 'wing left wing', 'left wing party', 'political left', 'radical left wing', 'right radical left', 'extreme left', 'left wing right', 'support radical left', 'right left wing', 'populist radical left', 'anddecreasesleftist', 'leftright', 'liberalleft'] 
#matched, unmatched = compile_and_test_patterns(far_left, test_strings)

#print("Matched strings:", matched)
#print("Unmatched strings:", unmatched)



islamist = ["\\bsharia.govern", "islamis", "islamic.state", "\\bis(is|il)?\\b", "muslim.brotherhood", "jihad", "salafi", "al.?qaeda", "^daesh$", "^dabiq$", "al.?shabaa?b", "^jemaa?h.islamiyah?$", "h[ie]zb[uo]llah?", "boko.haram"]

lone_actor = ["\\blone.+(?:act|wol|terror|offender)"]

environmentalism = ["\\benvironment.+(cause|extremi|radical|crimin|terror)", "climate.protest", "\\beco(?!n).*(radical|terror|extremi)","ecologically.motivated violen"]

foreign_fighter = ["\\bforeign.(fight|terrorist.fight)", "isis?.foreign.fight", "white.jihad"]

animal_rights = ["\\banimal.right"]

male_supremacist = ["\\bmisogyn(y|istic)\\b", "\\bgender.+based.+violence\\b", "\\banti.+wom[ae]n\\b", "\\bviolence.+against.+wom[ae]n\\b", "\\bincels?\\b", "^involuntary.celibat", "^male.supremacy$", "^red.pill"]

femcel = ["femcel"]


#Individual Differences

sex = ["boy", "girl", "\\bmale\\b", "\\bfemale\\b", "^gender$", "^sex$", "\\bwom[ae]n\\b(?!.*(rights|anti))", "\\bm[ae]n\\b(?!.*(rights|anti))"]

age = ["\\bage\\b", "\\bage.differences\\b", "school.+age", "\\bage.+child", "\\bage.+\\d", "\\bage.+(of|related) ", "age.+(diff|depend)", "aged.+\\d", "early age", "gestational.+age"]

status = ["\\b(subjective|perceived|social).+(social|sociometric|economic|socio.?economic)?.+(status|class)", "socio.?(economic|demographic)", "economic.+(stress|background|condition)", "\\bses\\b", "^income$", "^class$"]

employment = ["employ", "^welfare(?!.state)", "^work$", "^job$"]

urban = ["\\burban", "\\brural"]

adolescence = ["^adolescen(ts?|ce)$", "^youth$", "^teen(s?|agers?)$", "^juveniles?$", "^emerging.adults?$", "^youngsters?$", "^undergraduates?$"]

self_control = ["\\bself.control\\b", "\\bimpulsiv", "\\bself.regulat", "\\beffortful control\\b", "\\bexecutive function"]

law_abidance = ["\\blaw.(abidance|legitimacy)", "legal.(consciousness|awareness)", "policy legitimacy"]

digital_literacy = ["(digital|critical)? (medium|social media)? literacy"]

cognition = ["\\bcognit", "meta(.?awareness|cogniti)", "\\bthought", "\\bthink", "^memory$", "\\bdecision.mak(e|ing)", "^black.white$","^attitudes?$"]
#"\\bbias", "^creativity$", "\\bclosure$", "\\bknowledge\\b",

nostalgia = ["nostalgi"]

anomia = ["anomi[ea]", "value.change", "normless"]

personality = ["temperament$", "^personality$", "^personality.+(trait|invento|questionn|dimensi|type|factor|character|assess|develop)", "5.(factor|personali)", "big.5", "personal.(feature|disposition)"]

empathy = ["empath", "perspective.+taking", "sympathy", "empathic concern", "theory.(of.)?mind", "\\btom\\b"]

hate = ["\\bhate", "\\bhatred\\b", "^animosity$"]

sacred_values = ["\\bsacred.value", "\\bsacred.violen"]

passion = ["\\b(obsessive.)?passion"]

fanaticism = ["^fanati"]

determination = [ "\\bdevot", "^determination$", "\\bcommitment$"]

honor = ["\\bhonou?r", "^respect$"]

masculinity = ["\\bmasculin", "^manosphere$"]

martyrdom = ["\\bmartyr", "\\bhero"]

white_race = ["^white"]

trust = ["trust", "^credibility$"]

intolerance = ["toleran(ce|t)\\b"]

significance_quest = ["significance.(quest|loss)", "\\bself.esteem\\b", "\\bqfs\\b", "(need|search|quest|loss|personal).+(status|belong|meaning|significance)\\b", "meaning.+(life|existen)", "^meaning$", "\\bstatus.seek", "\\bbelonging\\b"]

uncertainty = ["\\buncertain", "identity (in)?security", "^insecurity$"]

conspiracy = ["\\bconspira"]

immigration = ["migration", "migrant", "\\brefugee", "^diaspora$", "^foreginer$", "asylum.seeker"]

pessimism = ["\\bpessimis"]

deviance = ["\\bdevia", "(illegal|destructive|illicit).act", "\\bsocial.adaptation", "\\bantisocial"]

morality = ["moral", "\\bprisoner.+dilemma\\b", "\\bethic", "\\bevil\\b", "^mfq$", "\\btrolley.(problem|dilemma)\\b"]

deprivation = ["\\bdepriv", "\\bclass.struggles?\\b", "\\boppress", "\\bsuppress", "\\brepress", "^struggle$", "\\bstrain", "\\bresource.loss\\b", "(economic|political).+(exclusion|discrimination)", "\\bethnic.exclsuion\\b", "\\bexclusionary.politics\\b", "^abuse$", "maltreat", "^occupation$", "^exploitation$", "\\bmarginali[sz]"]
           
racism = ["\\b(?!ost)racis"]

poverty = ["\\bpoverty\\b", "\\blow.income\\b", "economic.+(hardship|stress)"]

conformity = ["conform", "complian", "loyal"]

superiority = ["superior", "\\bsdo\\b", "\\bdomina", "group favoritism", "^power(ful)?$", "\\bsupremac", "^hierarch(y|ical)$"]

islamophobia = ["\\bislamophob", "\\banti.(muslim|islam)"]

system_justification = ["\\bsystem.justification\\b", "legitimacy$"]

social_skills = ["social.skill", "social.(competenc|functioni)"]

rationality = ["\\b(ir)?rational"]

autonomy = ["self.?(determination|efficacy)", "autonom"]

risk_taking = ["^risk.+(tak|behaviou?)", "(sensation|thrill).+seek", "reckless"]

political_agency = ["(political|civilian|\\bsocial).\\bagency", "\\bpolitical.(apath|access|effica)"]

political_engagement = ["(political|civic).+(engagement|participation|involvement|interest)", "interest.(in.?)politics", "political.party.support", "participation.(in.)?decision.making"]

altruism = ["pro.{0,2}social.{0,2}(behav|response)?", "\\baltruis"]

apocalypticism = ["apocalyp"]

prejudice = ["\\bprejudice\\b", "\\bstereotyp", "\\bhalo.effect", "\\bxenophob"]

cynicism = ["\\bcynic"]

skepticism = ["\\bs(k|c)epti"]

activism = ["^activis", "(^political|^non.?violent|^youth|^social|^community|^civi\w*)\\b.*?\\b(resist|acti|protest)", "active.citizen", "^collective.act", "^demonstrations?$", "^protest(ers?)?$", "^resistance$"]

authoritarianism = ["\\bauthorit"]

religiosity = ["^(extrinsic|intrinsic)?.*religiosity$", "^religion$", "^spiritual(ity)?$", "^islam$", "^islamic$", "^sufism$", "^shia$", "^sunni$","^jews?$", "^judaism$", "^christ", "^catholic$", "^hindu(ism)?$", "^muslims?$", "^buddh(a|ists?)$", "^mosque$", "^(catholic)?.*church$", "^religious.(belief|orientation|conversion|movement|cause|difference|experience|scripture|attitude|moderation|idea)"]

mobilization = ["^(?:(?!violent|radical|extremist|terror(ist)?|jihadi|resource|right.wing|foreign.fighter).)*mobili[sz]ation$", "^(social|protest).movement$"]

mortality_salience = ["mortality.salience", "death.anxiety", "fear(of.)?death", "^terror.management.theory$" ]

emotion = ["regulati.+difficult", "(emoti|affect|anger).+(regulation|proble|adjustm|compete)", "dysregulation", "emotional.problems?", "psychological distress", "mood", "irritability", "emotio", "affect\\b", "^sad(ness)?$", "happy", "happiness", "disgust", "affect.+intensity", "affect.+instab", "mood.+variab", "sham", "self.?consciou", "frustration", "feel", "affective investment"]

dogmatism = ["dogmat", "\\brigid", "\\battitude certainty\\b", "\\bcertain"]

fundamentalism = ["fundamentali"]

nationalism = ["nationali", "ethnocentri", "\\bnational.(attitude|pride)\\b", "\\bnativis"]

patriotism = ["patriot"]

populism = ["^populi(sm|sts?)(?!.radical)"]

conservatism = ["conservati", "^tradition$"]

liberalism = ["liberal"]

aggression = ["aggressive.behaviou?r", "^aggression$", "\\breactive aggression\\b", "\\baggressiveness\\b", "\\bantagonis", "\\bhostil", "^aggressive$"]

violence = ["^violence$", "^violent.attack$"]

criminality = ["^criminal(ity)?$", "crime\\b", "(?<!non)delinq", "\\bgangs?(.involvement)?\\b","\\bcriminolog", "^prison$", "^perpetration$", "^convict(s|ion)?$"]

fusion = ["\\bfusion\\b", "\\bfused\\b", "\\bunified\\b", "\\bunification\\b"]

ideology = ["\\bideolog(y|ies?)$", "political.(orientation|preference)", "^world.?view$"]

education = ["educat", "pedagogy"]

identity = ["\\bidenti(ty|ties?|fication)\\b", "^identity distress$", "emerging.+self", "representation.+self", "^affiliation$", "self.+(concept|construal|development|knowledge|representation|perception)", "self.+awareness"]

#Mental

resilience = ["\\bresilien", "\\bdifferential.susceptibility\\b"]

self_harm = ["\\bmutilation\\b", "self.injur", "self.harm", "^nssi$"]

suicide = ["^suicid(e|al|ality)$"]

substance_use = ["binge.drinking", "^addiction$", "drug.(ab)?use", "subst.+use", "alcohol", "cannabis", "^drug$", "marijuana", "tobacco", "smoking", "^misuse$", "^substance$", "\\buse disorder\\b"]

depression = ["depressi.*", "^mdd$", "mood.disorder", "affective.disorder"]

anxiety = ["anxiety", "^panic", "^behaviou?ral.inhibition$", "\\bphobia"]

fear = ["fear"]

iq = ["\\biq\\b", "^intelligence$"]

wellbeing = ["\\bquality.+life\\b", "well.?being", "life.sat"]

anger = ["\\banger\\b", "^angry$"]

adhd = ["hyperactiv", "\\bcallous.unemotional trait\\b", "hyperactivity disorder", "\\badhd\\b"]

narcissism = ["narcissis"]

ptsd = ["^ptsd$", "^trauma", "^survivors?"]

stress = ["\\b(di)?stress(?!\\sdisorder)"]

mental_health = ["psych.+symptom", "comorbid.+(?!anxiety)", "\\bmental.(disorders?|illness)\\b", "\\bdisorder.*\\b", "\\bmental.health", "\\bsymptom", "\\bpsychop.*\\b", "\\bpsychiatric.disorder.*\\b", "\\Bbpd\\b", "borderline personality", "\\b(psychological|somatic) symptom", "mental.disorder", "\\bsomatoform", "^bipolar$", "^mental$", "psychiatr(y|ic|ist)"]

schizophrenia = ["schizo", "psycho(sis|tic)"]

therapy = ["\\bin.?patient\\b", "therapy"]

autism = ["\\basd\\b", "\\basperger.syndrome\\b", "autis", "pervasive developmental disorder", "\\bhigh(ly)?.functioning\\b", "spectrum disorder"]

hope = ["\\bhope"]

dark_triad = ["\\bdark.triad\\b", "\\bdark.personality\\b", "\\bdark.tetrad\\b"]


#Physical

health = ["^health$", "^chronic illness$", "^pain$", "^ill(ness)?$", "diabetes", "cancer", "disease", "physical.+(illness|disorder)", "epilep", "health.related"]

public_health = ["^public.health$"]

neural = ["^neural\\b.+$", "^neuroscience.*$", "\\bf?mri\\b", "diffusion.tensor.imag", "brain", "hippocamp", "cortex", "cortica", "cingulate", "amygdala", "gyrus", "thalam", "limbic", "(gr[ea]y|white).+matter", "synap", "neuroimag", "functional.magnetic", "functional.connectivit", "endocannabin", "glutam", "neurotrans", "catecholamin", "adrenalin", "dopamin"]

genes = ["gene(\\b|t)", "gene.+envi"]

sports = ["physical.+(fitness|activity)", "\\bsport"]


#Environment

climate_change = ["\\bclimate.(change|shock|crisis|disruption|shift|conflict|protest)", "global.warming", "^climate$"]

globalization = ["\\bglobali[sz]"]

justice = ["justice", "\\bjust.world\\b", "\\bfreedom\\b(?!\\s(fighter|party))", "free.speech", "equal", "fair", "\\bgrievances?\\b",]

economy = ["^econom(y|ie|ic)", "\\bgdp\\b", "\\bgini\\b", "\\bincome.+caput\\b", "\\bcaput.income\\b", "(\\beuro\\b|\\bfinancial\\b).crisis\\b", "^inflation$"]

competition = ["\\bcompetiti", "\\brival", "^opposition$"]

security = ["\\b(?!(emotional|belief|identity).+)((in|cyber)?security|safe(ty)?|(in)?stability)\\b", "\\bsecuritization\\b", "stabilization", "^protection$"]

satisfaction = ["satisfaction\\b", "\\bgrudge\\b", " \\bdiscontent\\b"]

meritocracy = ["\\bmeritocra(tic|cy)\\b"]

corruption = ["\\bcorrupt"]

school = ["^schools?$", "^university$"]

teachers = ["\\bteacher"]

state = ["^states?$", "^govern(ment|ance)", "^welfare.states?$", "^state(.actor|power)$"]  

police = ["\\bpolice$", "\\bpolicing$"] 

propaganda = ["\\bpropaganda\\b"]

threat = ["\\bthreat", "\\bdanger\\b"]

democracy = ["\\bdemocra(tic|cies|tization)\\b", "^democracy$"]

politics = ["^politics?$", "^(political.)?part(y|ies)$"]

social_media = ["^youtube$", "^facebook$", "^reddit$", "^tiktok$", "^instagram$", "^twitter$", "^telegram$", "\\bsocial.medi(a|um)", "^posting$", "online.(discussion|discourse|social|network|conversation|comment|debate)", "social.platform", "^tweet$"]

internet = ["(?<!social )media\\b","internet", "\\bmeme\\b", "^web(site|.?forum)$", "video.gam", "digital.+(technology|medium)", "cyber(space)?", "\\bonline\\b(?!\\s+(discussion|discourse|social|network|conversation|comment|debate))", "^digital$"]

norms = ["\\bnorms?\\b", "\\bnormative\\b", "\\bnarrative", "\\bvalue", "\\bpublic.opinion\\b", "\\bhuman.rights?\\b"]

polarization = ["polari[sz]", "polar.opinion"]

capitalism = ["capitali"]

violence_exposure = ["\\bviolence.exposure\\b", "\\bexpos(ed|ure).+violen"]

language = ["language\\b", "lingu", "rhetoric", "^speech$", "^verbal$"]

elites = ["elite", "^establishment$"]

elections = ["\\belections?\\b", "^vot(e|er|ing.*)$", "\\belectoral\\b"]

peace = ["peace"]

conflict = ["\\bconflicts?$", "wars?$"]

crisis = ["covid", "cris[ie]s$", "^pandemic$"]

technology = ["^technology$"]

policy = ["^policy(.?maker)?$"]


#Social

intergroup_contact = ["\\binter.?group.(contact|process)", "\\binter.?ethnic.contact", "\\bcontact.(hypothesis|theory)"]   

social_network = ["^social.networks?$", "\\bcommunit(y|ies)$","^peer(.influences?|.interactions?|.relationships?|.relations?|.stress|.acceptance|.pressure)$", "^peers?$", "^friend(s|ship)?$", "^social.relationship"]

diversity = ["\\bdiversity\\b", "\\bheterogeneity\\b", "^heterogenous(.environment)?$", "\\bmultinational", "\\bpluralis", "\\bmulticultural", "^diverse$", "^homogenous$"]

consensus = ["\\bconsens", "\\bcommon.(understanding|consent)", "\\bagreement\\b"]

social_coherence = ["social.(coherence|cohesion)", "social.(bond|contact|tie|connection)", "social.support", "^social.capital", "^outsider$"]

neighborhood = ["neighbo"]

group_process = ["\\bgroup.(process|act|mechanism|dynamic|think|consens|interact)", "\\bsocial.(mechanism|dynamic)", "\\bcollective\\b.(dynamic|group)", "^(out|in)?groups?$"]

society = ["\\bsociet(y|ie|al)\\b"]

culture = ["^cultur", "civilization", "\\bsoci.+context", "sociali[sz]ation"]

social_exclusion = ["\\bexclu", "\\bostraci", "(personal|peer|social).+reject", "^rejection$", "isola", "lonel", "social.(withdrawal|disconnectedness|disintegration)", "\\balienation\\b", "friendless"]

segregation = ["segregat", "fragmentation", "separatism", "ethnic.division"]

integration = ["integrat", "inclusion", "^convergence$"]

victimization = ["victimi[sz](ed|ation)"]

dehumanization = ["dehumani[sz]ation", "^contempt$"]

discrimination = ["bull[yi]", "discriminat", "harass", "humiliat"]

family = ["\\bparent(s?|al)\\b", "^famil(y|ies)$", "intergenerational transmission", "mothe", "materna", "fathe", "paterna", "\\bsiblings?\\b", "\\bparenting\\b", "\\bparental (involvement|control)\\b", "parent.+style", "parent.+behav", "family.function", "^kinship$"]

minority = ["minorit"]

misinformation = ["(mis|dis)infor", "^fake.news$"]

discourse = ["^(political.|public.|social.)?discourse$", "^dialogue$"]

social_change = ["soci(al|etal|opolitical).(change|shift|evolution|reform|progress|development|transformation)", "^revolution$", "^opinion.dynamics?$"]

recruitment = ["^recruit(ment|ing)$"]

military = ["^military$"]

region = ["^region$", "^regional$", "^local$", "^location$", "^territory$"]

international = ["^(inter|trans)national$", "^cross.national$"]

institutions = ["\\binstitutions?$"]

feminism = ["\\bfeminis"]


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
    "male supremacist": male_supremacist,
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
    "passion": passion,
    "fanaticism": fanaticism,
    "determination": determination,
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
    "public health": public_health,
    "neural": neural,
    "genes": genes,
    "sports": sports,
    "conflict": conflict,
    "crisis": crisis,
    "technology": technology,
    "policy": policy,
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
    "social network": social_network,
    "minority": minority,
    "diversity": diversity,
    "consensus": consensus,
    "social cohesion": social_coherence,
    "neighborhood": neighborhood,
    "group process": group_process,
    "society": society,
    "culture": culture,
    "social exclusion": social_exclusion,
    "segregation": segregation,
    "integration": integration,
    "victimization": victimization,
    "dehumanization": dehumanization,
    "discrimination": discrimination,
    "family": family,
    "misinformation": misinformation,
    "discourse": discourse,
    "social change": social_change,
    "recruitment": recruitment,
    "military": military,
    "region": region, 
    "international": international, 
    "institutions": institutions}



# ===========================================================================================


