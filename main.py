import tkinter as tk #khai bao thu vien giao dien va gan cho tk
from tkinter import ttk, messagebox  #ttk la goi nang cap cua tkinter lam cho giao dien xin hon
from tkcalendar import DateEntry #tao ra o chon lich cho ngay sinh

import mysql.connector 

def connect_db(): 

    return mysql.connector.connect(
        # Tác dụng: Lệnh này 'mở cổng' kết nối và 'trả về' (return)
       
        host="localhost",
        # Chỉ định địa chỉ máy chủ CSDL. 'localhost': Vì đang chạy XAMPP trên chính máy của em.
        
        user="root",
        # Tên người dùng để đăng nhập MySQL.
        # 'root' là tên người dùng 'admin' mặc định của XAMPP.
        
        password="",
        
        # rỗng: Vì XAMPP mặc định không đặt mật khẩu.
        
        database="qlhocsinh"
        # Tác dụng: Chỉ định CSDL (cái 'ngăn tủ') mà chúng ta muốn làm việc.
     
    )

# ===== HÀM TẢI DỮ LIỆU TỪ CSDL LÊN BẢNG =====
def load_data():
    # Tác dụng: Hàm này sẽ xóa sạch bảng cũ và tải lại dữ liệu mới nhất từ MySQL.
    
    # 1. Xóa dữ liệu cũ trên bảng 
    for item in tree.get_children(): #  Lấy danh sách tất cả các dòng đang có trên bảng.
        tree.delete(item)  #  Xóa từng dòng một.

    # 2. Kết nối và Lấy dữ liệu mới
    conn = connect_db()  # Gọi cái "chìa khóa" em vừa tạo để mở cổng.
    cursor = conn.cursor() # Tạo một "con trỏ" để thực thi lệnh SQL.
    
    cursor.execute("SELECT * FROM hocsinh") 
    # Gửi lệnh SQL "Lấy TẤT CẢ từ bảng hocsinh".
    
    rows = cursor.fetchall() 
    # Lấy tất cả kết quả trả về và lưu vào biến 'rows'.

    # 3. Đưa dữ liệu vào bảng (Treeview)
    for row in rows:
        # 'row' là một dòng dữ liệu (ví dụ: (1, 'Nguyen', 'An', ...))
        tree.insert("", tk.END, values=row)
        #  Chèn dòng 'row' vào cuối bảng (tk.END).
        # 'values=row': Điền dữ liệu vào các cột tương ứng.

    # 4. Đóng kết nối (Quan trọng)
    conn.close()
    #  Đóng cổng kết nối sau khi dùng xong để tiết kiệm tài nguyên máy.

def them_hs():
    try:
        # 1. Lấy dữ liệu từ các ô nhập liệu
        mahs = entry_mahs.get()
        holot = entry_holot.get()
        ten = entry_ten.get()
        phai = gender_var.get()
        ngaysinh = entry_ngaysinh.get()
        lop = entry_lop.get()
        trangthai = cbb_trangthai.get()
        diachi = entry_diachi.get()

        # 2. Kiểm tra dữ liệu (Validation)
        if mahs == "" or ten == "":
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã HS và Tên!")
            return # Dừng hàm lại, không làm tiếp nữa

        # 3. Kết nối và Thêm vào CSDL
        conn = connect_db()
        cursor = conn.cursor()
        
        # Câu lệnh SQL để chèn dữ liệu (8 dấu %s đại diện cho 8 cột)
        sql = "INSERT INTO hocsinh (mahs, holot, ten, phai, ngaysinh, lop, trangthai, diachi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (mahs, holot, ten, phai, ngaysinh, lop, trangthai, diachi)
        
        cursor.execute(sql, values) # Thực thi lệnh
        conn.commit() # Phải có lệnh này thì MySQL mới lưu chính thức!
        conn.close()

        # 4. Thông báo và Tải lại bảng
        messagebox.showinfo("Thành công", "Đã thêm học sinh mới!")
        load_data() # bảng cập nhật ngay lập tức dòng vừa thêm
        
        #  Xóa trắng các ô nhập để nhập người tiếp theo
        entry_mahs.delete(0, tk.END)
        entry_ten.delete(0, tk.END)
        # ... em có thể làm tương tự cho các ô khác nếu thích

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm học sinh:\n{str(e)}")


def xoa_hs():
    try:
        selected_item = tree.selection() # Lấy dòng đang được bôi đen
        
        if not selected_item:
            # Nếu chưa chọn dòng nào thì báo lỗi và dừng lại
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn học sinh cần xóa trên bảng!")
            return

        # 2. Lấy Mã HS của dòng đã chọn
        values = tree.item(selected_item)['values'] #trả về ds dữ liệu của dòng đó: [101, 'Nguyen', 'An'...]
        mahs = values[0]  #mahs nam o vi tri dau

        # 3. Hiện hộp thoại Xác nhận (Yes/No)
        confirm = messagebox.askyesno("Xác nhận xóa", f"Bạn có chắc muốn xóa học sinh có Mã {mahs} không?")
        
        if confirm == True:
            # 4. Kết nối và Xóa trong CSDL
            conn = connect_db()
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM hocsinh WHERE mahs=%s", (mahs,))
           
            
            conn.commit() # Nhớ commit để lưu thay đổi!
            conn.close()

            # 5. Thông báo và Tải lại bảng
            messagebox.showinfo("Thành công", "Đã xóa học sinh!")
            load_data()
            
            #  Xóa trắng các ô nhập liệu
            entry_mahs.delete(0, tk.END)
            entry_ten.delete(0, tk.END)
            
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xóa:\n{str(e)}")

def sua_hs():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Chưa chọn", "Hãy chọn học sinh cần sửa trên bảng!")
        return

    values = tree.item(selected_item)['values']

    entry_mahs.delete(0, tk.END)
    entry_holot.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_lop.delete(0, tk.END)
    entry_diachi.delete(0, tk.END)

    # Điền dữ liệu cũ vào form để người dùng sửa
    entry_mahs.insert(0, values[0])
    entry_holot.insert(0, values[1])
    entry_ten.insert(0, values[2])
    gender_var.set(values[3])
    entry_ngaysinh.set_date(values[4])
    entry_lop.insert(0, values[5])
    cbb_trangthai.set(values[6])
    entry_diachi.insert(0, values[7])

def luu_hs():
    try:
        # 1. Lấy dữ liệu MỚI từ các ô nhập liệu
        mahs = entry_mahs.get()
        holot = entry_holot.get()
        ten = entry_ten.get()
        phai = gender_var.get()
        ngaysinh = entry_ngaysinh.get()
        lop = entry_lop.get()
        trangthai = cbb_trangthai.get()
        diachi = entry_diachi.get()

        # 2. Kết nối và Cập nhật (UPDATE)
        conn = connect_db()
        cursor = conn.cursor()
        
        # Lệnh SQL Update
        sql = """UPDATE hocsinh 
                 SET holot=%s, ten=%s, phai=%s, ngaysinh=%s, lop=%s, trangthai=%s, diachi=%s 
                 WHERE mahs=%s"""
        
        values = (holot, ten, phai, ngaysinh, lop, trangthai, diachi, mahs)
        
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        # 3. Thông báo và Tải lại bảng
        messagebox.showinfo("Thành công", "Đã lưu thông tin học sinh!")
        load_data()
        
        # Xóa trắng form sau khi lưu xong
        entry_mahs.delete(0, tk.END)
        entry_ten.delete(0, tk.END)
        # (Em có thể thêm code xóa các ô khác nếu muốn)

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu:\n{str(e)}")

def clear_input():
   
    entry_mahs.delete(0, tk.END)
    entry_holot.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_lop.delete(0, tk.END)
    entry_diachi.delete(0, tk.END)
    
    # Đặt lại các ô chọn về mặc định
    gender_var.set("Nam")
    entry_ngaysinh.set_date(None) # Hoặc đặt ngày hiện tại
    cbb_trangthai.set("")
    
    # Bỏ chọn dòng đang bôi đen trên bảng (nếu có)
    for item in tree.selection():
        tree.selection_remove(item)
#ham canh giua
def center_window(win,w = 800,h = 600):
    ws = win.winfo_screenwidth() #lay chieu rong man hinh
    hs = win.winfo_screenheight() #lay chieu cao man hinh
    x = (ws // 2) - (w //2)
    y = (hs // 2) - (h //2)
    win.geometry(f'{w}x{h}+{x}+{y}') #dat kich thuoc va vi tri

# tao cua so chinh
#root la cua so chinh la ngoi nha con lai la do dac trong nha
root = tk.Tk() #tao cua so chinh 
root.title(" Quản Lý Học Sinh ") #dat tieu de cho cua so
center_window(root,800,600) #kich thuoc cua so
root.resizable(False, False) # ngan nguoi dung thay doi kich thuoc


# tieu de cho ung dung
lbl_title = tk.Label(root,text = "QUAN LY HOC SINH",font = ("Arial",18,"bold")) #bold la in dam #tao nhan dan gan cho lbl_title
lbl_title.pack(pady = 10) #dat nhan dan do root va khoang trong tren duoi nhan dan la 10pixel

#tao khung du lieu(khay vo hinh de chua do dac trong nha)
frame_info = tk.Label(root)
frame_info.pack(pady = 5,padx = 10,fill = "x") #pack tu dong xep chong len nhau
# pady tao khoang dem giua tieu de va khung
# padx tao khoang dem 2 ben trai phai
# fill tu dong co dan theo chieu ngang de cai khay dep de hon
 #hang 0
 #tao nhan dan
lbl_mahs = tk.Label(frame_info,text ="Mã học sinh") 
lbl_mahs.grid(row = 0,column = 0,padx = 5,pady = 5,sticky = "w") 

#tao o nhap
entry_mahs = tk.Entry(frame_info,width = 20)
entry_mahs.grid(row = 0,column = 1,padx = 5,pady = 5,sticky ="w")

#hang 1
lbl_holot = tk.Label(frame_info,text ="Ho lot")
lbl_holot.grid(row = 1,column = 0,padx = 5,pady = 5,sticky ="w") #sticky ="w" la west dinh le trai

entry_holot = tk.Entry(frame_info,width = 20)
entry_holot.grid(row = 1,column = 1,padx = 5,pady = 5,sticky ="w")

lbl_ten = tk.Label(frame_info,text = "Ten")
lbl_ten.grid(row = 1,column = 2,padx = 5,pady = 5,sticky = "w")

entry_ten = tk.Entry(frame_info,width = 20)
entry_ten.grid(row = 1,column = 3,padx = 5,pady = 5,sticky = "w")

# --- Hàng 2: Phái và Ngày sinh ---
lbl_phai = tk.Label(frame_info, text="Phái:")
lbl_phai.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Tạo 1 biến đặc biệt để giữ giá trị của Radiobutton
gender_var = tk.StringVar(value="Nam") # Đặt giá trị mặc định là "Nam"

radio_nam = tk.Radiobutton(frame_info, text="Nam", variable=gender_var, value="Nam")
radio_nam.grid(row=2, column=1, padx=5, sticky="w")

radio_nu = tk.Radiobutton(frame_info, text="Nữ", variable=gender_var, value="Nữ")
radio_nu.grid(row=2, column=1, padx=60, sticky="w") # Dùng padx để đẩy nút "Nữ" sang bên phải

lbl_ngaysinh = tk.Label(frame_info, text="Ngày sinh:")
lbl_ngaysinh.grid(row=2, column=2, padx=5, pady=5, sticky="w")

entry_ngaysinh = DateEntry(frame_info, width=18, date_pattern="yyyy-mm-dd")
entry_ngaysinh.grid(row=2, column=3, padx=5, pady=5)



# 1. Tạo Nhãn (Label) cho chữ "Lớp:"
lbl_lop = tk.Label(frame_info, text="Lớp:")
lbl_lop.grid(row=3, column=0, padx=5, pady=5, sticky="w")


entry_lop = tk.Entry(frame_info, width=20)
entry_lop.grid(row=3, column=1, padx=5, pady=5)


# 3. Tạo Nhãn (Label) cho chữ "Trạng thái:"
lbl_trangthai = tk.Label(frame_info, text="Trạng thái:")
lbl_trangthai.grid(row=3, column=2, padx=5, pady=5, sticky="w")

trangthai_values = ["Đang học", "Đã tốt nghiệp", "Bảo lưu", "Bị đình chỉ"]


cbb_trangthai = ttk.Combobox(frame_info, values=trangthai_values, width=18)


cbb_trangthai.grid(row=3, column=3, padx=5, pady=5)

# --- Hàng 4: Địa chỉ ---

# 1. Tạo Nhãn (Label) cho chữ "Địa chỉ:"
lbl_diachi = tk.Label(frame_info, text="Địa chỉ:")
lbl_diachi.grid(row=4, column=0, padx=5, pady=5, sticky="w")

entry_diachi = tk.Entry(frame_info, width=60)
entry_diachi.grid(row=4, column=1, padx=5, pady=5, columnspan=3)

#KHUNG NÚT BẤM

# 1. Tạo "Khay" mới để chứa các nút bấm
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

# 2. Tạo 6 Nút Bấm BÊN TRONG 'frame_btn'
btn_them = tk.Button(frame_btn, text="Thêm", width=8, command=them_hs)
btn_them.grid(row=0, column=0, padx=5)

btn_luu = tk.Button(frame_btn, text="Lưu", width=8,command=luu_hs)
btn_luu.grid(row=0, column=1, padx=5)

btn_sua = tk.Button(frame_btn, text="Sửa", width=8, command=sua_hs)
btn_sua.grid(row=0, column=2, padx=5)

btn_huy = tk.Button(frame_btn, text="Hủy", width=8,command=clear_input)
btn_huy.grid(row=0, column=3, padx=5)

btn_xoa = tk.Button(frame_btn, text="Xóa", width=8,command=xoa_hs)
btn_xoa.grid(row=0, column=4, padx=5)

btn_thoat = tk.Button(frame_btn, text="Thoát", width=8, command=root.quit) #dung chuong trình
btn_thoat.grid(row=0, column=5, padx=5)

# BẢNG DANH SÁCH HỌC SINH 

# 1. Tạo Nhãn (Label) cho tiêu đề của bảng
lbl_ds = tk.Label(root, text="Danh sách học sinh", font=("Arial", 12, "bold"))
lbl_ds.pack(pady=5, padx=10, anchor="w")

# 2. Tạo Bảng (Treeview)
columns = ("mahs", "holot", "ten", "phai", "ngaysinh", "lop", "trangthai", "diachi")

tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

# 3. Định nghĩa Tiêu đề (Headings) và Cột (Columns) cho Bảng
tree.heading("mahs", text="Mã HS")
tree.column("mahs", width=60, anchor="center")

tree.heading("holot", text="Họ lót")
tree.column("holot", width=120)

tree.heading("ten", text="Tên")
tree.column("ten", width=80)

tree.heading("phai", text="Phái")
tree.column("phai", width=50, anchor="center")

tree.heading("ngaysinh", text="Ngày sinh")
tree.column("ngaysinh", width=90, anchor="center")

tree.heading("lop", text="Lớp")
tree.column("lop", width=70, anchor="center")

tree.heading("trangthai", text="Trạng thái")
tree.column("trangthai", width=100)

tree.heading("diachi", text="Địa chỉ")
tree.column("diachi", width=200)


# 4. Đặt Bảng (Treeview) lên cửa sổ
tree.pack(padx=10, pady=5, fill="both", expand=True)

load_data()
clear_input()

root.mainloop() # giu cho cua so luon hien thi khong thi no hien len roi tat lien