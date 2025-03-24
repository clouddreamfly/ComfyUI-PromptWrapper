import os
import folder_paths
from ..modules import opus_translation



# Prompt Translation
class PromptTranslation:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (["Helsinki-NLP/opus-mt-zh-en", "Helsinki-NLP/opus-mt-en-zh"],),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful photo of"
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "prompt_translation"
    CATEGORY = "PromptWrapper"

    def prompt_translation(self, model_name, prompt):
 
        # 获取ComfyUI的models目录下的模型路径
        model_path = os.path.join(folder_paths.models_dir, "nlp", model_name)

        if not os.path.exists(model_path):
            raise ValueError(f"Local model not found at {model_path}. Please download the model and place it in the ComfyUI/models/nlp folder.")
        
        output_text = opus_translation.translation(model_path, prompt)
        
        return (output_text,)
