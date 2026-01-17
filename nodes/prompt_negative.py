import os
from ..modules.build_prompt import BuildPrompt
from ..modules.config import config



# Negative Prompt
class NegativePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "preset_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "prompt_generate"
    CATEGORY = "PromptWrapper"

    def prompt_generate(self, language, seed, preset_prompt=""):
 
        # 获取Script的目录路径
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
        language_dir = config.assets[language] if language in config.assets else config.assets["default"]
        data_file = os.path.join(script_dir, "..", "assets", language_dir, "negative_datas.jsonl")

        build = BuildPrompt(data_file)
        negative_prompt = build.generate_prompt(seed)

        output_prompt = ""
        if preset_prompt != "" and negative_prompt != "":
            output_prompt = preset_prompt + "," + negative_prompt
        elif preset_prompt != "":
            output_prompt = preset_prompt
        elif negative_prompt != "":
            output_prompt = negative_prompt
        
        return (output_prompt,)
