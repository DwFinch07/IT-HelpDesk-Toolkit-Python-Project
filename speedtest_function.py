import speedtest
class Speed_test():
    def test_speed():
        s = speedtest.Speedtest()
        s.download()
        s.upload()
        results = s.results.dict()
        #print(f"Download: {results['download']/1_000_000:.2f} Mbps\nUpload: {results['upload']/1_000_000:.2f} Mbps")
        return f"Download: {results['download']/1_000_000:.2f} Mbps\nUpload: {results['upload']/1_000_000:.2f} Mbps"
