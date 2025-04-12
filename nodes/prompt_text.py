import os


# Input Prompt
class InputPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "default": "",
                    "multiline": True
                })
            }
        }

   
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "input_prompt"
    CATEGORY = "PromptWrapper"

    def input_prompt(self, text=""):

        return (text, )
    



# Random Line Prompt
class RandomLinePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip" : "string split is use \\n character."
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0, 
                    "max": 0xFFFFFFFFFFFFFFFF
                })
            },
            "optional": {
                "input_prompt": ("STRING", {"forceInput": True}),
            }
        }

   
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "random_text"
    OUTPUT_NODE = True
    CATEGORY = "PromptWrapper"

    def random_text(self, text="", seed=0, input_prompt=""):

        output_texts = []
        if input_prompt != "":
            lines = input_prompt.split("\n")
            for line in lines:
                output_texts.append(line)

        if text != "":
            lines = text.split("\n")
            for line in lines:
                output_texts.append(line)

        output_prompt = ""
        line_count = len(output_texts)
        if line_count > 0:
            line_index = seed % line_count
            output_prompt = output_texts[line_index]

        return (output_prompt, )