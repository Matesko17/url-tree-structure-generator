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

final_urls = []
for url in unique_urls:
    url_parts = url.split("/")
    url_parts_len = len(url_parts)

    if url_parts_len != current_tabs:
        tabdepth += 1 if url_parts_len > current_tabs else -1
        current_tabs = url_parts_len

    tab_padding = "\t" * tabdepth
    final_urls.append(f"{tab_padding}{url}\n")


with open("sitelist.new", "wt") as file:
    file.write(f"{base_url}\n")
    file.writelines(final_urls)
