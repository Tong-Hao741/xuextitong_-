# -*- coding:utf-8 -*-
# author Tong-Hao time:2020/4/30
import requests,re,time
from lxml import etree
import datetime
headers = {
                "Cookie": "你的cookie",
                "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChaoXingStudy/ChaoXingStudy_3_4.3.2_ios_phone_201911291130_27 (@Kalimdor)_11391565702936108810",
                "Referer": "http://mooc1-1.chaoxing.com/visit/interaction?s=a23e43ba56b6a3a14a8213ef3176f159"
            }
def fangwen(activeid, classid, courseid):
    url = "https://mobilelearn.chaoxing.com/widget/pcAnswer/teaAnswer?activeId={}&classId={}&fid=23923&courseId={}".format(
        activeid, int(classid), int(courseid))
    response = requests.get(url, headers=headers, timeout=5)

    print(url)
print("当前时间：{}\n==========正在查看  <{}>  的活动==========".format(datetime.datetime.now(), '英语'))

#不一定是英语，可以根据classid和courseid去更改。
url = 'https://mobilelearn.chaoxing.com/widget/pcpick/stu/index?courseId={}&jclassId={}'.format('211097145','23147496')
while True:
    time.sleep(1)
    resoponse = requests.get(url, headers=headers, timeout=5)
    # xpath解析文本
    html = etree.HTML(resoponse.text)
    divs = html.xpath('/html/body/div[2]/div[2]/div[@id="startList"]/div')

    if (divs):
        for div in divs:
            activeid = div.xpath('./div[1]/@onclick')[0]
            active = re.findall('activeDetail\((\d+),(\d+),.*?\)', activeid)[0]

            # activeType = 4 为抢答
            if (int(active[1]) == 4):
                fangwen(str(active[0]), '23147496', '211097145')
                print('抢答成功')
            else:
                print("暂无抢答\n")

        # print(active[1])
    else:
        print("暂无活动\n")

