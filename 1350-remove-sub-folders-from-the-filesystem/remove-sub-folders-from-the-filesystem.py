class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        d= set(folder)
        result = []

        for file in folder:
            is_sub_folder = False
            pos=file.rfind("/")
            prefix=file[0:pos]
            while( prefix !=""):
                if pos==-1:
                    break
                if prefix in d:
                    is_sub_folder = True
                    break
                pos=prefix.rfind("/")
                prefix=prefix[0:pos]
            if not is_sub_folder:
                result.append(file)
        return result

