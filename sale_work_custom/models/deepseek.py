from odoo import api,fields,models
import requests,json
from openai import OpenAI

class DeepSeek(models.Model):
    _name = 'deep.seek'


    name=fields.Many2one('res.partner',string='User Name')
    chat=fields.Char(string='Your Question')
    ans=fields.Text(string='Answer',readonly=1)

    def deepseek_answer(self):
        base_url='https://api.deepseek.com'
        api_key='sk-7afa7a6778b64bebae63351ee19ab42e'
        response = requests.get(base_url, params={'msg':'hello','appid':api_key})
        print(response,"response")

        # for rec in self:
        #     argument = {
        #         'q': rec.chat,
        #         'appid': api_key,}
        #     response=requests.get(base_url,params=argument)
        #     data=response.json()
        #     print(data)
        #     rec.ans=data

        # for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
        client = OpenAI(api_key=api_key, base_url=base_url)

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Hello"},
            ],
            max_tokens=1024,
            temperature=0.7,
            stream=False
        )

        print(response.choices[0].message.content)

        #
        # url = "https://api.deepseek.com"
        #
        # payload = json.dumps({
        #     "messages": [
        #         {
        #             "content": "You are a helpful assistant",
        #             "role": "system"
        #         },
        #         {
        #             "content": "Hi",
        #             "role": "user"
        #         }
        #     ],
        #     "model": "deepseek-chat",
        #     "frequency_penalty": 0,
        #     "max_tokens": 2048,
        #     "presence_penalty": 0,
        #     "response_format": {
        #         "type": "text"
        #     },
        #     "stop": None,
        #     "stream": False,
        #     "stream_options": None,
        #     "temperature": 1,
        #     "top_p": 1,
        #     "tools": None,
        #     "tool_choice": "none",
        #     "logprobs": False,
        #     "top_logprobs": None
        # })
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Accept': 'application/json',
        #     'Authorization': '"sk-7afa7a6778b64bebae63351ee19ab42e"'
        # }
        # param={
        #     'msg': self.chat,
        #     api_key:api_key
        # }
        #
        # response = requests.request("GET", url,timeout=100)
        #
        # print(response.text)
        # self.ans=response

