ci: clean lint test

clean:
	cd examples && \
	  make -f ../src/Makefile-piemaker clean

lint:
	checkmake src/Makefile-piemaker

test:
	cd examples && \
	  make -f ../src/Makefile-piemaker clean deps-extra-apt deps deps-upgrade deps lint test coverage complexity doc package reinstall test-integration test-examples

release-major:
	rtk release --release-increment-type major

release-minor:
	rtk release --release-increment-type minor

release-patch:
	rtk release --release-increment-type patch

release: release-minor

.PHONY: all ci clean lint test release-major release-minor release-patch
