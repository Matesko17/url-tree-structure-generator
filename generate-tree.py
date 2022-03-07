#!/usr/bin/env python3

# Read list of URLs from file
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


def url_recursion(url, dict_key: int, file):
    tab_spaces = "\t" * (dict_key - 2)
    file.write(f"{tab_spaces}{url}\n")
    
    if str(dict_key) not in url_part_dict:
        return None
    
    urls_to_check = url_part_dict[str(dict_key)]
    
    for url_to_check in urls_to_check:
        if url in url_to_check:
            url_recursion(url_to_check, dict_key + 1, file)

def main():
    file = open("sitelist.new", "wt")
    url_recursion(base_url, 2, file)
    file.close()


if __name__ == "__main__":
    main()
