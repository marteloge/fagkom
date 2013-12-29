# Fagkom.com

Fagkom.com &lt;3

### Oppsett av fagkom.com på egen box/mac (Google e.l. for windows)

1. Gå inn i mappen der du ønsker å ha prosjektet f.eks. `/home/<brukernavn>/webapps/`.
2. Klon prosjektet ved å kjøre git-kommandoen `git clone https://github.com/marteloge/fagkom.git`
3. Gå inn i mappen med kommandoen `cd fagkom`
4. Sett opp et virtuelt miljø
    * Kjør `virtualenv --distribute env`
    * Bruk `source env/bin/activate` for å aktivere det virtuelle miljøet. Dette må gjøres hver gang du skal inn i det virtuelle miljøet.
        * Du skal se `(env)` i starten av promptet hvis du kan gjort dette riktig.
        * Du kan kjøre `deactivate` fra hvor som helst for å deaktivere.
5. Installér alle pakkene du trenger ved å kjøre `pip install -r requirements.txt`
6. Sette opp database
    * Kjør `./manage.py syncdb` og fyll inn nødvendig info
    * Kjør `./manage.py migrate` for å migrere databasen (__Notér:__ Veldig usikker på akkurat hvordan dette er)
6. Ferdig! Bruk `./manage runserver` for å starte localhost på port 8000 :-)

__Tips:__ Må du skrive `python manage.py runserver` i stedet for `./manage.py runserver`, så må du gjøre `manage.py` kjørbar. Dette kan gjøres ved å kjøre kommandoen `chmod u+x manage.py`.
