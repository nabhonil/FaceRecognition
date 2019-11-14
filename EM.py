import requests
import urllib.parse

deviceName = "SEP00B0E1D2E42D"
userid = "Alex"
deviceProfile = "Alex_Cisco_8861_Device_Profile"
def doEMLogin():
    xmlReq = "<request><appInfo><appID>emapp</appID><appCertificate>Cisco123</appCertificate></appInfo><login><deviceName>"
    xmlReq = xmlReq + deviceName
    xmlReq = xmlReq + "</deviceName><userID>"
    xmlReq = xmlReq + userid
    xmlReq = xmlReq + "</userID><deviceProfile>"
    xmlReq = xmlReq + deviceProfile
    xmlReq = xmlReq + "</deviceProfile><exclusiveDuration><time>6000</time></exclusiveDuration></login></request>"

    url = 'http://nasinha-lnx:8080/emservice/EMServiceServlet'
    payload = {'xml': xmlReq}
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    r = requests.post(url, data=urllib.parse.urlencode(payload), headers=headers)
    			
    return r

if __name__ == "__main__":
    print (doEMLogin())
