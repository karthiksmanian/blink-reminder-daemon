import time
import datetime
import plyer

def remind():
    plyer.notification.notify(
        title="Blink Reminder",
        message="Karthik, time to blink your eyes!",
        app_name="Blink Reminder",
        toast=True
    )

def log_time(current_time, rounded_time, last_date, current_date):
    with open('reminder_logs.txt', 'a+') as file:
        file.seek(0)
        content = file.read()
        file.seek(0, 2)

        if last_date != current_date:
            file.write(f"{'=' * 20} {current_time.strftime('%Y-%m-%d')} {'=' * 20}\n\n")

        file.write(f"{' ' * 4}Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"{' ' * 4}Rounded Time: {rounded_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

def log_start_timestamp():
    with open('systemd_logs.txt', 'a') as file:
        current_time = datetime.datetime.now()
        file.write(f"Service started at: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

def main():
    ist_timezone = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    last_date = datetime.date.today() - datetime.timedelta(days=1)

    log_start_timestamp()
    
    while True:
        current_time = datetime.datetime.now(ist_timezone)
        rounded_time = current_time + datetime.timedelta(minutes=(20 - current_time.minute % 20))
        current_date = datetime.date.today()

        log_time(current_time, rounded_time, last_date, current_date)
        last_date = current_date

        delay = (rounded_time - current_time).total_seconds()
        time.sleep(delay)
        remind()

if __name__ == "__main__":
    main()

