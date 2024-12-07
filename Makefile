ci: clean lint test

clean:
	cd examples && \
	  make -f ../src/Makefile-piemaker clean

lint:
	checkmake src/Makefile-piemaker

test:
	cd examples && \
	  make -f ../src/Makefile-piemaker clean deps-extra-apt deps deps-upgrade deps style lint test coverage complexity doc package reinstall test-integration install-wheel test-examples

release-major:
	rtk release --release-increment-type major

release-minor:
	rtk release --release-increment-type minor

release-patch:
	rtk release --release-increment-type patch

release: release-minor

.PHONY: ci clean lint release release-major release-minor release-patch test