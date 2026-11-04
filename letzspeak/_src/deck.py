# Lëtz Speak Vocab — beginner deck. Format per line: id | lb | fr | en | note
# ids are permanent (progress is keyed by them) — never change an existing id.
MODULES = {
 1: ("Moien!", "Saluer et remercier", "Greetings & thanks"),
 2: ("Wéi geet et?", "Ça va ? Oui, non…", "How are you? Yes, no…"),
 3: ("Ech sinn …", "Se présenter", "Introducing yourself"),
 4: ("Länner a Sproochen", "Pays et langues", "Countries & languages"),
 5: ("Zuelen 0–20", "Les nombres 0–20", "Numbers 0–20"),
 6: ("D'Woch", "Les jours, le temps", "Days & time"),
 7: ("D'Famill", "La famille", "Family"),
 8: ("Am Café", "Au café", "At the café"),
 9: ("Wichteg Verben", "Verbes importants", "Key verbs"),
 10: ("Froen", "Questions et en cours", "Questions & in class"),
}
RAW = {
1: """
moien | Moien! | Bonjour ! / Salut ! (à toute heure) | Hello! / Hi! (any time) |
gudde-moien | Gudde Moien! | Bonjour ! (le matin) | Good morning! |
gudde-metteg | Gudde Mëtteg! | Bonjour ! (vers midi, l'après-midi) | Good afternoon! |
gudden-owend | Gudden Owend! | Bonsoir ! | Good evening! |
gutt-nuecht | Gutt Nuecht! | Bonne nuit ! | Good night! |
salut | Salut! | Salut ! | Hi! / Bye! (casual) |
addi | Äddi! | Au revoir ! | Goodbye! |
awar | Awar! | Salut ! À plus ! (familier) | See you! (casual) |
bis-geschwenn | Bis geschwënn! | À bientôt ! | See you soon! |
bis-muer | Bis muer! | À demain ! | See you tomorrow! |
scheinen-dag | Schéinen Dag! | Bonne journée ! | Have a nice day! |
scheinen-owend | Schéinen Owend! | Bonne soirée ! | Have a nice evening! |
merci | Merci! | Merci ! | Thank you! |
merci-villmools | Merci villmools! | Merci beaucoup ! | Thank you very much! |
wann-ech-gelift | wann ech gelift | s'il vous plaît / s'il te plaît | please |
keng-ursaach | Keng Ursaach! | De rien ! | You're welcome! |
entschellegt | Entschëllegt! | Excusez-moi ! / Pardon ! | Excuse me! / Sorry! |
glaichfalls | Gläichfalls! | De même ! / Vous aussi ! | You too! / Likewise! |
""",
2: """
wei-geet-et | Wéi geet et? | Ça va ? | How are you? |
wei-geet-et-dir | Wéi geet et dir? | Comment vas-tu ? | How are you? (informal) |
wei-geet-et-iech | Wéi geet et Iech? | Comment allez-vous ? | How are you? (formal) |
mir-geet-et-gutt | Mir geet et gutt. | Je vais bien. | I'm fine. |
an-dir | An dir? | Et toi ? | And you? (informal) |
an-iech | An Iech? | Et vous ? | And you? (formal) |
ganz-gutt | Ganz gutt! | Très bien ! | Very well! |
tipptopp | Tipptopp! | Super ! | Great! |
et-geet | Et geet. | Ça va, bof. | So-so. |
net-gutt | Net gutt. | Pas bien. | Not good. |
schlecht | Schlecht. | Mal. | Bad. |
jo | jo | oui | yes |
nee | nee | non | no |
jo-gar | Jo, gär! | Oui, volontiers ! | Yes, gladly! |
nee-merci | Nee, merci. | Non, merci. | No, thank you. |
kee-problem | Kee Problem! | Pas de problème ! | No problem! |
ech-och | Ech och. | Moi aussi. | Me too. |
""",
3: """
wei-heeschs-du | Wéi heeschs du? | Tu t'appelles comment ? | What's your name? (informal) |
wei-heescht-dir | Wéi heescht Dir? | Comment vous appelez-vous ? | What's your name? (formal) |
ech-heeschen | Ech heeschen … | Je m'appelle … | My name is … | Ech heeschen Anna. · Ech heesche Marc.
et-freet-mech | Et freet mech! | Enchanté(e) ! | Nice to meet you! |
mech-och | Mech och! | Moi de même ! | Nice to meet you too! |
vu-wou-kenns-du | Vu wou kënns du? | Tu viens d'où ? | Where are you from? (informal) |
vu-wou-kommt-dir | Vu wou kommt Dir? | Vous venez d'où ? | Where are you from? (formal) |
ech-kommen-aus | Ech kommen aus … | Je viens de … (pays) | I'm from … (country) | Ech kommen aus Portugal.
wou-wunns-du | Wou wunns du? | Tu habites où ? | Where do you live? (informal) |
wou-wunnt-dir | Wou wunnt Dir? | Où habitez-vous ? | Where do you live? (formal) |
ech-wunnen-zu | Ech wunnen zu … | J'habite à … (ville) | I live in … (town) | Ech wunnen zu Esch.
wei-al-bass-du | Wéi al bass du? | Tu as quel âge ? | How old are you? (informal) |
wei-al-sidd-dir | Wéi al sidd Dir? | Quel âge avez-vous ? | How old are you? (formal) |
ech-sinn-joer-al | Ech sinn … Joer al. | J'ai … ans. | I'm … years old. |
wat-schaffs-du | Wat schaffs du? | Tu fais quoi comme travail ? | What do you do for a living? |
ech-schaffen-als | Ech schaffen als … | Je travaille comme … | I work as … |
virnumm | de Virnumm | le prénom | first name |
familljennumm | de Familljennumm | le nom de famille | surname |
""",
4: """
letzebuerg | Lëtzebuerg | le Luxembourg | Luxembourg |
letzebuergesch | Lëtzebuergesch | le luxembourgeois (langue) | Luxembourgish (language) |
frankraich | Frankräich | la France | France |
franseisch | Franséisch | le français (langue) | French (language) |
daitschland | Däitschland | l'Allemagne | Germany |
daitsch | Däitsch | l'allemand (langue) | German (language) |
belsch | d'Belsch | la Belgique | Belgium |
portugal | Portugal | le Portugal | Portugal |
portugisesch | Portugisesch | le portugais (langue) | Portuguese (language) |
italien | Italien | l'Italie | Italy |
italieenesch | Italieenesch | l'italien (langue) | Italian (language) |
englesch | Englesch | l'anglais (langue) | English (language) |
ech-schwatzen | Ech schwätzen … | Je parle … | I speak … | Ech schwätzen Englesch. · Ech schwätze Franséisch.
schwatz-du-lb | Schwätz du Lëtzebuergesch? | Tu parles luxembourgeois ? | Do you speak Luxembourgish? (informal) |
schwatzt-dir-lb | Schwätzt Dir Lëtzebuergesch? | Vous parlez luxembourgeois ? | Do you speak Luxembourgish? (formal) |
e-bessen-lb | Ech schwätzen e bësse Lëtzebuergesch. | Je parle un peu luxembourgeois. | I speak a little Luxembourgish. |
ech-leiere-lb | Ech léiere Lëtzebuergesch. | J'apprends le luxembourgeois. | I'm learning Luxembourgish. |
ech-verstinn-net | Ech verstinn net. | Je ne comprends pas. | I don't understand. |
""",
5: """
null | null | 0 | 0 |
eent | eent | 1 | 1 |
zwee | zwee | 2 | 2 |
drai | dräi | 3 | 3 |
veier | véier | 4 | 4 |
fennef | fënnef | 5 | 5 |
sechs | sechs | 6 | 6 |
siwen | siwen | 7 | 7 |
aacht | aacht | 8 | 8 |
neng | néng | 9 | 9 |
zeng | zéng | 10 | 10 |
eelef | eelef | 11 | 11 |
zwielef | zwielef | 12 | 12 |
draizeng | dräizéng | 13 | 13 |
veierzeng | véierzéng | 14 | 14 |
fofzeng | fofzéng | 15 | 15 |
siechzeng | siechzéng | 16 | 16 |
siwwenzeng | siwwenzéng | 17 | 17 |
uechtzeng | uechtzéng | 18 | 18 |
nonzeng | nonzéng | 19 | 19 |
zwanzeg | zwanzeg | 20 | 20 |
""",
6: """
meindeg | Méindeg | lundi | Monday |
denschdeg | Dënschdeg | mardi | Tuesday |
mettwoch | Mëttwoch | mercredi | Wednesday |
donneschdeg | Donneschdeg | jeudi | Thursday |
freideg | Freideg | vendredi | Friday |
samschdeg | Samschdeg | samedi | Saturday |
sonndeg | Sonndeg | dimanche | Sunday |
haut | haut | aujourd'hui | today |
geschter | gëschter | hier | yesterday |
muer | muer | demain | tomorrow |
elo | elo | maintenant | now |
dag | den Dag | le jour | the day |
woch | d'Woch | la semaine | the week |
weekend | de Weekend | le week-end | the weekend |
moies | moies | le matin | in the morning |
mettes | mëttes | à midi / l'après-midi | at midday / in the afternoon |
owes | owes | le soir | in the evening |
wat-ass-haut | Wat ass haut? | On est quel jour ? | What day is it today? |
""",
7: """
famill | d'Famill | la famille | the family |
mamm | d'Mamm | la mère | the mother |
papp | de Papp | le père | the father |
elteren | d'Elteren | les parents | the parents |
brudder | de Brudder | le frère | the brother |
schwester | d'Schwëster | la sœur | the sister |
jong | de Jong | le fils / le garçon | the son / the boy |
duechter | d'Duechter | la fille (enfant) | the daughter |
kand | d'Kand | l'enfant | the child |
kanner | d'Kanner | les enfants | the children |
mann | de Mann | l'homme / le mari | the man / the husband |
fra | d'Fra | la femme / l'épouse | the woman / the wife |
bopi | de Bopi | le grand-père | the grandfather |
bomi | d'Bomi | la grand-mère | the grandmother |
frend | de Frënd / d'Frëndin | l'ami / l'amie | the friend (m / f) |
hues-du-kanner | Hues du Kanner? | Tu as des enfants ? | Do you have children? |
zwee-kanner | Ech hunn zwee Kanner. | J'ai deux enfants. | I have two children. |
bestuet | Ech si bestuet. | Je suis marié(e). | I'm married. |
""",
8: """
kaffi | de Kaffi | le café | the coffee |
tei | den Téi | le thé | the tea |
waasser | d'Waasser | l'eau | the water |
mellech | d'Mëllech | le lait | the milk |
zocker | den Zocker | le sucre | the sugar |
beier | de Béier | la bière | the beer |
wain | de Wäin | le vin | the wine |
brout | d'Brout | le pain | the bread |
kuch | de Kuch | le gâteau | the cake |
zopp | d'Zopp | la soupe | the soup |
ech-hatt-gar | Ech hätt gär … | Je voudrais … | I'd like … |
e-kaffi-weg | E Kaffi, wann ech gelift. | Un café, s'il vous plaît. | A coffee, please. |
mat-mellech | mat Mëllech | avec du lait | with milk |
ouni-zocker | ouni Zocker | sans sucre | without sugar |
wat-kascht-dat | Wat kascht dat? | Combien ça coûte ? | How much is that? |
bezuelen | Ech géif gär bezuelen. | Je voudrais payer. | I'd like to pay. |
rechnung | d'Rechnung | l'addition | the bill |
gudden-appetit | Gudden Appetit! | Bon appétit ! | Enjoy your meal! |
prost | Prost! | Santé ! | Cheers! |
""",
9: """
sinn | sinn | être | to be | ech sinn · du bass
hunn | hunn | avoir | to have | ech hunn · du hues
maachen | maachen | faire | to do / to make | ech maachen
goen | goen | aller | to go | ech ginn · du gees
kommen | kommen | venir | to come | ech kommen · du kënns
wunnen | wunnen | habiter | to live (somewhere) | ech wunnen
schaffen | schaffen | travailler | to work | ech schaffen
schwatzen | schwätzen | parler | to speak | ech schwätzen
verstoen | verstoen | comprendre | to understand | ech verstinn
leieren | léieren | apprendre | to learn | ech léieren
iessen | iessen | manger | to eat | ech iessen · du ëss
drenken | drénken | boire | to drink | ech drénken
schlofen | schlofen | dormir | to sleep | ech schlofen · du schléifs
liesen | liesen | lire | to read | ech liesen · du lies
kucken | kucken | regarder | to look / to watch | ech kucken
kafen | kafen | acheter | to buy | ech kafen · du keefs
""",
10: """
wien | Wien? | Qui ? | Who? |
wat | Wat? | Quoi ? / Que ? | What? |
wou | Wou? | Où ? | Where? |
weini | Wéini? | Quand ? | When? |
wei | Wéi? | Comment ? | How? |
firwat | Firwat? | Pourquoi ? | Why? |
wei-vill | Wéi vill? | Combien ? | How much? / How many? |
wei-seet-een | Wéi seet een dat op Lëtzebuergesch? | Comment on dit ça en luxembourgeois ? | How do you say that in Luxembourgish? |
wat-heescht-dat | Wat heescht dat? | Ça veut dire quoi ? | What does that mean? |
mei-lues | Méi lues, wann ech gelift. | Plus lentement, s'il vous plaît. | More slowly, please. |
nach-eng-keier | Nach eng Kéier, wann ech gelift. | Encore une fois, s'il vous plaît. | Once more, please. |
ech-weess-net | Ech weess et net. | Je ne sais pas. | I don't know. |
wei-schreift-een | Wéi schreift een dat? | Ça s'écrit comment ? | How do you spell that? |
eng-fro | Ech hunn eng Fro. | J'ai une question. | I have a question. |
richteg | richteg | juste / correct | right / correct |
falsch | falsch | faux | wrong |
""",
}
def deck():
    out=[]; ids=set()
    for m,txt in RAW.items():
        for line in txt.strip().splitlines():
            p=[x.strip() for x in line.split("|")]
            assert len(p)==5, line
            assert p[0] not in ids, p[0]; ids.add(p[0])
            out.append({"id":p[0],"lb":p[1],"fr":p[2],"en":p[3],"note":p[4],"m":m})
    return out
if __name__=="__main__":
    import json; d=deck(); print(len(d))
    json.dump({"modules":MODULES,"deck":d},open("/home/claude/work/deck.json","w"),ensure_ascii=False,indent=0)
