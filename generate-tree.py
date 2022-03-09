#!/usr/bin/env python3

# Read list of URLs from file
from typing import final


with open("sitelist.raw", "r") as f:
    urls = f.readlines()

urls = [url.strip().strip("/") for url in urls]
unique_urls = list(set(urls))
base_url = urls[0]
urls = urls[1:]
sorted_urls = list(sorted(unique_urls))


with open("sitelist.sort", "wt") as file:
    file.write(base_url)
    file.writelines(sorted_urls)

tabdepth = 0
current_tabs = len(base_url.split('/'))
url_part_dict = {}

# Adding domains to dict according to their split length
for url in unique_urls:
    url_length = len(url.split("/")) - 2

    if str(url_length) not in url_part_dict:
        url_part_dict[str(url_length)] = [url]
    else:
        url_part_dict[str(url_length)].append(url)


# Sorting each list in dict
for key, value in url_part_dict.items():
    url_part_dict[key] = sorted(value)
    

def url_recursion(url, dict_key: int, file, final_list):
    # print('rekurze')
    tab_spaces = "\t" * (dict_key - 2)
    if url in final_list:
        return None
    final_list.append(url)
    file.write(f"{tab_spaces}{url}\n")

    if str(dict_key) not in url_part_dict:
        return None

    urls_to_check = url_part_dict[str(dict_key)]

    # TODO: fix že se nikdy nedostane do 6???? urovne v rekurzi
    for url_to_check in urls_to_check:
        if (url + '/') in url_to_check:
            url_recursion(url_to_check, dict_key + 1, file, final_list)
    
        if url not in urls_to_check:
            current_dict = int(dict_key)
            remaining_dicts = len(url_part_dict) - int(dict_key) + 1 
            while remaining_dicts >= 1:
                # print(f"remaing_dicts: {remaining_dicts}")
                # print(f"remaing_dicts: {current_dict}")
                # print('while loop')
                new_urls_to_check = url_part_dict[str(current_dict)]

                for new_url_to_check in new_urls_to_check:
                    if (url + '/') in new_url_to_check:
                        url_recursion(new_url_to_check, current_dict + 1, file, final_list)

                current_dict += 1
                remaining_dicts -= 1
    list_diff = []
    for item in unique_urls:
        if item not in final_list:
            list_diff.append(item)
    return list_diff

def main():
    file = open("sitelist.new", "wt")
    final_list = []
    list_diff = url_recursion(base_url, 2, file, final_list)
    print(list_diff)
    print(len(list_diff))
    file.close()


if __name__ == "__main__":
    main()
