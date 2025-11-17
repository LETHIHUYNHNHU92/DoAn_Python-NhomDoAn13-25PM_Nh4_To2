import tkinter as tk #khai bao thu vien giao dien va gan cho tk
from tkinter import ttk, messagebox  #ttk la goi nang cap cua tkinter lam cho giao dien xin hon
from tkcalendar import DateEntry #tao ra o chon lich cho ngay sinh


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
root.title(" Quản lý Học sinh ") #dat tieu de cho cua so
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
btn_them = tk.Button(frame_btn, text="Thêm", width=8)
btn_them.grid(row=0, column=0, padx=5)

btn_luu = tk.Button(frame_btn, text="Lưu", width=8)
btn_luu.grid(row=0, column=1, padx=5)

btn_sua = tk.Button(frame_btn, text="Sửa", width=8)
btn_sua.grid(row=0, column=2, padx=5)

btn_huy = tk.Button(frame_btn, text="Hủy", width=8)
btn_huy.grid(row=0, column=3, padx=5)

btn_xoa = tk.Button(frame_btn, text="Xóa", width=8)
btn_xoa.grid(row=0, column=4, padx=5)

btn_thoat = tk.Button(frame_btn, text="Thoát", width=8, command=root.quit)
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

root.mainloop() # giu cho cua so luon hien thi khong thi no hien len roi tat lien