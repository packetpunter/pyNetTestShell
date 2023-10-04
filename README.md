# pyNetTestShell
An interactive python shell to test the network using external commands as well as some python libs for network performance

## Requirements
None - this is pure Python3, thanks to the likes of the tabulate project and the icmplib project.

## Behavior
The app is interactive, and upon launch, creates a new logfile. 

The logfile is located in ```output/$YEAR/$MONTH/$DAY``` and the file is named according to data in ```Config.py```, using the timestamp for the file name.

Once in, you have a shell where you can run pings, traceroutes, speedtests with logging to disk and some analysis.


## Usage

This application has two ways to interface with it. There is an interactive shell called TestShell, and an execuble-like mode for one-off testing via the module "Flamegrid"

#### Interactive Shell
```bash
python3 -m TestShell

```
##### Sample Output
```bash
Welcome to the Network Tester Interactive v2.1.0 app to test your network!

Type ? to list commands.
 For questions, please contact the administrator who granted you this access.


net_test> set target 1.1.1.1 4.4.4.4 8.8.8.8 reddit.com nmsu.edu
net_test> run route ping
TestSession: Begin route testing

TestSession: TEST route:: RESULTS 
╒════╤═══════════════════════╤═══════╤═════════╤═══════════════════╤════════════════╤═══════════════════════════════╕
│    │ TS                    │ SRC   │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop          │
╞════╪═══════════════════════╪═══════╪═════════╪═══════════════════╪════════════════╪═══════════════════════════════╡
│ TS │ 2023/10/04-T-17:12:42 │ self  │ 1.1.1.1 │          0.502167 │        2.02133 │ 1.1.1.1 responded in 24.256ms │
╘════╧═══════════════════════╧═══════╧═════════╧═══════════════════╧════════════════╧═══════════════════════════════╛
TestSession: TEST route:: RESULTS 
╒════╤═══════════════════════╤═══════╤═════════╤═══════════════════╤════════════════╤════════════════════════════════════╕
│    │ TS                    │ SRC   │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop               │
╞════╪═══════════════════════╪═══════╪═════════╪═══════════════════╪════════════════╪════════════════════════════════════╡
│ TS │ 2023/10/04-T-17:13:23 │ self  │ 4.4.4.4 │            0.0839 │         2.0752 │ 96.110.44.29 responded in 21.093ms │
╘════╧═══════════════════════╧═══════╧═════════╧═══════════════════╧════════════════╧════════════════════════════════════╛
TestSession: TEST route:: RESULTS 
╒════╤═══════════════════════╤═══════╤═════════╤═══════════════════╤════════════════╤══════════════════════════════════════╕
│    │ TS                    │ SRC   │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop                 │
╞════╪═══════════════════════╪═══════╪═════════╪═══════════════════╪════════════════╪══════════════════════════════════════╡
│ TS │ 2023/10/04-T-17:13:25 │ self  │ 8.8.8.8 │         0.0953571 │        1.43621 │ 108.170.254.65 responded in 20.346ms │
╘════╧═══════════════════════╧═══════╧═════════╧═══════════════════╧════════════════╧══════════════════════════════════════╛
TestSession: TEST route:: RESULTS 
╒════╤═══════════════════════╤═══════╤════════════╤═══════════════════╤════════════════╤════════════════════════════════════╕
│    │ TS                    │ SRC   │ DST        │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop               │
╞════╪═══════════════════════╪═══════╪════════════╪═══════════════════╪════════════════╪════════════════════════════════════╡
│ TS │ 2023/10/04-T-17:13:27 │ self  │ reddit.com │         0.0225385 │        1.47269 │ 96.110.44.29 responded in 20.481ms │
╘════╧═══════════════════════╧═══════╧════════════╧═══════════════════╧════════════════╧════════════════════════════════════╛
TestSession: TEST route:: RESULTS 
╒════╤═══════════════════════╤═══════╤══════════╤═══════════════════╤════════════════╤═══════════════════════════════════╕
│    │ TS                    │ SRC   │ DST      │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop              │
╞════╪═══════════════════════╪═══════╪══════════╪═══════════════════╪════════════════╪═══════════════════════════════════╡
│ TS │ 2023/10/04-T-17:13:29 │ self  │ nmsu.edu │        0.00386667 │        1.10933 │ 10.123.128.1 responded in 19.11ms │
╘════╧═══════════════════════╧═══════╧══════════╧═══════════════════╧════════════════╧═══════════════════════════════════╛
TestSession: Begin ping tests
TestSession: TEST ping:: RESULTS 
╒════╤═══════════════════════╤═══════╤══════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST      │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪══════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/04-T-17:14:35 │ self  │ nmsu.edu │      17.14 │     21.256 │     15.118 │              0 │
╘════╧═══════════════════════╧═══════╧══════════╧════════════╧════════════╧════════════╧════════════════╛
TestSession: TEST ping:: RESULTS 
╒════╤═══════════════════════╤═══════╤══════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST      │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪══════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/04-T-17:14:35 │ self  │ nmsu.edu │      17.14 │     21.256 │     15.118 │              0 │
╘════╧═══════════════════════╧═══════╧══════════╧════════════╧════════════╧════════════╧════════════════╛
TestSession: TEST ping:: RESULTS 
╒════╤═══════════════════════╤═══════╤══════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST      │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪══════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/04-T-17:14:35 │ self  │ nmsu.edu │      17.14 │     21.256 │     15.118 │              0 │
╘════╧═══════════════════════╧═══════╧══════════╧════════════╧════════════╧════════════╧════════════════╛
TestSession: TEST ping:: RESULTS 
╒════╤═══════════════════════╤═══════╤══════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST      │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪══════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/04-T-17:14:35 │ self  │ nmsu.edu │      17.14 │     21.256 │     15.118 │              0 │
╘════╧═══════════════════════╧═══════╧══════════╧════════════╧════════════╧════════════╧════════════════╛
TestSession: TEST ping:: RESULTS 
╒════╤═══════════════════════╤═══════╤══════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST      │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪══════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/04-T-17:14:35 │ self  │ nmsu.edu │      17.14 │     21.256 │     15.118 │              0 │
╘════╧═══════════════════════╧═══════╧══════════╧════════════╧════════════╧════════════╧════════════════╛
net_test> 
net_test> exit
 *** Goodbye ***!
```

#### One Off Execution

```bash
python3 -m Flamegrid test route 1.1.1.1
```
