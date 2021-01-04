#
# Makefile: To install rpn you only need to do `make install`.
# 			This program doesn't use non-standard Python libraries/
# 			So, as long as you have Python 3 everything should be OK.
#
#			Only if you wish to develop this program you should install
#			pytest and black.
#

.SILENT:install uninstall

install:
	if chmod +x $(CURDIR)/main.py ; then \
		if sudo ln -s $(CURDIR)/main.py /usr/local/bin/rpn; then \
			echo "  ✨ Installation successful! ✨"; \
			echo "  You can run rpn by typing 'rpn' from anywhere."; \
			exit 0; \
		else \
			echo "  Error: Failed to create symlink in /usr/local/bin"; \
			echo "  You can try running rpn by doing 'python main.py'"; \
			exit 1; \
		fi; \
	else \
		echo "  ❌ Error: Failed to create rpn executable"; \
		echo "  Still, you can test running rpn by doing 'python main.py'"; \
		exit 1; \
	fi

uninstall:
	if sudo rm /usr/local/bin/rpn; then \
		echo "  ✅ rpn was removed from /usr/local/bin"; \
		echo "  Feel free to delete any remaining rpn files and packages."; \
		exit 0; \
	else \
		echo "  ❌ Error: Failed to remove rpn from /usr/local/bin"; \
		echo "  Try removing it manually by doing 'sudo rm /usr/local/bin/rpn'"; \
		exit 1; \
	fi;

requirements:
	@echo "  Installing dev requirements..."; \
	pip install -r requirements.txt

black:
	black $(CURDIR)/main.py
	black $(CURDIR)/rpn/cli.py
	black $(CURDIR)/rpn/calculator.py
	black $(CURDIR)/rpn/operators.py
	black $(CURDIR)/rpn/tests

test:
	export PYTHONPATH=$(CURDIR)
	pytest

test-s:
	export PYTHONPATH=$(CURDIR)
	pytest -s

dev:
	@echo " 🧑‍💻 Preparing rpn for development..."
	make requirements
	make test

