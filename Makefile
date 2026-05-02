all: ci
ci: clean lint test

clean:
	cd examples && \
	  make -f ../src/Makefile-piemaker clean

deps-extra-apt:
	apt-get install -y markdownlint

lint:
	checkmake src/Makefile-piemaker
	find ./ -type f -name "*.json" | while IFS= read -r file; do echo "> $$file"; python3 -m json.tool "$$file"; done
	mdl -s .mdl-style.rb $(shell find . -path ./stage -prune -o -path ./examples/.venv -prune -o -name "CHANGELOG.md" -prune -o -name "*.md" -print)

test:
	cd examples && \
	  make -f ../src/Makefile-piemaker deps-extra-apt ci test-examples deps-upgrade update-dotfiles update-to-latest update-to-main && \
	  make -f ../src/Makefile-piemaker update-to-version TARGET_PIEMAKER_VERSION=1.0.0

release-major:
	rtk release --release-increment-type major

release-minor:
	rtk release --release-increment-type minor

release-patch:
	rtk release --release-increment-type patch

release: release-minor

.PHONY: all ci clean lint release release-major release-minor release-patch test