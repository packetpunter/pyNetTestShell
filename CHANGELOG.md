# Changelog

## 2.2.21 bug fixes
## Fixed
- The program logs to /network-testing, and now sets the files and directory to 777 unix permissions

## Changed
- The program must be run as root for traceroute

## 2.2.2 bug fixes
### Fixed
- The program can be called by "python -m TestShell" now or just "TestShell".
- The program logs to ~/network-testing per the README

## 2.2.1 stable version
- Finalized logging to use pandas Dataframes and store them
- Tester class is usable by Flamegrid and TestShell

## 2.2.0-alpha

### Added

- TestUtils package for providing centralized logging
- Flamegrid package for providing an alternative to the net_shell, for one time commands
- LinuxUtils package that provides various, basic-bitch status helper functions. lots of stuff to be improved there.
- icmplib functionality pulled into Tester so no external binaries are required

### Changed
- created target validation as TestObjects.TestTargets using custom objects
- creates TestResult dataframe for each test result

## 2.1.0

### Added

- changelog

### Changed

- move to production branch
- removed alpha tag

## 2.1-alpha

### Added

- sleep method
- config parsing correctly
- progress bars

### Changed

- python build structure

## 2.0-alpha

### Deprecated

- single shell.py

### Changed

- license type
- dedicated Tester module

### Added

- Config.yml parsing

## 1.21

### Added

- Initial release
- single shell.py with all functionality built in
- required either pyinstaller release file or running within virtual environment
