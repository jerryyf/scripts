#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import argparse

async def req0_fetch(client, ssl=True, proxy=None, url=None):
    method = 'GET'
    cookies = {
        'FTClientSessionId': '3b519b6c-ffb1-4d1a-85a0-a220c5ec9d14',
        'spoor-id': '3b519b6c-ffb1-4d1a-85a0-a220c5ec9d14',
        'usnatUUID': 'ddafaf6b-5feb-4ab4-9a79-6fdedb0ae45b',
        'FTSession_s': '015S525vm0YN04jueSsS9xii0wAAAZeCfMq4w8I.MEUCIG-MU36KAJuoGCAx7QV0hRoNWU42cqB6UEKGU0KR6MRfAiEAn4rQtWS_C3ro4IXh53nmBC5AEkQc0ZFLdncswpO99BQ',
        'session': 'eyJjc3JmU2VjcmV0IjoieEVzME50cV9hWFZWcDIwMFNZcFk4dWYyIn0=',
        'session.sig': 'qlz47pFiMPLRbS12Aon5YtHFJNY',
        'FTAllocation': '5e52e76e-6f9b-460d-88ee-792b12f718a2',
        'optimizelyEndUserId': 'oeu1750240908089r0.3038331353541326',
        'ravelinDeviceId': 'rjs-30b3da22-6a5a-4649-b179-14a7285676c8',
        '_ga': 'GA1.1.1169006883.1750240909',
        'consentUUID': '1e8f5ba8-dc94-4720-b79a-219c4b6525ab_45',
        # 'consentDate': '2025-06-18T10:01:53.709Z',
        'FTCookieConsentGDPR': 'true',
        'express:sess': 'eyJjc3JmU2VjcmV0IjoicThucl80eEVRYmdCR1ZzblNHQURlejM3IiwiZmxhc2giOnsic3VibWl0dGVkRW1haWxBZGRyZXNzIjpbImFzZGZhc2RmQHlvcG1haWwuY29tIl19fQ==',
        'express:sess.sig': 'ts2v45QTrGTR3-MkG9V9CnfCDs4',
        '_gcl_au': '1.1.312300832.1750240928',
        '_clck': 'od1gzb%7C2%7Cfwv%7C0%7C1995',
        'FTConsent': 'behaviouraladsOnsite%3Aon%2CcookiesOnsite%3Aoff%2CcookiesUseraccept%3Aoff%2CdemographicadsOnsite%3Aon%2CenhancementByemail%3Aoff%2CenhancementByfax%3Aoff%2CenhancementByphonecall%3Aoff%2CenhancementBypost%3Aoff%2CenhancementBysms%3Aoff%2CmarketingByemail%3Aoff%2CmarketingByfax%3Aoff%2CmarketingByphonecall%3Aoff%2CmarketingBypost%3Aoff%2CmarketingBysms%3Aoff%2CmembergetmemberByemail%3Aoff%2CpermutiveadsOnsite%3Aon%2CpersonalisedmarketingOnsite%3Aon%2CprogrammaticadsOnsite%3Aon%2CrecommendedcontentOnsite%3Aon',
        '_ga_6VD8DR7FRW': 'GS2.1.s1750240908$o1$g1$t1750240936$j32$l0$h1933660216$d0rT4kcD09UhN32MtFVIEoxcFTEdNmhk4mw',
        'permutive-id': 'faa94dc4-66b8-4f46-b8fd-80b4cf4197c3',
        '__exponea_etc__': 'f446a11d-259b-4c0d-8e5d-2f9735bd8090',
        '__exponea_time2__': '-0.04656410217285156',
        'FTCookieConsentSync': 'false',
        'ft-access-decision-policy': 'GRANTED_SUBX_REG_3_30',
        'zit.data.toexclude': '0',
        '_sxh': '1690,',
        '__gads': 'ID=632a1ab74b7e9afc:T=1750240938:RT=1750241241:S=ALNI_Mb89cqUX7bQRnFj3SxohTldSbvVEg',
        '__eoi': 'ID=93ed2b4e6032988f:T=1750240938:RT=1750241241:S=AA-AfjaUqqlQsjBcRKSJ3yLX56y1',
        'OriginalReferer': 'None',
        'FtComEntryPoint': '/content/5aeda50d-a3b5-4a20-97bd-75a22d7d061b',
        '_rdt_uuid': '1750240928315.53c05826-f5db-4202-aacc-2944d5e4f831',
        '_uetsid': '4bb266904c2b11f088d2911011256fed',
        '_uetvid': '4bb29ac04c2b11f08ebe5d4b22b07faf',
        '_fs_cd_cp_pRdRgnTnF68pCV2F': 'Aa-XEGNqQfKKm4oqMpQD0TGGijjfMt9rAxF0U4ASfe6VCwtQF9dSrJTlS5cAdgjOCAcb2wTAx6Aw3eYYjZNMF1VrRyEVf2fYRbohbtxGO9cWS13DC6OAChCMWecON9exDqYCTRCwtjl1ai6SvGe1Yt7eTLI=',
        '_sxo': '{"R":0,"tP":0,"tM":0,"sP":0,"sM":0,"dP":0,"dM":0,"dS":0,"tS":0,"cPs":0,"lPs":[],"sSr":0,"sWids":[],"wN":0,"cdT":0,"F":1,"RF":1,"w":0,"SFreq":0,"last_wid":0,"bid":1036,"accNo":"","clientId":"","isEmailAud":0,"isPanelAud":0,"hDW":0,"isRegAud":0,"isExAud":0,"isDropoff":0,"devT":4,"exPW":0,"Nba":-1,"userName":"","dataLayer":"","localSt":"","emailId":"","emailTag":"","subTag":"","lVd":"","oS":"","cPu":"","pspv":0,"pslv":0,"pssSr":0,"pswN":0,"psdS":0,"pscdT":0,"RP":0,"TPrice":0,"ML":"","isReCaptchaOn":false,"reCaptchaSiteKey":"","reCaptchaSecretKey":"","extRefer":"","dM2":0,"tM2":0,"sM2":0,"RA":0,"ToBlock":-1}',
        '_clsk': '1rz0h1o%7C1750245009772%7C1%7C0%7Cb.clarity.ms%2Fcollect',
        '__adblocker': 'false',
        'dicbo_id': '%7B%22dicbo_fetch%22%3A1750245012322%7D',
    }
    headers = {
        'Host': 'www.ft.com',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=0, i',
    }
    payload = None
    async with client.request(
         ssl=ssl,
        method=method,
        url=url,
        headers=headers,
        cookies=cookies,
        data=payload,
        proxy=proxy
    ) as response:
        return (response.status, response.headers, response.cookies, response.headers.get('content-length', 0), await response.text())

async def main():
    parser = argparse.ArgumentParser(description='Save ft.com articles in full without registration')
    parser.add_argument('-u', '--url', help='URL to be downloaded', required=True)

    args = parser.parse_args()

    async with aiohttp.ClientSession() as client:
        (status, headers, cookies, length, body) = await req0_fetch(client, url=args.url)
        with open("./article.html", "w") as f:
            f.write(body)
            print("Saved to file article.html.")
            f.close()

if __name__ == '__main__':
    asyncio.run(main())

