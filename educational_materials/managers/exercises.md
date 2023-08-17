
## Задачи

### Задача 1

Напишите расписание cron, которое позволит запускать задачу:

* в 8:30 каждый понедельник.
* в 12:00 каждый понедельник, среду и пятницу.
* в 15 минут каждого часа в 00:00, 06:00, 12:00 и 18:00.

**Ответ**

```
30 8 * * 1              в 8:30 каждый понедельник.
0 12 * * 1,3,5          в 12:00 каждый понедельник, среду и пятницу.
15 0,6,12,18 * * *      в 15 минут каждого часа в 00:00, 06:00, 12:00 и 18:00.
```

* каждые 10 минут в течение часа.
* в начале каждого часа с 9:00 до 17:00 с понедельника по пятницу.
* в 30 минут каждого часа с 1:00 до 5:00 и с 12:00 до 15:00.

**Ответ**

```
*/10 * * * *            каждые 10 минут в течение часа.
0 9-17 * * 1-5          в начале каждого часа с 9:00 до 17:00 с понедельника по пятницу.
30 1-5,12-15 * * *      в 30 минут каждого часа с 1:00 до 5:00 и с 12:00 до 15:00.
```

* каждые 2 минуты. 
* каждые 3 минуты с 10:00 до 18:00.
* каждые 10 минут в полночь (0:00) по понедельникам.

**Ответ**

```
*/2 * * * *             каждые 2 минуты. 
*/3 10-18 * * *         каждые 3 минуты с 10:00 до 18:00.
*/10 0 * * 1            каждые 10 минут в полночь (0:00) по понедельникам.
```


### Задача 2

Создайте скрипт и соответствующие unit'ы systemctl для следующей задачи: нужно отследить изменения в файле, и если он содержит подстроку "critical error", отправить сообщение пользователю. 

**Ответ**

Скрипт для проверки `check_script.sh`.

([код](/projects/managers/check_script.sh)):

```bash
#!/bin/bash

file="/path/to/watched/file"
substring="critical error"

if grep -q "$substring" "$file"; then
    echo "Found critical error in $file"
    # Add your notification command here, e.g., sendmail or notify-send
else
    echo "No critical error found in $file"
fi
```

Конфигурация для Unit service `check_critical.service`:

([код](/projects/managers/check_critical.service)):

```ini
[Unit]
Description=Check File for Critical Error

[Service]
Type=simple
ExecStart=/path/to/your/check_script.sh
```

Конфигурация для Unit path `check_critical.path`:

([код](/projects/managers/check_critical.path)):

```ini
[Unit]
Description=Watch My File

[Path]
PathModified=/path/to/watched/file
Unit=check_critical.service

[Install]
WantedBy=multi-user.target
```

Код для активации сервиса:

```bash 
sudo chmod +x check_script.sh
sudo systemctl enable /path/to/check_critical.service
sudo systemctl enable /path/to/check_critical.service
sudo systemctl start pass_monitor.path

```