from .nodes.prompt_translation import PromptTranslation


NODE_CLASS_MAPPINGS = {
    "PromptTranslation": PromptTranslation,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTranslation": "Prompt Translation",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 