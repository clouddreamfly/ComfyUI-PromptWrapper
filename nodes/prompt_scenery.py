import os
from ..modules.build_prompt import BuildPrompt
from ..modules.build_prompt import EMPTY_OPTION, RANDOM_OPTION, DEFAULT_OPTION
from ..modules.config import config


styles = [
    "none", "all"
]

artists = [
    "none", "all", "popular", "greg mode", "3D", "abstract", "angular",
    "anime", "architecture", "art nouveau", "art deco", "baroque", "bauhaus", "cartoon",
    "character", "children's illustration", "cityscape", "cinema", "clean", "cloudscape",
    "collage", "colorful", "comics", "cubism", "dark", "detailed", "digital", "expressionism",
    "fantasy", "fashion", "fauvism", "figurativism", "gore", "graffiti", "graphic design",
    "high contrast", "horror", "impressionism", "installation", "landscape", "light",
    "line drawing", "low contrast",	"luminism",	"magical realism", "manga",	"melanin",
    "messy", "monochromatic", "nature", "nudity", "photography", "pop art",	"portrait",
    "primitivism", "psychedelic", "realism", "renaissance",	"romanticism",
    "scene", "sci-fi", "sculpture",	"seascape",	"space", "stained glass", "still life",
    "storybook realism", "street art", "streetscape", "surrealism", "symbolism", "textile",
    "ukiyo-e", "vibrant", "watercolor", "whimsical"
]



# Scenery Prompt 
class SceneryPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # 选择语言
                "language": (["Chinese", "English"], {
                    "default": "Chinese"
                }),
                "style": (styles, { "default": DEFAULT_OPTION }),
                "artist": (artists, { "default": DEFAULT_OPTION }),
                "seed": ("INT", { "default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF }),
                # 预设前缀提示词
                "preset_prefix": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                # 预设后缀提示词
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
    FUNCTION = "generate_prompt"
    CATEGORY = "PromptWrapper"

    def generate_prompt(self, language, style, artist, seed,
        preset_prefix="", preset_suffix="", input_prompt=""):
 
        styles = (style,)
        artists = (artist,)
        
        # 获取Script的目录路径
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
        language_dir = "zh" if language == "Chinese" else "en"
        data_file = os.path.join(script_dir, "../assets", language_dir, "scenery_datas.jsonl")

        build = BuildPrompt(data_file)
        scenery_prompt = build.generate_prompt(seed, styles, artists)

        prompt_words = []

        if input_prompt != "":
            prompt_words.append(input_prompt)

        if preset_prefix != "":
            prompt_words.append(preset_prefix)

        if scenery_prompt != "":
            prompt_words.append(scenery_prompt)

        if preset_suffix != "":
            prompt_words.append(preset_suffix)

        if len(prompt_words) > 0:
            output_prompt = ", ".join(prompt_words)
            return (output_prompt, )
        else:
            return ("", )

