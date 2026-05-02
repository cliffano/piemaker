ID := piemaker
COMPONENTS := python-lib
MAKEFILE_NAME := Makefile-$(ID)
TARGET_VERSION_VARIABLE := TARGET_$(shell echo $(ID) | tr '[:lower:]-' '[:upper:]_')_VERSION

all: ci
ci: clean lint test

clean:
	for component in $(COMPONENTS); do \
	  (cd examples/$$component/ && make -f ../../src/$(MAKEFILE_NAME) clean && cd ../../); \
	done

deps-extra-apt:
	apt-get install -y markdownlint

lint:
	checkmake src/$(MAKEFILE_NAME)
	find ./ -type f -name "*.json" | while IFS= read -r file; do echo "> $$file"; python3 -m json.tool "$$file"; done
	mdl -s .mdl-style.rb $(shell find . -path ./stage -prune -o -path ./examples -prune -o -name "CHANGELOG.md" -prune -o -name "*.md" -print)

test:
	for component in $(COMPONENTS); do \
	  (cd examples/$$component/ && \
	    make -f ../../src/$(MAKEFILE_NAME) deps-extra-apt ci test-examples deps-upgrade update-dotfiles update-to-latest update-to-main && \
	    make -f ../../src/$(MAKEFILE_NAME) update-to-version $(TARGET_VERSION_VARIABLE)=1.0.0 &&\
		cd ../../); \
	done

release-major:
	rtk release --release-increment-type major

release-minor:
	rtk release --release-increment-type minor

release-patch:
	rtk release --release-increment-type patch

release: release-minor

.PHONY: all ci clean deps-extra-apt lint test release-major release-minor release-patch release