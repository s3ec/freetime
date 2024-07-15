#!/bin/bash

searches=(    
    "how to start a career in penetration testing"
    "tips for maintaining work-life balance"
    "cybersecurity measures for a small online business"
    "pentesting methodologies and best practices"
    "healthy snacks for boosting energy"
    "prioritizing tasks effectively"
    "how to improve productivity at work"
    "best cybersecurity practices for small businesses"
    "penetration testing tools for beginners"
    "healthy breakfast ideas for busy mornings"
    "time management techniques for students"
    "protecting personal information online"
    "pentesting certifications to consider"
    "benefits of mindfulness at work"
    "cybersecurity tips for remote workers"
    "steps to conduct a successful penetration test"
    "yoga exercises for reducing stress"
    "productivity apps for organizing tasks"
    "common cybersecurity threats in 2024"
    "ways to secure personal devices from cyber attacks"
    "penetration testing in cloud environments"
    "ergonomic workspace setup for improved productivity"
    "cybersecurity hygiene for everyday internet use"
    "importance of documentation in penetration testing"
    "benefits of regular exercise on mental health"
    "productivity techniques for creative professionals"
    "cybersecurity challenges in the age of IoT"
    "pentesting ethical considerations"
    "creating a healthy meal plan for the week"
    "implementing agile practices for productivity"
    "cybersecurity implications of remote learning"
    "penetration testing case studies"
    "the impact of sleep on productivity"
    "social engineering in cybersecurity"
    "pentesting tools for network security"
    "healthy habits for a busy lifestyle"
    "utilizing technology for improved productivity"
    "cybersecurity regulations and compliance"
    "pentesting against mobile applications"
    "importance of breaks for productivity"
    "cybersecurity for personal finance management"
    "reporting findings in penetration testing"
    "mindful eating for a healthier life"
    "productivity strategies for entrepreneurs"
    "managing cybersecurity in a hybrid work environment"
    "penetration testing in industrial control systems"
    "healthy evening routines for better sleep"
    "time-blocking for productivity"
    "cybersecurity in smart home devices"
    "automating pentesting processes"
    "mental health practices in high-stress work environments"
    "cybersecurity career paths and specializations"
    "penetration testing for web applications"
    "incorporating exercise into a busy day"
    "optimizing email communication for productivity"
    "latest trends in cybersecurity threats"
    "penetration testing for e-commerce platforms"
    "promoting teamwork for improved productivity"
    "cybersecurity considerations for online gaming"
)

for ((i=0; i<${#searches[@]}; i+=3)); do
    for ((j=0; j<3 && (i+j)<${#searches[@]}; j++)); do
        search="${searches[i+j]}"
        query="${search// /%20}"
        url="https://www.bing.com/search?q=${query}&form=QBLH&sp=-1&ghc=1&lq=0&pq=ad&sc=0-2&qs=n&sk=&cvid=462DB2E033E441C89E87EF1AAD50DEDF&ghsh=0&ghacc=0&ghpl="
        echo "Searching for: ${search}"


curl --path-as-is -i -s --output /dev/null -k -X $'GET' \
    -H $'Host: www.bing.com' -H $'Cache-Control: max-age=0' -H $'Sec-Ch-Ua: \"Edge\";v=\"127\", \"Chromium\";v=\"127\", \"Not=A?Brand\";v=\"24\"' -H $'Sec-Ch-Ua-Mobile: ?1' -H $'Sec-Ch-Ua-Platform: \"Android\"' -H $'Dnt: 1' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 EdgA/127.0.0.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' -H $'X-Edge-Shopping-Flag: 0' -H $'Sec-Ms-Gec: D1A1627DFC61DBAD01138F04C88104DC6F8A970AE36B89EF78228AF6E6E38A6D' -H $'Sec-Ms-Gec-Version: 1-126.0.2592.68' -H $'Sec-Ms-Inbox-Fonts: Roboto' -H $'X-Client-Data: eyIxIjoiMCIsIjEwIjoiXCJTNUx6bE5nNUR4UEVtK1FZS0REZ0FJUStqdklQbmpENWVmZFQ2d05ZZVFRPVwiIiwiMiI6IjAiLCIzIjoiMCIsIjQiOiItMTgyOTc2NzczMjgzMTI3MDY2OSIsIjUiOiJcInV6d3lDQTVZbkR6NEFPcTgrR3B5T2g1LzBlQ2JHUWlGQjdDWjNYOEJ0cWc9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjIxMTQ4NDE4OTY1NTA1IiwiOSI6ImRlc2t0b3AifQ==' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Referer: https://www.bing.com/?scope=web&cc=IN&FORM=ANSPH1&pc=U531' -H $'Accept-Encoding: gzip, deflate, br' -H $'Accept-Language: en-US,en;q=0.9' -H $'Priority: u=0, i' \
    -b $'MUID=392F7E08D7446F962FAA6A59D6FD6E5F; MUIDB=392F7E08D7446F962FAA6A59D6FD6E5F; _EDGE_V=1; SRCHD=AF=ANSPA1; SRCHUID=V=2&GUID=CF085C0520594156A1492E4F300BF37B&dmnchg=1; MSPTC=x69y0Fa43JCI_qc6nxHjfSsbMMFyZXZi14ws50Fo3jo; mapc=rm=0; MMCASM=ID=3A605B743FCE4F7CA81727780CADBD91; MSFPC=GUID=4d7077c3ea034c7e914a19c51430f40c&HASH=4d70&LV=202403&V=4&LU=1711688707598; _UR=cdxcls=0&QS=0&TQS=0; EDGSRCHHPGUSR=CIBV=1.1670.0; MUIDB=392F7E08D7446F962FAA6A59D6FD6E5F; _TTSS_IN=isADRU=1&hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=; _tarLang=default=te; _TTSS_OUT=hist=WyJlbiIsInRlIl0=; ANIMIA=FRE=1; ANON=A=EAAA6C552E047401D6566084FFFFFFFF&E=1d95&W=1; MSCCSC=1; GC=6GgbXeG0IwTa77uebMiQvezPYTC5DY-rW04l8Ce-ZTZxMMWdndp8sXIsNpY6EE0o50dU0CFEJn613_KxGmfHRg; SRCHUSR=DOB=20240329&T=1719552749000; ABDEF=V=13&ABDV=13&MRB=0&MRNB=1719552776513; USRLOC=HS=1&ELOC=LAT=26.509096145629883|LON=80.24266052246094|N=Kanpur%2C%20Uttar%20Pradesh|ELT=6|&BID=MjQwNjI4MTEzOTQwXzYzNzdmNjQ1OWE1YzE2Yzc4ZTM3ZmUzNjg1M2ViOTgxMjkyMGQ1YzQwYWM4NzI2ZmEzNjNkZjZhYjExZmMwZmY=; _RwBf=W=0&r=0&ilt=1&ihpd=0&ispd=1&rc=9806&rb=9806&gb=0&rg=0&pc=9806&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=17&l=2024-06-27T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-06-22T22:56:51.3669448-07:00&rwflt=2024-06-27T08:06:27.2426961-07:00&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=8076&s=2023-03-16T04:22:02.6809410+00:00&ts=2024-06-28T06:09:17.8626750+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=mkGNSg88W79lUqLJorELUB2bn7Uoni8wOXVCAHlZs-R1BivlD5kRx6znJ7hc1zAPK9MF12DvFKRBbWi20Kr8rw&rwmrst=2024-06-28T11:02:30+05:30&A=EAAA6C552E047401D6566084FFFFFFFF; WLS=C=d02c411c617540ae&N=teja; _U=1-p0ylonknP4eQAEP_ZLF3lYOtUKdt2fJC6KBWgiutQVdAXbmSFD4QvTh41EpO2PgJX9wJiI42wQN3d7kFLyc2RUUU5nne9fVPbs7g_d9pCXqy-DjSJNkmrxXH-i_WXvehB9ROJV1vfQJE3Dh8E093ncLwkB0xReEm1zqdU2I08w510qJzrPpkWE9UZk6am6x9hT1O9unCAHJVFDDbCG_mA; _SS=SID=3E23E297112E61B40E40F63B10FB60EC&PC=U531; SRCHS=PC=U531; ak_bmsc=B42FFE1B6DB82E487B072C699CD9C81F~000000000000000000000000000000~YAAQPLcsMZwg1k6QAQAAS792XRiO2P9TiPgVqG3uJxrS9jIb9scYvXGBZB+UWkB5I99SejzZkk4Z+PxNdBC/GtWmNlSjsbPsy8Db1/mbRf9RBkIbvIrtrV1ET/Xwze7WMgU2GGhqjl5+riDlxrIBWdyZh5bf36A3mjqyRJc8hUu5ZXVjI0Tnyu8hKaSr3fq8PSi/D8jAizl9cvYo/Em6Hb6kWc+3Ymyd5s8t7lS17Q1UlWMiiKLmNwbSYf4x7rBsDpbHkHT6ObKqSz1LvsN9/RfmqHlXp1A29QU3MelNjvk1Yv+hrxkAujeUbq079fRbv4azC0eoLEkTg56ZeHgHTqUMHoMpeiHVcmO9PBEzTCZvujJa3hbeS2c+2ZV+EevsN759Rk0xGC1ftAOToaYwStY9Hg==; _EDGE_S=SID=3E23E297112E61B40E40F63B10FB60EC&mkt=en-in; _HPVN=CS=eyJQbiI6eyJDbiI6NzQsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjc0LCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjo3NCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNi0yOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjozMjUsIlRvYm4iOjB9; bm_sv=A82CF9A031365BB032D33EEDB43FBE43~YAAQPLcsMb8g1k6QAQAAMs52XRjjBGjCYY6VnrGimjlf8nOQpgAzPujT5cw+mGRqGD8BfpeJWnUnVgVzU8tl91rsOnK9Mlvcd3KX9p07VxKoV0gwpV8/ldmiJMQmeg8xXP7bXOYO7/akF2XAlgYjHe6eupZzKtoxOip28y/fOJ5aQt8HL2QaxfMrFh51G3f5Z5t/yVIEjMk2RXnKAdlaK4FW0Xqvxn7bnmCH5OCqLSGi/27P/O5jXMb4vZ2j/N4=~1; dsc=order=BingPages; SRCHHPGUSR=SRCHLANG=en&IG=11BC254961354451B471D939CDE36784&PV=15.0.0&BRW=MW&BRH=MM&CW=1257&CH=598&SCW=1257&SCH=598&DPR=1.5&UTC=330&DM=1&CIBV=1.1782.0&EXLTT=31&HV=1719554985&WTS=63847285498&PRVCW=1272&PRVCH=598&cdxupdttm=638476997897120621&cdxtone=Creative&cdxtoneopts=,clgalileo,clgalileonsr,dlbmtc,dlbpc4575,dlbrngnp,dlbtc,dlbuc07,dlbuf03,preclsngnp' ${url}
 sleep $(( RANDOM % 5 + 4 ))
    done
echo "Waiting for 15 minutes before the next set of searches..."
    sleep 900  # Sleep for 15 minutes
done

