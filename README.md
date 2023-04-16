由于chatgpt网页版不稳定，遂调用api搭建自己的网页
请确保拥有科学上网环境
### 1.运行环境设置

`git clone https://github.com/csuer411/chatgpt_webui.git`

`cd chatgpt_webui`

`pip install -r requirements.txt`

#### 2.修改密钥以及prompt

在 `config.py` 中修改`openai_api_key`的值为自己的密钥，你可以从这个网站得到 [platform.openai.com](https://platform.openai.com) 

同时修改 `prompt_words` 为自己的提示词

#### 3.运行

`python chatgpt.py `
