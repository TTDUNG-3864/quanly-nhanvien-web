from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ===== Class nhân viên =====
class NhanVien:
    def __init__(self, id, ten, tuoi, luong):
        self.id = id
        self.ten = ten
        self.tuoi = tuoi
        self.luong = luong

# ===== Danh sách nhân viên =====
ds = []

# ===== Route hiển thị danh sách =====
@app.route("/")
def index():
    return render_template("index.html", ds=ds)

# ===== Route thêm nhân viên =====
@app.route("/add", methods=["POST"])
def add():
    id = request.form["id"]
    ten = request.form["ten"]
    tuoi = int(request.form["tuoi"])
    luong = float(request.form["luong"])
    ds.append(NhanVien(id, ten, tuoi, luong))
    return redirect("/")

# ===== Route xóa nhân viên =====
@app.route("/delete/<id>")
def delete(id):
    global ds
    ds = [nv for nv in ds if nv.id.lower() != id.lower()]
    return redirect("/")

# ===== Route sửa nhân viên =====
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    nv = next((nv for nv in ds if nv.id.lower() == id.lower()), None)
    if not nv:
        return "❌ Không tìm thấy nhân viên!"
    if request.method == "POST":
        nv.ten = request.form["ten"]
        nv.tuoi = int(request.form["tuoi"])
        nv.luong = float(request.form["luong"])
        return redirect("/")
    return render_template("edit.html", nv=nv)

# ===== Main =====
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
