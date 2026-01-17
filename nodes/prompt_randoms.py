import os
from ..modules.build_prompt import BuildPrompt
from ..modules.build_prompt import buildOptionList, buildClassifyDatas, buildPromptWeight
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config



# Randoms Prompt 
class RandomsPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # 选择语言
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                "classify1": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify2": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify3": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify4": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify5": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify6": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify7": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify8": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "seed": ("INT", { "default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF }),
                # 启用
                "enable": ("BOOLEAN", {"default": True})
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "randoms_prompt"
    CATEGORY = "PromptWrapper"

    def randoms_prompt(self, language, classify1, classify2, classify3, classify4, classify5, classify6, classify7, classify8,
        seed=0, enable=True, input_prompt=""):
        
        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if enable == True:
            # 获取Script的目录路径
            script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
            language_dir = config.assets[language] if language in config.assets else config.assets["default"]
            classifys = [classify1, classify2, classify3, classify4, classify5, classify6, classify7, classify8]

            for classify in classifys:
                if classify != EMPTY_OPTION:
                    classify_datas = buildClassifyDatas(classify)
                    file_name = f"{classify_datas}.jsonl"
                    data_file = os.path.join(script_dir, "..", "assets", language_dir, file_name)

                    build = BuildPrompt(data_file)
                    prompt = build.generate_prompt(seed)

                    if prompt != "":
                        prompt_words.append(prompt)


        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )





# Randoms Weight Prompt
class RandomsWeightPrompt:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 选择语言
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                "classify1": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify1_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify2": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify2_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify3": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify3_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify4": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify4_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify5": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify5_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify6": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify6_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify7": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify7_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "classify8": (buildOptionList(config.classifies, True, False), {
                    "default": DEFAULT_OPTION
                }),
                "classify8_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                "seed": ("INT", { "default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF }),
                # 启用
                "enable": ("BOOLEAN", {"default": True})
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "randoms_weight_prompt"
    CATEGORY = "PromptWrapper"

    def randoms_weight_prompt(self, language, classify1, classify1_weight, classify2, classify2_weight, 
        classify3, classify3_weight, classify4, classify4_weight, classify5, classify5_weight, classify6, classify6_weight, 
        classify7, classify7_weight, classify8, classify8_weight, 
        seed=0, enable=True, input_prompt=""):
        
        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if enable == True:
            # 获取Script的目录路径
            script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
            language_dir = config.assets[language] if language in config.assets else config.assets["default"]
            classify_weights = [(classify1, classify1_weight), (classify2, classify2_weight), (classify3, classify3_weight),
                                (classify4, classify4_weight), (classify5, classify5_weight), (classify6, classify6_weight),
                                (classify7, classify7_weight), (classify8, classify8_weight)]

            for classify_weight in classify_weights:
                classify = classify_weight[0]
                weight = classify_weight[1]

                if classify != EMPTY_OPTION:
                    classify_datas = buildClassifyDatas(classify)
                    file_name = f"{classify_datas}.jsonl"
                    data_file = os.path.join(script_dir, "..", "assets", language_dir, file_name)

                    build = BuildPrompt(data_file)
                    prompt = buildPromptWeight(build.generate_prompt(seed), weight)

                    if prompt != "":
                        prompt_words.append(prompt)


        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )
