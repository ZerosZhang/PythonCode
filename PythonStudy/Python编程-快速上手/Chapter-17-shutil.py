# -*- coding: utf-8 -*-
import os

"""
shutil.copy(source, destination)
shutil.copytree(source, destination)
shuilt.move(source,destination)
os.unlink(path)
os.rmdir(path)
shuilt.rmtree(path)
"""

"""
send2trash.send2trash()
os,rename(oldfilename, newfilename)     # 修改前后的filename   可以用于file文件的重命名
os.renames(oldpathfile, newpathfile)   # 修改前后的文件路径及file文件名， 可以重命名文件的路径(文件的上级目录名)及文件名  
"""

# 遍历文件夹


"""
os.walk()返回3个值：
1. 当前文件夹名称的字符串
2. 当前文家中子文件夹的字符串列表
3. 当前文件夹中文件的字符串的列表
"""
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    pass
import zipfile

# example_zip = zipfile.ZipFile('cats.zip')
# zip_file_name_list = example_zip.namelist()
#
# for _file in zip_file_name_list:
#     extracted_path = os.path.abspath(example_zip.extract(_file))
#     os.renames(extracted_path, _file.encode('cp437').decode('gbk'))
#
# example_zip.close()

new_zip = zipfile.ZipFile('cats中文_new.zip', 'a')
for folderName, subfolders, filenames in os.walk('cats'):
    for _file in filenames:
        _path = os.path.join(folderName, _file)
        print(_path)
        new_zip.write(_path, compress_type=zipfile.ZIP_DEFLATED)
    for _folder in subfolders:
        _path = os.path.join(folderName, _folder)
        print(_path)
        new_zip.write(_path, compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
