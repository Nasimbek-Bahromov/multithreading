#  python fileni yonidagi barcha txt fayllarni umumiy so'zlarini sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak)

# from multiprocessing import Process, Manager
# import os

# def count_words(file_path, result_dict):
#     try:
#         with open(file_path, 'r') as file:
#             matn = file.read()
#             words = matn.split()
#             result_dict[file_path] = len(words)
#     except Exception as e:
#         print(f"Error reading {file_path}: {e}")
#         result_dict[file_path] = 0

# def main(files):
#     manager = Manager()
#     result_dict = manager.dict()
#     processes = []
    
#     for file_path in files:
#         if os.path.exists(file_path):
#             process = Process(target=count_words, args=(file_path, result_dict))
#             processes.append(process)
#             process.start()
#         else:
#             print(f"File not found: {file_path}")
#             result_dict[file_path] = 0

#     for process in processes:
#         process.join()
    
#     word_count = sum(result_dict.values())
    
#     return word_count

# if __name__ == "__main__":
#     files = [
#         'file1.txt',  
#         'file2.txt',
#         'file3.txt'
#     ]
#     word_count = main(files)
#     print(f"txt fayllardagi so`zlar: {word_count}")

#  python fileni yonidagi barcha txt fayllarni ichidagi raqamlarni sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak) 


# from multiprocessing import Process, Manager
# import re

# def count_comments(file_path, result_dict):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             comment_count = len(re.findall(r'#.*', text, re.MULTILINE))
#             result_dict[file_path] = comment_count
#     except Exception as e:
#         print(f"Faylni o'qishda xatolik: {file_path}: {e}")
#         result_dict[file_path] = 0

# def main(directory):
#     manager = Manager()
#     result_dict = manager.dict()
#     processes = []

#     files = [f for f in os.listdir(directory) if f.endswith('.txt')]

#     for file_name in files:
#         file_path = os.path.join(directory, file_name)
#         process = Process(target=count_comments, args=(file_path, result_dict))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     return result_dict

# if __name__ == "__main__":
#     import os
#     directory = '.' 
#     result_dict = main(directory)
    
#     izohlar_soni = sum(result_dict.values())
#     print(f"Barcha txt fayllardagi izohlar soni: {izohlar_soni}")
#     print("Fayl boshiga izohlar:")
#     for file_path, count in result_dict.items():
#         print(f"{file_path}: {count}")

#  3) python fileni yonidagi barcha txt fayllarni ichidagi gaplarni sonini qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak)

# from multiprocessing import Process, Manager
# import os

# def count_words(file_path, result_dict):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             words = text.split()
#             result_dict[file_path] = len(words)
#     except Exception as e:
#         print(f"Faylni o'qishda xatolik: {file_path}: {e}")
#         result_dict[file_path] = 0

# def main(directory):
#     manager = Manager()
#     result_dict = manager.dict()
#     processes = []

#     files = [f for f in os.listdir(directory) if f.endswith('.txt')]

#     for file_name in files:
#         file_path = os.path.join(directory, file_name)
#         process = Process(target=count_words, args=(file_path, result_dict))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     return result_dict

# if __name__ == "__main__":
#     directory = '.'  
#     result_dict = main(directory)
    
#     umumiy_sozlar_soni = sum(result_dict.values())
#     print(f"Barcha txt fayllardagi so'zlar soni: {umumiy_sozlar_soni}")
#     print("Fayl boshiga so'zlar soni:")
#     for file_path, count in result_dict.items():
#         print(f"{file_path}: {count}")

# 4) python fileni yonidagi barcha txt fayllarni ichidan eng uzun gapni qaytarish (file soni qancha bo'lsa shuncha protses yaratilinishi kerak

# from multiprocessing import Process, Manager
# import os

# def find_longest_word(file_path, result_dict):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             words = text.split()
#             longest_word = max(words, key=len)
#             result_dict[file_path] = longest_word
#     except Exception as e:
#         print(f"Faylni o'qishda xatolik: {file_path}: {e}")
#         result_dict[file_path] = ""

# def main(directory):
#     manager = Manager()
#     result_dict = manager.dict()
#     processes = []

#     files = [f for f in os.listdir(directory) if f.endswith('.txt')]

#     for file_name in files:
#         file_path = os.path.join(directory, file_name)
#         process = Process(target=find_longest_word, args=(file_path, result_dict))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     return result_dict

# if __name__ == "__main__":
#     directory = '.'  
#     result_dict = main(directory)
    
#     print("Har bir fayl uchun eng katta so'z:")
#     for file_path, word in result_dict.items():
#         print(f"{file_path}: {word}")


# from multiprocessing import Process, Manager
# import os

# def remove_special_characters(file_path, result_dict):
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read()
#             cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
#             with open(file_path, 'w') as file:
#                 file.write(cleaned_text)
#             result_dict[file_path] = "Shartli belgilar tozalandi"
#     except Exception as e:
#         print(f"Faylni o'qishda xatolik: {file_path}: {e}")
#         result_dict[file_path] = "Xatolik"

# def main(directory):
#     manager = Manager()
#     result_dict = manager.dict()
#     processes = []

#     files = [f for f in os.listdir(directory) if f.endswith('.txt')]

#     for file_name in files:
#         file_path = os.path.join(directory, file_name)
#         process = Process(target=remove_special_characters, args=(file_path, result_dict))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     return result_dict

# if __name__ == "__main__":
#     directory = '.'  
#     result_dict = main(directory)
    
#     print("Natijalar:")
#     for file_path, message in result_dict.items():
#         print(f"{file_path}: {message}")


# 6-chisiga ulgurmadim vaqtim yetmadi ustoz








