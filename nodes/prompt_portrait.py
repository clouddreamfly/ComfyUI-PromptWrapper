import os
from ..modules.build_prompt import buildOptionList, buildPromptWeight, build_prompt_manager
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config


# Portrait Prompt 人像提示词
class PortraitPrompt:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                # 镜头角度
                "lens_angle": (buildOptionList(build_prompt_manager.lens_angle_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 镜头角度权重
                "lens_angle_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 国籍1
                "nationality_1": (buildOptionList(build_prompt_manager.nationality_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 国籍2
                "nationality_2": (buildOptionList(build_prompt_manager.nationality_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 国籍混合权重
                "nationality_mix_weight": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 性别
                "gender": (buildOptionList(build_prompt_manager.gender_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 双性化权重
                "androgynous_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 年龄
                "age": (buildOptionList(build_prompt_manager.age_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 年龄权重
                "age_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 身体部分
                "body_part": (buildOptionList(build_prompt_manager.body_part_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 身体部分权重
                "body_part_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 体型类型
                "body_type": (buildOptionList(build_prompt_manager.body_type_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 体型类型权重
                "body_type_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 脸型
                "face_shape": (buildOptionList(build_prompt_manager.face_shape_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 脸型权重
                "face_shape_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 漂亮的脸权重
                "pretty_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 普通的脸权重
                "ordinary_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 丑陋的脸权重
                "ugly_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 面部不对称权重
                "facial_asymmetry_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 脸部的表情
                "facial_expression": (buildOptionList(build_prompt_manager.facial_expression_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                 # 脸部的表情权重
                "facial_expression_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼睛形状
                "eyes_shape": (buildOptionList(build_prompt_manager.eyes_shape_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 眼睛的颜色
                "eyes_color": (buildOptionList(build_prompt_manager.eyes_color_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 眉毛风格
                "eyebrows_style": (buildOptionList(build_prompt_manager.eyebrows_style_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 眉毛颜色
                "eyebrows_color": (buildOptionList(build_prompt_manager.eyebrows_color_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 睫毛风格
                "eyelashs_style": (buildOptionList(build_prompt_manager.eyelashs_style_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 睫毛颜色
                "eyelashs_color": (buildOptionList(build_prompt_manager.eyelashs_color_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 鼻子形状
                "nose_shape": (buildOptionList(build_prompt_manager.nose_shape_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 头发风格
                "hair_style": (buildOptionList(build_prompt_manager.hair_style_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 头发的颜色
                "hair_color": (buildOptionList(build_prompt_manager.hair_color_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 头发的长度
                "hair_length": (buildOptionList(build_prompt_manager.hair_length_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 蓬松度权重
                "disheveled_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 嘴巴形状
                "mouth_shape": (buildOptionList(build_prompt_manager.mouth_shape_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 嘴唇形状
                "lips_shape": (buildOptionList(build_prompt_manager.lips_shape_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 嘴唇颜色
                "lips_color": (buildOptionList(build_prompt_manager.lips_color_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 胡须风格
                "beard_style": (buildOptionList(build_prompt_manager.beard_style_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 胡须颜色
                "beard_color": (buildOptionList(build_prompt_manager.beard_color_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 胡须长度
                "beard_length": (buildOptionList(build_prompt_manager.beard_length_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 随机种子值
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                # 启用
                "enable": ("BOOLEAN", {"default": True}),
                # 预设提示词
                "preset_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
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

    def prompt_generate(self,
            language,
            lens_angle=EMPTY_OPTION,
            lens_angle_weight=1,
            nationality_1=EMPTY_OPTION,
            nationality_2=EMPTY_OPTION,
            nationality_mix_weight=0.5,
            gender=EMPTY_OPTION,
            androgynous_weight=0,
            age=18,
            age_weight=1,
            body_part=EMPTY_OPTION,
            body_part_weight=1,
            body_type=EMPTY_OPTION,
            body_type_weight=1,
            face_shape=EMPTY_OPTION,
            face_shape_weight=1,
            pretty_face_weight=1,
            ordinary_face_weight=0,
            ugly_face_weight=0,
            facial_asymmetry_weight=0,
            facial_expression=EMPTY_OPTION,
            facial_expression_weight=1,
            eyes_shape=EMPTY_OPTION,
            eyes_color=EMPTY_OPTION,
            eyebrows_style=EMPTY_OPTION,
            eyebrows_color=EMPTY_OPTION,
            eyelashs_style=EMPTY_OPTION,
            eyelashs_color=EMPTY_OPTION,
            nose_shape=EMPTY_OPTION,
            hair_style=EMPTY_OPTION,
            hair_color=EMPTY_OPTION,
            hair_length=EMPTY_OPTION,
            disheveled_weight=0,
            mouth_shape=EMPTY_OPTION,
            lips_shape=EMPTY_OPTION,
            lips_color=EMPTY_OPTION,
            beard_style=EMPTY_OPTION,
            beard_color=EMPTY_OPTION,
            beard_length=EMPTY_OPTION,
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
            portrait_prompt = build_prompt_manager.generate_portrait_prompt(
                lens_angle=lens_angle,
                lens_angle_weight=lens_angle_weight,
                nationality_1=nationality_1,
                nationality_2=nationality_2,
                nationality_mix_weight=nationality_mix_weight,
                gender=gender,
                androgynous_weight=androgynous_weight,
                age=age,
                age_weight=age_weight,
                body_part=body_part,
                body_part_weight=body_part_weight,
                body_type=body_type,
                body_type_weight=body_type_weight,
                face_shape=face_shape,
                face_shape_weight=face_shape_weight,
                pretty_face_weight=pretty_face_weight,
                ordinary_face_weight=ordinary_face_weight,
                ugly_face_weight=ugly_face_weight,
                facial_asymmetry_weight=facial_asymmetry_weight,
                facial_expression=facial_expression,
                facial_expression_weight=facial_expression_weight,
                eyes_shape=eyes_shape,
                eyes_color=eyes_color,
                eyebrows_style=eyebrows_style,
                eyebrows_color=eyebrows_color,
                eyelashs_style=eyelashs_style,
                eyelashs_color=eyelashs_color,
                nose_shape=nose_shape,
                hair_style=hair_style,
                hair_color=hair_color,
                hair_length=hair_length,
                disheveled_weight=disheveled_weight,
                mouth_shape=mouth_shape,
                lips_shape=lips_shape,
                lips_color=lips_color,
                beard_style=beard_style,
                beard_color=beard_color,
                beard_length=beard_length,
                seed=seed
            )

            if portrait_prompt != "":
                prompt_words.append(portrait_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )



# Portrait Skin Prompt 人像皮肤提示词
class PortraitSkinPrompt:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                # 皮肤
                "skin": (buildOptionList(build_prompt_manager.skin_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 皮肤权重
                "skin_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                 # 皮肤细节权重
                "skin_details_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皮肤毛孔权重
                "skin_pores_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皮肤瑕疵权重
                "skin_imperfections_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皮肤粉刺权重
                "skin_acne_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 晒黑的皮肤权重
                "tanned_skin_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 素颜权重
                "bare_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 湿润的脸权重
                "moist_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 干燥的脸权重
                "dried_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 酒窝权重
                "dimples_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皱纹权重
                "wrinkles_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 雀斑权重
                "freckles_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 痣权重
                "moles_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼部细节权重
                "eyes_details_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 圆形瞳孔权重
                "circular_pupils_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 虹膜细节权重
                "iris_details_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 圆形虹膜权重
                "circular_iris_weight": ("FLOAT", {
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

    def prompt_generate(
            self,
            language="",
            skin=EMPTY_OPTION,
            skin_weight=1,
            skin_details_weight=0,
            skin_pores_weight=0,
            skin_imperfections_weight=0,
            skin_acne_weight=0,
            tanned_skin_weight=0,
            bare_face_weight=0,
            moist_face_weight=0,
            dried_face_weight=0,
            dimples_weight=0,
            wrinkles_weight=0,
            freckles_weight=0,
            moles_weight=0,
            eyes_details_weight=0,
            circular_pupils_weight=0,
            iris_details_weight=0,
            circular_iris_weight=0,
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
            skin_prompt = build_prompt_manager.generate_portrait_skin_prompt(
                skin=skin,
                skin_weight=skin_weight,
                skin_details_weight=skin_details_weight,
                skin_pores_weight=skin_pores_weight,
                skin_imperfections_weight=skin_imperfections_weight,
                skin_acne_weight=skin_acne_weight,
                tanned_skin_weight=tanned_skin_weight,
                bare_face_weight=bare_face_weight,
                moist_face_weight=moist_face_weight,
                dried_face_weight=dried_face_weight,
                dimples_weight=dimples_weight,
                wrinkles_weight=wrinkles_weight,
                freckles_weight=freckles_weight,
                moles_weight=moles_weight,
                eyes_details_weight=eyes_details_weight,
                circular_pupils_weight=circular_pupils_weight,
                iris_details_weight=iris_details_weight,
                circular_iris_weight=circular_iris_weight,
                seed=seed
            )

            if skin_prompt != "":
                prompt_words.append(skin_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )




# Portrait Fashion Prompt 人像时装提示词
class PortraitFashionPrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                # 衣服
                "clothes": (buildOptionList(build_prompt_manager.clothes_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 衣服权重
                "clothes_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 衣服颜色
                "clothes_color": (buildOptionList(build_prompt_manager.clothes_color_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 衣服颜色权重
                "clothes_color_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 上衣
                "up_clothes": (buildOptionList(build_prompt_manager.up_clothes_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 上衣权重
                "up_clothes_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 下衣
                "down_clothes": (buildOptionList(build_prompt_manager.down_clothes_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 下衣权重
                "down_clothes_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 裤子
                "trousers": (buildOptionList(build_prompt_manager.trousers_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 裤子权重
                "trousers_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 内衣
                "underwear": (buildOptionList(build_prompt_manager.underwear_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 内衣权重
                "underwear_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 内库
                "underpants": (buildOptionList(build_prompt_manager.underpants_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 内库权重
                "underpants_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 袜子
                "socks": (buildOptionList(build_prompt_manager.socks_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 袜子权重
                "socks_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 鞋子
                "shoes": (buildOptionList(build_prompt_manager.shoes_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 鞋子权重
                "shoes_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 帽子
                "hat": (buildOptionList(build_prompt_manager.hat_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 帽子权重
                "hat_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 手套
                "gloves": (buildOptionList(build_prompt_manager.gloves_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 手套权重
                "gloves_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 头部装饰
                "head_decoration": (buildOptionList(build_prompt_manager.head_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 头部装饰权重
                "head_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 耳朵装饰
                "ears_decoration": (buildOptionList(build_prompt_manager.ears_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 耳朵装饰权重
                "ears_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 颈部装饰
                "neck_decoration": (buildOptionList(build_prompt_manager.neck_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 颈部装饰权重
                "neck_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 胸部装饰
                "chest_decoration": (buildOptionList(build_prompt_manager.chest_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 胸部装饰权重
                "chest_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腰部装饰
                "waist_decoration": (buildOptionList(build_prompt_manager.waist_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 腰部装饰权重
                "waist_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                 # 手臂装饰
                "arms_decoration": (buildOptionList(build_prompt_manager.arms_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 手臂装饰权重
                "arms_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 手部装饰
                "hands_decoration": (buildOptionList(build_prompt_manager.hands_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 手部装饰权重
                "hands_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腿部装饰
                "legs_decoration": (buildOptionList(build_prompt_manager.legs_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 腿部装饰权重
                "legs_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 脚部装饰
                "feet_decoration": (buildOptionList(build_prompt_manager.feet_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 脚部装饰权重
                "feet_decoration_weight": ("FLOAT", {
                    "default": 1,
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
        clothes=EMPTY_OPTION,
        clothes_weight=1,
        clothes_color=EMPTY_OPTION,
        clothes_color_weight=0,
        up_clothes=EMPTY_OPTION,
        up_clothes_weight=0,
        down_clothes=EMPTY_OPTION,
        down_clothes_weight=0,
        trousers=EMPTY_OPTION,
        trousers_weight=0,
        underwear=EMPTY_OPTION,
        underwear_weight=0,
        underpants=EMPTY_OPTION,
        underpants_weight=0,
        socks=EMPTY_OPTION,
        socks_weight=0,
        shoes=EMPTY_OPTION,
        shoes_weight=0,
        hat=EMPTY_OPTION,
        hat_weight=0,
        gloves=EMPTY_OPTION,
        gloves_weight=0,
        head_decoration=EMPTY_OPTION,
        head_decoration_weight=0,
        ears_decoration=EMPTY_OPTION,
        ears_decoration_weight=0,
        neck_decoration=EMPTY_OPTION,
        neck_decoration_weight=0,
        chest_decoration=EMPTY_OPTION,
        chest_decoration_weight=0,
        waist_decoration=EMPTY_OPTION,
        waist_decoration_weight=0,
        arms_decoration=EMPTY_OPTION,
        arms_decoration_weight=0,
        hands_decoration=EMPTY_OPTION,
        hands_decoration_weight=0,
        legs_decoration=EMPTY_OPTION,
        legs_decoration_weight=0,
        feet_decoration=EMPTY_OPTION,
        feet_decoration_weight=0,
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
            fashion_prompt = build_prompt_manager.generate_portrait_fashion_prompt(
                clothes=clothes,
                clothes_weight=clothes_weight,
                clothes_color=clothes_color,
                clothes_color_weight=clothes_color_weight,
                up_clothes=up_clothes,
                up_clothes_weight=up_clothes_weight,
                down_clothes=down_clothes,
                down_clothes_weight=down_clothes_weight,
                trousers=trousers,
                trousers_weight=trousers_weight,
                underwear=underwear,
                underwear_weight=underwear_weight,
                underpants=underpants,
                underpants_weight=underpants_weight,
                socks=socks,
                socks_weight=socks_weight,
                shoes=shoes,
                shoes_weight=shoes_weight,
                hat=hat,
                hat_weight=hat_weight,
                gloves=gloves,
                gloves_weight=gloves_weight,
                head_decoration=head_decoration,
                head_decoration_weight=head_decoration_weight,
                ears_decoration=ears_decoration,
                ears_decoration_weight=ears_decoration_weight,
                neck_decoration=neck_decoration,
                neck_decoration_weight=neck_decoration_weight,
                chest_decoration=chest_decoration,
                chest_decoration_weight=chest_decoration_weight,
                waist_decoration=waist_decoration,
                waist_decoration_weight=waist_decoration_weight,
                arms_decoration=arms_decoration,
                arms_decoration_weight=arms_decoration_weight,
                hands_decoration=hands_decoration,
                hands_decoration_weight=hands_decoration_weight,
                legs_decoration=legs_decoration,
                legs_decoration_weight=legs_decoration_weight,
                feet_decoration=feet_decoration,
                feet_decoration_weight=feet_decoration_weight,
                seed=seed
            )

            if fashion_prompt != "":
                prompt_words.append(fashion_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )




# Portrait Pose Prompt 人像姿态提示词
class PortraitPosePrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                # 姿态
                "pose": (buildOptionList(build_prompt_manager.pose_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 姿态权重
                "pose_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 动作
                "action":(buildOptionList(build_prompt_manager.action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 动作权重
                "action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 头部动作
                "head_action": (buildOptionList(build_prompt_manager.head_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 头部动作权重
                "head_action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 胸部动作
                "chest_action": (buildOptionList(build_prompt_manager.chest_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 胸部动作权重
                "chest_action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腰部动作
                "waist_action": (buildOptionList(build_prompt_manager.waist_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 腰部动作权重
                "waist_action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 手臂动作
                "arms_action": (buildOptionList(build_prompt_manager.arms_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 手臂动作权重
                "arms_action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 手部动作
                "hands_action": (buildOptionList(build_prompt_manager.hands_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 手部动作权重
                "hands_action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腿部动作
                "legs_action": (buildOptionList(build_prompt_manager.legs_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 腿部动作权重
                "legs_action_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 脚部动作
                "feet_action": (buildOptionList(build_prompt_manager.feet_action_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 脚部动作权重
                "feet_action_weight": ("FLOAT", {
                    "default": 1,
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
        pose=EMPTY_OPTION,
        pose_weight=1,
        action=EMPTY_OPTION,
        action_weight=0,
        head_action=EMPTY_OPTION,
        head_action_weight=0,
        chest_action=EMPTY_OPTION,
        chest_action_weight=0,
        waist_action=EMPTY_OPTION,
        waist_action_weight=0,
        arms_action=EMPTY_OPTION,
        arms_action_weight=0,
        hands_action=EMPTY_OPTION,
        hands_action_weight=0,
        legs_action=EMPTY_OPTION,
        legs_action_weight=0,
        feet_action=EMPTY_OPTION,
        feet_action_weight=0,
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
            pose_prompt = build_prompt_manager.generate_portrait_pose_prompt(
                pose=pose,
                pose_weight=pose_weight,
                action=action,
                action_weight=action_weight,
                head_action=head_action,
                head_action_weight=head_action_weight,
                chest_action=chest_action,
                chest_action_weight=chest_action_weight,
                waist_action=waist_action,
                waist_action_weight=waist_action_weight,
                arms_action=arms_action,
                arms_action_weight=arms_action_weight,
                hands_action=hands_action,
                hands_action_weight=hands_action_weight,
                legs_action=legs_action,
                legs_action_weight=legs_action_weight,
                feet_action=feet_action,
                feet_action_weight=feet_action_weight,
                seed=seed
            )

            if pose_prompt != "":
                prompt_words.append(pose_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
        
        return (output_prompt, )




# Portrait Cosmetics Prompt 人像化妆提示词
class PortraitCosmeticPrompt:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (config.languages, {
                    "default": config.languages[0]
                }),
                # 化妆风格
                "makeup_style": (buildOptionList(build_prompt_manager.makeup_style_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 化妆风格权重
                "makeup_style_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 化妆颜色
                "makeup_color": (buildOptionList(build_prompt_manager.makeup_color_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 化妆颜色权重
                "makeup_color_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼影权重
                "eyeshadow_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼线权重
                "eyeliner_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 烟熏权重
                "mascara_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腮红权重
                "blush_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 口红权重
                "lipstick_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "round": 0.01,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 唇彩权重
                "lip_gloss_weight": ("FLOAT", {
                    "default": 1,
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
        language='',
        makeup_style=EMPTY_OPTION,
        makeup_style_weight=1,
        makeup_color=EMPTY_OPTION,
        makeup_color_weight=0,
        eyeshadow_weight=0,
        eyeliner_weight=0,
        mascara_weight=0,
        blush_weight=0,
        lipstick_weight=0,
        lip_gloss_weight=0,
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
            cosmetic_prompt = build_prompt_manager.generate_portrait_cosmetic_prompt(
                makeup_style=makeup_style,
                makeup_style_weight=makeup_style_weight,
                makeup_color=makeup_color,
                makeup_color_weight=makeup_color_weight,
                eyeshadow_weight=eyeshadow_weight,
                eyeliner_weight=eyeliner_weight,
                mascara_weight=mascara_weight,
                blush_weight=blush_weight,
                lipstick_weight=lipstick_weight,
                lip_gloss_weight=lip_gloss_weight,
                seed=seed
            )

            if cosmetic_prompt != "":
                prompt_words.append(cosmetic_prompt)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return (output_prompt, )

