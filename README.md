# Python-Rest-Framework
Python Rest Framework


## TODO:

- [x] Сериалайзер должен вести себя как поле, что бы можно было делать вложенность
- [x] Научить сериалайзер работать не с одним объектом а с множеством. many=True
- [x] Научиться понимать что данные неверные до того, как мы пробрасываем их в валидаторы
- [x] Сериалайзер должен вести себя как поле, что бы можно было делать вложенность
- [x] Научить сериалайзер object -> dict
- [x] Научиться вложенные сериалайзеры работать как обязательные.
- [ ] Сделать `child` у ListField необязаельным. Если не указан, то хаваем что дают.
- [ ] Добавить Dict, Json филды.
- [ ] Добавить Date, DateTime, Time филды.
- [ ] Сделать рендеры и парсеры, прописать в доке по serializers.
- [ ] Добавить SerializerMethodField.
- [ ] Добавить документацию по методам филдов.
- [ ] Протестировать сериалайзеры, и дофиксить баги.
- - [x] Протестировать юзер кейсы использования.
- - [ ] Протестировать все методы и логику взаимодействия внутри сериалайзера.
- [ ] Написать APIView, и все CRUDGenericView
- [ ] Научиться парсить тело запроса что бы преобразовывать в валидный дикт и пробрасывать в сериалайзер
- [ ] Научиться делать хэндлеры с ошибками и ывбрасывать их через self.fail или Исключение
- [ ] Перевести все на english.


```python
>>> from rest_framework.serializers.serializers import Serializer
>>> from rest_framework.serializers.fields import CharField, IntegerField

class Test(Serializer):
    char_field = CharField(required=False, min_length=10)
    int_field = IntegerField(required=True)

ser = Test(data={field_name: field_value,...})
res_valid = ser.is_valid()  # ser.is_valid(raise_exception=True)

if res_valid:
    print(ser.validated_data)
else:
    print(ser.errors)

```
