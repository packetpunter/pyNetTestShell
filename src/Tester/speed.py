import speedtest

def speed_runner():
    ''' run speedtest '''
    tester = speedtest.Speedtest()
    server = tester.get_best_server()
    tester.download()
    tester.upload()
    results_url = tester.results.share()
    results = tester.results.dict()
    rstr = "Speedtest results: {s} {down}mbps Down, {up}mbps Up, {ping}ms Latency\nSpeedtest URL: {url}".format(
            s = server['sponsor'] + " " + server['name'] + " ",
            down = round(results['download']/1024/1024, 0),
            up = round(results['upload']/1024/1024,0),
            ping = round(results['ping'],1),
            url = results_url
    )
    return rstr
