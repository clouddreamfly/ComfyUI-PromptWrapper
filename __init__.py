from .nodes.prompt_translation import PromptTranslation
from .nodes.prompt_generate import GeneratePrompt
from .nodes.prompt_scenery import SceneryPrompt
from .nodes.prompt_negative import NegativePrompt
from .nodes.prompt_light import LightPrompt
from .nodes.prompt_style import DrawStylePrompt
from .nodes.prompt_portrait import PortraitPrompt
from .nodes.prompt_portrait import PortraitSkinPrompt
from .nodes.prompt_portrait import PortraitFashionPrompt
from .nodes.prompt_portrait import PortraitPosePrompt
from .nodes.prompt_portrait import PortraitCosmeticPrompt



NODE_CLASS_MAPPINGS = {
    "PromptTranslation": PromptTranslation,
    "GeneratePrompt": GeneratePrompt,
    "SceneryPrompt" : SceneryPrompt,
    "NegativePrompt" : NegativePrompt,
    "LightPrompt" : LightPrompt,
    "DrawStylePrompt" : DrawStylePrompt,
    "PortraitPrompt": PortraitPrompt,
    "PortraitSkinPrompt": PortraitSkinPrompt,
    "PortraitFashionPrompt": PortraitFashionPrompt,
    "PortraitPosePrompt": PortraitPosePrompt,
    "PortraitCosmeticPrompt": PortraitCosmeticPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTranslation": "Prompt Translation",
    "GeneratePrompt": "Generate Prompt",
    "SceneryPrompt": "Generate Scenery Prompt",
    "NegativePrompt": "Generate Negative Prompt",
    "LightPrompt": "Generate Light Prompt",
    "DrawStylePrompt" : "Generate Draw Style Prompt",
    "PortraitPrompt": "Portrait Prompt",
    "PortraitSkinPrompt": "Portrait Skin Prompt",
    "PortraitFashionPrompt": "Portrait Fashion Prompt",
    "PortraitPosePrompt": "Portrait Pose Prompt",
    "PortraitCosmeticPrompt": "Portrait Cosmetic Prompt",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 