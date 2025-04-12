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
                "unique_id": "UNIQUE_ID"
            },
        }

   
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "preview"
    OUTPUT_NODE = True
    CATEGORY = "PromptWrapper"

    def preview(self, text, unique_id=None):

        return {"ui": {"text": text}, "result": (text,)}
    

