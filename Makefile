all: ci
ci: clean lint test

clean:
	cd examples && \
	  make -f ../src/Makefile-piemaker clean

lint:
	checkmake src/Makefile-piemaker

test:
	cd examples && \
	  make -f ../src/Makefile-piemaker deps-extra-apt ci test-examples update-to-latest update-to-main && \
	  make -f ../src/Makefile-piemaker update-to-version TARGET_PIEMAKER_VERSION=1.0.0

release-major:
	rtk release --release-increment-type major

release-minor:
	rtk release --release-increment-type minor

release-patch:
	rtk release --release-increment-type patch

release: release-minor

.PHONY: all ci clean lint release release-major release-minor release-patch test