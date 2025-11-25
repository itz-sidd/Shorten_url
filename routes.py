# from flask import Blueprint, request, jsonify, redirect
# from extensions import db, redis_client
# from models import URL
# from utils import encode

# shortener_bp = Blueprint('shortener', __name__)

# @shortener_bp.route('/shorten', methods=['POST'])
# def shorten_url():
#     data = request.get_json()
#     original_url = data.get('original_url')
    
#     if not original_url:
#         return jsonify({"error": "Missing URL"}), 400

#     # 1. create new record
#     new_url = URL(original_url=original_url)
#     db.session.add(new_url)
#     db.session.commit() # This generates the ID
    
#     # 2. Generate short_code using the ID
#     short_code = encode(new_url.id)
    
#     # 3. Update the record with the code
#     new_url.short_code = short_code
#     db.session.commit()

#     return jsonify({
#         "original_url": original_url,
#         "short_url": f"http://localhost:5000/{short_code}"
#     }), 201

# @shortener_bp.route('/<short_code>', methods=['GET'])
# def redirect_url(short_code):
#     # --- CACHING LAYER (The Resume Booster) ---
#     # Check Redis first
#     cached_url = redis_client.get(short_code)
    
#     if cached_url:
#         # Decode bytes to string and redirect
#         return redirect(cached_url.decode('utf-8'))
    
#     # --- DATABASE LAYER (The Fallback) ---
#     url_entry = URL.query.filter_by(short_code=short_code).first()
    
#     if url_entry:
#         # Store in Redis for next time (Expire in 1 hour)
#         redis_client.setex(short_code, 3600, url_entry.original_url)
#         return redirect(url_entry.original_url)
    
#     return jsonify({"error": "URL not found"}), 404

from flask import Blueprint, request, jsonify, redirect, render_template # <--- Add render_template
from extensions import db, redis_client
from models import URL
from utils import encode

shortener_bp = Blueprint('shortener', __name__)

# --- NEW ROUTE FOR FRONTEND ---
@shortener_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# --- EXISTING API ROUTES ---
@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    # ... (Keep existing code exactly the same) ...
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

    return jsonify({
        "original_url": original_url,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@shortener_bp.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    # ... (Keep existing code exactly the same) ...
    try:
        cached_url = redis_client.get(short_code)
        if cached_url:
            print("Cache Hit!", flush=True)
            return redirect(cached_url.decode('utf-8'))
    except Exception as e:
        print(f"Redis Error: {e}", flush=True)

    url_entry = URL.query.filter_by(short_code=short_code).first()
    
    if url_entry:
        try:
            redis_client.setex(short_code, 3600, url_entry.original_url)
        except Exception:
            pass
        return redirect(url_entry.original_url)
    
    return jsonify({"error": "URL not found"}), 404