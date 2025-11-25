# from flask import Blueprint, request, jsonify, redirect, render_template # <--- Add render_template
# from extensions import db, redis_client
# from models import URL
# from utils import encode

# shortener_bp = Blueprint('shortener', __name__)

# # --- NEW ROUTE FOR FRONTEND ---
# @shortener_bp.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')

# # --- EXISTING API ROUTES ---
# @shortener_bp.route('/shorten', methods=['POST'])
# def shorten_url():
#     # ... (Keep existing code exactly the same) ...
#     data = request.get_json()
#     original_url = data.get('original_url')
    
#     if not original_url:
#         return jsonify({"error": "Missing URL"}), 400

#     new_url = URL(original_url=original_url)
#     db.session.add(new_url)
#     db.session.commit()
    
#     short_code = encode(new_url.id)
#     new_url.short_code = short_code
#     db.session.commit()

#     return jsonify({
#         "original_url": original_url,
#         "short_url": f"http://localhost:5000/{short_code}"
#     }), 201

# @shortener_bp.route('/<short_code>', methods=['GET'])
# def redirect_url(short_code):
#     # ... (Keep existing code exactly the same) ...
#     try:
#         cached_url = redis_client.get(short_code)
#         if cached_url:
#             print("Cache Hit!", flush=True)
#             return redirect(cached_url.decode('utf-8'))
#     except Exception as e:
#         print(f"Redis Error: {e}", flush=True)

#     url_entry = URL.query.filter_by(short_code=short_code).first()
    
#     if url_entry:
#         try:
#             redis_client.setex(short_code, 3600, url_entry.original_url)
#         except Exception:
#             pass
#         return redirect(url_entry.original_url)
    
#     return jsonify({"error": "URL not found"}), 404

from flask import Blueprint, request, jsonify, redirect, render_template
from extensions import db, redis_client
from models import URL
from utils import encode

shortener_bp = Blueprint('shortener', __name__)

# --- FRONTEND ROUTE ---
@shortener_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# --- API ROUTE (FIXED) ---
@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('original_url')
    
    if not original_url:
        return jsonify({"error": "Missing URL"}), 400

    new_url = URL(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
    
    short_code = encode(new_url.id)
    new_url.short_code = short_code
    db.session.commit()

    # --- THE FIX IS HERE ---
    # request.host_url automatically uses "https://...onrender.com/" when live
    # and "http://localhost:5000/" when local.
    return jsonify({
        "original_url": original_url,
        "short_url": f"{request.host_url}{short_code}"
    }), 201

@shortener_bp.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    # --- REDIS CACHE CHECK ---
    try:
        cached_url = redis_client.get(short_code)
        if cached_url:
            print("Cache Hit!", flush=True)
            return redirect(cached_url.decode('utf-8'))
    except Exception as e:
        print(f"Redis Error: {e}", flush=True)

    # --- DATABASE FALLBACK ---
    url_entry = URL.query.filter_by(short_code=short_code).first()
    
    if url_entry:
        # Save to Redis for next time
        try:
            redis_client.setex(short_code, 3600, url_entry.original_url)
        except Exception:
            pass
        return redirect(url_entry.original_url)
    
    return jsonify({"error": "URL not found"}), 404