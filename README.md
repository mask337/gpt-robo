# about gpt-robo
## Folder Tree
- chatgpt
  - content_text
  - program
- hardware
  - model
  - program
    - base
    - motion
- s2t
- speech
- README.md

## chatgpt
### content_text
ChatGPTAPIに与える基本プロンプトの管理フォルダ
### program
ChatGPTAPIのやり取りをするプログラムフォルダ

## hardware
### model
ハードウェアの3D modelを管理するフォルダ
スライスしたデータも同梱予定
### program
RaspberryPiのプログラムや回路図等の管理フォルダ
直下に全体を制御するプログラムを配置する
#### base
RaspberryPiの電子部品制御プログラムの置き場
以降のプログラムはbase内のclassをimportして開発すること
#### motion
モーションのプログラムを配置する

## s2t
Speech to Textのプログラムフォルダ

## speech
発話機構のプログラムフォルダ

## README.md
This file

# Manual

## ChatGPT API
class name "gpt"
chatgpt talk function
return last message given by ChatGPT
```
gpt.response_gpt(response, user_content)
```
- response
past conversations and system messages
  - list
    - dict
      - role (system/user/assistant)
      - content string

- user_content
user input text
string type

### sample
response
```
[
{'role': 'system', 'content': 'あなたは友達です'}
{'role': 'user', 'content': 'こんにちは'},
{'role': 'assistant', 'content': 'こんにちは。何かお困りのことや話したいことがあれば、いつでもお気軽にお話しください。私ができる範囲でお手伝いいたします。'}
]
```
user_content
```
"私は人間です"
```

response_gpt
```
print(gpt.response_gpt(response, user_content))
```

result
```
'了解しました。何かお困りのことや話したいことがあれば、いつでもお気軽にお話しください。私ができる範囲でお手伝いいたします。'
```
