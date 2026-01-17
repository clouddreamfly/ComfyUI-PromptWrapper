from .nodes.prompt_translation import PromptTranslation, PromptTranslationHY
from .nodes.prompt_generate import GeneratePrompt
from .nodes.prompt_scenery import SceneryPrompt
from .nodes.prompt_negative import NegativePrompt
from .nodes.prompt_light import LightPrompt
from .nodes.prompt_draw_artist import DrawArtistPrompt
from .nodes.prompt_draw_style import DrawStylePrompt
from .nodes.prompt_portrait import PortraitPrompt
from .nodes.prompt_portrait import PortraitSkinPrompt
from .nodes.prompt_portrait import PortraitFashionPrompt
from .nodes.prompt_portrait import PortraitPosePrompt
from .nodes.prompt_portrait import PortraitCosmeticPrompt
from .nodes.prompt_combine import CombinePrompt, MultiCombinePrompt
from .nodes.prompt_replace import ReplacePrompt, MultiReplacePrompt
from .nodes.prompt_custom import CustomPrompt
from .nodes.prompt_save import SavePrompt
from .nodes.prompt_text import InputPrompt, RandomLinePrompt
from .nodes.prompt_preview import PreviewPrompt
from .nodes.prompt_randoms import RandomsPrompt, RandomsWeightPrompt



NODE_CLASS_MAPPINGS = {
    "PromptTranslation": PromptTranslation,
    "PromptTranslationHY": PromptTranslationHY,
    "GeneratePrompt": GeneratePrompt,
    "SceneryPrompt" : SceneryPrompt,
    "NegativePrompt" : NegativePrompt,
    "LightPrompt" : LightPrompt,
    "DrawArtistPrompt" : DrawArtistPrompt,
    "DrawStylePrompt" : DrawStylePrompt,
    "PortraitPrompt": PortraitPrompt,
    "PortraitSkinPrompt": PortraitSkinPrompt,
    "PortraitFashionPrompt": PortraitFashionPrompt,
    "PortraitPosePrompt": PortraitPosePrompt,
    "PortraitCosmeticPrompt": PortraitCosmeticPrompt,
    "CombinePrompt": CombinePrompt,
    "MultiCombinePrompt": MultiCombinePrompt,
    "ReplacePrompt": ReplacePrompt,
    "MultiReplacePrompt": MultiReplacePrompt,
    "CustomPrompt": CustomPrompt,
    "SavePrompt": SavePrompt,
    "InputPrompt": InputPrompt,
    "RandomLinePrompt": RandomLinePrompt,
    "RandomsPrompt": RandomsPrompt,
    "RandomsWeightPrompt": RandomsWeightPrompt,
    "PreviewPrompt": PreviewPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTranslation": "Prompt Translation",
    "PromptTranslationHY": "Prompt Translation HY",
    "GeneratePrompt": "Generate Prompt",
    "SceneryPrompt": "Generate Scenery Prompt",
    "NegativePrompt": "Generate Negative Prompt",
    "LightPrompt": "Generate Light Prompt",
    "DrawArtistPrompt" : "Generate Draw Artist Prompt",
    "DrawStylePrompt" : "Generate Draw Style Prompt",
    "PortraitPrompt": "Portrait Prompt",
    "PortraitSkinPrompt": "Portrait Skin Prompt",
    "PortraitFashionPrompt": "Portrait Fashion Prompt",
    "PortraitPosePrompt": "Portrait Pose Prompt",
    "PortraitCosmeticPrompt": "Portrait Cosmetic Prompt",
    "CombinePrompt": "Combine Prompt",
    "MultiCombinePrompt": "Multi Combine Prompt",
    "ReplacePrompt": "Replace Prompt",
    "MultiReplacePrompt": "Multi Replace Prompt",
    "CustomPrompt": "Custom Prompt",
    "SavePrompt": "Save Prompt",
    "InputPrompt": "Input Prompt",
    "RandomLinePrompt": "Random Line Prompt",
    "RandomsPrompt": "Randoms Prompt",
    "RandomsWeightPrompt": "Randoms Weight Prompt",
    "PreviewPrompt": "Preview Prompt",
}

WEB_DIRECTORY = "./nodejs"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY'] 

