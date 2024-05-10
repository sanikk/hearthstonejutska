# Luonnoksia

### sync vs async

Sync:
main, ui

async:




eli jos service olis sync taas, ja pyöris tällä samalla threadilla.
sitten pitää tehdä tohon service <-> dir_monitor väliin tuo sync/async-kikkailu.


tämä luo tkinterin eventin 50ms päästä ja sitten toistaa sitä 50ms välein: 
root.after(50, after_callback)
    def after_callback(self):
        try:
            content = self.syncqueue.get(block=False)
        except queue.Empty:
            self.root.after(50, self.after_callback)
            return
        if content:
            self.output_box.insert('end', content)



### uus plani

jos tekis tolla tkinterin afterilla kyselyn -> log_servicellä koitetaan ottaa kontsaa. jos ei tullut, toistetaan tuolla 
guin puolella, 50ms viiveellä, root.after(50, after_callback)