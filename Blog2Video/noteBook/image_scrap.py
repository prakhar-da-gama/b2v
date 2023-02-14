from tkinter.constants import N
#Image generation parameters !
n = 3
print(audioclip_duration)
size = len(words)

number_images = int(audioclip_duration/n)
if number_images > len(words):
  number_images = len(words)
print(number_images)

from bing_image_downloader import downloader
for x in words:
  downloader.download(x, limit=1,  output_dir='dataset', adult_filter_off = True, force_replace=False, timeout=60)
