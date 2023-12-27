<img align="right" src="https://raw.github.com/cliffano/piemaker/master/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/piemaker/actions/workflows/ci-workflow.yaml/badge.svg)](https://github.com/cliffano/piemaker/actions/workflows/ci-workflow.yaml)
<br/>

PieMaker
--------

PieMaker is a Makefile for building Python packages.

It provides utility targets for linting, building, testing, documenting Python packages.

Have a look at [Awstaga](http://github.com/cliffano/awstaga) as an example project which uses PieMaker.

Installation
------------

1. Copy `src/Makefile-piemaker` to be the `Makefile` of your project:
    curl https://raw.githubusercontent.com/cliffano/piemaker/main/src/Makefile-piemaker -o Makefile
2. Create configuration file `piemaker.yml` with properties described in [Configuration](#configuration) section
3. Run the available `Makefile` targets described in [Usage](#usage) section

Configuration
-------------

Create PieMaker configuration file called `piemaker.yml` with contains the following properties:

| Property | Description | Example |
|----------|-------------|---------|
| package_name | The name of the Python package | `somepackage` |
| author | The author of the package | `Some Author` |

Usage
-----

The following targets are available:

| Target | Description |
|--------|-------------|
| ci | CI target to be executed by CI/CD tool, end to end build of the Python package |
| stage | Ensure stage directory exists |
| clean | Remove all temporary (staged, generated, cached) files |
| deps | Retrieve package dependencies using [Poetry](https://python-poetry.org/) |
| deps-extra | Retrieve extra tools: Python [VirtualEnv](https://virtualenv.pypa.io/) |
| update-to-latest | Update Makefile to the latest version on origin's main branch |
| update-to-version | Update Makefile to the version defined in `TARGET_PIEMAKER_VERSION` parameter |
| lint | Run lint checks against source and test code using [pylint](https://www.pylint.org/), then generate lint report using [pylint_report](https://pypi.org/project/pylint-report/) |
| complexity | Run complexity checks against source and test code using [wily](https://wily.readthedocs.io/), then generate complexity report |
| test | Run unit testing using [pytest](https://pytest.org), then generate test report |
| test-integration | Run integration testing using [pytest](https://pytest.org), then generate test report |
| coverage | Run coverage checks using [Coverage.py]https://github.com/nedbat/coveragepy), then generate coverage report |
| release-major | Create a major release using [rtk](https://github.com/cliffano/rtk) |
| release-minor | Create a minor release using [rtk](https://github.com/cliffano/rtk) |
| release-patch | Create a patch release using [rtk](https://github.com/cliffano/rtk) |
| package | Build the Python package using [Poetry](https://python-poetry.org/) |
| install | Install the built package using [Poetry](https://python-poetry.org/) |
| uninstall | Uninstall the package using [Pip](https://pypi.org/project/pip/) |
| reinstall | Uninstall, rebuild, and then install the package again |
| publish | Publish package to PyPi using [Poetry](https://python-poetry.org/) |
| doc | Generate package documentation using [Sphinx](https://www.sphinx-doc.org/) |
