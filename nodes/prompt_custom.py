import os
from ..modules.build_prompt import BuildPrompt
from ..modules.build_prompt import buildOptionList, buildClassifyDatas
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config



def _ReadClassifyList():
    # 获取Script的目录路径
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    custom_dir = os.path.join(script_dir, "..", "user")
    filenames = os.listdir(custom_dir)

    classify_list = []
    for filename in filenames:
        if filename.endswith("_datas.jsonl") and os.path.isfile(os.path.join(custom_dir, filename)):
            data_name = filename.replace("_datas.jsonl", "")
            data_name = data_name.replace("_", "")
            classify_list.append(data_name)

    return classify_list



# Custom Prompt
class CustomPrompt:

    @classmethod
    def INPUT_TYPES(s):

        classify_list = _ReadClassifyList()
        classify_list = buildOptionList(classify_list, True, False)
        custom_data_list = buildOptionList([], True, True)

        return {
            "required": {
                "classify": (classify_list, {
                    "default": DEFAULT_OPTION
                }),
                "prompt": (custom_data_list, {
                    "default": DEFAULT_OPTION
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "preset_prompt": ("STRING", {
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

    def prompt_generate(self, classify, prompt="", seed=0, preset_prompt="", input_prompt=""):
 
        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if preset_prompt != "":
            prompt_words.append(preset_prompt)

        if classify != EMPTY_OPTION:

            if prompt == RANDOM_OPTION:
                # 获取Script的目录路径
                script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
                classify_datas = buildClassifyDatas(classify)
                custom_filename = f"{classify_datas}.jsonl"
                custom_data_filename = os.path.join(script_dir, "..", "user", custom_filename)

                build = BuildPrompt(custom_data_filename)
                prompt = build.generate_prompt(seed)
                if prompt != "":
                    prompt_words.append(prompt)

            elif prompt != EMPTY_OPTION:
                prompt_words.append(prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )

        

