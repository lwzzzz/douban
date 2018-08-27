#登录豆瓣写短评，这里没有使用验证码处理后续会添加进来
import requests
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

}
#登录需要提交post信息，form_email是你的邮箱账号，form_password是你的登录密码，这里使用
data = {
"source": "movie",
"redir": "https://movie.douban.com/",
"form_email": "*****",
"form_password": "**",
"login": u"登录",
}
#写短评需要提交的数据  tags是你的标签  comment是你的简短评论 ck目前不清楚
# interest应该 是想看还是看过想看  想看对应的是collect  看过对应是wish（这里属于自己的猜测）
#rating 这里就是评分
#foldcollect这里不清楚
#tags 就是标签
#comment就是简短评论
data1 = {
"ck": "U5xz",
"interest": "collect",
"rating": "5",
"foldcollect": "F",
"tags": "测试",
"comment": "真香"
}
url = "https://accounts.douban.com/login"
targeturl =""

res = requests.session()
req=res.post(url=url,headers = headers,data=data)

rq=res.post("https://movie.douban.com/j/subject/1295644/interest",data=data1,headers=headers)
print(rq.status_code,req.status_code)