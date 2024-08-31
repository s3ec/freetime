import time

# Wait for 10,800 seconds (3 hours)
time.sleep(10800)

# Print the message
print("Searching is going to start")


import requests
import time
import random


cookies = {
    'MUID': '09FD4A46F67D695C27C65EF8F79968B3',
    'MUIDB': '09FD4A46F67D695C27C65EF8F79968B3',
    '_EDGE_V': '1',
    'SRCHD': 'AF=NOFORM',
    'SRCHUID': 'V=2&GUID=B0C3D5194A2749DE99B9FB549361A06B&dmnchg=1',
    'ANON': 'A=D8003EBF03381FA3F87B4289FFFFFFFF&E=1e02&W=1',
    'NAP': 'V=1.9&E=1da8&C=a2ywj3KUY4BrtikO75Yj77hJ07l8MbnCKDd_b5pNdeDsH60S_6Mr7w&W=1',
    'PPLState': '1',
    'KievRPSSecAuth': 'FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACCIDfOUoriwhCARIa7E5mRzbZG/Vk+oZwmLH1idd0V4CD8ws3MHAh3snZtcIT9gHbEyO36okUmpctkJSeJlVjpP4xjPExY9MmSKizT39vk9souE/qwAPgV11XfbWqKXmYnwQsZLOoyQM0KnsOQ0DBWwhmFg2TVQex5Ojf2s8id/1EHpYS5EXv0fznp/xGOERehpCTRwotj5t9bvjXFYA7SWfAL5DffAf6kbQ+0OnlAV/a/o1w0cnYcsEY8eNrv3HuQ6jJ8C2sO3K8c4SIplMMDEh4BbeO2fvVMifC7EzFOvBfPLshrrZuEUxyGDZHshvCVisN/jhLS8H12mN1km1bXVDOPrEHe7Feit/VDBdq+7U9MWT//i9fubkGUKVtKvERnhNCVEuUvLyGKnrF/fmRHVAhLTUNlBaQDtIyLbzEpi2tdS+YPLfRP/OcAw+E1ApLanChCm2eYRthHhfTgb9oLGZ39ENCUd7/bAkWEckp4wjaiIGwKAbdDlraU4AFCgOYZJh1bb7MSaOnTzAMHsXdZ0XRxN1VcTi60OqhGcZNKc/RRFM+I1JZBolNIdmqe8+kC7Sk5PsS+oFL8CjK8mGrjGpuu7b2abYCSCPmDvJEp38i6N3RK/Q2fwZ22wwpgfcHQG1sznFX5FoNrDly1Fjod6QMQjgJF+G+I+D8/78oGN5Y5SAUN/kdImn8k9FGnTAgAWt5ZxgbXJPCfS9eAalITiik7HQBJsdzSc7YW6Mh/xNF/2e+jklOoZJVoNoD6t59uElH2/mxsBBUqF63/WiLDEcurMx7Gy44V5a3jJk1mPn7d1RK4Yqvq2EBM+qY+5PC57YJ9tEfc07d30YDwcKPo+gjcfHhQeoRn0whNgCbIzaPQUUbIWvmhYnBZcOKjP0ZHbE9mB9jmaPTPUAAANzahgvKCUZSHFCJaeXbheKN+yk3QLwPCSfCv0kixH5hz6kUEPE99bAffAMNx3LvCb1JIfbCFyxbIP6OpezBjahebVn1zNVKXxyCzW45c+7RLQtxF6UZsziroYd8Q9gWK24m/IkaSVerrHIlArHNP5YIPxMO/hgYN/EDtURf7x+h7ssbCCfYpGX5hpC0iod2y0QLSCaLS8EvxoRcYl/5HqzlUVb59uNpPXjMbR0arIXKBe0RYb3APwWc+4CVAD43xqDsHoDk/quowiewY5MQbf61sSz/QPFqlaDL3hTyBxOlksw9xYPtB/N2/1MWuIfKkcdn0cT6weyNbw+BDSgjOvKMh6zjpyjB+pUZT1AN2cBZmmHzoIp4ThK1LvAGF6mL7RvmKYfRW9QoDqr7QcfD/p11IWY2NfSkXx0dA3Uzahuq+Qh633KkvqAFBfL2uDFrjaoGLocbULl60uC/nMRxHBZJ+fYIIAUAPeAVRvJLNlYPCHrNxNgZqXxicaW',
    '_U': '1rbAVr8sLsmVInZ5HYbgIsoi-E8WnZTsCBNrwMdXE7yGLPLaSMqHraUiPRm50uFLuSTMBktlKCYLkUxINJk0DOWnbqk0VNgmZTTQg1_h6fHilzG7xGRPSg533jtw6q0wshGYxVhSYNYrhr2soRcVv7cvvws8C4dNC5fflhp9gOD08cXTrSXlO4O4KO_5YEUWaganJ3tnwBUetWbqK8Fay2w',
    'WLID': 'B7daODAET9JR0nI5fET8NUkszflcmNdeflAGo6cybanhyGsGTA3RAYFHwO/NQ/GxhXkmn3fsVKpzM/BcGkR9X8f43w3AaJ0Ar3fa0XKQyN0=',
    'MUIDB': '09FD4A46F67D695C27C65EF8F79968B3',
    'MSPTC': '-8_3oD3FK0fFFkUW4a8phFWxRJJvdoQm7j1zzGGE_LE',
    '_RwBf': 'r=0&ilt=1&ihpd=1&ispd=0&rc=5292&rb=5292&gb=0&rg=0&pc=5275&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=3&l=2024-07-26T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-07-26T23:27:47.9738531-07:00&rwflt=2024-07-19T21:58:22.1944447-07:00&o=0&p=BINGTRIAL5TO250P201808&c=ML1OVB&t=1641&s=2023-11-10T13:16:19.7240052+00:00&ts=2024-07-27T06:27:55.9343390+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=bZ7heD3SjnHREyo3WP7mYJJT6Ih9GxFAU2R4QC4aHn2rfUcfnzpOpyStTTFfztZ83gRBUREjewxtlpnw-pP1Z2SFBK1IcCnMYWG8cv022SY&A=',
    '_uetvid': '586c81a0437e11ef854f4518d60098dd',
    'MSCC': 'NR',
    'WLS': 'C=82b022bcb40fdc2b&N=ck',
    '_SS': 'SID=27565F24EFF861540C4E4BEEEE44602F',
    'ak_bmsc': 'FCA7546EFF2D1AFAE502F43DB7CC20BE~000000000000000000000000000000~YAAQPCEPF3GAILyQAQAAj8il+Rj2//NpmCynst4ObDo9r1qqEuynWDgE+xHd2a6HwKCMHsJVaE1Jpi5XIAj1SCgm/1iWdwQxSHoR35fhvT5wW8lIDaYPSd4AmM0+75ZP9FbpIG6Z9ECmDyATxNXg/0vbQ0aMr9d9xUCMVlKXS2qR8NVnesd5SjkElJuuUs+ewFvDcLEW541Uzuf7Rpcffor4tK+76b8XnOSbs462U5Q0cCZrthamtEBpJs+PR/W6WG2y6NhouG02s8RLm0EF/DCWrqPSx/Mz1LJe39huXGl/JK5jVA81zmh8g76xxnhqyiXLvsuW3LeHqge40JDO9r5ApcZ6HwaEBKorCY83Prqp1wUZVBzdMnCzL7rm7YEF3Q8B+Wi+/Q==',
    'BCP': 'AD=0&AL=0&SM=0',
    '_UR': 'QS=0&TQS=0',
    '_HPVN': 'CS=eyJQbiI6eyJDbiI6NSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6NSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6NSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNy0yOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyMiwiVG9ibiI6MH0=',
    '_EDGE_S': 'SID=27565F24EFF861540C4E4BEEEE44602F&mkt=en-in',
    'SRCHUSR': 'DOB=20240716&T=1722175316000&POEX=W&TPC=1722061677000',
    '_C_ETH': '1',
    'bm_sv': '53E32E4D1D1F615B73BE82DFDECF4A4D~YAAQtI0sMfvcjeKQAQAADuCm+RhgoLSblyB5iOj/VnoB30Qh4EcNTrU9mgzD6waZQbzkpZpvW0X72NjCi1oLNhFXmR6jDWm+CFFnnQPMVBTZYa7C+1lbRu4f+TRD4+xLILZis1neznQ8tDjUKHNqBvtsz7TKQ2fvupq2ajtvR+gBqfUcA0D/fbWs09S2RX/vC48XkhyiSFapwnCkOG0ItlY+9ClyqPVZuvB1z7EKYAHM63/9SQage0oE06Gtkw==~1',
    'USRLOC': 'HS=1&ELOC=LAT=26.507747650146484|LON=80.23416137695312|N=Kanpur%2C%20Uttar%20Pradesh|ELT=4|',
    'dsc': 'order=Images',
    'SRCHHPGUSR': 'SRCHLANG=en&IG=0C698195B54440B1AA1B70C76FC71216&PV=15.0.0&BRW=MW&BRH=MM&CW=1263&CH=591&SCW=1263&SCH=591&DPR=1.5&UTC=330&DM=1&CIBV=1.1794.0&EXLTT=3&HV=1722175390&PRVCW=1263&PRVCH=591',
}

headers = {
    'Host': 'www.bing.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="127", "Edge";v="127"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 EdgA/127.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Sec-Gpc': '1',
    'Accept-Language': 'en-US,en;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.bing.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=0, i',
    # 'Cookie': 'MUID=09FD4A46F67D695C27C65EF8F79968B3; MUIDB=09FD4A46F67D695C27C65EF8F79968B3; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=B0C3D5194A2749DE99B9FB549361A06B&dmnchg=1; ANON=A=D8003EBF03381FA3F87B4289FFFFFFFF&E=1e02&W=1; NAP=V=1.9&E=1da8&C=a2ywj3KUY4BrtikO75Yj77hJ07l8MbnCKDd_b5pNdeDsH60S_6Mr7w&W=1; PPLState=1; KievRPSSecAuth=FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACCIDfOUoriwhCARIa7E5mRzbZG/Vk+oZwmLH1idd0V4CD8ws3MHAh3snZtcIT9gHbEyO36okUmpctkJSeJlVjpP4xjPExY9MmSKizT39vk9souE/qwAPgV11XfbWqKXmYnwQsZLOoyQM0KnsOQ0DBWwhmFg2TVQex5Ojf2s8id/1EHpYS5EXv0fznp/xGOERehpCTRwotj5t9bvjXFYA7SWfAL5DffAf6kbQ+0OnlAV/a/o1w0cnYcsEY8eNrv3HuQ6jJ8C2sO3K8c4SIplMMDEh4BbeO2fvVMifC7EzFOvBfPLshrrZuEUxyGDZHshvCVisN/jhLS8H12mN1km1bXVDOPrEHe7Feit/VDBdq+7U9MWT//i9fubkGUKVtKvERnhNCVEuUvLyGKnrF/fmRHVAhLTUNlBaQDtIyLbzEpi2tdS+YPLfRP/OcAw+E1ApLanChCm2eYRthHhfTgb9oLGZ39ENCUd7/bAkWEckp4wjaiIGwKAbdDlraU4AFCgOYZJh1bb7MSaOnTzAMHsXdZ0XRxN1VcTi60OqhGcZNKc/RRFM+I1JZBolNIdmqe8+kC7Sk5PsS+oFL8CjK8mGrjGpuu7b2abYCSCPmDvJEp38i6N3RK/Q2fwZ22wwpgfcHQG1sznFX5FoNrDly1Fjod6QMQjgJF+G+I+D8/78oGN5Y5SAUN/kdImn8k9FGnTAgAWt5ZxgbXJPCfS9eAalITiik7HQBJsdzSc7YW6Mh/xNF/2e+jklOoZJVoNoD6t59uElH2/mxsBBUqF63/WiLDEcurMx7Gy44V5a3jJk1mPn7d1RK4Yqvq2EBM+qY+5PC57YJ9tEfc07d30YDwcKPo+gjcfHhQeoRn0whNgCbIzaPQUUbIWvmhYnBZcOKjP0ZHbE9mB9jmaPTPUAAANzahgvKCUZSHFCJaeXbheKN+yk3QLwPCSfCv0kixH5hz6kUEPE99bAffAMNx3LvCb1JIfbCFyxbIP6OpezBjahebVn1zNVKXxyCzW45c+7RLQtxF6UZsziroYd8Q9gWK24m/IkaSVerrHIlArHNP5YIPxMO/hgYN/EDtURf7x+h7ssbCCfYpGX5hpC0iod2y0QLSCaLS8EvxoRcYl/5HqzlUVb59uNpPXjMbR0arIXKBe0RYb3APwWc+4CVAD43xqDsHoDk/quowiewY5MQbf61sSz/QPFqlaDL3hTyBxOlksw9xYPtB/N2/1MWuIfKkcdn0cT6weyNbw+BDSgjOvKMh6zjpyjB+pUZT1AN2cBZmmHzoIp4ThK1LvAGF6mL7RvmKYfRW9QoDqr7QcfD/p11IWY2NfSkXx0dA3Uzahuq+Qh633KkvqAFBfL2uDFrjaoGLocbULl60uC/nMRxHBZJ+fYIIAUAPeAVRvJLNlYPCHrNxNgZqXxicaW; _U=1rbAVr8sLsmVInZ5HYbgIsoi-E8WnZTsCBNrwMdXE7yGLPLaSMqHraUiPRm50uFLuSTMBktlKCYLkUxINJk0DOWnbqk0VNgmZTTQg1_h6fHilzG7xGRPSg533jtw6q0wshGYxVhSYNYrhr2soRcVv7cvvws8C4dNC5fflhp9gOD08cXTrSXlO4O4KO_5YEUWaganJ3tnwBUetWbqK8Fay2w; WLID=B7daODAET9JR0nI5fET8NUkszflcmNdeflAGo6cybanhyGsGTA3RAYFHwO/NQ/GxhXkmn3fsVKpzM/BcGkR9X8f43w3AaJ0Ar3fa0XKQyN0=; MUIDB=09FD4A46F67D695C27C65EF8F79968B3; MSPTC=-8_3oD3FK0fFFkUW4a8phFWxRJJvdoQm7j1zzGGE_LE; _RwBf=r=0&ilt=1&ihpd=1&ispd=0&rc=5292&rb=5292&gb=0&rg=0&pc=5275&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=3&l=2024-07-26T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-07-26T23:27:47.9738531-07:00&rwflt=2024-07-19T21:58:22.1944447-07:00&o=0&p=BINGTRIAL5TO250P201808&c=ML1OVB&t=1641&s=2023-11-10T13:16:19.7240052+00:00&ts=2024-07-27T06:27:55.9343390+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=bZ7heD3SjnHREyo3WP7mYJJT6Ih9GxFAU2R4QC4aHn2rfUcfnzpOpyStTTFfztZ83gRBUREjewxtlpnw-pP1Z2SFBK1IcCnMYWG8cv022SY&A=; _uetvid=586c81a0437e11ef854f4518d60098dd; MSCC=NR; WLS=C=82b022bcb40fdc2b&N=ck; _SS=SID=27565F24EFF861540C4E4BEEEE44602F; ak_bmsc=FCA7546EFF2D1AFAE502F43DB7CC20BE~000000000000000000000000000000~YAAQPCEPF3GAILyQAQAAj8il+Rj2//NpmCynst4ObDo9r1qqEuynWDgE+xHd2a6HwKCMHsJVaE1Jpi5XIAj1SCgm/1iWdwQxSHoR35fhvT5wW8lIDaYPSd4AmM0+75ZP9FbpIG6Z9ECmDyATxNXg/0vbQ0aMr9d9xUCMVlKXS2qR8NVnesd5SjkElJuuUs+ewFvDcLEW541Uzuf7Rpcffor4tK+76b8XnOSbs462U5Q0cCZrthamtEBpJs+PR/W6WG2y6NhouG02s8RLm0EF/DCWrqPSx/Mz1LJe39huXGl/JK5jVA81zmh8g76xxnhqyiXLvsuW3LeHqge40JDO9r5ApcZ6HwaEBKorCY83Prqp1wUZVBzdMnCzL7rm7YEF3Q8B+Wi+/Q==; BCP=AD=0&AL=0&SM=0; _UR=QS=0&TQS=0; _HPVN=CS=eyJQbiI6eyJDbiI6NSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6NSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6NSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNy0yOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyMiwiVG9ibiI6MH0=; _EDGE_S=SID=27565F24EFF861540C4E4BEEEE44602F&mkt=en-in; SRCHUSR=DOB=20240716&T=1722175316000&POEX=W&TPC=1722061677000; _C_ETH=1; bm_sv=53E32E4D1D1F615B73BE82DFDECF4A4D~YAAQtI0sMfvcjeKQAQAADuCm+RhgoLSblyB5iOj/VnoB30Qh4EcNTrU9mgzD6waZQbzkpZpvW0X72NjCi1oLNhFXmR6jDWm+CFFnnQPMVBTZYa7C+1lbRu4f+TRD4+xLILZis1neznQ8tDjUKHNqBvtsz7TKQ2fvupq2ajtvR+gBqfUcA0D/fbWs09S2RX/vC48XkhyiSFapwnCkOG0ItlY+9ClyqPVZuvB1z7EKYAHM63/9SQage0oE06Gtkw==~1; USRLOC=HS=1&ELOC=LAT=26.507747650146484|LON=80.23416137695312|N=Kanpur%2C%20Uttar%20Pradesh|ELT=4|; dsc=order=Images; SRCHHPGUSR=SRCHLANG=en&IG=0C698195B54440B1AA1B70C76FC71216&PV=15.0.0&BRW=MW&BRH=MM&CW=1263&CH=591&SCW=1263&SCH=591&DPR=1.5&UTC=330&DM=1&CIBV=1.1794.0&EXLTT=3&HV=1722175390&PRVCW=1263&PRVCH=591',
}





search_queries = [
    'cybersecurity skills in demand for remote jobs',
    'remote jobs for CPENT certified professionals',
    'best remote jobs for application security engineers',
    'freelance cybersecurity job opportunities',
    'remote job search tips for cybersecurity professionals',
    'how to find remote jobs in API security',
    'remote jobs for security analysts',
    'top remote jobs for cybersecurity consultants',
    'how to build a remote career in Web3 security',
    'trending skills for remote cybersecurity jobs',
    'best remote jobs for vulnerability analysts',
    'remote jobs for security architects',
    'best remote jobs in cybersecurity',
    'top remote job websites for tech professionals',
    'trending cybersecurity skills in 2024',
    'how to find remote penetration testing jobs',
    'remote jobs for application security experts',
    'top paying remote jobs in IT',
    'best certifications for remote cybersecurity jobs',
    'work from home opportunities for network security professionals',
    'API security remote job listings',
    'remote jobs for certified ethical hackers',
    'how to start a remote career in cybersecurity',
    'freelance platforms for cybersecurity experts',
    'remote job trends in cybersecurity',
    'best remote jobs for CEH certified professionals',
    'job boards for remote security engineer positions',
    'top skills for remote cybersecurity analysts',
    'how to negotiate salary for remote cybersecurity jobs',
    'remote cybersecurity internships',
    'remote jobs for Web3 security specialists',
    'best remote jobs for threat detection experts',
    'remote work opportunities in information security',
    'top remote jobs for LPT Master certified professionals',
    'how to transition to remote work in cybersecurity',
    'how to get remote cybersecurity contracts'
]



# Perform searches with delay and longer breaks
for index, query in enumerate(search_queries, start=1):
    params = {
        'q': query,
        'PC': 'U316',
        'FORM': 'CHROMN',
    }

    response = requests.get('https://www.bing.com/search', params=params, cookies=cookies, headers=headers)
    
    # Process the response as needed (currently no printing)
    # You can store results in a list or perform any other processing
    
    # Introduce a random delay between 4 to 8 seconds
    time.sleep(random.uniform(4, 8))
    
    # Check if we have completed 3 searches
    if index % 3 == 0:
        # Wait for 15 minutes (900 seconds)
        print(f"Completed {index} searches. Waiting for 15 minutes...")
        time.sleep(900)  # 15 minutes
        
        
        
import requests
import time
import random

cookies = {
    'MUID': '09FD4A46F67D695C27C65EF8F79968B3',
    'MUIDB': '09FD4A46F67D695C27C65EF8F79968B3',
    '_EDGE_V': '1',
    'SRCHD': 'AF=NOFORM',
    'SRCHUID': 'V=2&GUID=B0C3D5194A2749DE99B9FB549361A06B&dmnchg=1',
    'ak_bmsc': '02B703E431DABD2BF80E60A81F7D00FE~000000000000000000000000000000~YAAQ3gVaaPT+8rWQAQAAk8rmuxgGoKxVSNMMJiknpqqEQq7pfiJ9Gu4l6FcMHaO0f1wi4U+ByUtUiaKkv8J6VNcp0fAiOUl2IINHoOZpn8SFBmLTiDbmUB2PyowtUCJ3cvVTfh6zKCBkYm7T+imz8jO75p8zKeiGOzR025QuYNVYl/keepWSYo6sI8OCPST/aBtLeVNTlVLAADuEu+ZxfaVC8hJMSy6IRVehi/fKnJoNhyVKheaBqPl5cTVzO+CEChVsZZkMxElqnBY8ywIN14Qjw2+XJZsR7D6QzJR5H/naNVpdL8wduAUvUX7rJVrZgNs4jdxdVsZwGnpLJXFy4JKC16Wp9Cgf4vltaC9EylOAunCiye1KiapGFbHU4Kkjv561JjEKYQ==',
    'BCP': 'AD=0&AL=0&SM=0',
    '_UR': 'cdxcls=0&QS=0&TQS=0',
    '_Rwho': 'u=d&ts=2024-07-16',
    'CSRFCookie': 'f23c4029-b438-4c4b-9a12-34a5ecf1e812',
    'ANON': 'A=D8003EBF03381FA3F87B4289FFFFFFFF&E=1e02&W=1',
    'NAP': 'V=1.9&E=1da8&C=a2ywj3KUY4BrtikO75Yj77hJ07l8MbnCKDd_b5pNdeDsH60S_6Mr7w&W=1',
    'PPLState': '1',
    'KievRPSSecAuth': 'FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACCIDfOUoriwhCARIa7E5mRzbZG/Vk+oZwmLH1idd0V4CD8ws3MHAh3snZtcIT9gHbEyO36okUmpctkJSeJlVjpP4xjPExY9MmSKizT39vk9souE/qwAPgV11XfbWqKXmYnwQsZLOoyQM0KnsOQ0DBWwhmFg2TVQex5Ojf2s8id/1EHpYS5EXv0fznp/xGOERehpCTRwotj5t9bvjXFYA7SWfAL5DffAf6kbQ+0OnlAV/a/o1w0cnYcsEY8eNrv3HuQ6jJ8C2sO3K8c4SIplMMDEh4BbeO2fvVMifC7EzFOvBfPLshrrZuEUxyGDZHshvCVisN/jhLS8H12mN1km1bXVDOPrEHe7Feit/VDBdq+7U9MWT//i9fubkGUKVtKvERnhNCVEuUvLyGKnrF/fmRHVAhLTUNlBaQDtIyLbzEpi2tdS+YPLfRP/OcAw+E1ApLanChCm2eYRthHhfTgb9oLGZ39ENCUd7/bAkWEckp4wjaiIGwKAbdDlraU4AFCgOYZJh1bb7MSaOnTzAMHsXdZ0XRxN1VcTi60OqhGcZNKc/RRFM+I1JZBolNIdmqe8+kC7Sk5PsS+oFL8CjK8mGrjGpuu7b2abYCSCPmDvJEp38i6N3RK/Q2fwZ22wwpgfcHQG1sznFX5FoNrDly1Fjod6QMQjgJF+G+I+D8/78oGN5Y5SAUN/kdImn8k9FGnTAgAWt5ZxgbXJPCfS9eAalITiik7HQBJsdzSc7YW6Mh/xNF/2e+jklOoZJVoNoD6t59uElH2/mxsBBUqF63/WiLDEcurMx7Gy44V5a3jJk1mPn7d1RK4Yqvq2EBM+qY+5PC57YJ9tEfc07d30YDwcKPo+gjcfHhQeoRn0whNgCbIzaPQUUbIWvmhYnBZcOKjP0ZHbE9mB9jmaPTPUAAANzahgvKCUZSHFCJaeXbheKN+yk3QLwPCSfCv0kixH5hz6kUEPE99bAffAMNx3LvCb1JIfbCFyxbIP6OpezBjahebVn1zNVKXxyCzW45c+7RLQtxF6UZsziroYd8Q9gWK24m/IkaSVerrHIlArHNP5YIPxMO/hgYN/EDtURf7x+h7ssbCCfYpGX5hpC0iod2y0QLSCaLS8EvxoRcYl/5HqzlUVb59uNpPXjMbR0arIXKBe0RYb3APwWc+4CVAD43xqDsHoDk/quowiewY5MQbf61sSz/QPFqlaDL3hTyBxOlksw9xYPtB/N2/1MWuIfKkcdn0cT6weyNbw+BDSgjOvKMh6zjpyjB+pUZT1AN2cBZmmHzoIp4ThK1LvAGF6mL7RvmKYfRW9QoDqr7QcfD/p11IWY2NfSkXx0dA3Uzahuq+Qh633KkvqAFBfL2uDFrjaoGLocbULl60uC/nMRxHBZJ+fYIIAUAPeAVRvJLNlYPCHrNxNgZqXxicaW',
    '_U': '1rbAVr8sLsmVInZ5HYbgIsoi-E8WnZTsCBNrwMdXE7yGLPLaSMqHraUiPRm50uFLuSTMBktlKCYLkUxINJk0DOWnbqk0VNgmZTTQg1_h6fHilzG7xGRPSg533jtw6q0wshGYxVhSYNYrhr2soRcVv7cvvws8C4dNC5fflhp9gOD08cXTrSXlO4O4KO_5YEUWaganJ3tnwBUetWbqK8Fay2w',
    'WLS': 'C=82b022bcb40fdc2b&N=ck',
    'WLID': 'B7daODAET9JR0nI5fET8NUkszflcmNdeflAGo6cybanhyGsGTA3RAYFHwO/NQ/GxhXkmn3fsVKpzM/BcGkR9X8f43w3AaJ0Ar3fa0XKQyN0=',
    'MUIDB': '09FD4A46F67D695C27C65EF8F79968B3',
    'MSCC': 'NR',
    'SRCHUSR': 'DOB=20240716&T=1721139382000&POEX=W&TPC=1721139479000',
    '_uetsid': '586bec20437e11efb9641f510564b118',
    '_uetvid': '586c81a0437e11ef854f4518d60098dd',
    'MSPTC': '-8_3oD3FK0fFFkUW4a8phFWxRJJvdoQm7j1zzGGE_LE',
    '_EDGE_S': 'F=1&SID=35BE153F5ED76BE63A6401815F336A88&mkt=en-in&ui=en-in',
    'USRLOC': 'HS=1&ELOC=LAT=26.515796661376953|LON=80.23897552490234|N=Kanpur%2C%20Uttar%20Pradesh|ELT=4|',
    'ai_session': 'INjbI4KAiovhddxQMQb7zs|1721139384848|1721139856018',
    '_HPVN': 'CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNy0xNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo4LCJUb2JuIjowfQ==',
    'bm_sv': 'C184B163B6A11C6AE4B4596D65C42A35~YAAQHLcsMb4TQLiQAQAATQfuuxie5ZUjAGLs+Yh+JUA8/GuKt52lpHw7en3Tj64bH5GHmGXTbz5T7r1QvDPUetuel81B8HjunbBD3Z58ly3l7rY5Hulpf4EEEwNIgkXUk5PyWPIDGqOTF6hn/fVIhgRopwrJjc1+dP5/DD5x4FP2h09z/liLGiXotUVEGB3t8iwjV/1uueaRcuvgBG9VbMr2C/codiUwulHZ09g9MBbwzc37c4N1RBTRlkQGuIg=~1',
    '_SS': 'SID=35BE153F5ED76BE63A6401815F336A88&R=4857&RB=4857&GB=0&RG=0&RP=4854&OCID=ML2GB2',
    '_RwBf': 'r=0&ilt=1&ihpd=1&ispd=0&rc=4857&rb=4857&gb=0&rg=0&pc=4854&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=16&l=2024-07-16T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=1&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-07-16T07:17:51.0390901-07:00&rwflt=2024-07-16T07:17:45.8980625-07:00&o=0&p=BINGTRIAL5TO250P201808&c=ML1OVB&t=1641&s=2023-11-10T13:16:19.7240052+00:00&ts=2024-07-16T14:24:19.6831203+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=bZ7heD3SjnHREyo3WP7mYJJT6Ih9GxFAU2R4QC4aHn2rfUcfnzpOpyStTTFfztZ83gRBUREjewxtlpnw-pP1Z2SFBK1IcCnMYWG8cv022SY&A=D8003EBF03381FA3F87B4289FFFFFFFF',
    'dsc': 'order=Images',
    'SRCHHPGUSR': 'SRCHLANG=en&IG=FE1AB5011C0846D8B2272973E29C5842&BRW=M&BRH=S&CW=1280&CH=591&SCW=1263&SCH=4658&DPR=1.5&UTC=330&DM=1&WTS=63856736182&PV=15.0.0&HV=1721139861&PRVCW=1280&PRVCH=591&CIBV=1.1790.0&EXLTT=10',
    'ipv6': 'hit=1721143464837',
}

headers = {
    'Host': 'www.bing.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
    'Sec-Ch-Ua-Model': '""',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Sec-Gpc': '1',
    'Accept-Language': 'en-US,en;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.bing.com/?FORM=Z9FD1',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=0, i',
    # 'Cookie': 'MUID=09FD4A46F67D695C27C65EF8F79968B3; MUIDB=09FD4A46F67D695C27C65EF8F79968B3; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=B0C3D5194A2749DE99B9FB549361A06B&dmnchg=1; ak_bmsc=02B703E431DABD2BF80E60A81F7D00FE~000000000000000000000000000000~YAAQ3gVaaPT+8rWQAQAAk8rmuxgGoKxVSNMMJiknpqqEQq7pfiJ9Gu4l6FcMHaO0f1wi4U+ByUtUiaKkv8J6VNcp0fAiOUl2IINHoOZpn8SFBmLTiDbmUB2PyowtUCJ3cvVTfh6zKCBkYm7T+imz8jO75p8zKeiGOzR025QuYNVYl/keepWSYo6sI8OCPST/aBtLeVNTlVLAADuEu+ZxfaVC8hJMSy6IRVehi/fKnJoNhyVKheaBqPl5cTVzO+CEChVsZZkMxElqnBY8ywIN14Qjw2+XJZsR7D6QzJR5H/naNVpdL8wduAUvUX7rJVrZgNs4jdxdVsZwGnpLJXFy4JKC16Wp9Cgf4vltaC9EylOAunCiye1KiapGFbHU4Kkjv561JjEKYQ==; BCP=AD=0&AL=0&SM=0; _UR=cdxcls=0&QS=0&TQS=0; _Rwho=u=d&ts=2024-07-16; CSRFCookie=f23c4029-b438-4c4b-9a12-34a5ecf1e812; ANON=A=D8003EBF03381FA3F87B4289FFFFFFFF&E=1e02&W=1; NAP=V=1.9&E=1da8&C=a2ywj3KUY4BrtikO75Yj77hJ07l8MbnCKDd_b5pNdeDsH60S_6Mr7w&W=1; PPLState=1; KievRPSSecAuth=FABKBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACCIDfOUoriwhCARIa7E5mRzbZG/Vk+oZwmLH1idd0V4CD8ws3MHAh3snZtcIT9gHbEyO36okUmpctkJSeJlVjpP4xjPExY9MmSKizT39vk9souE/qwAPgV11XfbWqKXmYnwQsZLOoyQM0KnsOQ0DBWwhmFg2TVQex5Ojf2s8id/1EHpYS5EXv0fznp/xGOERehpCTRwotj5t9bvjXFYA7SWfAL5DffAf6kbQ+0OnlAV/a/o1w0cnYcsEY8eNrv3HuQ6jJ8C2sO3K8c4SIplMMDEh4BbeO2fvVMifC7EzFOvBfPLshrrZuEUxyGDZHshvCVisN/jhLS8H12mN1km1bXVDOPrEHe7Feit/VDBdq+7U9MWT//i9fubkGUKVtKvERnhNCVEuUvLyGKnrF/fmRHVAhLTUNlBaQDtIyLbzEpi2tdS+YPLfRP/OcAw+E1ApLanChCm2eYRthHhfTgb9oLGZ39ENCUd7/bAkWEckp4wjaiIGwKAbdDlraU4AFCgOYZJh1bb7MSaOnTzAMHsXdZ0XRxN1VcTi60OqhGcZNKc/RRFM+I1JZBolNIdmqe8+kC7Sk5PsS+oFL8CjK8mGrjGpuu7b2abYCSCPmDvJEp38i6N3RK/Q2fwZ22wwpgfcHQG1sznFX5FoNrDly1Fjod6QMQjgJF+G+I+D8/78oGN5Y5SAUN/kdImn8k9FGnTAgAWt5ZxgbXJPCfS9eAalITiik7HQBJsdzSc7YW6Mh/xNF/2e+jklOoZJVoNoD6t59uElH2/mxsBBUqF63/WiLDEcurMx7Gy44V5a3jJk1mPn7d1RK4Yqvq2EBM+qY+5PC57YJ9tEfc07d30YDwcKPo+gjcfHhQeoRn0whNgCbIzaPQUUbIWvmhYnBZcOKjP0ZHbE9mB9jmaPTPUAAANzahgvKCUZSHFCJaeXbheKN+yk3QLwPCSfCv0kixH5hz6kUEPE99bAffAMNx3LvCb1JIfbCFyxbIP6OpezBjahebVn1zNVKXxyCzW45c+7RLQtxF6UZsziroYd8Q9gWK24m/IkaSVerrHIlArHNP5YIPxMO/hgYN/EDtURf7x+h7ssbCCfYpGX5hpC0iod2y0QLSCaLS8EvxoRcYl/5HqzlUVb59uNpPXjMbR0arIXKBe0RYb3APwWc+4CVAD43xqDsHoDk/quowiewY5MQbf61sSz/QPFqlaDL3hTyBxOlksw9xYPtB/N2/1MWuIfKkcdn0cT6weyNbw+BDSgjOvKMh6zjpyjB+pUZT1AN2cBZmmHzoIp4ThK1LvAGF6mL7RvmKYfRW9QoDqr7QcfD/p11IWY2NfSkXx0dA3Uzahuq+Qh633KkvqAFBfL2uDFrjaoGLocbULl60uC/nMRxHBZJ+fYIIAUAPeAVRvJLNlYPCHrNxNgZqXxicaW; _U=1rbAVr8sLsmVInZ5HYbgIsoi-E8WnZTsCBNrwMdXE7yGLPLaSMqHraUiPRm50uFLuSTMBktlKCYLkUxINJk0DOWnbqk0VNgmZTTQg1_h6fHilzG7xGRPSg533jtw6q0wshGYxVhSYNYrhr2soRcVv7cvvws8C4dNC5fflhp9gOD08cXTrSXlO4O4KO_5YEUWaganJ3tnwBUetWbqK8Fay2w; WLS=C=82b022bcb40fdc2b&N=ck; WLID=B7daODAET9JR0nI5fET8NUkszflcmNdeflAGo6cybanhyGsGTA3RAYFHwO/NQ/GxhXkmn3fsVKpzM/BcGkR9X8f43w3AaJ0Ar3fa0XKQyN0=; MUIDB=09FD4A46F67D695C27C65EF8F79968B3; MSCC=NR; SRCHUSR=DOB=20240716&T=1721139382000&POEX=W&TPC=1721139479000; _uetsid=586bec20437e11efb9641f510564b118; _uetvid=586c81a0437e11ef854f4518d60098dd; MSPTC=-8_3oD3FK0fFFkUW4a8phFWxRJJvdoQm7j1zzGGE_LE; _EDGE_S=F=1&SID=35BE153F5ED76BE63A6401815F336A88&mkt=en-in&ui=en-in; USRLOC=HS=1&ELOC=LAT=26.515796661376953|LON=80.23897552490234|N=Kanpur%2C%20Uttar%20Pradesh|ELT=4|; ai_session=INjbI4KAiovhddxQMQb7zs|1721139384848|1721139856018; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNy0xNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo4LCJUb2JuIjowfQ==; bm_sv=C184B163B6A11C6AE4B4596D65C42A35~YAAQHLcsMb4TQLiQAQAATQfuuxie5ZUjAGLs+Yh+JUA8/GuKt52lpHw7en3Tj64bH5GHmGXTbz5T7r1QvDPUetuel81B8HjunbBD3Z58ly3l7rY5Hulpf4EEEwNIgkXUk5PyWPIDGqOTF6hn/fVIhgRopwrJjc1+dP5/DD5x4FP2h09z/liLGiXotUVEGB3t8iwjV/1uueaRcuvgBG9VbMr2C/codiUwulHZ09g9MBbwzc37c4N1RBTRlkQGuIg=~1; _SS=SID=35BE153F5ED76BE63A6401815F336A88&R=4857&RB=4857&GB=0&RG=0&RP=4854&OCID=ML2GB2; _RwBf=r=0&ilt=1&ihpd=1&ispd=0&rc=4857&rb=4857&gb=0&rg=0&pc=4854&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=16&l=2024-07-16T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=1&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-07-16T07:17:51.0390901-07:00&rwflt=2024-07-16T07:17:45.8980625-07:00&o=0&p=BINGTRIAL5TO250P201808&c=ML1OVB&t=1641&s=2023-11-10T13:16:19.7240052+00:00&ts=2024-07-16T14:24:19.6831203+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=bZ7heD3SjnHREyo3WP7mYJJT6Ih9GxFAU2R4QC4aHn2rfUcfnzpOpyStTTFfztZ83gRBUREjewxtlpnw-pP1Z2SFBK1IcCnMYWG8cv022SY&A=D8003EBF03381FA3F87B4289FFFFFFFF; dsc=order=Images; SRCHHPGUSR=SRCHLANG=en&IG=FE1AB5011C0846D8B2272973E29C5842&BRW=M&BRH=S&CW=1280&CH=591&SCW=1263&SCH=4658&DPR=1.5&UTC=330&DM=1&WTS=63856736182&PV=15.0.0&HV=1721139861&PRVCW=1280&PRVCH=591&CIBV=1.1790.0&EXLTT=10; ipv6=hit=1721143464837',
}


search_queries = [
    'best practices for healthy aging',
    'common diseases in elderly patients',
    'how aging affects the cardiovascular system',
    'role of diet in preventing age-related diseases',
    'human anatomy changes with age',
    'how to manage arthritis pain in older adults',
    'effects of aging on the brain',
    'latest research on dementia and aging',
    'preventing osteoporosis in aging populations',
    'impact of aging on the respiratory system',
    'how to maintain muscle mass as you age',
    'age-related changes in the digestive system',
    'managing diabetes in older adults',
    'best exercises for seniors',
    'role of genetics in aging',
    'how to support mental health in elderly patients',
    'importance of hydration in older adults',
    'common surgeries for aging populations',
    'preventative care for elderly patients',
    'how to manage chronic pain in aging patients',
    'impact of aging on vision and hearing',
    'latest advancements in geriatric medicine',
    'role of physical therapy in aging',
    'how to improve mobility in elderly patients',
    'age-related changes in skin and hair',
    'nutrition tips for aging populations',
    'how to prevent falls in older adults',
    'managing heart disease in the elderly',
    'role of sleep in healthy aging',
    'how to cope with age-related memory loss',
    'impact of aging on the immune system',
    'how to handle end-of-life care',
    'best practices for senior healthcare',
    'aging and its effect on the urinary system',
    'role of caregivers in elderly healthcare',
    'how to address loneliness in older adults',
    'managing high blood pressure in elderly patients',
    'importance of routine check-ups for seniors',
    'how to reduce the risk of stroke in older adults',
    'impact of aging on the reproductive system',
    'how to manage multiple chronic conditions in the elderly',
    'importance of vaccination for older adults',
    'role of technology in elderly healthcare',
    'how to improve cognitive function in aging populations',
    'impact of aging on mental health',
    'how to manage anxiety and depression in elderly patients',
    'role of exercise in preventing age-related diseases',
    'how to enhance quality of life for aging patients',
    'impact of aging on oral health',
    'managing sleep disorders in the elderly',
    'how to support aging patients with cancer',
    'importance of social engagement for seniors',
    'how to manage incontinence in older adults',
    'best practices for elderly nutrition',
    'how to handle age-related hormonal changes',
    'role of alternative medicine in aging care',
    'how to educate patients about healthy aging',
    'impact of aging on the endocrine system',
    'how to manage obesity in older adults'
]





# Perform searches with delay and longer breaks
for index, query in enumerate(search_queries, start=1):
    params = {
        'q': query,
        'PC': 'U316',
        'FORM': 'CHROMN',
    }

    response = requests.get('https://www.bing.com/search', params=params, cookies=cookies, headers=headers)
    
    # Process the response as needed (currently no printing)
    # You can store results in a list or perform any other processing
    
    # Introduce a random delay between 4 to 8 seconds
    time.sleep(random.uniform(4, 8))
    
    # Check if we have completed 3 searches
    if index % 3 == 0:
        # Wait for 15 minutes (900 seconds)
        print(f"Completed {index} searches. Waiting for 15 minutes...")
        time.sleep(900)  # 15 minutes
