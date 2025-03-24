
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import torch


def translation(model_path, input_text):

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    OutputPipeline = pipeline("translation", model=model, tokenizer=tokenizer, device=device)

    output_text = OutputPipeline(input_text)
    
    return output_text[0]["translation_text"]



if __name__ == '__main__':

    model_path = r"D:\WorkSpace\AIPaint\sd-comfyui-app\models\nlp\Helsinki-NLP\opus-mt-zh-en"
    input_text = "中文翻译英文"
    
    output_text = translation(model_path, input_text)
    
    print("output:")
    print(output_text)