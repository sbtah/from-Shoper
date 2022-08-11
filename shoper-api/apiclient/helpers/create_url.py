from helpers.get_token import SHOPER_DOMAIN

test = "MeowBaby® Soft Plastic Balls 7cm for the Ball Pit Certified – Set 500pcs: Violet/Light Pink/Lime Green Green/Turquoise"
validate_string = (
    """ĂÀàâÁáäĄąĆćŹźŻżÈèÉéêĘÊęüÜŁłŃńÒòÓóöŚŠś,.<>~`’/?'";:][}{)(*&^%$#@!®–+∅Øß\xa0"""
)
replace_dict = {
    "Ă": "A",
    "À": "A",
    "à": "a",
    "â": "a",
    "ä": "a",
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
    "Ê": "E",
    "ę": "e",
    "ê": "e",
    "Ü": "U",
    "ü": "u",
    "Ł": "L",
    "ł": "l",
    "Ń": "N",
    "ń": "n",
    "Ò": "O",
    "ò": "o",
    "Ó": "O",
    "ó": "o",
    "ö": "o",
    "Ś": "s",
    "Š": "S",
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
    "/": "-",
    "?": "",
    "'": "",
    '"': "",
    ";": "",
    ":": "",
    "]": "",
    "[": "",
    "}": "",
    "{": "",
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
    "–": "",
    "+": "",
    "Ø": "",
    "ß": "ss",
    "∅": "",
    "’": "",
    "\xa0": "",
}


def create_seo_url(shoper_sku, product_name):
    """
    Create a safe SEO relative URL for product.
    This method can be used at POST request level.
    URL is created from product's SKU+language_tag.
    """

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
    return f"{shoper_sku}-{new.replace(' ', '-')}"


def create_relative_url(original_url):
    """
    Creates a relative URL from absolute.
    Used to creation of relative URLS for redirects.
    """

    return original_url.split(f"https://{SHOPER_DOMAIN}")[1]
