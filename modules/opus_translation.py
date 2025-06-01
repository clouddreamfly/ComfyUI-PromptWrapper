
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import MarianMTModel, MarianTokenizer
from transformers import pipeline
import torch


def translation(model_path, input_text):

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    OutputPipeline = pipeline("translation", model=model, tokenizer=tokenizer, device=device)

    output_text = OutputPipeline(input_text)
    
    return output_text[0]["translation_text"]




def translation2(model_path, input_text):

    tokenizer = MarianTokenizer.from_pretrained(model_path)

    model = MarianMTModel.from_pretrained(model_path)

    translated = model.generate(**tokenizer(input_text, return_tensors="pt", padding=True))

    output_texts = []
    for trans in translated:
        output_texts.append(tokenizer.decode(trans, skip_special_tokens=True))

    output_text = ""
    if len(output_texts) > 0:
        output_text = ",".join(output_texts)

    return output_text




if __name__ == '__main__':

    model_path = r"D:\WorkSpace\AIPaint\sd-comfyui-app\models\nlp\Helsinki-NLP\opus-mt-tc-bible-big-zhx-en"
    input_text = "中文翻译英文，牡丹花，蓝色的花朵"
    
    output_text = translation2(model_path, input_text)
    
    print("output:")
    print(output_text)