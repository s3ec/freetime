import requests
import time
import random

cookies = {
    'MUID': '00E2F22422E365EC3836E68323A264B4',
    'MUIDB': '00E2F22422E365EC3836E68323A264B4',
    '_EDGE_V': '1',
    'SRCHD': 'AF=NOFORM',
    'SRCHUID': 'V=2&GUID=4DFC31FEDEB24E94BC086DA2B4FBB51A&dmnchg=1',
    '_UR': 'cdxcls=0&QS=0&TQS=0',
    'ANON': 'A=6CADC3B02CF7BB522456E37EFFFFFFFF&E=1deb&W=1',
    'NAP': 'V=1.9&E=1d91&C=Eg5MzQgr_xRVfonElWaN3ux8qNkMLNw4SUpxLh80iJO3u3_iozEKng&W=1',
    'PPLState': '1',
    'MUIDB': '00E2F22422E365EC3836E68323A264B4',
    '_HPVN': 'CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNy0wNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyMCwiVG9ibiI6MH0=',
    'KievRPSSecAuth': 'FAC6BBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACHL3FiXkhfe0eAQooaMen3ERPZdoMYbiJEByCqJ8BANJ536KUkZJLStX2eAytxRJi4vef7eiOO6th9v/lRIkh++mtqavijKUbmi0vIwDh2Lpf73Yn5DCeSMwbj9aX1UFSIX64YKbntmWFpYwcwijwmD4F8YYlAk8b/RosM7+1Wc0hZBJBuheqvHuJi03ArnBGAKPfJUiZrl4OVMOUY2fLaERYnJkOYhJivfaQ5MyLsEw8Vig2khrqII2BzxQurkKSbAEEQK6W206t5Ehe6ik2KWbuomjgUqlnaj189l03v5o4OGNYupWzlexcfutsi2jDlHOB2XlGLP0kSfkSMNx9/eWyWUBsYXKNn0/aPdM15v5Q6xemHgtUlcFemDfmtoMcoH9qI7Ox7xmK30oDQWOzojQCvVSQ6yoiVH2YZ4KGtuBXHNXtaDWl4km0p67GGAy7wUgmZPgPzr8dMtqIZKrBr8f9Vn6qO9DA2f6EDPd1vwAmezfS+dKrNb9JpsoOtUzol1JGmZwnekjzlM5bKoRqTubKvHMGZjOFUBlIT9gDL3AQKyl21AN1IghWTHzZiT/5Qa4IumkYE2vqVvBekgAcARrKvdDDyITzXx1gOHZ4OCILLKzGvfxhYZ2/8gUr3MUGMBSWL0Cy/1oqiO6EfEwenASlvHKEq09Tp2aJ/0wDtpazRUq/vYti6c+K5Y3TU1MKRaRtUGhzgdWBIyN6jKunCU/uV7CFlOjrbozfGuOaXkiSvjMaSDkH9lhzXC/VxWGFe5SGAE0pOeCDhIJqTOYbNc5eKG1FS9bxlMQy6Sr2580YDIDyEWJ1V/AYX21S0j8rD0cT/Ys8vEXNNJWQJkhqKj6q5Hskyyi8PDvqekj4OQruf36zNjlbHtR8d8Ggf3HXpgcwcjpBBFpXaPtQk0wcXG6MOp8zQ3pWz4hoQ7C9eeqdbyV1aZKyEqDLlkc6vg1qgkA1ikpB8WuphnF47P8Z9ktSNCN3PRbXV3obY+sA3Qr0a6z1IvD1FrIvpIiB9VUqgX4QNqSFv8Z2k7lybzlCflaMIXbY5VQdS4KwoVap7rAFpSoDYRJSIh3Yv4EhNJhuffOG3DkNsf9uKdfFWrNL5U5/hs/E7YGUQzKJY73eUZH7XeYr0Hw8qqHkPHdc1kFAmLE6WH75ZdPdh4xgCz9pKy8etsgHDTbCgLUZLxytBCu01H6hBscq6L8GDGIvdbnB4RbSkhpsCBXu/UGl8JJu9C0MVTVes+29+tETNbuGPR0whUa7eeNKVpkZPIS2dTx1Q4LY4UT/LZRAzrtcZQM+RPF3dXuy19KILr8zpIyhWI0XiWhmpgn3SRR0AHNFeGxN538FXPekHB9wfXZC2cTcn6+ZSAdI9Psdl5UdGtatnrJ+GLhIoKwn5JOPFVD0DUYJueAQVonnnqSITEWp0ujHkqmNteYuQzLoLVqLiws63dXXUfwDQRGQ9ZwCQMJQRwWaeg1qto4DPBdLgBIl58Oc7fgLFq/xeuUZa+Fc77UAJoITg+LYmntUhtRpaHfsEvwpQhUFACt5JPRo0R8Z6PBBi9cb0Fh42IOdQ==',
    '_U': '1upMmTNWpbMRyrsxnCSDI6zWhTiF35g4T-WYM5n7iryQ_Qp_EQMP0ooeMtGy0km-2RdSQQjepc8wc0GL6IlhvdvRN0Q8E51wqxpVxEiK6egkIfWJaX0tlqrxF-ovuWIIodBiwQWdg15uuStnffTHS6ECs4DShgQtBfGxEPBIcw-md9wBkmmfP_qe5tHaoVZhnctIZ4nHTwkJGv7LUKe7t_-hwC0zcsVi6VDJDntm7yDhB0E3bpcz0xH4Wr2xxl_gW',
    'WLID': 'aXlwLq2ZkJ0l7E4fFc2ZIJpEQvpNsk9dGK6lTsAjtLD9STkzzknG3AMXgwuukMGEIO1ttS2xp+21d2C4HtTx8JfCZZ0o5w3AnZs/nndhBUY=',
    'SRCHS': 'PC=U316',
    'WLS': 'C=fb0fe0915cfa05fb&N=Lakshmi+pavitra',
    'BCP': 'AD=0&AL=0&SM=0',
    '_EDGE_S': 'SID=2C60EB159AC5694B2FEFFFA29B6268EE&mkt=en-in&ui=en-in',
    'MSCC': 'NR',
    '_tarLang': 'default=en',
    '_TTSS_IN': 'isADRU=1',
    '_TTSS_OUT': 'hist=WyJlbiJd',
    'ak_bmsc': '05B99CC4C4F3F8D2E1F3D33348F19D05~000000000000000000000000000000~YAAQzQVaaMd4KpGQAQAAuzmwoBi/l4xo8ycGA5GWSDbcPu1W4ntt59p1IRcfoMhuVzECLcInrQ9BwwuqlJUkG0sDvRLfgREwSQUGGeao6fHWhrbISSixjq5yks6RKtTM5yvwi2FNZMUEztrQr9ufyTKOmtSxLbJWEW/D1H/HRRTASMOHZe9/qj5eVK+wWSUC1P2X1KVxgEUAC2QpaEmiZ8yOngC6XVXW3drWuwffpsuo4ZE9jDrvSHW21KNiBtgUfDEqemGiI1pbH40AfyXF3+m1fnTlTKn5lXQBi//ZPIuDqkmg7NsH55xmBLbPh7lXKyRYsmasuF2K2V441PctIo+ZZUMxDg+x3sChDhQ/AcNU52FjMIvCmKH+hHZyEqmJxUka',
    'ANIMIA': 'FRE=1',
    '_SS': 'PC=U316&SID=2C60EB159AC5694B2FEFFFA29B6268EE&OCID=ML2BF0',
    'SRCHUSR': 'DOB=20240623&T=1720689814000&TPC=1720682829000&POEX=W',
    'ABDEF': 'V=13&ABDV=13&MRNB=1720689823707&MRB=0',
    '_C_ETH': '1',
    'bm_sv': 'DC40509E076C899E55DC3A52D596F906~YAAQh40sMTTHRlSQAQAAOCkdoRhgREiArhRdasyHWYlP2S4pAf7R9m6JywdHIdi4yu2QZKD4mK8yZyodS7G5YP728PWr2BbDLPylPHyvyMzH74UDU1XPOJVSkbP7ME/Vlm1oJPvo/DxOCy976+6c+lZU5aGTGMN8Nas9nP3WGNShSieDUGSubz9r+hPj1ILthhH7sLSx2CFS3OWVwoI5FchF2GO4OcG+OopmeA9YsD3PbWeHuBHg1sHmiHOuYfA=~1',
    'dsc': 'order=Images',
    'ipv6': 'hit=1720693575765',
    'SRCHHPGUSR': 'SRCHLANG=en&IG=5B3C7F1E3AB94C658F2E2F5CFE044354&PV=15.0.0&BRW=M&BRH=S&CW=1280&CH=551&SCW=1263&SCH=4799&DPR=1.5&UTC=330&DM=1&WTS=63856029948&HV=1720689979&PRVCW=1280&PRVCH=551&CIBV=1.1788.0&cdxupdttm=638562614157625604',
}

headers = {
    'Host': 'www.bing.com',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Full-Version': '"125.0.6422.141"',
    'Sec-Ch-Ua-Arch': '"x86"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Bitness': '"64"',
    'Sec-Ch-Ua-Full-Version-List': '"Chromium";v="125.0.6422.141", "Not.A/Brand";v="24.0.0.0"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
    # 'Cookie': 'MUID=00E2F22422E365EC3836E68323A264B4; MUIDB=00E2F22422E365EC3836E68323A264B4; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=4DFC31FEDEB24E94BC086DA2B4FBB51A&dmnchg=1; _UR=cdxcls=0&QS=0&TQS=0; ANON=A=6CADC3B02CF7BB522456E37EFFFFFFFF&E=1deb&W=1; NAP=V=1.9&E=1d91&C=Eg5MzQgr_xRVfonElWaN3ux8qNkMLNw4SUpxLh80iJO3u3_iozEKng&W=1; PPLState=1; MUIDB=00E2F22422E365EC3836E68323A264B4; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNy0wNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoyMCwiVG9ibiI6MH0=; KievRPSSecAuth=FAC6BBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACHL3FiXkhfe0eAQooaMen3ERPZdoMYbiJEByCqJ8BANJ536KUkZJLStX2eAytxRJi4vef7eiOO6th9v/lRIkh++mtqavijKUbmi0vIwDh2Lpf73Yn5DCeSMwbj9aX1UFSIX64YKbntmWFpYwcwijwmD4F8YYlAk8b/RosM7+1Wc0hZBJBuheqvHuJi03ArnBGAKPfJUiZrl4OVMOUY2fLaERYnJkOYhJivfaQ5MyLsEw8Vig2khrqII2BzxQurkKSbAEEQK6W206t5Ehe6ik2KWbuomjgUqlnaj189l03v5o4OGNYupWzlexcfutsi2jDlHOB2XlGLP0kSfkSMNx9/eWyWUBsYXKNn0/aPdM15v5Q6xemHgtUlcFemDfmtoMcoH9qI7Ox7xmK30oDQWOzojQCvVSQ6yoiVH2YZ4KGtuBXHNXtaDWl4km0p67GGAy7wUgmZPgPzr8dMtqIZKrBr8f9Vn6qO9DA2f6EDPd1vwAmezfS+dKrNb9JpsoOtUzol1JGmZwnekjzlM5bKoRqTubKvHMGZjOFUBlIT9gDL3AQKyl21AN1IghWTHzZiT/5Qa4IumkYE2vqVvBekgAcARrKvdDDyITzXx1gOHZ4OCILLKzGvfxhYZ2/8gUr3MUGMBSWL0Cy/1oqiO6EfEwenASlvHKEq09Tp2aJ/0wDtpazRUq/vYti6c+K5Y3TU1MKRaRtUGhzgdWBIyN6jKunCU/uV7CFlOjrbozfGuOaXkiSvjMaSDkH9lhzXC/VxWGFe5SGAE0pOeCDhIJqTOYbNc5eKG1FS9bxlMQy6Sr2580YDIDyEWJ1V/AYX21S0j8rD0cT/Ys8vEXNNJWQJkhqKj6q5Hskyyi8PDvqekj4OQruf36zNjlbHtR8d8Ggf3HXpgcwcjpBBFpXaPtQk0wcXG6MOp8zQ3pWz4hoQ7C9eeqdbyV1aZKyEqDLlkc6vg1qgkA1ikpB8WuphnF47P8Z9ktSNCN3PRbXV3obY+sA3Qr0a6z1IvD1FrIvpIiB9VUqgX4QNqSFv8Z2k7lybzlCflaMIXbY5VQdS4KwoVap7rAFpSoDYRJSIh3Yv4EhNJhuffOG3DkNsf9uKdfFWrNL5U5/hs/E7YGUQzKJY73eUZH7XeYr0Hw8qqHkPHdc1kFAmLE6WH75ZdPdh4xgCz9pKy8etsgHDTbCgLUZLxytBCu01H6hBscq6L8GDGIvdbnB4RbSkhpsCBXu/UGl8JJu9C0MVTVes+29+tETNbuGPR0whUa7eeNKVpkZPIS2dTx1Q4LY4UT/LZRAzrtcZQM+RPF3dXuy19KILr8zpIyhWI0XiWhmpgn3SRR0AHNFeGxN538FXPekHB9wfXZC2cTcn6+ZSAdI9Psdl5UdGtatnrJ+GLhIoKwn5JOPFVD0DUYJueAQVonnnqSITEWp0ujHkqmNteYuQzLoLVqLiws63dXXUfwDQRGQ9ZwCQMJQRwWaeg1qto4DPBdLgBIl58Oc7fgLFq/xeuUZa+Fc77UAJoITg+LYmntUhtRpaHfsEvwpQhUFACt5JPRo0R8Z6PBBi9cb0Fh42IOdQ==; _U=1upMmTNWpbMRyrsxnCSDI6zWhTiF35g4T-WYM5n7iryQ_Qp_EQMP0ooeMtGy0km-2RdSQQjepc8wc0GL6IlhvdvRN0Q8E51wqxpVxEiK6egkIfWJaX0tlqrxF-ovuWIIodBiwQWdg15uuStnffTHS6ECs4DShgQtBfGxEPBIcw-md9wBkmmfP_qe5tHaoVZhnctIZ4nHTwkJGv7LUKe7t_-hwC0zcsVi6VDJDntm7yDhB0E3bpcz0xH4Wr2xxl_gW; WLID=aXlwLq2ZkJ0l7E4fFc2ZIJpEQvpNsk9dGK6lTsAjtLD9STkzzknG3AMXgwuukMGEIO1ttS2xp+21d2C4HtTx8JfCZZ0o5w3AnZs/nndhBUY=; SRCHS=PC=U316; WLS=C=fb0fe0915cfa05fb&N=Lakshmi+pavitra; BCP=AD=0&AL=0&SM=0; _EDGE_S=SID=2C60EB159AC5694B2FEFFFA29B6268EE&mkt=en-in&ui=en-in; MSCC=NR; _tarLang=default=en; _TTSS_IN=isADRU=1; _TTSS_OUT=hist=WyJlbiJd; ak_bmsc=05B99CC4C4F3F8D2E1F3D33348F19D05~000000000000000000000000000000~YAAQzQVaaMd4KpGQAQAAuzmwoBi/l4xo8ycGA5GWSDbcPu1W4ntt59p1IRcfoMhuVzECLcInrQ9BwwuqlJUkG0sDvRLfgREwSQUGGeao6fHWhrbISSixjq5yks6RKtTM5yvwi2FNZMUEztrQr9ufyTKOmtSxLbJWEW/D1H/HRRTASMOHZe9/qj5eVK+wWSUC1P2X1KVxgEUAC2QpaEmiZ8yOngC6XVXW3drWuwffpsuo4ZE9jDrvSHW21KNiBtgUfDEqemGiI1pbH40AfyXF3+m1fnTlTKn5lXQBi//ZPIuDqkmg7NsH55xmBLbPh7lXKyRYsmasuF2K2V441PctIo+ZZUMxDg+x3sChDhQ/AcNU52FjMIvCmKH+hHZyEqmJxUka; ANIMIA=FRE=1; _SS=PC=U316&SID=2C60EB159AC5694B2FEFFFA29B6268EE&OCID=ML2BF0; SRCHUSR=DOB=20240623&T=1720689814000&TPC=1720682829000&POEX=W; ABDEF=V=13&ABDV=13&MRNB=1720689823707&MRB=0; _C_ETH=1; bm_sv=DC40509E076C899E55DC3A52D596F906~YAAQh40sMTTHRlSQAQAAOCkdoRhgREiArhRdasyHWYlP2S4pAf7R9m6JywdHIdi4yu2QZKD4mK8yZyodS7G5YP728PWr2BbDLPylPHyvyMzH74UDU1XPOJVSkbP7ME/Vlm1oJPvo/DxOCy976+6c+lZU5aGTGMN8Nas9nP3WGNShSieDUGSubz9r+hPj1ILthhH7sLSx2CFS3OWVwoI5FchF2GO4OcG+OopmeA9YsD3PbWeHuBHg1sHmiHOuYfA=~1; dsc=order=Images; ipv6=hit=1720693575765; SRCHHPGUSR=SRCHLANG=en&IG=5B3C7F1E3AB94C658F2E2F5CFE044354&PV=15.0.0&BRW=M&BRH=S&CW=1280&CH=551&SCW=1263&SCH=4799&DPR=1.5&UTC=330&DM=1&WTS=63856029948&HV=1720689979&PRVCW=1280&PRVCH=551&CIBV=1.1788.0&cdxupdttm=638562614157625604',
}

# List of search queries
search_queries = [
    'remote jobs in AI-driven manufacturing',
    'remote jobs in AI-driven entertainment',
    'remote jobs in AI-driven retail',
    'remote AI engineer jobs',
    'remote jobs in sustainable tech industry',
    'remote jobs in cognitive computing',
    'remote jobs for quantum AI engineers',
    'remote jobs in edge computing 2024',
    'remote jobs in AI-enhanced cybersecurity',
    'remote jobs in smart cities technology',
    'remote jobs in AI-driven finance',
    'remote jobs in AI-powered marketing',
    'remote jobs in AI-based customer service',
    'remote jobs in ethical AI development',
    'remote jobs in AI-driven education',
    'best remote tech jobs 2024',
    'remote software developer positions',
    'remote cloud architect jobs',
    'top remote jobs in blockchain technology',
    'remote cybersecurity analyst roles 2024',
    'remote jobs in fintech industry',
    'remote robotics engineer positions',
    'remote VR/AR developer jobs',
    'remote IoT specialist roles 2024',
    'best remote jobs in data science',
    'remote jobs for big data engineers',
    'remote UX/UI designer opportunities',
    'remote web developer positions',
    'remote mobile app developer jobs 2024',
    'remote jobs in quantum computing',
    'remote jobs for DevOps engineers',
    'remote tech support specialist roles 2024',
    'remote IT project manager jobs',
    'top companies offering remote tech roles',
    'remote jobs in virtual reality',
    'remote AI ethics researcher positions',
    'remote jobs in autonomous vehicles industry',
    'remote blockchain developer opportunities 2024',
    'remote jobs in cybersecurity consulting',
    'remote jobs for AI trainers',
    'remote tech startup jobs 2024',
    'remote jobs in natural language processing',
    'remote jobs for cloud solutions architects',
    'remote jobs in bioinformatics 2024',
    'remote jobs in 5G technology',
    'remote jobs in AI-driven healthcare',
    'remote jobs for AR content creators',
    'remote jobs in AI-driven agriculture',
    'remote jobs in AI-driven logistics',
    'AI software developer remote positions',
    'remote machine learning engineer openings',
    'remote data scientist opportunities 2024',
    'best remote jobs in artificial intelligence',
    'remote jobs for AI specialists',
    'top companies hiring remote AI professionals',
    'remote AI research positions',
    'AI startup remote job openings',
    'remote AI consultant roles 2024',
    'remote jobs in new tech 2024',
    'remote jobs in AI-driven transportation'
   
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