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
sudo python3 -m TestShell

```
##### Sample Output
```bash
Welcome to the Network Tester Interactive v2.2.0 app to test your network!

Type ? to list commands.
 For questions, please contact the administrator who granted you this access.


net_test> set targets 1.1.1.1 4.4.4.4 reddit.com
net_test> run route ping speed
HISTORY LOGGER::: route Result 
╒════╤═══════════════════════╤════════════════════╤═════════╤═══════════════════╤════════════════╤═════════════════════════════════════╕
│    │ TS                    │ SRC                │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop                │
╞════╪═══════════════════════╪════════════════════╪═════════╪═══════════════════╪════════════════╪═════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:32:55 │ self via 10.1.10.1 │ 1.1.1.1 │          0.102231 │        1.51931 │ 71.25.197.110 responded in 20.769ms │
╘════╧═══════════════════════╧════════════════════╧═════════╧═══════════════════╧════════════════╧═════════════════════════════════════╛
HISTORY LOGGER::: route Result 
╒════╤═══════════════════════╤════════════════════╤═════════╤═══════════════════╤════════════════╤═════════════════════════════════════╕
│    │ TS                    │ SRC                │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop                │
╞════╪═══════════════════════╪════════════════════╪═════════╪═══════════════════╪════════════════╪═════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:33:39 │ self via 10.1.10.1 │ 4.4.4.4 │            0.0465 │         1.8574 │ 96.110.37.233 responded in 21.475ms │
╘════╧═══════════════════════╧════════════════════╧═════════╧═══════════════════╧════════════════╧═════════════════════════════════════╛
HISTORY LOGGER::: route Result 
╒════╤═══════════════════════╤════════════════════╤════════════╤═══════════════════╤════════════════╤════════════════════════════════════╕
│    │ TS                    │ SRC                │ DST        │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop               │
╞════╪═══════════════════════╪════════════════════╪════════════╪═══════════════════╪════════════════╪════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:33:43 │ self via 10.1.10.1 │ reddit.com │         0.0338333 │        1.56475 │ 96.110.39.110 responded in 24.46ms │
╘════╧═══════════════════════╧════════════════════╧════════════╧═══════════════════╧════════════════╧════════════════════════════════════╛
HISTORY LOGGER::: ping Result 
╒════╤═══════════════════════╤═══════╤═════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST     │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪═════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ 1.1.1.1 │     19.908 │     22.093 │     18.868 │              0 │
╘════╧═══════════════════════╧═══════╧═════════╧════════════╧════════════╧════════════╧════════════════╛
HISTORY LOGGER::: ping Result 
╒════╤═══════════════════════╤═══════╤═════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST     │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪═════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ 4.4.4.4 │          0 │          0 │          0 │              1 │
╘════╧═══════════════════════╧═══════╧═════════╧════════════╧════════════╧════════════╧════════════════╛
HISTORY LOGGER::: ping Result 
╒════╤═══════════════════════╤═══════╤════════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST        │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪════════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ reddit.com │     19.547 │     24.884 │     18.315 │              0 │
╘════╧═══════════════════════╧═══════╧════════════╧════════════╧════════════╧════════════╧════════════════╛
HISTORY LOGGER::: speed Result 
╒════╤═══════════════════════╤═══════╤══════════════════════╤══════════════╤════════════╤═════════════════╤═════════════════════════════════════════════════╕
│    │ TS                    │ SRC   │ DST                  │ Speed_Down   │ Speed_Up   │ Speed_Latency   │ Speed_URL                                       │
╞════╪═══════════════════════╪═══════╪══════════════════════╪══════════════╪════════════╪═════════════════╪═════════════════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ NextLight Denver, CO │ 649.0 Mbps   │ 26.0 Mbps  │ 23.9 ms         │ http://www.speedtest.net/result/15364450453.png │
╘════╧═══════════════════════╧═══════╧══════════════════════╧══════════════╧════════════╧═════════════════╧═════════════════════════════════════════════════╛
net_test> exit
 *** Goodbye ***!
```

#### One Off Execution

```bash
python3 -m Flamegrid test route 1.1.1.1
```

#### Sample Log File
```bash
╘════╧═══════════════════════╧═══════╧══════════════════════╧══════════════╧════════════╧═════════════════╧═════════════════════════════════════════════════╛
2023/10/11 12:32|  route Result 
╒════╤═══════════════════════╤════════════════════╤═════════╤═══════════════════╤════════════════╤═════════════════════════════════════╕
│    │ TS                    │ SRC                │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop                │
╞════╪═══════════════════════╪════════════════════╪═════════╪═══════════════════╪════════════════╪═════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:32:55 │ self via 10.1.10.1 │ 1.1.1.1 │          0.102231 │        1.51931 │ 71.25.197.110 responded in 20.769ms │
╘════╧═══════════════════════╧════════════════════╧═════════╧═══════════════════╧════════════════╧═════════════════════════════════════╛
2023/10/11 12:32|  route Result 
╒════╤═══════════════════════╤════════════════════╤═════════╤═══════════════════╤════════════════╤═════════════════════════════════════╕
│    │ TS                    │ SRC                │ DST     │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop                │
╞════╪═══════════════════════╪════════════════════╪═════════╪═══════════════════╪════════════════╪═════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:33:39 │ self via 10.1.10.1 │ 4.4.4.4 │            0.0465 │         1.8574 │ 96.110.37.233 responded in 21.475ms │
╘════╧═══════════════════════╧════════════════════╧═════════╧═══════════════════╧════════════════╧═════════════════════════════════════╛
2023/10/11 12:32|  route Result 
╒════╤═══════════════════════╤════════════════════╤════════════╤═══════════════════╤════════════════╤════════════════════════════════════╕
│    │ TS                    │ SRC                │ DST        │   Route_AvgJitter │   Route_AvgRtt │ Route_HighestLossHop               │
╞════╪═══════════════════════╪════════════════════╪════════════╪═══════════════════╪════════════════╪════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:33:43 │ self via 10.1.10.1 │ reddit.com │         0.0338333 │        1.56475 │ 96.110.39.110 responded in 24.46ms │
╘════╧═══════════════════════╧════════════════════╧════════════╧═══════════════════╧════════════════╧════════════════════════════════════╛
2023/10/11 12:33|  ping Result 
╒════╤═══════════════════════╤═══════╤═════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST     │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪═════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ 1.1.1.1 │     19.908 │     22.093 │     18.868 │              0 │
╘════╧═══════════════════════╧═══════╧═════════╧════════════╧════════════╧════════════╧════════════════╛
2023/10/11 12:33|  ping Result 
╒════╤═══════════════════════╤═══════╤═════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST     │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪═════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ 4.4.4.4 │          0 │          0 │          0 │              1 │
╘════╧═══════════════════════╧═══════╧═════════╧════════════╧════════════╧════════════╧════════════════╛
2023/10/11 12:33|  ping Result 
╒════╤═══════════════════════╤═══════╤════════════╤════════════╤════════════╤════════════╤════════════════╕
│    │ TS                    │ SRC   │ DST        │   Ping_Avg │   Ping_Max │   Ping_Min │   Ping_PctLoss │
╞════╪═══════════════════════╪═══════╪════════════╪════════════╪════════════╪════════════╪════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ reddit.com │     19.547 │     24.884 │     18.315 │              0 │
╘════╧═══════════════════════╧═══════╧════════════╧════════════╧════════════╧════════════╧════════════════╛
2023/10/11 12:34|  speed Result 
╒════╤═══════════════════════╤═══════╤══════════════════════╤══════════════╤════════════╤═════════════════╤═════════════════════════════════════════════════╕
│    │ TS                    │ SRC   │ DST                  │ Speed_Down   │ Speed_Up   │ Speed_Latency   │ Speed_URL                                       │
╞════╪═══════════════════════╪═══════╪══════════════════════╪══════════════╪════════════╪═════════════════╪═════════════════════════════════════════════════╡
│ TS │ 2023/10/11-T-12:34:30 │ self  │ NextLight Denver, CO │ 649.0 Mbps   │ 26.0 Mbps  │ 23.9 ms         │ http://www.speedtest.net/result/15364450453.png │
╘════╧═══════════════════════╧═══════╧══════════════════════╧══════════════╧════════════╧═════════════════╧═════════════════════════════════════════════════╛
```