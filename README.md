**SOA_serialize**

Измерение времени сериализации и десириализации различных типов

**Пример использования:**

```
echo "/get_result FORMAT" | nc -u localhost 2000
```

где FORMAT из списка ['json', 'yaml', 'native', 'xml']

например:
```
echo "/get_result json" | nc -u localhost 2000
```

Запустить сервер:
```
sudo docker-compose build && sudo docker-compose up
```
