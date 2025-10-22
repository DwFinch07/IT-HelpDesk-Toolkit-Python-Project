import os
def test_ping():

    hostname = "google.com"
    response = os.system("ping " + hostname)
    if response == 1:
        ping_stats = "Network Active"
    else:
        ping_stats = "Network Failed"
    return ping_stats
if __name__ == "__main__":
    print(test_ping())