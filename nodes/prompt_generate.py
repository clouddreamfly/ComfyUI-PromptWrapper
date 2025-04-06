import os
from ..modules.build_prompt import BuildPrompt, BuildPromptManager
from ..modules.build_prompt import buildOptionList, buildClassifyDatas, buildPromptWeight, build_prompt_manager
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config



# Generate Prompt
class GeneratePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "language": (["Chinese", "English"], {
                    "default": "Chinese"
                }),
                "classify": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "preset_prefix": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
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
    FUNCTION = "prompt_generate"
    CATEGORY = "PromptWrapper"

    def prompt_generate(self, language, classify, seed, preset_prefix="", preset_suffix="", ainput_prompt=""):
 
        prompt_words = []

        if ainput_prompt != "":
            prompt_words.append(ainput_prompt)

        if classify != EMPTY_OPTION:
            # 获取Script的目录路径
            script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
            language_dir = "zh" if language == "Chinese" else "en"
        
            classify_datas = buildClassifyDatas(classify)
            file_name = f"{classify_datas}.jsonl"
            data_file = os.path.join(script_dir, "../assets", language_dir, file_name)

            build = BuildPrompt(data_file)
            prompt = build.generate_prompt(seed)

            prompt = preset_prefix + prompt + preset_suffix
            if prompt != "":
                prompt_words.append(prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )

        

