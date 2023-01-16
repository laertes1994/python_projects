import httpx
import base64

BOT_WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/pYVw2pyfSyiJQTUhb_R1BA"
with open("/Users/neil.zhu/Git_Repo/python_projects/reminder_bot.py", "rb") as f:
   raw_image_content: bytes = f.read()
   base64_encoded_image: str = base64.b64encode(raw_image_content).decode("latin-1")

json_payload1 = {
   "tag": "text",
   "text": {
       "content": "记得点外卖",
       "mentioned_list": [""],
       "mentioned_email_list": [""],
       "at_all": True
  }
}

json_payload2 = {
    "tag": "image","image_base64": {"content": base64_encoded_image}
}

httpx.post(url=BOT_WEBHOOK_URL, json=json_payload1)
httpx.post(url=BOT_WEBHOOK_URL, json=json_payload2)