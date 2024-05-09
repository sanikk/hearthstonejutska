### async
eli ensin
- palikka joka pystyy lähettämään viestiä kun tapahtuma
- palikka joka tekee jotain kun tulee viesti.

- palikka joka lukee logia aina kun on tapahtuma ja lähettää sen
- palikka joka prosessoi tapahtuman

Eli kurkkaillaan sitä sopivasti, ehkä tarkkaillaan hakemistoa?

    Tää vielä johonkin omaan threadiin muita häiritsemästä, asyncillä päivityksiä.

    Vaihtoehtoja
    ~~#1 async suoraan gui~~
    #2 async service, async gui
    #3 async service, sync gui(poll)
    #4 sync service, sync gui. poll poll poll.
