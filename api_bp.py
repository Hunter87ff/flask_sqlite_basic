from flask import Blueprint, request, redirect, Response, render_template
import config


bp = Blueprint('checkout_discount', __name__)

@bp.route("/api/login", methods=['POST'])
def api_login():
    data = request.form.to_dict()
    print(data)
    user = config.User(data)
    response = Response(response="<script> document.location.href='/checkout';</script>")
    if user.is_authorised:
        response.set_cookie(key="username", value=user.username     , max_age=3600)
        response.set_cookie(key="password", value=user.password     , max_age=3600)
        response.set_cookie(key="student",  value=str(user.student) , max_age=3600)
        response.set_cookie(key="name",     value=user.name         , max_age=3600)
        return response
    
    if not user.is_registered: 
        user.register()
        return response
    
    return {"success": False, "event": "Invalid Password", "data": user.to_dict()}, 401

