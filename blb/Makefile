ara: kjv.sh kjv.awk ara.tsv arafortune
	cat kjv.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar cz kjv.awk ara.tsv >> $@
	chmod +x $@
	strfile arafortune

test: kjv.sh
	shellcheck -s sh kjv.sh

clean:
	rm -f ara

install: ara
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)/usr/share/fortune/ara
	cp -f ara $(DESTDIR)$(PREFIX)/bin
	cp -f arafortune $(DESTDIR)/usr/share/fortune/ara
	cp -f arafortune.dat $(DESTDIR)/usr/share/ara
	chmod 755 $(DESTDIR)$(PREFIX)/bin/ara

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/ara
	rm -f $(DESTDIR)/usr/share/fortune/ara/arafortune 
	rm -f $(DESTDIR)/usr/share/fortune/ara/arafortune.dat

.PHONY: test clean install uninstall
