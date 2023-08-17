## Задачи

В описании задач дается название утилит, которые можно использовать для ее решения. Предполагается, что вы самостоятельно найдете правильные параметры, используя документацию `man имя_утилиты` или поиск в сети.

### Задача 1

Напишите скрипт, который будет делать резервную копию файла. Резервный файл должен содержать дату создания в имени.

**Ответ**

([код](/projects/bash/file_backup.sh)):

```bash
#!/bin/bash
file_to_backup="myfile.txt"
backup_file="backup_$(date +'%Y%m%d%H%M%S').txt"
cp "$file_to_backup" "$backup_file"
echo "Backup created: $backup_file"
```

### Задача 2

Напишите скрипт, который удaлит файлы старше 30 дней в выбранной директории. Используйте утилиту `find` для поиска файлов. В пути до файлов, включая имя файлов, не должно быть пробелов и специальных символов. В этой задаче предполагается, что пути содержат только латинские буквы, цифры, тире и подчеркивания.

**Ответ**

([код](/projects/bash/old_file_remover.sh)):

```bash
#!/bin/bash

# Define the directory to search in and the days threshold
directory="/path/to/directory"
days_threshold=30

# Store the output of the find command in a variable
found_paths=$(find "$directory" -type f -mtime +$days_threshold)

# Iterate through the paths and remove each file
for path in $found_paths; do
    rm "$path"
    echo "Deleted: $path"
done
```

### Задача 3

Напишите скрипт, который будет мониторить использование памяти определенным процессом, например, вашей программой, и ежесекундно записывать в файл объем использованной памяти. Используйте утилиту `ps` для получения информации о процессе и `awk` для получения суммарного объема использованной памяти.

Cкрипт `memory_monitor.sh` написать так, чтобы его можно было использовать, как показано ниже:

```bash
# Launch your program (replace "./my_program" with the actual command to run your program)
./my_program &

# Capture the PID of the launched program
program_pid=$!

# Start the monitoring script with the captured PID as an argument
./memory_monitor.sh "$program_pid"
```

**Ответ**

([код](/projects/bash/memory_usage_monitor.sh)):

```bash
#!/bin/bash

# File to store the memory usage data
output_file="memory_usage_log.txt"

# Header for the output file (if it doesn't exist)
if [ ! -f "$output_file" ]; then
    echo "Datetime Memory_Usage(KB)" > "$output_file"
fi

# Function to get memory usage of the process by PID
get_memory_usage() {
    local pid=$1
    local memory_usage=$(ps -o rss= -p "$pid" | awk '{ sum+=$1 } END { print sum }')
    echo "$memory_usage"
}

# Check if a process ID was provided as an argument
if test -z "$1" ; then
    echo "Usage: $0 <process_id>"
    exit 1
fi

# Main loop to monitor and log memory usage
while true; do
    datetime=$(date +"%Y-%m-%d %H:%M:%S")
    pid="$1"
    memory_usage=$(get_memory_usage "$pid")

    # Append data to the output file
    echo "$datetime $memory_usage" >> "$output_file"

    # Wait for 1 second before the next iteration
    sleep 1
done
```

### Задача 4

Напишите скрипт, который будет проверять доступность cайта. Это может пригодиться во многих приложениях, когда происходит отправка данных или работоспособность одного приложения зависит от другого, расположенного на другом сервере. Используйте утилиту `curl`, которая позволяет делать запросы.

**Ответ**

([код](/projects/bash/site_availability_checker.sh)):

```bash
#!/bin/bash
website="https://example.com"
response=$(curl -Is "$website" | head -n 1)
if [[ "$response" == *"200 OK"* ]]; then
    echo "Website is reachable."
else
    echo "Website is down or unreachable."
fi
```

### Задача 5

Напишите скрипт для мониторинга портов, открытых на удаленной машине. Для этого используйте утилиту `nc`.

**Ответ**

([код](/projects/bash/open_ports_checker.sh)):

```bash
#!/bin/bash

# Remote website to check (replace example.com and 80 with the appropriate values)
remote_host="example.com"
port="80"

# Function to check if the port is open on the remote site
check_port_open() {
    local host=$1
    local port=$2
    nc -z -w5 "$host" "$port" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Port $port is open on $host"
    else
        echo "Port $port is closed or unreachable on $host"
    fi
}

# Call the function to check the port
check_port_open "$remote_host" "$port"
```

