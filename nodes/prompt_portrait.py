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
                "language": (["Chinese", "English"],{
                    "default": "Chinese",
                }),
                # 镜头角度
                "lens_angle": (buildOptionList(build_prompt_manager.lens_angle_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 镜头角度权重
                "lens_angle_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
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
                    "step": 0.05,
                    "display": "slider",
                }),
                # 年龄
                "age": (buildOptionList(build_prompt_manager.age_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 体型类型
                "body_type": (buildOptionList(build_prompt_manager.body_type_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 体型类型权重
                "body_type_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                # 脸型
                "face_shape": (buildOptionList(build_prompt_manager.face_shape_prompt.get_dataset()), {
                    "default": DEFAULT_OPTION,
                }),
                # 脸型权重
                "face_shape_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                # 漂亮的脸权重
                "pretty_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 普通的脸权重
                "ordinary_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 丑陋的脸权重
                "ugly_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 面部不对称权重
                "facial_asymmetry_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
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
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
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

        language = "zh" if language == "Chinese" else "en"
        build_prompt_manager.reload_build_prompt_datas(language)

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

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )



# Portrait Skin Prompt 人像皮肤提示词
class PortraitSkinPrompt:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (["Chinese", "English"],{
                    "default": "Chinese",
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
                    "step": 0.05,
                    "display": "slider",
                }),
                 # 皮肤细节权重
                "skin_details_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皮肤毛孔权重
                "skin_pores_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皮肤瑕疵权重
                "skin_imperfections_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皮肤粉刺权重
                "skin_acne_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 晒黑的皮肤权重
                "tanned_skin_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 素颜权重
                "bare_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 湿润的脸权重
                "moist_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 干燥的脸权重
                "dried_face_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 酒窝权重
                "dimples_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 皱纹权重
                "wrinkles_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 雀斑权重
                "freckles_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 痣权重
                "moles_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼部细节权重
                "eyes_details_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 圆形瞳孔权重
                "circular_pupils_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 虹膜细节权重
                "iris_details_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 圆形虹膜权重
                "circular_iris_weight": ("FLOAT", {
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
        language = "zh" if language == "Chinese" else "en"
        build_prompt_manager.reload_build_prompt_datas(language)

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
                circular_pupil_weight=circular_pupil_weight,
                iris_details_weight=iris_details_weight,
                circular_iris_weight=circular_iris_weight,
                seed=seed
            )

            if skin_prompt != "":
                prompt_words.append(skin_prompt)

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )




# Portrait Fashion Prompt 人像时装提示词
class PortraitFashionPrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (["Chinese", "English"],{
                    "default": "Chinese",
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
                    "step": 0.05,
                    "display": "slider",
                }),
                # 下衣
                "down_chothes": (buildOptionList(build_prompt_manager.down_chothes_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 下衣权重
                "down_chothes_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
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
                    "step": 0.05,
                    "display": "slider",
                }),
                # 脖子装饰
                "neck_decoration": (buildOptionList(build_prompt_manager.neck_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 脖子装饰权重
                "neck_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腰间装饰
                "waist_decoration": (buildOptionList(build_prompt_manager.waist_decoration_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 腰间装饰权重
                "waist_decoration_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
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
        up_clothes=EMPTY_OPTION,
        up_clothes_weight=0,
        down_chothes=EMPTY_OPTION,
        down_chothes_weight=0,
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
        neck_decoration=EMPTY_OPTION,
        neck_decoration_weight=0,
        waist_decoration=EMPTY_OPTION,
        waist_decoration_weight=0,
        gloves=EMPTY_OPTION,
        gloves_weight=0,
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
            fashion_prompt = build_prompt_manager.generate_portrait_fashion_prompt(
                clothes=clothes,
                clothes_weight=clothes_weight,
                up_clothes=up_clothes,
                up_clothes_weight=up_clothes_weight,
                down_chothes=down_chothes,
                down_chothes_weight=down_chothes_weight,
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
                neck_decoration=neck_decoration,
                neck_decoration_weight=neck_decoration_weight,
                waist_decoration=waist_decoration,
                waist_decoration_weight=waist_decoration_weight,
                gloves=gloves,
                gloves_weight=gloves_weight,
                seed=0
            )

            if fashion_prompt != "":
                prompt_words.append(fashion_prompt)

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )



# Portrait Pose Prompt 人像姿态提示词
class PortraitPosePrompt:
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (["Chinese", "English"],{
                    "default": "Chinese",
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
                    "step": 0.05,
                    "display": "slider",
                }),
                # 头部姿态
                "head_pose": (buildOptionList(build_prompt_manager.head_pose_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 头部姿态权重
                "head_pose_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 胸部姿态
                "chest_pose": (buildOptionList(build_prompt_manager.chest_pose_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 胸部姿态权重
                "chest_pose_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 手部姿态
                "hand_pose": (buildOptionList(build_prompt_manager.hand_pose_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 手部姿态权重
                "hand_pose_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腿部姿态
                "leg_pose": (buildOptionList(build_prompt_manager.leg_pose_prompt.get_dataset()), {
                    "default": EMPTY_OPTION,
                }),
                # 腿部姿态权重
                "leg_pose_weight": ("FLOAT", {
                    "default": 1,
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
        pose=EMPTY_OPTION,
        pose_weight=1,
        action=EMPTY_OPTION,
        action_weight=0,
        head_pose=EMPTY_OPTION,
        head_pose_weight=0,
        chest_pose=EMPTY_OPTION,
        chest_pose_weight=0,
        hand_pose=EMPTY_OPTION,
        hand_pose_weight=0,
        leg_pose=EMPTY_OPTION,
        leg_pose_weight=0,
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
            pose_prompt = build_prompt_manager.generate_portrait_pose_prompt(
                pose=pose,
                pose_weight=pose_weight,
                action=action,
                action_weight=action_weight,
                head_pose=head_pose,
                head_pose_weight=head_pose_weight,
                chest_pose=chest_pose,
                chest_pose_weight=chest_pose_weight,
                hand_pose=hand_pose,
                hand_pose_weight=hand_pose_weight,
                leg_pose=leg_pose,
                leg_pose_weight=leg_pose_weight,
                seed=seed
            )

            if pose_prompt != "":
                prompt_words.append(pose_prompt)

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )


# Portrait Cosmetics Prompt 人像化妆提示词
class PortraitCosmeticPrompt:

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "required": {
                # 语言选择
                "language": (["Chinese", "English"],{
                    "default": "Chinese"
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
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼影权重
                "eyeshadow_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 眼线权重
                "eyeliner_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 烟熏权重
                "mascara_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 腮红权重
                "blush_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 口红权重
                "lipstick_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # 唇彩权重
                "lip_gloss_weight": ("FLOAT", {
                    "default": 1,
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
        
        language = "zh" if language == "Chinese" else "en"
        build_prompt_manager.reload_build_prompt_datas(language)

        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if preset_prompt != "":
            prompt_words.append(preset_prompt)

        if enable == True:
            cosmetic_prompt = generate_portrait_cosmetic_prompt(
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

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )
