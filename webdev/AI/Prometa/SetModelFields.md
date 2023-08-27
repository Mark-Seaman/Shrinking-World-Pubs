Rewrite this Django function to set each field in a data model from a JSON file.

def update_record(name, doc_path):
    json = pub_json_path(name, doc_path)
    s = read_json(json)
    b = Pub.objects.get_or_create(name=name)[0]
    b.doc_path = doc_path
    b.title = s["site_title"]
    b.subtitle = s["site_subtitle"]
    b.domain = s.get("domain")
    b.url = s["url"]
    b.description = s["description"]
    b.css = s["css"]
    b.image_path = s["image_path"]
    b.cover_image = s.get("cover_image")
    b.pub_type = s.get("pub_type", "blog")
    b.menu = s.get("menu")
    b.logo = s.get("logo")
    b.auto_remove = s.get("auto_remove", False)
    b.auto_index = s.get("auto_index", False)  # simple_index
    b.simple_index = s.get("simple_index", False)
    b.auto_contents = s.get("auto_contents", False)
    b.index_folders = s.get("index_folders", False)
    b.index_months = s.get("index_months", False)
    b.save()
    return b

pub.py

    import json
    from django.db import models

    def update_record(name, doc_path):
        json_path = pub_json_path(name, doc_path)
        with open(json_path, 'r') as file:
            data = json.load(file)
            pub = create_pub(data)


    def create_pub(data):      
        # Name is unique ID      
        pub, created = Pub.objects.get_or_create(name=name)
        for field in Pub._meta.get_fields():
            field_name = field.name
            if field_name in data:
                setattr(pub, field_name, data[field_name])
        pub.save()
        return pub
