from datetime import datetime, timedelta


def filtered_file():
    file_txt = 'hblog.txt'
    key = "Key TSTFEED0030|7E3E|0400"
    with open(file_txt, 'r') as f:
        content = f.read()
        content_split = content.split('\n')
        filtered_log = []
        for i in content_split:
            if key in i:
                filtered_log.append(i)
        return str(filtered_log)


print(filtered_file())


def parse_and_log_timestamps(log_string):

    timestamp_start = "Timestamp "
    timestamp_length = 8  # Довжина часової мітки

    # Знаходимо першу часову мітку
    start_index = log_string.find(timestamp_start)
    while start_index != -1:
        # Витягаємо часову мітку
        timestamp_str = log_string[
                        start_index + len(timestamp_start):start_index + len(timestamp_start) + timestamp_length]

        try:
            # Перетворюємо рядок у часовий об'єкт
            timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

            # Знаходимо наступну часову мітку
            end_index = log_string.find(timestamp_start, start_index + 1)
            if end_index != -1:
                next_timestamp_str = log_string[end_index + len(timestamp_start):end_index + len(
                    timestamp_start) + timestamp_length]
                next_timestamp = datetime.strptime(next_timestamp_str, "%H:%M:%S")

                # Обчислюємо різницю між часовими мітками
                time_difference = next_timestamp - timestamp
                time_dif_seconds = time_difference.total_seconds()

                if time_dif_seconds == -32.0:
                    with open('hb_test.log', 'a') as log_file:
                        log_file.write(f"WARNING: Heartbeat is {time_dif_seconds} seconds.\n")
                elif time_dif_seconds <= -33.0:
                    with open('hb_test.log', 'a') as log_file:
                        log_file.write(f"ERROR: Heartbeat is {time_dif_seconds} seconds.\n")
                else:
                    pass

        except ValueError:
            # Якщо не вдалося перетворити рядок у часовий об'єкт
            pass
        #
        # Знаходимо наступну часову мітку
        start_index = log_string.find(timestamp_start, start_index + 1)


# Приклад виклику функції з рядком, що містить часові мітки
log_string_example = filtered_file()
parse_and_log_timestamps(log_string_example)

