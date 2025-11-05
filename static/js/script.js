// Xác nhận trước khi xóa nhân viên
document.querySelectorAll('.delete-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        if(!confirm("Bạn có chắc muốn xóa nhân viên này không?")) {
            e.preventDefault(); // Ngăn chặn link
        }
    });
});
