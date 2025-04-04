import json


# dataset
class Dataset:
    def __init__(self, data_path):

        self.sample_datas = self.load_data(data_path)
        

    def load_data(self, path):
    
        sample_datas = []
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if line != "":
                    try:
                        data = json.loads(line.strip())
                        sample_datas.append(data)
                    except:
                        print("jsonl file parse error:", path)
                        break
                    
                    
                
        return sample_datas
        
        
    def __len__(self):
    
        return len(self.sample_datas)
        

    def __getitem__(self, index):
    
        sample_data = self.sample_datas[index]
        text = str(sample_data["text"])
        style = str(sample_data["style"]) if "style" in sample_data else None
        artist = str(sample_data["artist"]) if "artist" in sample_data else None
        
        return text, style, artist