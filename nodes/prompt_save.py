import os
import json


# Save Prompt
class SavePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "forceInput": True
                }),
                "filename": ("STRING", {
                    "default": "custom"
                })
            }
        }
    
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    OUTPUT_NODE = True
    FUNCTION = "save"
    CATEGORY = "PromptWrapper"


    def save(self, text="", filename=""):
 
        text = text.strip()
        if text != "" and text != "\n" and text != "\r\n":
            # 获取Script的目录路径
            script_dir = os.path.dirname(os.path.abspath(__file__)) 
            save_dir = os.path.join(script_dir, "..", "user")

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_path = os.path.join(save_dir, f"{filename}_datas.jsonl")
            with open(save_path, "a+", encoding="utf-8") as fp:
                data = { "text": text }
                text_data = json.dumps(data, ensure_ascii=False)
                size = fp.tell()
                if size == 0:
                    fp.write(text_data)
                else:
                    fp.write(f"\n{text_data}")

        
        return {"ui": {"text": text}}


