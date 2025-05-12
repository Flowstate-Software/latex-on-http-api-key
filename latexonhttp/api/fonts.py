# -*- coding: utf-8 -*-
"""
    latexonhttp.api.fonts
    ~~~~~~~~~~~~~~~~~~~~~
    Manage LaTeX-On-HTTP fonts.

    :copyright: (c) 2019 Yoan Tournade.
    :license: AGPL, see LICENSE for more details.
"""
from flask import Blueprint, request, jsonify
from fclist import fclist
from latexonhttp.auth import require_api_key

fonts_app = Blueprint("fonts", __name__)


@fonts_app.route("", methods=["GET"])
@require_api_key
def fonts_list():
    fonts = []
    for font in fclist():
        fonts.append(
            {"family": font.family, "name": font.fullname, "styles": list(font.style)}
        )
    # TODO Group by families?
    return ({"fonts": fonts}, 200)
