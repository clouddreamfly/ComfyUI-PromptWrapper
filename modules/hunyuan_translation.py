
from transformers  import AutoModelForCausalLM, AutoTokenizer



def translation(model_path, model_file, target_language, input_text):

    tokenizer = AutoTokenizer.from_pretrained(model_path, gguf_file=model_file, clean_up_tokenization_spaces=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, gguf_file=model_file, device_map="auto")  # You may want to use bfloat16 and/or move to GPU here
    messages = [
        {"role": "user", "content": "Translate the following segment into English, without additional explanation.\n\nGet something off your chest"},
    ]
    tokenized_chat = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=False,
        return_tensors="pt"
    )

    outputs = model.generate(tokenized_chat.to(model.device), max_new_tokens=2048)
    output_text = tokenizer.decode(outputs[0])
    
    return output_text


def translation2(model_path, target_language, input_text):

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")  # You may want to use bfloat16 and/or move to GPU here
    messages = [
        {"role": "user", "content": "Translate the following segment into {}, without additional explanation.\n\n{}".format(target_language, input_text)},
    ]
    tokenized_chat = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=False,
        return_tensors="pt"
    )

    outputs = model.generate(tokenized_chat.to(model.device), max_new_tokens=2048)
    output_content = tokenizer.decode(outputs[0])

    output_text = ""
    if output_content is not None:
        text_length = len(output_content)
        if text_length > 0:
            start_text = "<｜hy_place▁holder▁no▁8｜>"
            end_text = "<｜hy_place▁holder▁no▁2｜>"
            start_index = output_content.find(start_text)
            end_index = output_content.rfind(end_text)
            if start_index >= 0 and end_index >= 0:
                start_index += len(start_text)
                output_text = output_content[start_index : end_index]

    return output_text



if __name__ == '__main__':

    model_path = r"D:\WorkSpace\AIPaint\sd-comfyui-app\models\unet"
    model_file = "Hunyuan-MT-7B.Q4_K_S.gguf"
    target_language = "English"
    input_text = "牡秋天的枫叶，是诗人笔下的灵感源泉。古往今来，无数诗人为枫叶写下了优美的诗篇，赞美它的美丽、它的坚韧、它的浪漫。这些诗篇，如同枫叶一样，在岁月的长河中流传千古，成为了中华文化的瑰宝。"
    
    #output_text = translation(model_path, model_file, target_language, input_text)

    model_name_or_path = r"D:\WorkSpace\AIPaint\sd-comfyui-app\models\nlp\tencent\HY-MT1.5-1.8B"
    output_text = translation2(model_name_or_path, target_language, input_text)
    
    print("output:")
    print(output_text)