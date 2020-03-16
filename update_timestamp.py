import datetime

open("index.html", "w").write(
    open("index.template.html", "r")
    .read()
    .replace("{date}", datetime.date.today().isoformat())
    .replace("{timestamp}", datetime.datetime.now().isoformat())
)
