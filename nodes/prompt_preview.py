import os


# Preview Prompt
class PreviewPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

   
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "preview"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    INPUT_IS_LIST = True
    CATEGORY = "PromptWrapper"

    def preview(self, text, unique_id=None, extra_pnginfo=None):
    
        return {"ui": {"text": text}, "result": (text,)}
    

