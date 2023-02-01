import httpx
import base64

BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/mfs-ABKGRiaJCz18txmt-A"

json_payload1 = {
   "tag": "text",
   "text": {
       "content": "请更新CPAS报表,URL: https://docs.google.com/spreadsheets/d/1O2gsnsV3BNLe5bdxOs5SmRX8D1zqakGLD33H_kGDGqY/edit#gid=0",
       "mentioned_list": [""],
       "mentioned_email_list": ["neil.zhu@shopee.com"]
  }
}


httpx.post(url=BOT_WEBHOOK_URL, json=json_payload1)
