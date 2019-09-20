#! /usr/bin/env python3

import sys
import json
import urllib.request
import urllib.parse


class SchoolListCrawler:
    """curl 'http://api.eol.cn/gkcx/api/?access_token=&
    admissions=&
    central=&
    department=&
    dual_class=&
    f211=&
    f985=&
    is_dual_class=&
    keyword=&
    page=3&
    province_id=&
    request_type=1&
    school_type=&
    signsafe=&
    size=20&
    sort=view_total&
    type=&
    uri=apigkcx/api/school/hotlists' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://gkcx.eol.cn/school/search' -H 'Origin: https://gkcx.eol.cn' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"access_token":"","admissions":"","central":"","department":"","dual_class":"","f211":"","f985":"","is_dual_class":"","keyword":"","page":3,"province_id":"","request_type":1,"school_type":"","size":20,"sort":"view_total","type":"","uri":"apigkcx/api/school/hotlists"}' --compressed"""

    apiURL: str = 'http://api.eol.cn/gkcx/api/'

    def getSchoolList(self, page: int, size: int):
        args = {
            'access_token': '',
            'admissions': '',
            'central': '',
            'department': '',
            'dual_class': '',
            'f211': '',
            'f985': '',
            'is_dual_class': '',
            'keyword': '',
            'page': str(page),
            'province_id': '',
            'request_type': '1',
            'school_type': '',
            'signsafe': '',
            'size': str(size),
            'sort': 'view_total',
            'type': '',
            'uri': 'apigkcx/api/school/hotlists'
        }

        headers = {
            'Accept': 'application/json, text/plain',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        }

        req = urllib.request.Request(self.apiURL+'?'+urllib.parse.urlencode(
            args), data=json.dumps(args).encode('utf-8'), headers=headers)

        resp = urllib.request.urlopen(req, timeout=10)

        return json.loads(resp.read().decode('utf-8'))

    def getFullSchoolList(self, progressFunction=lambda num, school: None):
        i, j = 1, 1
        schoolList = {}

        while True:
            nowList = self.getSchoolList(i, 20)

            assert nowList['code'] == '0000'

            if len(nowList['data']['item']) == 0:
                break

            for school in nowList['data']['item']:
                schoolList[school['name']] = school
                progressFunction(j, school)
                j += 1
            i += 1
        return schoolList


if __name__ == "__main__":
    filename = 'schoolList.json' if len(sys.argv) != 2 else sys.argv[1]
    crawler = SchoolListCrawler()

    with open(filename, 'w') as output:
        json.dump(crawler.getFullSchoolList(lambda num,
                                            school: print('%d: %s Done' % (num, school['name']))), output, ensure_ascii=False, indent=1)
