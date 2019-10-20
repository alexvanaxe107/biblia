PREFIX = /usr/local

ara: kjv.sh kjv.awk ara.tsv
	cat kjv.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar cz kjv.awk ara.tsv >> $@
	chmod +x $@

test: kjv.sh
	shellcheck -s sh kjv.sh

clean:
	rm -f ara

install: ara
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f ara $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/ara

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/ara

.PHONY: test clean install uninstall
