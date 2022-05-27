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


def create_seo_url(language_code, product_name, shoper_sku):
    """Create a safe SEO relative URL for product."""

    new = ""
    for x in product_name:
        if x in validate_string:
            new += replace_dict.get(x)
        else:
            new += x
    # Cant use shoper_id because at this point it doesnt exist.
    # ID is returned in response after this post.
    # Implementation of current ID in permalink: create seperate/after PUT call to product by ID of POST response.
    # Basically setting seo_url after the creation of Product.
    return f"{shoper_sku}{language_code[3:]}-{new.replace(' ', '-')}"


def create_seo_url_from_id(language_code, product_name, shoper_id):
    """Create a safe SEO relative URL for product."""

    new = ""
    for x in product_name:
        if x in validate_string:
            new += replace_dict.get(x)
        else:
            new += x
    # Cant use shoper_id because at this point it doesnt exist.
    # ID is returned in response after this post.
    # Implementation of current ID in permalink: create seperate/after PUT call to product by ID of POST response.
    # Basically setting seo_url after the creation of Product.
    return f"{language_code[3:]}-{new.replace(' ', '-')}-{shoper_id}"


def create_relative_url(original_url):
    """Creates a relative URL from absolute."""

    return original_url.split("https://meowbaby.eu")[1]
