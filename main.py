import datetime
import hashlib

if __name__ == '__main__':
    param = {"externalLoginType": 1, "datatype": "1", "callback": "skuInfoCB", "cgi_source": "mitem",
             "sku": "10057351150533", "t": "0.04607759043801263", "_fd": "jdm", "selfMark": "bj"}
    appid = 'm_core'
    functionid = 'mview_switch'
    cookies = {

    }
    headers = {
        'authority': 'api.m.jd.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__jdu=16419545343171240324964; shshshfpa=ce86420e-d7fd-3e45-a2f9-be3717cab680-1651901453; shshshfpb=gkLOs3VMLHCYE5RWxLX1_uQ; __jdv=76161171|direct|-|none|-|1670813283283; areaId=18; ipLoc-djd=18-1482-0-0; __jdc=122270672; wlfstk_smdl=l3eh7ukaltnab507dldv2j6qbjgux80i; 3AB9D23F7A4B3C9B=W3C2PM6N3KUG2J53HRATJPQJXRVXGNS4MXFT6FFI2OJ64KAOYFTFD5UWO2SUA6XCA6XUOAE6ASGVNOQC3PSULVR7Q4; visitkey=3912712583203241; warehistory="10057351150532,"; wxa_level=1; retina=0; cid=9; wqmnx1=MDEyNjM3MnR0ZHIxMS4zNTRsKHMuNilXNSggZWgwMGk2cjRhNFZVSEZI; jxsid=16715145371450326667; webp=1; __jda=122270672.16419545343171240324964.1641954534.1670813283.1671514537.25; __jdb=122270672.1.16419545343171240324964|25.1671514537; mba_muid=16419545343171240324964; __wga=1671514537569.1671514537569.1671514537569.1671514537569.1.1; sc_width=1920; PPRD_P=UUID.16419545343171240324964-LOGID.1671514537576.435719510; mba_sid=16715145373489372371431899756.1; __jd_ref_cls=MDownLoadFloat_TopNewExpo; _gia_s_local_fingerprint=75decaf87cef940a144da34f0d4a23d9; shshshfp=059bf0b87ed0437cf9147668ef74d2f3; shshshsID=c98e8bece7253740dbdaa79e3226142a_1_1671514538308; _gia_s_e_joint={"eid":"W3C2PM6N3KUG2J53HRATJPQJXRVXGNS4MXFT6FFI2OJ64KAOYFTFD5UWO2SUA6XCA6XUOAE6ASGVNOQC3PSULVR7Q4","ma":"","im":"","os":"Windows 10","ip":"218.77.110.13","ia":"","uu":"","at":"5"}; equipmentId=W3C2PM6N3KUG2J53HRATJPQJXRVXGNS4MXFT6FFI2OJ64KAOYFTFD5UWO2SUA6XCA6XUOAE6ASGVNOQC3PSULVR7Q4; fingerprint=75decaf87cef940a144da34f0d4a23d9; deviceVersion=107.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome',
        'origin': 'https://prodev.m.jd.com',
        'referer': 'https://prodev.m.jd.com/mall/active/G7sQ92vWSBsTHzk4e953qUGWQJ4/index.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    }
    dtime = datetime.datetime.now()
    st = str(dtime).replace("-", "").replace(":", "").replace(" ", "").replace(".", "")[:-3]
    stt = str(dtime.timestamp())[:-3].replace('.', '')
    hash = hashlib.sha256();
    hash.update(bytes(str(param), encoding='utf-8'))
    bodyenc = hash.hexdigest()
    ai = "a8b69"
    token = 'tk02wbddc1c6818nRXeQRUBS5zkqDNIGcXwi7kyukONBbYACQqfzFplPLuk/9C3pYn3IWazTdZT5u3Vt5vI2Jw9U/jxE'
    fp = "5351643059805253"
    st = '20221220151036215'
    key = token
    rd = '7e43CAC0hDfy'
    data = token + fp + st + ai + rd
