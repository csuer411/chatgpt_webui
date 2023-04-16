import gradio as gr
import openai
import config
openai.api_key = config.openai_api_key
prompt_words = config.prompt_words
def add_text(history, text):
    history = history + [(text, None)]
    return history, ""


def bot(history):
    messages = []
    for item in history:
        messages.append({"role": "user", "content": item[0]})
        messages.append({"role": "assistant", "content": item[1]})
    messages = messages[:-1]
    messages.insert(0, {"role": "system", "content": prompt_words})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)   
    response = response['choices'][0]['message']['content']
    history[-1][1] = response
    return history

with gr.Blocks() as demo:
    with gr.Column():
        chatbot = gr.Chatbot([], elem_id="chatbot")
        question = gr.Textbox(
                show_label=False,
                placeholder="Enter your prompt here...",
            ).style(width="90%")
        clear = gr.Button("Clear").style(width="10%")
    clear.click(lambda: None, None, chatbot, question)
    question.submit(add_text, [chatbot, question], [chatbot, question]).then(
        bot, chatbot, chatbot
    )

demo.launch()
