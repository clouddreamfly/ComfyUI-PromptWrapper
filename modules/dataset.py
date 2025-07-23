import json


# dataset
class Dataset:
    def __init__(self, data_path):
        pass

    def load_data(self, path): 
        pass



# jsonl dataset
class JsonlDataset(Dataset):
    def __init__(self, data_path):

        self.sample_datas = self.load_data(data_path)
        

    def load_data(self, path):
    
        sample_datas = []
        with open(path, 'r', encoding='utf-8') as fp:
            for line_num, line in enumerate(fp, 1):
                if line != "" and line != "\n" and line != "\r\n":
                    try:
                        data = json.loads(line.strip())
                        sample_datas.append(data)
                    except:
                        print("jsonl file parse error:{}, line:{}".format(path, line_num))
                        continue
        
        return sample_datas


    def __len__(self):
    
        return len(self.sample_datas)


    def __getitem__(self, index):
    
        sample_data = self.sample_datas[index]
        text = str(sample_data["text"]) if "text" in sample_data else ""
        style = str(sample_data["style"]) if "style" in sample_data else None
        artist = str(sample_data["artist"]) if "artist" in sample_data else None
        
        return text, style, artist



# json dataset
class JsonDataset(Dataset):
    def __init__(self, data_path):

        self.sample_datas = self.load_data(data_path)


    def load_data(self, path):
    
        sample_datas = {}
        with open(path, 'r', encoding='utf-8') as fp:
            bom = fp.read(1)
            if bom != "\ufeff":
                fp.seek(0)
            
            try:
                sample_datas = json.load(fp)
            except:
                print("json file parse error:", path)
        
        return sample_datas


    def __len__(self):
    
        return len(self.sample_datas)


    def __getattr__(self, key):

        return self.sample_datas[key] if key in self.sample_datas else None


