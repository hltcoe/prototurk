# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [0.4.2] - 2021-09-22
### Changed
- Maximum CSV size limit increased from Python default of 128K to 100MB

## [0.4.1] - 2021-08-24
### Fixed
- Fixed CSS issue that caused two scroll bars to be displayed on Task
  Asssignment page.  One scroll bar was inside the iframe, while the
  other was out.

## [0.4.0] - 2021-08-19
### Added
- Added `prototurk-populate` command line script.

## [0.3.3] - 2020-01-06
### Changed
- On Task Assignment page, browser focus is initially set to the
  iframe, not the outer page.

## [0.3.2] - 2019-11-11
### Added
- Added `--version` flag, using technique #3 from 
  https://packaging.python.org/guides/single-sourcing-package-version/
- Added `--js-map-path` flag for specifying the location of .js.map
  files.  Useful for debugging apps created by frameworks like React.

## [0.3.1] - 2019-11-06
### Added
- Task page now has 'Next Task' and 'Previous Task' buttons

## [0.3.0] - 2019-11-05
### Added
- UI now styled with Bootstrap
- Task page now displayed within an iFrame

## [0.2.3] - 2019-11-04
### Added
- Added BSD 2-clause LICENSE file
### Fixed
- Regression caused by changing template filename

## [0.2.2] - 2019-11-03
### Fixed
- Corrected capitalization on project pages - 'ProtoTurk', not 'Prototurk'
- JSON deserialization exception now caught and handled properly

## [0.2.1] - 2019-11-03
### Fixed
- README should now be used for the package long description

## [0.2.0] - 2019-11-03
### Added
- Added CHANGELOG.md file
- HTTP header 'Cache-Control' now set to 'no-store'
- HTTP requests for `.js.map` files now receive 404 response
- README now used for long description that PyPI displays as "Project description"
- Task Assignment page now displays Task #
- Task List page now displays CSV and HTML Template filenames

## [0.1.1] - 2019-10-31
### Added
- URL and description added to `setup.py` 

## [0.1.0] - 2019-10-31
- Initial release
