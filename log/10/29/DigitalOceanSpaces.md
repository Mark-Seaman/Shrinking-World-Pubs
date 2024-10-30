# Configure Spaces at DigitalOcean

Here's a step-by-step guide to set up DigitalOcean Spaces to serve images for a Django application hosted on DigitalOcean's App Platform:

---

<img src="https://shrinking-world-media.sfo2.digitaloceanspaces.com/world.jpg" width="300">


### 1. **Create a Space on DigitalOcean**

- **Log in to DigitalOcean** and go to the **Spaces** section.
- Click on **Create Space**.
- Choose your **Data Center Region** (select the closest region to reduce latency).
- Name your Space, then select **Restrict File Listing** if you want only authenticated access to files.
    - https://shrinking-world-media.sfo2.digitaloceanspaces.com

- Click **Create Space**.

### 2. **Generate API Keys for Access**
   - Go to the **API** section of DigitalOcean.
   - Under **Spaces access keys**, click **Generate New Key**.
   - Save your **Access Key** and **Secret Key** as you'll need them for Django.

### 3. **Install Required Python Packages**
In your Django project, you’ll need `boto3` (for AWS SDK compatibility) and `django-storages` to manage file storage in Spaces.
   
```bash

    pip install boto3 django-storages

```

### 4. **Configure Django to Use DigitalOcean Spaces**

   In `settings.py`, configure the necessary settings to connect to Spaces:

```python

    # Add 'storages' to your INSTALLED_APPS
    INSTALLED_APPS = [
        # other apps...
        'storages',
    ]

    # DigitalOcean Spaces credentials
    AWS_ACCESS_KEY_ID = 'your-access-key'
    AWS_SECRET_ACCESS_KEY = 'your-secret-key'
    AWS_STORAGE_BUCKET_NAME = 'your-space-name'
    AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'  # Change region if necessary
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',  # Adjust as necessary
    }

    # Static files (CSS, JavaScript, etc.)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # Media files (images, videos)
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/"
   
```

   Replace `'your-access-key'`, `'your-secret-key'`, `'your-space-name'`, and `'your-region'` with the actual details from DigitalOcean.

### 5. **Update Your Django Models to Use DigitalOcean Spaces**
   If you have models that handle image uploads, they will now automatically use Spaces for storage because `DEFAULT_FILE_STORAGE` has been set.

   For example:

```python

    from django.db import models

    class Profile(models.Model):
        profile_image = models.ImageField(upload_to='profiles/')
   

```

   When users upload images, they will be stored in the specified Spaces.

### 6. **Set Environment Variables on DigitalOcean App Platform**
   - Deploy your app to App Platform.
   - In the **App Settings**, add the following environment variables:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_STORAGE_BUCKET_NAME`
     - `AWS_S3_ENDPOINT_URL`
   - Make sure these values match those in your local `settings.py`.

### 7. **Run Migrations and Test the Setup**
   - Run `python manage.py migrate` to ensure any database dependencies are up to date.
   - Upload an image via your app’s interface and confirm it is stored in DigitalOcean Spaces.

### 8. **Verify Image Delivery**
   
- Go to your application and check that images are loaded from your Space’s URL, something like:

```

     https://nyc3.digitaloceanspaces.com/your-space-name/path-to-image.jpg


```

- If everything is set correctly, images should display as expected.

---

### Optional: **Use a Custom Domain for DigitalOcean Spaces**

To use a custom domain (e.g., `media.yourdomain.com`):

- Go to **Settings** in your Space and create a CNAME record pointing to the Space.
- Update `AWS_S3_ENDPOINT_URL` in `settings.py` to match your custom domain:
     
```

    AWS_S3_ENDPOINT_URL = 'https://media.yourdomain.com'

```

This setup optimizes your Django app by offloading media handling to DigitalOcean Spaces, allowing your App Platform deployment to stay lean and scalable.