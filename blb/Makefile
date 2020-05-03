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
	cp -f ara $(DESTDIR)$(PREFIX)/bin
	cp -f arafortune /usr/share/fortune
	cp -f arafortune.dat /usr/share/fortune
	chmod 755 $(DESTDIR)$(PREFIX)/bin/ara

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/ara
	rm -f /usr/share/fortune/arafortune 
	rm -f /usr/share/fortune/arafortune .dat

.PHONY: test clean install uninstall
