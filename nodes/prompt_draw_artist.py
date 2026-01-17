import os
from ..modules.build_prompt import buildOptionList, buildPromptWeight, build_prompt_manager
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config


# Draw Artist Prompt 绘画艺术提示词
class DrawArtistPrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                # 绘画艺术
                "draw_artist_1": (buildOptionList(build_prompt_manager.draw_artist_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画艺术权重
                "draw_artist_1_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画艺术
                "draw_artist_2": (buildOptionList(build_prompt_manager.draw_artist_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画艺术权重
                "draw_artist_2_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画艺术
                "draw_artist_3": (buildOptionList(build_prompt_manager.draw_artist_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画艺术权重
                "draw_artist_3_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画艺术
                "draw_artist_4": (buildOptionList(build_prompt_manager.draw_artist_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画艺术权重
                "draw_artist_4_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 绘画艺术
                "draw_artist_5": (buildOptionList(build_prompt_manager.draw_artist_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 绘画艺术权重
                "draw_artist_5_weight": ("FLOAT", {
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
        draw_artist_1=EMPTY_OPTION,
        draw_artist_1_weight=1,
        draw_artist_2=EMPTY_OPTION,
        draw_artist_2_weight=0,
        draw_artist_3=EMPTY_OPTION,
        draw_artist_3_weight=0,
        draw_artist_4=EMPTY_OPTION,
        draw_artist_4_weight=0,
        draw_artist_5=EMPTY_OPTION,
        draw_artist_5_weight=0,
        seed=0,
        enable=True,
        preset_prompt="",
        input_prompt=""
    ):
        
        language_dir = config.assets[language] if language in config.assets else config.assets["default"]
        build_prompt_manager.reload_build_prompt_datas(language_dir)

        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if preset_prompt != "":
            prompt_words.append(preset_prompt)

        if enable == True:
            draw_artist_prompt = build_prompt_manager.generate_draw_artist_prompt(
                draw_artist_1=draw_artist_1,
                draw_artist_1_weight=draw_artist_1_weight,
                draw_artist_2=draw_artist_2,
                draw_artist_2_weight=draw_artist_2_weight,
                draw_artist_3=draw_artist_3,
                draw_artist_3_weight=draw_artist_3_weight,
                draw_artist_4=draw_artist_4,
                draw_artist_4_weight=draw_artist_4_weight,
                draw_artist_5=draw_artist_5,
                draw_artist_5_weight=draw_artist_5_weight,
                seed=seed
            )

            if draw_artist_prompt != "":
                prompt_words.append(draw_artist_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )
 