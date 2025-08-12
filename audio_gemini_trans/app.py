import gradio as gr
from google import genai
from googletrans import Translator
import os

GENAI_API_KEY = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=GENAI_API_KEY)
translator = Translator()

def describe_and_translate(audio_path):
    # audio_path는 filepath 문자열임

    # 파일 업로드
    myfile = client.files.upload(file=audio_path)

    # 모델 호출
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=["Describe this audio clip", myfile]
    )

    original_text = response.text

    # 번역
    translated = translator.translate(original_text, src='en', dest='ko')

    return original_text, translated.text

iface = gr.Interface(
    fn=describe_and_translate,
    inputs=gr.Audio(type="filepath", label="Audio File을 업로드 해주세요."),
    outputs=[gr.Textbox(label="영어"), gr.Textbox(label="한국어")],
    title="Gemini 기반 오디오 자동 설명 + 한국어 번역",
)

if __name__ == "__main__":
    iface.launch()
