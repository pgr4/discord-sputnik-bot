from ytmusicapi import YTMusic

headers = '''accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
authorization: SAPISIDHASH 1668834631_c0a546aab97c744c13c6126af6737c65334cdcdc
content-length: 2096
content-type: application/json
cookie: VISITOR_INFO1_LIVE=_E71lbmhxOc; HSID=AsU_ebzJmnxX7kkFk; SSID=AeT7UYq8B25FXS3LB; APISID=HY0t-GU2Bwzgng5L/AiU8HNdEaKskUgY0-; SAPISID=-Ewyv_DEZBgpywXo/AAfqUyXt1UsYzAEQJ; __Secure-1PAPISID=-Ewyv_DEZBgpywXo/AAfqUyXt1UsYzAEQJ; __Secure-3PAPISID=-Ewyv_DEZBgpywXo/AAfqUyXt1UsYzAEQJ; LOGIN_INFO=AFmmF2swRAIgCHihrcBviwA0EMdzBRbe0eqdTwJzuQI4hJNFSLa1JZgCIC0TXxVUDp01NLebp8iTA9XLhNz-cnkKIL9ysYag23Kt:QUQ3MjNmeDN6bG9rVmtJUlBpVTRaSmk2VFZfTDV0N0JOSjRVcURFVG84czRxNEc4aFFNNkEzM18tSzVXX3JpR0RhdnMwYzZyMXV4RjVWVGM2NWp6dUJmWXFWLXVXWW9KUmFaVmNUbkZ5ZG5VOV9LeXl3c3NxT1c4XzdRb2FmdFRFWDZCT3VpN2RXNC1pQm5BUXNMVWMzV2J2aWx4SDhPTkZR; YT_CL={"loctok":"AKhgDTPQ9v-sI-C6C7JOQt1jKnO8n_FIbyI-NcKyL6hTDg5h2BaBMUDaGqcJcNZ5-chJeoUoirq3-fKTHUvI_E5wTcsBjg"}; SID=QAh7eCKGuVaJYA705lskpgAGoh82G8QKdsU3FXLRlKK2c8zMDY40BwwtU38UXhhWq9CaeA.; __Secure-1PSID=QAh7eCKGuVaJYA705lskpgAGoh82G8QKdsU3FXLRlKK2c8zMKdcAcQvH8EDCx7dt-G3WIQ.; __Secure-3PSID=QAh7eCKGuVaJYA705lskpgAGoh82G8QKdsU3FXLRlKK2c8zMIO9gx0BdMgRLuUoCdbN7Fw.; PREF=tz=UTC&f6=40000000&f5=30000&f7=100; YSC=O39mNBa2aMo; wide=1; SIDCC=AIKkIs0Qk0wNHMDKx5k-lEdcdXqG6oisxSAmtagMtU8lMn97nMGiJx9UlrkeVHKHjhmv52mP5hlN; __Secure-1PSIDCC=AIKkIs2CZpC_Zl42R-cxPYBEptnKqo5fZ83SsszDa6dwi67Dpogpc-hTF_8jY0E--SD3xyyMrf8; __Secure-3PSIDCC=AIKkIs3XnfsSQwO0MwFJn_1ApgoiVW_EVI8CDquQ8NNdB0wEPwg3YkDxFurN8XEvY3ppR5nTB-k
origin: https://music.youtube.com
referer: https://music.youtube.com/
sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-arch: "x86"
sec-ch-ua-bitness: "64"
sec-ch-ua-full-version: "107.0.5304.107"
sec-ch-ua-full-version-list: "Google Chrome";v="107.0.5304.107", "Chromium";v="107.0.5304.107", "Not=A?Brand";v="24.0.0.0"
sec-ch-ua-mobile: ?0
sec-ch-ua-model
sec-ch-ua-platform: "Windows"
sec-ch-ua-platform-version: "10.0.0"
sec-ch-ua-wow64: ?0
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
x-client-data: CJW2yQEIpLbJAQjEtskBCKmdygEIn+nKAQiTocsBCPyqzAEIwbzMAQjTvMwBCMbhzAEI+ujMAQji68wBCP7tzAEI9fHMAQic88wBCKHzzAEIjffMAQiY98wBCJD4zAE=
Decoded:
message ClientVariations {
  // Active client experiment variation IDs.
  repeated int32 variation_id = [3300117, 3300132, 3300164, 3313321, 3323039, 3330195, 3347836, 3350081, 3350099, 3354822, 3355770, 3356130, 3356414, 3356917, 3357084, 3357089, 3357581, 3357592, 3357712];
}
x-goog-authuser: 0
x-goog-visitor-id: CgtfRTcxbGJtaHhPYyjEyuGbBg%3D%3D
x-origin: https://music.youtube.com
x-youtube-client-name: 67
x-youtube-client-version: 1.20221114.01.00
'''

yt = YTMusic()
idk = yt.setup(filepath='headers_auth.json', headers_raw=headers)
    
def get_album_info(album_name: str):
    search_results = YTMusic.search(yt, query=album_name, filter='albums', ignore_spelling="")
    ret = search_results[0]
    return ret

