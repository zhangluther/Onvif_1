import time
from onvif import ONVIFCamera
import zeep
import requests
from requests.auth import HTTPDigestAuth


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


#抓图
def snap():
    # Get target profile
    zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue
    # mycam = ONVIFCamera("192.168.3.76", 2020, "admin", "ts@648123")
    mycam = ONVIFCamera("192.168.3.76", 2020, "admin", "ts@648123")
    print(mycam.devicemgmt.GetHostname())
    media = mycam.create_media_service()  # 创建媒体服务
    print(media.url)
    media_profile = media.GetProfiles()[0]  # 获取配置信息
    # print(media_profile)
    # print(media_profile["token"])
    print(media_profile.token)
    res = media.GetSnapshotUri({'ProfileToken': media_profile["token"]})
    # res = media.GetSnapshotUri({'ProfileToken': "profile_1"})
    print(res)
    response = requests.get(res.Uri, auth=HTTPDigestAuth("admin", "pass"))
    res = "{_time}.png".format(_time=time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))
    with open(res, 'wb') as f:  # 保存截图
        f.write(response.content)


print(snap())