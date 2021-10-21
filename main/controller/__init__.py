"""  
Endpoint Resolvers and Views
"""
import os
import uuid
from pprint import pprint

import git
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify, render_template, Response

from main.config import app
from main.graphql import schema
from git import Repo


@app.route("/")
def index():
    """

    :return: String
    """
    namespace = "povertyproof.net"
    return f"Your unique access key is {str(uuid.uuid5(uuid.NAMESPACE_DNS, namespace))}"


@app.route("/github-repo-actions", methods=['POST', "GET"])
def github_repository_post_hook():
    """
    Get data from GitHub
    """
    pprint(request.json)
    response = request.json
    aut = "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"
    auth = f"https://{aut}:x-oauth-basic@github.com@github.com/mitch1009/php-boilerplate.git"
    if os.path.exists(f"./repositories/php-boilerplate"):
        pull = git.cmd.Git(auth)
        pull.pull()
    else:
        Repo.clone_from(auth, f"./repositories/php-boilerplate")
    return Response(status=200)


@app.route("/proofs", methods=["GET"])
def graphql_playground():
    """

    Returns:

    """
    return PLAYGROUND_HTML, 200


@app.route("/proofs", methods=["POST"])
def _server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
