import os

# String to Number
class String2Number:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {
                    "default": "0"
                })
            }
        }

   
    RETURN_TYPES = ("STRING", "FLOAT", "INT", "BOOLEAN")
    RETURN_NAMES = ("string", "float", "int", "bool")
    FUNCTION = "convert"
    CATEGORY = "PromptWrapper"

    def convert(self, string=""):

        try:
            fvalue = float(string)
        except ValueError as e:
            print("error:", e)
            fvalue = 0.0
        except:
            fvalue = 0.0

        try:
            ivalue = int(string)
        except ValueError as e:
            print("error:", e)
            ivalue = 0
        except:
            ivalue = 0

        try:
            bvalue = bool(string)
        except ValueError as e:
            print("error:", e)
            bvalue = False
        except:
            bvalue = False

        return (string, fvalue, ivalue, bvalue)
    


# Number to String
class Number2String:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "number": ("FLAOT|INT|BOOLEAN", {
                    "default": "0"
                })
            }
        }

   
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "convert"
    CATEGORY = "PromptWrapper"

    def convert(self, number=0):

        try:
            string = str(number)
        except ValueError as e:
            print("error:", e)
            string = ""
        except:
            string = ""

        return (string, )
    


# Number to String
class Equation2Value:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1": ("FLAOT|INT", {
                    "default": "0"
                }),
                "operator": (["+", "-", "*", "/", "%"], {
                    "default": "+"
                }),
                "value2": ("FLAOT|INT", {
                    "default": "0"
                })
            }
        }

   
    RETURN_TYPES = ("FLAOT|INT",)
    RETURN_NAMES = ("=",)
    FUNCTION = "calculate"
    CATEGORY = "PromptWrapper"

    def calculate(self, value1=0, operator="+", value2=0):

        result = 0
        try:
            if operator == "+":
                result = value1 + value2
            elif operator == "-":
                result = value1 - value2
            elif operator == "*":
                result = value1 * value2
            elif operator == "/":
                result = value1 / value2
            elif operator == "%":
                result = value1 % value2
            else:
                result = "error"
        except:
            result = "this is calculate error"

        return (result, )