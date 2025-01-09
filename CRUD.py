class DigitalMarketing:
    def __init__(self):
        self.campaigns = []

    # Create: افزودن کمپین جدید
    def add_campaign(self, id, name, budget, platform, start_date=None, end_date=None):
        new_campaign = {
            "id": id,
            "name": name,
            "budget": budget,
            "platform": platform,
            "start_date": start_date,
            "end_date": end_date,
            "status": "Active"
        }
        self.campaigns.append(new_campaign)
        print(f'کمپین "{name}" با موفقیت اضافه شد.')

    # Read: مشاهده لیست کمپین‌ها یا جزئیات یک کمپین خاص
    def get_campaign(self, id=None):
        if id is None:
            print("لیست کمپین‌ها:", self.campaigns)
        else:
            campaign = next((c for c in self.campaigns if c["id"] == id), None)
            if campaign:
                print("جزئیات کمپین:", campaign)
            else:
                print("کمپینی با این شناسه پیدا نشد.")

    # Update: ویرایش جزئیات یک کمپین
    def update_campaign(self, id, updated_details):
        campaign = next((c for c in self.campaigns if c["id"] == id), None)
        if campaign:
            campaign.update(updated_details)
            print(f'کمپین "{campaign["name"]}" با موفقیت به‌روزرسانی شد.')
        else:
            print("کمپینی با این شناسه پیدا نشد.")

    # Delete: حذف یک کمپین
    def delete_campaign(self, id):
        campaign = next((c for c in self.campaigns if c["id"] == id), None)
        if campaign:
            self.campaigns.remove(campaign)
            print(f'کمپین "{campaign["name"]}" با موفقیت حذف شد.')
        else:
            print("کمپینی با این شناسه پیدا نشد.")

    # Pause: متوقف کردن یک کمپین
    def pause_campaign(self, id):
        campaign = next((c for c in self.campaigns if c["id"] == id), None)
        if campaign:
            campaign["status"] = "Paused"
            print(f'کمپین "{campaign["name"]}" متوقف شد.')
        else:
            print("کمپینی با این شناسه پیدا نشد.")

    # Resume: از سرگیری یک کمپین متوقف شده
    def resume_campaign(self, id):
        campaign = next((c for c in self.campaigns if c["id"] == id), None)
        if campaign:
            campaign["status"] = "Active"
            print(f'کمپین "{campaign["name"]}" از سر گرفته شد.')
        else:
            print("کمپینی با این شناسه پیدا نشد.")

    # Filter: فیلتر کردن کمپین‌ها بر اساس پلتفرم یا وضعیت
    def filter_campaigns(self, platform=None, status=None):
        filtered = self.campaigns
        if platform:
            filtered = [c for c in filtered if c["platform"] == platform]
        if status:
            filtered = [c for c in filtered if c["status"] == status]
        print("نتایج فیلتر شده:", filtered)

# Example Usage
marketing = DigitalMarketing()

marketing.add_campaign(1, "کمپین گوگل ادز", 5000, "Google", "2025-01-01", "2025-02-01")
marketing.add_campaign(2, "کمپین اینستاگرام", 3000, "Instagram", "2025-01-10", "2025-02-15")
marketing.add_campaign(3, "کمپین فیسبوک", 4000, "Facebook", "2025-01-15", "2025-02-20")

marketing.get_campaign()  # مشاهده تمام کمپین‌ها

marketing.get_campaign(1)  # مشاهده جزئیات کمپین با شناسه 1

marketing.update_campaign(1, {"budget": 5500, "platform": "Google Ads"})  # به‌روزرسانی کمپین

marketing.pause_campaign(2)  # متوقف کردن کمپین با شناسه 2

marketing.resume_campaign(2)  # از سرگیری کمپین با شناسه 2

marketing.filter_campaigns(platform="Google")  # فیلتر کردن بر اساس پلتفرم

marketing.filter_campaigns(status="Active")  # فیلتر کردن بر اساس وضعیت

marketing.delete_campaign(3)  # حذف کمپین با شناسه 3

marketing.get_campaign()  # مشاهده لیست به‌روزرسانی‌شده کمپین‌ها
