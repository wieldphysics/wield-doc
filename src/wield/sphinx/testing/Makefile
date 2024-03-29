.PHONY: list print collect complete coverage timing

# this is simpler to make multi-line scripts that can save variables and such
.ONESHELL:

#this is necessary to prevent the "intermediate" report files in the reports directory from being deleted
.SECONDARY:

clean:
	-rm -rf pytest-collection.txt
	-rm -rf pytest-collection.html
	-rm -rf test_results
	-rm -rf conda-env.txt
	-rm -rf timing.txt
	-rm -rf tests.rst
	-rm -rf conda-env.txt
	-rm -rf conda-list.txt
	-rm -rf conda-list-nopip.txt
	-rm -rf conda-export.txt
	-rm -rf pip-list.txt
	-rm -rf pip-freeze.txt
	-rm -rf python-import2.txt
	-rm -rf python-import1.txt

complete:
	$(MAKE) pytest-collection.txt
	$(MAKE) tests.rst
	if [ ! -f fast-mode-flag.txt ]; then $(MAKE) -k all; fi
	$(MAKE) timing
	$(MAKE) coverage

collect: pytest-collection.txt

pytest-collection.txt:
	pytest . ../  --rootdir='.' -c './pytest.ini' --ws-co --html='' --color=yes | tee pytest-collection.txt
	cat pytest-collection.txt | aha -b > pytest-collection.html
	sed -i -e 's/\x1b\[[0-9;]*m//g' pytest-collection.txt # strip ansi codes
	-mkdir -p test_results/reports/inprogress
	-mkdir -p test_results/reports/assets;
	-mkdir -p test_results/reports/coverage;
	-mkdir -p test_results/reports/failed;
	-mkdir -p test_results/reports/all;
	if which conda >> /dev/null; then conda env export --from-history > test_results/conda_env.txt; fi

tests.rst: pytest-collection.txt
	python3 -m wield.pytest.parse_collection pytest-collection.txt --api_rst > tests.rst

conda-env.txt:
	conda env export --from-history > conda-env.txt
	conda list > conda-list.txt
	conda list --no-pip > conda-list-nopip.txt
	conda list --export > conda-export.txt
	pip list > pip-list.txt
	pip freeze > pip-freeze.txt
	find -L . -name '*.py' -type f -print0 | xargs -0 sed -n 's/^\(from\|import\) \([^. ][^. ]*\.[^. ]*\)\(\.\| \).*$$/\2/p' | sort -u > python-import2.txt
	find -L . -name '*.py' -type f -print0 | xargs -0 sed -n 's/^\(from\|import\) \([^. ][^. ]*\)\(\.\| \).*$$/\2/p' | sort -u > python-import1.txt

coverage: 
		coverage combine --keep test_results/reports/coverage/*
		rm test_results/coverage/* || true
		coverage html -d test_results/coverage/
		# this is a bit hacky I know. Should use a greedy regex or more restrictive
		sed -i -e 's|>/[^<>]*/wield/|>wield/|' test_results/coverage/*.html
		sed -i -e 's|>/[^<>]*/gwinc/|>gwinc/|' test_results/coverage/*.html

timing:
		printf "" > timing.txt;
		for F in test_results/reports/all/*.html; do \
			FNAME=$$(basename $$F); \
			TIMING="$${FNAME%.html} $$(sed -n -e 's/^.*ran in \([0-9]\+.*[0-9]\+\) seconds.*$$/\1/p' $$F)"; \
			echo $$TIMING;\
			echo $$TIMING >> timing.txt;\
		done
		sort -k 2n timing.txt -o timing.txt;
		# remove the timing column
		awk '{print $$1}' timing.txt > timing_sort.txt

test_results/reports/all/%.html:  
		$(eval FILE := $(shell python3 -m wield.pytest.parse_collection pytest-collection.txt $*))
		$(eval PREHTML := test_results/reports/inprogress/$*.html)
		ln --force -T -s ../assets test_results/reports/inprogress/assets;
		#-pytest $(FILE) --ws-skip-slow --html=$(PREHTML)
		# This long command runs the specific pytest and generates a coverage file
		coverage run --source=$(cat modules) --branch --context=$* --data-file=test_results/reports/coverage/$* \
			-m pytest  -c './pytest.ini' --rootdir='.' $(FILE) --ws-skip-slow -m 'not largemem' --html=$(PREHTML)
		if [ "$$?" -eq 0 ]; \
    then \
			mv $(PREHTML) test_results/reports/; \
			ln --force -T -s ../$*.html test_results/reports/all/$*.html; \
			ln --force -T -s ../assets test_results/reports/all/assets; \
		else\
			ln --force -T -s ../assets test_results/reports/failed/assets; \
			mv $(PREHTML) test_results/reports/failed/; \
			ln --force -T -s ../failed/$*.html test_results/reports/all/$*.html; \
			false; \
    fi


print:
	python3 -m wield.pytest.parse_collection pytest-collection.txt --sort timing_sort.txt;

# @echo $(TESTS);

TESTS = $(shell python3 -m wield.pytest.parse_collection pytest-collection.txt --sort timing_sort.txt 2> /dev/null)

# remove all for it to not re-build failed tests
$(TESTS): %: test_results/reports/all/%.html
		@echo $*

all: $(TESTS) tests.rst pytest-collection.txt


.DEFAULT_GOAL := complete

