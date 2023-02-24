import speedtest

def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000 # convert to megabits
    upload_speed = st.upload() / 1000000 # convert to megabits
    return download_speed, upload_speed

if __name__ == '__main__':
    download_speed, upload_speed = test_speed()
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
