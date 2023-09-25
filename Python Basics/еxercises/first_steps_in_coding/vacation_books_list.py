book_pages = int(input())
pages_per_hour = int(input())
days_count = int(input())

total_reading_hours = book_pages // pages_per_hour
reading_hours_per_day = total_reading_hours // days_count

print(reading_hours_per_day)
