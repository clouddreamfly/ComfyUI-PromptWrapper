import os
from ..modules.build_prompt import BuildPrompt
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config




# Scenery Prompt 
class SceneryPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # 选择语言
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                "seed": ("INT", { "default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF }),
                # 预设前缀提示词
                "preset_prefix": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                # 预设后缀提示词
                "preset_suffix": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate_prompt"
    CATEGORY = "PromptWrapper"

    def generate_prompt(self, language, seed,
        preset_prefix="", preset_suffix="", input_prompt=""):
        
        # 获取Script的目录路径
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
        language_dir = config.assets[language] if language in config.assets else config.assets["default"]
        data_file = os.path.join(script_dir, "..", "assets", language_dir, "scenery_datas.jsonl")

        build = BuildPrompt(data_file)
        scenery_prompt = build.generate_prompt(seed)

        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        scenery_prompt = preset_prefix + scenery_prompt + preset_suffix
        if scenery_prompt != "":
            prompt_words.append(scenery_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
 
        return (output_prompt, )

