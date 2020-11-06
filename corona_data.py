import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt, endCreateDt):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    params = {
        'serviceKey':"W3NXZOvN9bn5tXdY6r8pJVbxqx38VMviQdISK6fnIkdizOYI/8QNXthcyN7XlH8N22xmHSe96QIQS73wITszEg==",
        'pageNo':'1',
        'numOfRows':'10',
        'startCreateDt': startCreateDt,
        'endCreateDt': endCreateDt, #'20201027'
    }

    res = requests.get(url, params=params)

    # print(res.url)
    # print(res.text)

    # xml to dict
    dict_data = xmltodict.parse(res.text)
    # print(dict_data)


    # dict to json
    json_data = json.dumps(dict_data)
    # print(json_data, type(json_data))

    # json to dict
    dict_data = json.loads(json_data)
    #pprint(dict_data['response']['body']['items']['item'])

    # total count로 데이터가 가져와졌는지 확인
    totalCount = dict_data['response']['body']['totalCount']
    if totalCount == "0":
        return False


    # 지역 정보르 담은 리스트
    area_data = dict_data['response']['body']['items']['item']
    area_data.reverse()
    # print(area_data)
    return area_data
