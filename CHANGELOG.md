# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## 1.9.0 - 2025-04-21
### Added
- Add sphinx-build extra-dep for sphinx-apidoc

### Changed
- Replace /opt/poetry-venv to .venv for VirtualEnv home
- Change example min Python to 3.11
- Upgrade deps

## 1.8.0 - 2025-01-06
### Changed
- Modify poetry and poetry-plugin-up to use explicit version due to incompatibility when installing plugin via poetry self add

## 1.7.0 - 2024-12-07
### Added
- Add new update-to-latest which updates to latest version tag

### Changed
- Rename Makefile target update-to-latest to update-to-main

## 1.6.0 - 2024-12-07
### Added
- Add -x flag to test-examples target's bash calls

## 1.5.0 - 2024-11-23
### Added
- Add tests-integration and examples folders to style target

## 1.4.0 - 2024-11-09
### Added
- Add style target using black

## 1.3.0 - 2024-06-03
### Added
- Add install-wheel Makefile target

### Changed
- Switch release workflow steps to use release-action

## 1.2.1 - 2024-03-30
### Fixed
- Fix test-examples to run from within examples/ directory

## 1.2.0 - 2024-03-29
### Added
- Add deps-upgrade Makefile target

## 1.1.1 - 2024-01-14
### Fixed
- Fix missing coverage report by excluding .gitignore file

## 1.1.0 - 2023-12-31
### Added
- Add staging folder for each Makefile target

### Changed
- Complexity now expects poetry.lock to be present

## 1.0.0 - 2023-12-29
### Added
- Initial version
