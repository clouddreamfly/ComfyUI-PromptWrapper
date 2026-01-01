import os
import folder_paths
from ..modules import opus_translation
from ..modules import hunyuan_translation



# Prompt Translation
class PromptTranslation:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (["Helsinki-NLP/opus-mt-zh-en", "Helsinki-NLP/opus-mt-en-zh", "Helsinki-NLP/opus-mt-tc-bible-big-zhx-en"],),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful photo of"
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "prompt_translation"
    CATEGORY = "PromptWrapper"

    def prompt_translation(self, model_name, prompt):
 
        # 获取ComfyUI的models目录下的模型路径
        model_path = os.path.join(folder_paths.models_dir, "nlp", model_name)

        if not os.path.exists(model_path):
            raise ValueError(f"Local model not found at {model_path}. Please download the model and place it in the ComfyUI/models/nlp folder.")
        
        output_text = opus_translation.translation(model_path, prompt)
        
        return (output_text,)



# Hunyuan Translation Languages
SupportLanguages = [
    ("Chinese", "zh", "中文"),
    ("English", "en", "英语"),
    ("French", "fr", "法语"),
    ("Portuguese", "pt", "葡萄牙语"),
    ("Spanish", "es", "西班牙语"),
    ("Japanese", "ja", "日语"),
    ("Turkish", "tr", "土耳其语"),
    ("Russian", "ru", "俄语"),
    ("Arabic", "ar", "阿拉伯语"),
    ("Korean", "ko", "韩语"),
    ("Thai", "th", "泰语"),
    ("Italian", "it", "意大利语"),
    ("German", "de", "德语"),
    ("Vietnamese", "vi", "越南语"),
    ("Malay", "ms", "马来语"),
    ("Indonesian", "id", "印尼语"),
    ("Filipino", "tl", "菲律宾语"),
    ("Hindi", "hi", "印地语"),
    ("Traditional Chinese", "zh-Hant", "繁体中文"),
    ("Polish", "pl", "波兰语"),
    ("Czech", "cs", "捷克语"),
    ("Dutch", "nl", "荷兰语"),
    ("Khmer", "km", "高棉语"),
    ("Burmese", "my", "缅甸语"),
    ("Persian", "fa", "波斯语"),
    ("Gujarati", "gu", "古吉拉特语"),
    ("Urdu", "ur", "乌尔都语"),
    ("Telugu", "te", "泰卢固语"),
    ("Marathi", "mr", "马拉地语"),
    ("Hebrew", "he", "希伯来语"),
    ("Bengali", "bn", "孟加拉语"),
    ("Tamil", "ta", "泰米尔语"),
    ("Ukrainian", "uk", "乌克兰语"),
    ("Tibetan", "bo	", "藏语"),
    ("Kazakh", "kk", "哈萨克语"),
    ("Mongolian", "mn", "蒙古语"),
    ("Uyghur", "ug", "维吾尔语"),
    ("Cantonese", "yue", "粤语")
]

Languages = [ Language[0] for Language in SupportLanguages ]
ChineseNames = [ Language[2] for Language in SupportLanguages ]

# Prompt Translation HY
class PromptTranslationHY:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (["tencent/HY-MT1.5-1.8B", "tencent/Hunyuan-MT-7B"],),
                "target_language": (ChineseNames,),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful photo of"
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "prompt_translation"
    CATEGORY = "PromptWrapper"

    def prompt_translation(self, model_name, target_language, prompt):
 
        # 获取ComfyUI的models目录下的模型路径
        model_path = os.path.join(folder_paths.models_dir, "nlp", model_name)

        if not os.path.exists(model_path):
            raise ValueError(f"Local model not found at {model_path}. Please download the model and place it in the ComfyUI/models/nlp folder.")
        
        select_index = 0
        select_language = Languages[select_index]
        for language_name in ChineseNames:
            if target_language == language_name:
                select_language = Languages[select_index]
                break
            select_index += 1
        
        output_text = hunyuan_translation.translation2(model_path, select_language, prompt)
        
        return (output_text,)