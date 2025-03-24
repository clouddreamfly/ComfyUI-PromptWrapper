
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch


def translation(model_path, task_prefix, input_text, max_length):

    # 
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    #
    model = T5ForConditionalGeneration.from_pretrained(model_path)

    # when generating, we will use the logits of right-most token to predict the next token
    # so the padding should be on the left
    tokenizer.padding_side = "left"
    tokenizer.pad_token = tokenizer.eos_token # to avoid an error
    
    input_task_text = task_prefix + input_text
    inputs = tokenizer(input_task_text, return_tensors="pt", padding=False)

    output_sequences = model.generate(
        input_ids=inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        do_sample=False, # disable sampling to test if batching affects output
        max_length=max_length,
        num_beams=4, 
        early_stopping=True
    )
    
    output_text = tokenizer.batch_decode(output_sequences, skip_special_tokens=True)

    return output_text[0][len("<pad> "):]



if __name__ == '__main__':

    model_path = r"D:\WorkSpace\AIPaint\sd-comfyui-app\models\nlp\t5-small"
    task_prefix = "translate English to German: "
    input_text = "Create a new string object from the given object. "
    max_length = 512
    
    output_text = translation(model_path, task_prefix, input_text, max_length)
    
    print("output:")
    print(output_text)