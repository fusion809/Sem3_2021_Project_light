export OPENGL=0
include /data/GitHub/others/rebound/src/Makefile.defs

all: librebound
	@echo ""
	@echo "Compiling problem file ..."
	$(CC) -I/data/GitHub/others/rebound/src/ -Wl,-rpath,./ $(OPT) $(PREDEF) computeTrajectory.c -L. -lrebound $(LIB) -o rebound
	@echo ""
	@echo "REBOUND compiled successfully."

librebound: 
	@echo "Compiling shared library librebound.so ..."
	$(MAKE) -C /data/GitHub/others/rebound/src/
	@-rm -f librebound.so
	@ln -s /data/GitHub/others/rebound/src/librebound.so .

clean:
	@echo "Cleaning up shared library librebound.so ..."
	@-rm -f librebound.so
	$(MAKE) -C /data/GitHub/others/rebound/src clean
	@echo "Cleaning up local directory ..."
	@-rm -vf rebound
