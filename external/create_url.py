validate_string = """ÀàÁáĄąĆćŹźŻżÈèÉéĘęŁłŃńÒòÓóŚś,.<>~`/?'";:][}{)(*&^%$#@!®"""
replace_dict = {
    "À": "A",
    "à": "a",
    "Á": "A",
    "á": "a",
    "Ą": "A",
    "ą": "a",
    "Ć": "C",
    "ć": "c",
    "Ź": "Z",
    "ź": "z",
    "Ż": "Z",
    "ż": "z",
    "È": "E",
    "è": "e",
    "É": "E",
    "é": "e",
    "Ę": "E",
    "ę": "e",
    "Ł": "L",
    "ł": "l",
    "Ń": "N",
    "ń": "n",
    "Ò": "O",
    "ò": "o",
    "Ó": "O",
    "ó": "o",
    "Ś": "s",
    "ś": "s",
    "Ź": "Z",
    "ź": "z",
    "Ż": "Z",
    "ż": "z",
    ",": "",
    ".": "",
    "<": "",
    ">": "",
    "~": "",
    "`": "",
    "/": "",
    "?": "",
    "'": "",
    '"': "",
    ";": "",
    ":": "",
    "]": "",
    "[": "",
    "}": "",
    "{": "{",
    ")": "",
    "(": "",
    "*": "",
    "&": "",
    "^": "",
    "%": "",
    "$": "",
    "#": "",
    "@": "",
    "!": "",
    "®": "",
}


def create_seo_url(language_code, string, product_id):
    """Create a safe SEO relative URL for product."""

    new = ""
    for x in string:
        if x in validate_string:
            new += replace_dict.get(x)
        else:
            new += x

    return f"{language_code[3:]}-{new.replace(' ', '-')}-{product_id}"


def create_relative_url(original_url):
    """Creates a relative URL from absolute."""

    return original_url.split("https://meowbaby.eu")[1]
