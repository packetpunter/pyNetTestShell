# Changelog

## 2.2.0-alpha

### Added

- TestUtils package for providing centralized logging
- Flamegrid package for providing an alternative to the net_shell, for one time commands
- LinuxUtils package that provides various, basic-bitch status helper functions. lots of stuff to be improved there.

### Changed
- moved a lot of logging functionality out of TestSession into centralized TestUtils.LogEngine
- created target validation as TestUtils.TestTargets using custom objects
- attempts first TestUtils.TestResult object for standard test result objects
    - created basic dataframe structure for each test type

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
