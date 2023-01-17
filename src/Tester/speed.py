import speedtest

def speed_runner():
    ''' run speedtest '''
    tester = speedtest.Speedtest()
    server = tester.get_best_server()
    tester.download()
    tester.upload()
    results_url = tester.results.share()
    results = tester.results.dict()
    rstr = "Speedtest results: {}mbps Down, {}mbps Up, {}ms Latency\nSpeedtest URL: {}".format(
            round(results['download']/1024/1024, 0),
            round(results['upload']/1024/1024,0),
            round(results['ping'],1),
            results_url
    )
    return rstr