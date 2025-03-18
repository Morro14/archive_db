import yadisk
from credentials import token

y = yadisk.YaDisk(token=token)


data = y.get_public_meta(
    "https://disk.yandex.ru/i/_-HOJ0vnPPsusw", preview_crop=True, preview_size=""
)
print(data)
