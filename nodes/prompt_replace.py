import os
import re


# 字符串替换
def string_replace(pattern, replace, string, match_full=False, match_case=False, match_regex=False):
    flags = 0
    if match_full == True and match_case == True and match_regex == True:
        flags = 0
    elif match_full == True and match_case == True:
        flags = 0
    elif match_full == True and match_regex == True:
        flags = re.IGNORECASE
    elif match_case == True and match_regex == True:
        flags = 0
    elif match_full == True:
        flags = re.IGNORECASE
    elif match_case == True:
        flags = 0
    elif match_regex == True:
        flags = re.IGNORECASE
    else:
        flags = re.IGNORECASE

    return re.sub(pattern, replace, string, flags=flags)



# Replace Prompt
class ReplacePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {
                    "forceInput": True
                }),
                "pattern_A": ("STRING", {
                    "default": ""
                }),
                "replace_A": ("STRING", {
                    "default": ""
                }),
                "pattern_B": ("STRING", {
                    "default": ""
                }),
                "replace_B": ("STRING", {
                    "default": ""
                }),
                "pattern_C": ("STRING", {
                    "default": ""
                }),
                "replace_C": ("STRING", {
                    "default": ""
                }),
                "match_full": ("BOOLEAN", {
                    "default": False
                }),
                "match_case": ("STRING", {
                    "default": False
                }),
                "match_regex": ("STRING", {
                    "default": False
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "replace"
    CATEGORY = "PromptWrapper"

    def replace(self, prompt="", pattern_A="", replace_A="", pattern_B="", replace_B="", pattern_C="", replace_C="", 
        match_full=False, match_case=False, match_regex=False):
 
        output_prompt = ""
        if prompt != "":
            output_prompt = prompt
            if pattern_A != "":
                output_prompt = string_replace(pattern_A, replace_A, output_prompt, match_full, match_case, match_regex)

            if pattern_B != "":
                output_prompt = string_replace(pattern_B, replace_B, output_prompt, match_full, match_case, match_regex)

            if pattern_C != "":
                output_prompt = string_replace(pattern_C, replace_C, output_prompt, match_full, match_case, match_regex)
        
        return (output_prompt, )



# Multi Replace Prompt
class MultiReplacePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING",{
                    "forceInput": True
                }),
                "pattern_A": ("STRING", {
                    "default": ""
                }),
                "replace_A": ("STRING", {
                    "default": ""
                }),
                "pattern_B": ("STRING", {
                    "default": ""
                }),
                "replace_B": ("STRING", {
                    "default": ""
                }),
                "pattern_C": ("STRING", {
                    "default": ""
                }),
                "replace_C": ("STRING", {
                    "default": ""
                }),
                "pattern_D": ("STRING", {
                    "default": ""
                }),
                "replace_D": ("STRING", {
                    "default": ""
                }),
                "pattern_E": ("STRING", {
                    "default": ""
                }),
                "replace_E": ("STRING", {
                    "default": ""
                }),
                "pattern_F": ("STRING", {
                    "default": ""
                }),
                "replace_F": ("STRING", {
                    "default": ""
                }),
                "match_full": ("BOOLEAN", {
                    "default": False
                }),
                "match_case": ("STRING", {
                    "default": False
                }),
                "match_regex": ("STRING", {
                    "default": False
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "replace"
    CATEGORY = "PromptWrapper"

    def replace(self, prompt="", pattern_A="", replace_A="", pattern_B="", replace_B="", pattern_C="", replace_C="", 
        pattern_D="", replace_D="", pattern_E="", replace_E="", pattern_F="", replace_F="",
        match_full=False, match_case=False, match_regex=False):
 
        output_prompt = ""
        if prompt != "":
            output_prompt = prompt
            if pattern_A != "":
                output_prompt = string_replace(pattern_A, replace_A, output_prompt, match_full, match_case, match_regex)

            if pattern_B != "":
                output_prompt = string_replace(pattern_B, replace_B, output_prompt, match_full, match_case, match_regex)

            if pattern_C != "":
                output_prompt = string_replace(pattern_C, replace_C, output_prompt, match_full, match_case, match_regex)

            if pattern_D != "":
                output_prompt = string_replace(pattern_D, replace_D, output_prompt, match_full, match_case, match_regex)

            if pattern_E != "":
                output_prompt = string_replace(pattern_E, replace_E, output_prompt, match_full, match_case, match_regex)

            if pattern_F != "":
                output_prompt = string_replace(pattern_F, replace_F, output_prompt, match_full, match_case, match_regex)
        
        return (output_prompt, )

