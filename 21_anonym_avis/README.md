# Oppgave

Sdsdfhd, fdg, dereet,
ops sorry for skrivemaskin-problemet der! Det er så vanskelig å skrive med trykksverte klint utover fingra.

Svein Sviske her, toppredaktør i et medie, som foretrekker å forholde seg anonym i denne oppgaven, thank you very much.

Uansett, vi har ei lita dataavdeling her på huset. Kodeknekkere av rang, skal du vite. Jeg hilser på dem ved kaffemaskinen, drar min klassiske vits: “Hvorfor ser dere så sure ut, det må være fordi kaffen deres smaker helt PYTHON”, HÆHÆHÆHÆÆHÆHÆHÆHH.

Okay, nok om det. Vi har én strategi her på huset, å danke ut Norges største riksavis, du gjetta det, Verdens Gang. Eller Gnag som vi kallern etter en solid sigarillos på bakrommet. HÆHÆHÆHÆHÆ.

Hvordan utkonkurrerer man noen? Ved å kopiere ALT de gjør selvsagt. Derfor har kodeknukkerne våre laget et script jeg kan kjøre, som alltid gir meg tittelen på toppsaken på VG. Så kan jeg bare skrive den om litt, og dundre den inn i systemet, og call it a day!

Men, troru ikke VG har oppdatert sida, si a? De lømlene. Så nå kjørern ikke lenger, og det er krise fordi nå har jeg ikke hatt noe nytt å melde på 4-5 sekunder her.

De datafolka sier det holder å bytte ut kun én greie i koden for å få den til å kjøre igjen, men jeg hakke tid til å vente på dem.

Sender du meg den greia vi må endre det til? Koden har jeg lagt ved under her. Pling meg når du har koden da. Så krangler jeg litt med folk på intern-Slack-en imens jeg!

Klem fra Sviskern

import requests
from bs4 import BeautifulSoup

def shamelessly_steal_top_article(url):
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
first_article_title = soup.find('h1', {'class': 'headline'}).text.strip()
return first_article_title

url = "https://www.vg.no/"

first_article_title = shamelessly_steal_top_article(url)

if first_article_title:

print(f"The title of the first article is: {first_article_title}")

# Svar

```sh
python3 start.py

```

Svar: h2
