# استفاده از تصویر رسمی Python
FROM python:3.10-slim

# تنظیم دایرکتوری کاری در کانتینر
WORKDIR /app

# کپی کردن فایل‌های پروژه به کانتینر
COPY . /app

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# باز کردن پورت ۸۰۰۰ برای اجرای پروژه
EXPOSE 8000

# فرمان پیش‌فرض برای اجرای سرور جنگو
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENV PYTHONPATH="${PYTHONPATH}:/app/DigitalMarketing"

