{"filter":false,"title":"custom_storages.py","tooltip":"/custom_storages.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":47},"action":"insert","lines":["from django.conf import settings","from storages.backends.s3boto import S3BotoStorage","","class StaticStorage(S3BotoStorage):","    location = settings.STATICFILES_LOCATION","    ","class MediaStorage(S3BotoStorage):","    location = settings.MEDIAFILES_LOCATION    "],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":8},"end":{"row":1,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563313903467,"hash":"4e5847e1d490b76a9a72b2d6e8280ab93da6ee1d"}