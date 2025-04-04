import os
from ..modules.build_prompt import buildOptionList, buildPromptWeight, build_prompt_manager
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config


# Draw Style Prompt 绘画风格提示词
class DrawStylePrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (["Chinese", "English"],{
                    "default": "Chinese",
                }),
                # 绘画风格
                "draw_style_1": (buildOptionList(build_prompt_manager.draw_style_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画风格权重
                "draw_style_1_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画风格
                "draw_style_2": (buildOptionList(build_prompt_manager.draw_style_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画风格权重
                "draw_style_2_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画风格
                "draw_style_3": (buildOptionList(build_prompt_manager.draw_style_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画风格权重
                "draw_style_3_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画风格
                "draw_style_4": (buildOptionList(build_prompt_manager.draw_style_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画风格权重
                "draw_style_4_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画风格
                "draw_style_5": (buildOptionList(build_prompt_manager.draw_style_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画风格权重
                "draw_style_5_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
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
        draw_style_1=EMPTY_OPTION,
        draw_style_1_weight=1,
        draw_style_2=EMPTY_OPTION,
        draw_style_2_weight=0,
        draw_style_3=EMPTY_OPTION,
        draw_style_3_weight=0,
        draw_style_4=EMPTY_OPTION,
        draw_style_4_weight=0,
        draw_style_5=EMPTY_OPTION,
        draw_style_5_weight=0,
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
            draw_style_prompt = build_prompt_manager.generate_draw_style_prompt(
                draw_style_1=draw_style_1,
                draw_style_1_weight=draw_style_1_weight,
                draw_style_2=draw_style_2,
                draw_style_2_weight=draw_style_2_weight,
                draw_style_3=draw_style_3,
                draw_style_3_weight=draw_style_3_weight,
                draw_style_4=draw_style_4,
                draw_style_4_weight=draw_style_4_weight,
                draw_style_5=draw_style_5,
                draw_style_5_weight=draw_style_5_weight,
                seed=seed
            )

            if draw_style_prompt != "":
                prompt_words.append(draw_style_prompt)

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )