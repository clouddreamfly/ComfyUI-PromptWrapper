import os


# Combine Prompt
class CombinePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_A": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_B": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_C": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "combine"
    CATEGORY = "PromptWrapper"

    def combine(self, text_A="", text_B="", text_C=""):
 
        texts = [text_A, text_B, text_C]
        prompts = []
        for text in texts:
            if text != "" and text != "\n" and text != "\r\n":
                prompts.append(text)


        output_prompt = ""
        if len(prompts) > 0:
            output_prompt = ",".join(prompts)
        
        return (output_prompt, )



# Multi Combine Prompt
class MultiCombinePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_A": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_B": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_C": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_D": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_E": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "text_F": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "combine"
    CATEGORY = "PromptWrapper"

    def combine(self, text_A="", text_B="", text_C="", text_D="", text_E="", text_F=""):
 
        texts = [text_A, text_B, text_C, text_D, text_E, text_F]
        prompts = []
        for text in texts:
            if text != "" and text != "\n" and text != "\r\n":
                prompts.append(text)


        output_prompt = ""
        if len(prompts) > 0:
            output_prompt = ",".join(prompts)
        
        return (output_prompt, )

