import os
from ..modules.build_prompt import buildOptionList, buildPromptWeight, build_prompt_manager
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config


# Light Prompt 光影提示词
class LightPrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (["Chinese", "English"],{
                    "default": "Chinese",
                }),
                # 光的类型
                "light_type": (buildOptionList(build_prompt_manager.light_type_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 光的类型权重
                "light_type_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 光的色
                "light_color": (buildOptionList(build_prompt_manager.light_color_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 光的色彩权重
                "light_color_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 光的方向
                "light_direction": (buildOptionList(build_prompt_manager.light_direction_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 光的方向权重
                "light_direction_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 随机种子值
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                # 启用
                "enable": ("BOOLEAN", {"default": True}),
                # 预设提示词
                "preset_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                })
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            }
        }
    

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "prompt_generate"
    CATEGORY = "PromptWrapper"


    def prompt_generate(self,
        language="",
        light_type=EMPTY_OPTION,
        light_type_weight=1,
        light_color=EMPTY_OPTION,
        light_color_weight=0,
        light_direction=EMPTY_OPTION,
        light_direction_weight=0,
        seed=0,
        enable=True,
        preset_prompt="",
        input_prompt=""
    ):
        
        language = "zh" if language == "Chinese" else "en"
        build_prompt_manager.reload_build_prompt_datas(language)

        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if preset_prompt != "":
            prompt_words.append(preset_prompt)

        if enable == True:
            light_prompt = build_prompt_manager.generate_light_prompt(
                light_type=light_type,
                light_type_weight=light_type_weight,
                light_color=light_color,
                light_color_weight=light_color_weight,
                light_direction=light_direction,
                light_direction_weight=light_direction_weight,
                seed=seed
            )

            if light_prompt != "":
                prompt_words.append(light_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
        
        return (output_prompt, )
