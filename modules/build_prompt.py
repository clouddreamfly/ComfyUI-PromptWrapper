import os
from .dataset import Dataset, JsonlDataset, JsonDataset
from .config import config



EMPTY_OPTION = "--"
RANDOM_OPTION = "random 🎲"
DEFAULT_OPTION = EMPTY_OPTION

# 构建选项列表
def buildOptionList(option_list, is_empty=True, is_random=True):

    if option_list is None and is_empty == False and is_random == True:
        return []

    new_option_list = [EMPTY_OPTION] if is_empty == True else []

    if is_random == True:
        new_option_list.append(RANDOM_OPTION)

    if isinstance(option_list, list):
        new_option_list.extend(option_list)

    elif isinstance(option_list, Dataset):
        for index in range(len(option_list)):
            text, _, _, = option_list[index]
            new_option_list.append(text)

    return new_option_list


# 构建提示词与权重
def buildPromptWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight, 2)})"


# 构建分类数据
def buildClassifyDatas(text):
    return text.replace(" ", "_") + "_datas"


# 构建分类提示词
def buildClassifyPrompt(text):
    return text.replace(" ", "_") + "_prompt"


# 构建数据
def buildJsonDatas(text):
    return text.replace(" ", "_") + "_datas"


# 构建提示词
def buildJsonPrompt(text):
    return text.replace(" ", "_") + "_prompt"


# 构建提示词
class BuildPrompt:

    def __init__(self, path):
    
        ext = os.path.splitext(path)[1]
        if ext.lower() == ".json":
            self._dataset = JsonDataset(path)
        else:
            self._dataset = JsonlDataset(path)
        
        
    def get_dataset(self):

        return self._dataset


    def choice_prompt(self, seed):

        length = len(self._dataset)
        if length == 0:
            return ""

        index = seed % length
        datas = self._dataset[index]
        
        prompt = ""
        if isinstance(datas, tuple) or isinstance(datas, list):
            prompt = datas[0]
        elif isinstance(datas, str):
            prompt = datas

        return prompt


    def get_prompt(self, key):

        prompt = ""
        datas = getattr(self._dataset, key, None)
        if datas is not None:
            prompt = datas["text"] if "text" in datas else ""

        return prompt


    def generate_prompt(self, seed, styles="", artists=""):
        
        length = len(self._dataset)
        if length == 0:
            return ""

        index = seed % length
        datas = self._dataset[index]
        
        prompt = ""
        if isinstance(datas, tuple) or isinstance(datas, list):
            prompt = datas[0]
        elif isinstance(datas, str):
            prompt = datas

        return prompt



# 构建提示词管理
class BuildPromptManager:

    def __init__(self, path, config, language="zh"):

        self.path = path
        self.config = config
        self.language = language
        self.build_prompts = self.load_build_prompt_datas(path, config, language)


    def reload_build_prompt_datas(self, language="zh"):

        if self.language != language:
            self.language = language
            self.build_prompts = self.load_build_prompt_datas(self.path, self.config, self.language)


    def load_build_prompt_datas(self, path, config, language="zh"):

        build_prompts = {}
        for classify in config.classifies:
            
            classify_datas = buildClassifyDatas(classify)
            classify_prompt = buildClassifyPrompt(classify)
            file_name = f"{classify_datas}.jsonl"
            data_path = os.path.join(path, language, file_name)
            build_prompts[classify_prompt] = BuildPrompt(data_path)

        for data_name in config.json_datas:

            json_datas = buildJsonDatas(data_name)
            json_prompt = buildJsonPrompt(data_name)
            file_name = f"{json_datas}.json"
            data_path = os.path.join(path, language, file_name)
            build_prompts[json_prompt] = BuildPrompt(data_path)

        return build_prompts


    def __getattr__(self, key):

        return self.build_prompts[key] if key in self.build_prompts else None
    

    # 生成肖像提示词
    def generate_portrait_prompt(self,
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
        seed=0
    ):

        if lens_angle_weight > 0:
            if lens_angle == RANDOM_OPTION:
                lens_angle = self.lens_angle_prompt.choice_prompt(seed)
                lens_angle = buildPromptWeight(lens_angle, lens_angle_weight)
            elif lens_angle != EMPTY_OPTION:
                lens_angle = buildPromptWeight(lens_angle, lens_angle_weight)
            else:
                lens_angle = ""
        else:
            lens_angle = ""

        nationality = ""
        if nationality_1 != EMPTY_OPTION or nationality_2 != EMPTY_OPTION:
            if nationality_1 == RANDOM_OPTION:
                nationality_1 = self.nationality_prompt.choice_prompt(seed)
            if nationality_2 == RANDOM_OPTION:
                nationality_2 = self.nationality_prompt.choice_prompt(seed)

            if nationality_1 != EMPTY_OPTION and nationality_2 != EMPTY_OPTION:
                nationality = f"[{nationality_1}:{nationality_2}:{round(nationality_mix_weight, 2)}]"
                # nationality = buildPromptWeight(nationality, nationality_mix_weight)
            else:
                nationality = nationality_1 if nationality_1 != EMPTY_OPTION else nationality_2
                nationality = buildPromptWeight(nationality, 1.05)

        if gender == RANDOM_OPTION:
            gender = self.gender_prompt.choice_prompt(seed)
            gender = buildPromptWeight(gender, 1.05)
        elif gender != EMPTY_OPTION:
            gender = buildPromptWeight(gender, 1.05)
        else:
            gender = ""

        if androgynous_weight > 0:
            androgynous = self.portrait_prompt.get_prompt("androgynous")
            androgynous = buildPromptWeight(androgynous, androgynous_weight)
        else:
            androgynous = ""

        if age == RANDOM_OPTION:
            age = self.age_prompt.choice_prompt(seed)
            age = buildPromptWeight(age, 1.05)
        elif age != EMPTY_OPTION:
            age = buildPromptWeight(age, 1.05)
        else:
            age = ""

        if body_type_weight > 0:
            if body_type == RANDOM_OPTION:
                body_type = self.body_type_prompt.choice_prompt(seed)
                body_type = buildPromptWeight(body_type, body_type_weight)
            elif body_type != EMPTY_OPTION:
                body_type = buildPromptWeight(body_type, body_type_weight)
            else:
                body_type = ""
        else:
            body_type = ""

        if face_shape_weight > 0:
            if face_shape == RANDOM_OPTION:
                face_shape = self.face_shape_prompt.choice_prompt(seed)
                face_shape = buildPromptWeight(face_shape, face_shape_weight)
            elif face_shape != EMPTY_OPTION:
                face_shape = buildPromptWeight(face_shape, face_shape_weight)
            else:
                face_shape = ""
        else:
            face_shape = ""

        if pretty_face_weight > 0:
            pretty_face = self.portrait_prompt.get_prompt("pretty_face")
            pretty_face = buildPromptWeight(pretty_face, pretty_face_weight)
        else:
            pretty_face = ""

        if ordinary_face_weight > 0:
            ordinary_face = self.portrait_prompt.get_prompt("ordinary_face")
            ordinary_face = buildPromptWeight(ordinary_face, ordinary_face_weight)
        else:
            ordinary_face = ''
        
        if ugly_face_weight > 0:
            ugly_face = self.portrait_prompt.get_prompt("ugly_face")
            ugly_face = buildPromptWeight(ugly_face, ugly_face_weight)
        else:
            ugly_face = ""

        if facial_asymmetry_weight > 0:
            facial_asymmetry = self.portrait_prompt.get_prompt("facial_asymmetry")
            facial_asymmetry = buildPromptWeight(facial_asymmetry, facial_asymmetry_weight)
        else:
            facial_asymmetry = ""

        if facial_expression_weight > 0:
            if facial_expression == RANDOM_OPTION:
                facial_expression = self.facial_expression_prompt.choice_prompt(seed)
                facial_expression = buildPromptWeight(facial_expression, facial_expression_weight)
            elif facial_expression != EMPTY_OPTION:
                facial_expression = buildPromptWeight(facial_expression, facial_expression_weight)
            else:
                facial_expression = ""
        else:
            facial_expression = ""

        if eyes_shape == RANDOM_OPTION:
            eyes_shape = self.eyes_shape_prompt.choice_prompt(seed)
            eyes_shape = buildPromptWeight(eyes_shape, 1.05)
        elif eyes_shape != EMPTY_OPTION:
            eyes_shape = buildPromptWeight(eyes_shape, 1.05)
        else:
            eyes_shape = ""

        if eyes_color == RANDOM_OPTION:
            eyes_color = self.eyes_color_prompt.choice_prompt(seed)
            eyes_color = buildPromptWeight(eyes_color, 1.05)
        elif eyes_color != EMPTY_OPTION:
            eyes_color = buildPromptWeight(eyes_color, 1.05)
        else:
            eyes_color = ""

        if eyebrows_style == RANDOM_OPTION:
            eyebrows_style = self.eyebrows_style_prompt.choice_prompt(seed)
            eyebrows_style = buildPromptWeight(eyebrows_style, 1.05)
        elif eyebrows_style != EMPTY_OPTION:
            eyebrows_style = buildPromptWeight(eyebrows_style, 1.05)
        else:
            eyebrows_style = ""

        if eyebrows_color == RANDOM_OPTION:
            eyebrows_color = self.eyebrows_color_prompt.choice_prompt(seed)
            eyebrows_color = buildPromptWeight(eyebrows_color, 1.05)
        elif eyebrows_color != EMPTY_OPTION:
            eyebrows_color = buildPromptWeight(eyebrows_color, 1.05)
        else:
            eyebrows_color = ""
            
        if eyelashs_style == RANDOM_OPTION:
            eyelashs_style = self.eyelashs_style_prompt.choice_prompt(seed)
            eyelashs_style = buildPromptWeight(eyelashs_style, 1.05)
        elif eyelashs_style != EMPTY_OPTION:
            eyelashs_style = buildPromptWeight(eyelashs_style, 1.05)
        else:
            eyelashs_style = ""

        if eyelashs_color == RANDOM_OPTION:
            eyelashs_color = self.eyelashs_color_prompt.choice_prompt(seed)
            eyelashs_color = buildPromptWeight(eyelashs_color, 1.05)
        elif eyelashs_color != EMPTY_OPTION:
            eyelashs_color = buildPromptWeight(eyelashs_color, 1.05)
        else:
            eyelashs_color = ""

        if nose_shape == RANDOM_OPTION:
            nose_shape = self.nose_shape_prompt.choice_prompt(seed)
            nose_shape = buildPromptWeight(nose_shape, 1.05)
        elif nose_shape != EMPTY_OPTION:
            nose_shape = buildPromptWeight(nose_shape, 1.05)
        else:
            nose_shape = ""

        if hair_style == RANDOM_OPTION:
            hair_style = self.hair_style_prompt.choice_prompt(seed)
            hair_style = buildPromptWeight(hair_style, 1.05)
        elif hair_style != EMPTY_OPTION:
            hair_style = buildPromptWeight(hair_style, 1.05)
        else:
            hair_style = ""
        
        if hair_color == RANDOM_OPTION:
            hair_color = self.hair_color_prompt.choice_prompt(seed)
            hair_color = buildPromptWeight(hair_color, 1.05)
        elif hair_color != EMPTY_OPTION:
            hair_color = buildPromptWeight(hair_color, 1.05)
        else:
            hair_color = ""
        
        if hair_length == RANDOM_OPTION:
            hair_length = self.hair_length_prompt.choice_prompt(seed)
            hair_length = buildPromptWeight(hair_length, 1.05)
        elif hair_length != EMPTY_OPTION:
            hair_length = buildPromptWeight(hair_length, 1.05)
        else:
            hair_length = ""

        if disheveled_weight > 0:
            disheveled = self.portrait_prompt.get_prompt("disheveled")
            disheveled = buildPromptWeight(disheveled, disheveled_weight)
        else:
            disheveled = ""

        if mouth_shape == RANDOM_OPTION:
            mouth_shape = self.mouth_shape_prompt.choice_prompt(seed)
            mouth_shape = buildPromptWeight(mouth_shape, 1.05)
        elif mouth_shape != EMPTY_OPTION:
            mouth_shape = buildPromptWeight(mouth_shape, 1.05)
        else:
            mouth_shape = ""

        if lips_shape == RANDOM_OPTION:
            lips_shape = self.lips_shape_prompt.choice_prompt(seed)
            lips_shape = buildPromptWeight(lips_shape, 1.05)
        elif lips_shape != EMPTY_OPTION:
            lips_shape = buildPromptWeight(lips_shape, 1.05)
        else:
            lips_shape = ""

        if lips_color == RANDOM_OPTION:
            lips_color = self.lips_color_prompt.choice_prompt(seed)
            lips_color = buildPromptWeight(lips_color, 1.05)
        elif lips_color != EMPTY_OPTION:
            lips_color = buildPromptWeight(lips_color, 1.05)
        else:
            lips_color = ""

        if beard_style == RANDOM_OPTION:
            beard_style = self.beard_style_prompt.choice_prompt(seed)
            beard_style = buildPromptWeight(beard_style, 1.05)
        elif beard_style != EMPTY_OPTION:
            beard_style = buildPromptWeight(beard_style, 1.05)
        else:
            beard_style = ""

        if beard_color == RANDOM_OPTION:
            beard_color = self.beard_color_prompt.choice_prompt(seed)
            beard_color = buildPromptWeight(beard_color, 1.05)
        elif beard_color != EMPTY_OPTION:
            beard_color = buildPromptWeight(beard_color, 1.05)
        else:
            beard_color = ""

        if beard_length == RANDOM_OPTION:
            beard_length = self.beard_length_prompt.choice_prompt(seed)
            beard_length = buildPromptWeight(beard_length, 1.05)
        elif beard_length != EMPTY_OPTION:
            beard_length = buildPromptWeight(beard_length, 1.05)
        else:
            beard_length = ""

        build_words = [
            lens_angle,
            nationality, gender, androgynous, age, body_type,
            face_shape, pretty_face, ordinary_face, ugly_face, facial_asymmetry, facial_expression,
            eyes_shape, eyes_color, eyebrows_style, eyebrows_color, eyelashs_style, eyelashs_color,
            nose_shape,
            hair_style, hair_color, hair_length, disheveled,
            mouth_shape,
            lips_shape, lips_color,
            beard_style, beard_color, beard_length
        ]

        prompt_words = []
        for words in build_words:
            if words is not None and words != "":
                prompt_words.append(words)

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            
        return output_prompt


    # 生成人像皮肤提示词
    def generate_portrait_skin_prompt(self,
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
        seed=0
    ):

        prompt_words = []

        if skin_weight > 0:
            if skin == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.skin_prompt.choice_prompt(seed), skin_weight))
            elif skin != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(skin, skin_weight))

        if skin_details_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("skin_details"), skin_details_weight))

        if skin_pores_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("skin_pores"), skin_pores_weight))

        if skin_imperfections_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("skin_imperfections"), skin_imperfections_weight))

        if skin_acne_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("skin_acne"), skin_acne_weight))

        if tanned_skin_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("tanned_skin"), tanned_skin_weight))

        if bare_face_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("bare_face"), bare_face_weight))

        if moist_face_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("moist_face"), moist_face_weight))

        if dried_face_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("dried_face"), dried_face_weight))

        if dimples_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("dimples"), dimples_weight))

        if wrinkles_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("wrinkles"), wrinkles_weight))

        if freckles_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("freckles"), freckles_weight))

        if moles_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("moles"), moles_weight))

        if eyes_details_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("eyes_details"), eyes_details_weight))

        if circular_pupils_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("circular_pupil"), circular_pupils_weight))

        if iris_details_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("iris_details"), iris_details_weight))

        if circular_iris_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("circular_iris"), circular_iris_weight))


        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ', '.join(prompt_words)
            
        return output_prompt


    # 生成人像时装提示词
    def generate_portrait_fashion_prompt(self,
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
        seed=0
    ):

        prompt_words = []

        if clothes_weight > 0:
            if clothes == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.clothes_prompt.choice_prompt(seed), clothes_weight))
            elif clothes != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(clothes, clothes_weight))

        if clothes_color_weight > 0:
            if clothes_color == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.clothes_color_prompt.choice_prompt(seed), clothes_color_weight))
            elif clothes_color != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(clothes_color, clothes_color_weight))

        if up_clothes_weight > 0:
            if up_clothes == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.up_clothes_prompt.choice_prompt(seed), up_clothes_weight))
            elif up_clothes != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(up_clothes, up_clothes_weight))

        if down_clothes_weight > 0:
            if down_clothes== RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.down_clothes_prompt.choice_prompt(seed), down_clothes_weight))
            elif down_clothes != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(down_clothes, down_clothes_weight))

        if trousers_weight > 0:
            if trousers == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.trousers_prompt.choice_prompt(seed), trousers_weight))
            elif trousers != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(trousers, trousers_weight))

        if underwear_weight > 0:
            if underwear == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.underwear_prompt.choice_prompt(seed), underwear_weight))
            elif underwear != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(underwear, underwear_weight))

        if underpants_weight > 0:
            if underpants == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.underpants_prompt.choice_prompt(seed), underpants_weight))
            elif underpants != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(underpants, underpants_weight))

        if socks_weight > 0:
            if socks == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.socks_prompt.choice_prompt(seed), socks_weight))
            elif socks != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(socks, socks_weight))

        if shoes_weight > 0:
            if shoes == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.shoes_prompt.choice_prompt(seed), shoes_weight))
            elif shoes != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(shoes, shoes_weight))

        if hat_weight > 0:
            if hat == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.hat_prompt.choice_prompt(seed), hat_weight))
            elif hat != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(hat, hat_weight))

        if gloves_weight > 0:
            if gloves == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.gloves_prompt.choice_prompt(seed), gloves_weight))
            elif gloves != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(gloves, gloves_weight))

        if head_decoration_weight > 0:
            if head_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.head_decoration_prompt.choice_prompt(seed), head_decoration_weight))
            elif head_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(head_decoration, head_decoration_weight))

        if neck_decoration_weight > 0:
            if neck_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.neck_decoration_prompt.choice_prompt(seed), neck_decoration_weight))
            elif neck_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(neck_decoration, neck_decoration_weight))

        if chest_decoration_weight > 0:
            if chest_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.chest_decoration_prompt.choice_prompt(seed), chest_decoration_weight))
            elif chest_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(chest_decoration, chest_decoration_weight))

        if waist_decoration_weight > 0:
            if waist_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.waist_decoration_prompt.choice_prompt(seed), waist_decoration_weight))
            elif waist_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(waist_decoration, waist_decoration_weight))

        if arms_decoration_weight > 0:
            if arms_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.arms_decoration_prompt.choice_prompt(seed), arms_decoration_weight))
            elif arms_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(arms_decoration, arms_decoration_weight))

        if hands_decoration_weight > 0:
            if hands_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.hands_decoration_prompt.choice_prompt(seed), hands_decoration_weight))
            elif hands_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(hands_decoration, hands_decoration_weight))

        if legs_decoration_weight > 0:
            if legs_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.legs_decoration_prompt.choice_prompt(seed), legs_decoration_weight))
            elif legs_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(legs_decoration, legs_decoration_weight))

        if feet_decoration_weight > 0:
            if feet_decoration == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.feet_decoration_prompt.choice_prompt(seed), feet_decoration_weight))
            elif feet_decoration != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(feet_decoration, feet_decoration_weight))

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ', '.join(prompt_words)

        return output_prompt


    # 生成人像姿态提示词
    def generate_portrait_pose_prompt(self,
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
        seed=0
    ):

        prompt_words = []

        if pose_weight > 0:
            if pose == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.pose_prompt.choice_prompt(seed), pose_weight))
            elif pose != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(pose, pose_weight))

        if action_weight > 0:
            if action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.action_prompt.choice_prompt(seed), action_weight))
            elif action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(action, action_weight))

        if head_action_weight > 0:
            if head_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.head_action_prompt.choice_prompt(seed), head_action_weight))
            elif head_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(head_action, head_action_weight))

        if chest_action_weight > 0:
            if chest_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.chest_action_prompt.choice_prompt(seed), chest_action_weight))
            elif chest_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(chest_action, chest_action_weight))

        if waist_action_weight > 0:
            if waist_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.waist_action_prompt.choice_prompt(seed), waist_action_weight))
            elif waist_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(waist_action, waist_action_weight))

        if arms_action_weight > 0:
            if arms_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.arms_action_prompt.choice_prompt(seed), arms_action_weight))
            elif arms_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(arms_action, arms_action_weight))

        if hands_action_weight > 0:
            if hands_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.hands_action_prompt.choice_prompt(seed), hands_action_weight))
            elif hands_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(hands_action, hands_action_weight))

        if legs_action_weight > 0:
            if legs_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.legs_action_prompt.choice_prompt(seed), legs_action_weight))
            elif legs_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(legs_action, legs_action_weight))

        if feet_action_weight > 0:
            if feet_action == RANDOM_OPTION:
                prompt_words.append(buildPromptWeight(self.feet_action_prompt.choice_prompt(seed), feet_action_weight))
            elif feet_action != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(feet_action, feet_action_weight))

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ', '.join(prompt_words)

        return output_prompt



    # 生成人像化妆提示词
    def generate_portrait_cosmetic_prompt(self,
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
        seed=0
    ):
        prompt_words = []

        if makeup_style_weight > 0:
            if makeup_style == RANDOM_OPTION:
                makeup_style = self.makeup_style_prompt.choice_prompt(seed)
                prompt_words.append(buildPromptWeight(makeup_style, makeup_style_weight))
            elif makeup_style != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(makeup_style, makeup_style_weight))

        if makeup_color_weight > 0:
            if makeup_color == RANDOM_OPTION:
                makeup_color = self.makeup_color_prompt.choice_prompt(seed)
                prompt_words.append(buildPromptWeight(makeup_color, makeup_color_weight))
            elif makeup_color != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(makeup_color, makeup_color_weight))

        if eyeshadow_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("eyeshadow_make_up"), eyeshadow_weight))

        if eyeliner_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("eyeliner_make_up"), eyeliner_weight))

        if mascara_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("mascara_make_up"), mascara_weight))

        if blush_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("blush_make_up"), blush_weight))

        if lipstick_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("lipstick_make_up"), lipstick_weight))

        if lip_gloss_weight > 0:
            prompt_words.append(buildPromptWeight(self.portrait_prompt.get_prompt("lip_gloss_make_up"), lip_gloss_weight))

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ', '.join(prompt_words)

        return output_prompt


    # 生成光线提示词
    def generate_light_prompt(self,
        light_type=EMPTY_OPTION,
        light_type_weight=1,
        light_color=EMPTY_OPTION,
        light_color_weight=0,
        light_direction=EMPTY_OPTION,
        light_direction_weight=0,
        seed=0
    ):
        prompt_words = []

        if light_type_weight > 0:
            if light_type == RANDOM_OPTION:
                light_type = self.light_type_prompt.choice_prompt(seed)
                prompt_words.append(buildPromptWeight(light_type, light_type_weight))
            elif light_type != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(light_type, light_type_weight))

        if light_color_weight > 0:
            if light_color == RANDOM_OPTION:
                light_color = self.light_color_prompt.choice_prompt(seed)
                prompt_words.append(buildPromptWeight(light_color, light_color_weight))
            elif light_color != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(light_color, light_color_weight))

        if light_direction_weight > 0:
            if light_direction == RANDOM_OPTION:
                light_direction = self.light_direction_prompt.choice_prompt(seed)
                prompt_words.append(buildPromptWeight(light_direction, light_direction_weight))
            elif light_direction != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(light_direction, light_direction_weight))


        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ', '.join(prompt_words)

        return output_prompt


    # 生成绘画风格提示词
    def generate_draw_style_prompt(self,
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
        seed=0
    ):
        prompt_words = []

        if draw_style_1_weight > 0:
            if draw_style_1 == RANDOM_OPTION:
                draw_style_1 = self.draw_style_prompt.choice_prompt(seed)
                prompt_words.append(buildPromptWeight(draw_style_1, draw_style_1_weight))
            elif draw_style_1 != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(draw_style_1, draw_style_1_weight))

        if draw_style_2_weight > 0:
            if draw_style_2 == RANDOM_OPTION:
                draw_style_2 = self.draw_style_prompt.choice_prompt(seed + 1)
                prompt_words.append(buildPromptWeight(draw_style_2, draw_style_2_weight))
            elif draw_style_2 != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(draw_style_2, draw_style_2_weight))

        if draw_style_3_weight > 0:
            if draw_style_3 == RANDOM_OPTION:
                draw_style_3 = self.draw_style_prompt.choice_prompt(seed + 2)
                prompt_words.append(buildPromptWeight(draw_style_3, draw_style_3_weight))
            elif draw_style_3 != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(draw_style_3, draw_style_3_weight))

        if draw_style_4_weight > 0:
            if draw_style_4 == RANDOM_OPTION:
                draw_style_4 = self.draw_style_prompt.choice_prompt(seed + 3)
                prompt_words.append(buildPromptWeight(draw_style_4, draw_style_4_weight))
            elif draw_style_4 != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(draw_style_4, draw_style_4_weight))

        if draw_style_5_weight > 0:
            if draw_style_5 == RANDOM_OPTION:
                draw_style_5 = self.draw_style_prompt.choice_prompt(seed + 4)
                prompt_words.append(buildPromptWeight(draw_style_5, draw_style_5_weight))
            elif draw_style_5 != EMPTY_OPTION:
                prompt_words.append(buildPromptWeight(draw_style_5, draw_style_5_weight))

        output_prompt = ""
        if len(prompt_words) > 0:
            output_prompt = ', '.join(prompt_words)

        return output_prompt






# 初始化
def _init_build_prompt_manager():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(script_dir, "../assets")
    return BuildPromptManager(config_dir, config)

# 初始化
build_prompt_manager = _init_build_prompt_manager()


    