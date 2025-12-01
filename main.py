import tkinter as tk 
from tkinter import ttk, messagebox  
from tkcalendar import DateEntry
import pandas as pd
from datetime import datetime

import mysql.connector 

def connect_db(): 

    return mysql.connector.connect(
       
       
        host="localhost",
        user="root",
        password="",
        
        database="qlhocsinh"
       
    )


def load_data():
    
    for item in tree.get_children(): 
        tree.delete(item)  

   
    conn = connect_db()  
    cursor = conn.cursor() 
    
    cursor.execute("SELECT * FROM hocsinh") 
   
    rows = cursor.fetchall() 
    
    for row in rows:
        tree.insert("", tk.END, values=row)
        
    conn.close()
    
def them_hs():
    try:
        
        mahs = entry_mahs.get()
        holot = entry_holot.get()
        ten = entry_ten.get()
        phai = gender_var.get()
        ngaysinh = entry_ngaysinh.get()
        lop = entry_lop.get()
        trangthai = cbb_trangthai.get()
        diachi = entry_diachi.get()

      
        if mahs == "" or ten == "":
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã HS và Tên!")
            return 
       
        conn = connect_db()
        cursor = conn.cursor()
        
       
        sql = "INSERT INTO hocsinh (mahs, holot, ten, phai, ngaysinh, lop, trangthai, diachi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (mahs, holot, ten, phai, ngaysinh, lop, trangthai, diachi)
        
        cursor.execute(sql, values) 
        conn.commit() 
        conn.close()

       
        messagebox.showinfo("Thành công", "Đã thêm học sinh mới!")
        load_data() # bảng cập nhật ngay lập tức dòng vừa thêm
        
        entry_mahs.delete(0, tk.END)
        entry_ten.delete(0, tk.END)
       
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm học sinh:\n{str(e)}")


def xoa_hs():
    try:
        selected_item = tree.selection() 
        
        if not selected_item:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn học sinh cần xóa trên bảng!")
            return

      
        values = tree.item(selected_item)['values'] 
        mahs = values[0] 

        confirm = messagebox.askyesno("Xác nhận xóa", f"Bạn có chắc muốn xóa học sinh có Mã {mahs} không?")
        
        if confirm == True:
            
            conn = connect_db()
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM hocsinh WHERE mahs=%s", (mahs,))
           
            
            conn.commit() 
            conn.close()

           
            messagebox.showinfo("Thành công", "Đã xóa học sinh!")
            load_data()
            
          
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
        
        mahs = entry_mahs.get()
        holot = entry_holot.get()
        ten = entry_ten.get()
        phai = gender_var.get()
        ngaysinh = entry_ngaysinh.get()
        lop = entry_lop.get()
        trangthai = cbb_trangthai.get()
        diachi = entry_diachi.get()

        
        conn = connect_db()
        cursor = conn.cursor()
        
      
        sql = """UPDATE hocsinh 
                 SET holot=%s, ten=%s, phai=%s, ngaysinh=%s, lop=%s, trangthai=%s, diachi=%s 
                 WHERE mahs=%s"""
        
        values = (holot, ten, phai, ngaysinh, lop, trangthai, diachi, mahs)
        
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

        
        messagebox.showinfo("Thành công", "Đã lưu thông tin học sinh!")
        load_data()
        
       
        entry_mahs.delete(0, tk.END)
        entry_ten.delete(0, tk.END)
      

    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu:\n{str(e)}")

def clear_input():
   
    entry_mahs.delete(0, tk.END)
    entry_holot.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_lop.delete(0, tk.END)
    entry_diachi.delete(0, tk.END)
    
  
    gender_var.set("Nam")
    entry_ngaysinh.set_date(None) 
    cbb_trangthai.set("")
    
    for item in tree.selection():
        tree.selection_remove(item)


def tim_kiem_hs():
    try:
        
        keyword = entry_timkiem.get()
        
        if keyword == "":
            messagebox.showwarning("Thông báo", "Vui lòng nhập tên hoặc mã số để tìm!")
            return

      
        for item in tree.get_children():
            tree.delete(item)

        
        conn = connect_db()
        cursor = conn.cursor()
        
        sql = "SELECT * FROM hocsinh WHERE ten LIKE %s OR mahs LIKE %s"
        params = (f"%{keyword}%", f"%{keyword}%")
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        
        if len(rows) == 0:
             messagebox.showinfo("Thông báo", "Không tìm thấy học sinh nào!")
        
        for row in rows:
            tree.insert("", tk.END, values=row)
            
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi tìm kiếm:\n{str(e)}")

def xuat_excel():
    try:
       
        conn = connect_db()
        
        sql = "SELECT * FROM hocsinh"
        df = pd.read_sql(sql, conn)
        
       
        df.columns = ['Mã HS', 'Họ lót', 'Tên', 'Phái', 'Ngày sinh', 'Lớp', 'Trạng thái', 'Địa chỉ']
        
        
        ngay_gio = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ten_file = f"DanhSachHocSinh_{ngay_gio}.xlsx"
        
      
        df.to_excel(ten_file, index=False, engine='openpyxl')
        
        conn.close()
        
        messagebox.showinfo("Thành công", f"Đã xuất file Excel: {ten_file}\n(File nằm trong thư mục dự án)")
        
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xuất file:\n{str(e)}")

def center_window(win,w = 800,h = 600):
    ws = win.winfo_screenwidth() 
    hs = win.winfo_screenheight() 
    x = (ws // 2) - (w //2)
    y = (hs // 2) - (h //2)
    win.geometry(f'{w}x{h}+{x}+{y}') 


root = tk.Tk() 
root.title(" Quản Lý Học Sinh ") 
center_window(root,800,600) 
root.resizable(False, False) 


lbl_title = tk.Label(root,text = "QUẢN LÝ HỌC SINH",font = ("Arial",18,"bold")) 
lbl_title.pack(pady = 10) 

frame_info = tk.Frame(root)
frame_info.pack(pady = 5,padx = 10,fill = "x") 

lbl_mahs = tk.Label(frame_info,text ="Mã học sinh") 
lbl_mahs.grid(row = 0,column = 0,padx = 5,pady = 5,sticky = "w") 


entry_mahs = tk.Entry(frame_info,width = 20)
entry_mahs.grid(row = 0,column = 1,padx = 5,pady = 5,sticky ="w")

lbl_holot = tk.Label(frame_info,text ="Họ lót")
lbl_holot.grid(row = 1,column = 0,padx = 5,pady = 5,sticky ="w") #sticky ="w" la west dinh le trai

entry_holot = tk.Entry(frame_info,width = 20)
entry_holot.grid(row = 1,column = 1,padx = 5,pady = 5,sticky ="w")

lbl_ten = tk.Label(frame_info,text = "Tên")
lbl_ten.grid(row = 1,column = 2,padx = 5,pady = 5,sticky = "w")

entry_ten = tk.Entry(frame_info,width = 20)
entry_ten.grid(row = 1,column = 3,padx = 5,pady = 5,sticky = "w")

lbl_phai = tk.Label(frame_info, text="Phái:")
lbl_phai.grid(row=2, column=0, padx=5, pady=5, sticky="w")

gender_var = tk.StringVar(value="Nam") 

radio_nam = tk.Radiobutton(frame_info, text="Nam", variable=gender_var, value="Nam")
radio_nam.grid(row=2, column=1, padx=5, sticky="w")

radio_nu = tk.Radiobutton(frame_info, text="Nữ", variable=gender_var, value="Nữ")
radio_nu.grid(row=2, column=1, padx=60, sticky="w") 

lbl_ngaysinh = tk.Label(frame_info, text="Ngày sinh:")
lbl_ngaysinh.grid(row=2, column=2, padx=5, pady=5, sticky="w")

entry_ngaysinh = DateEntry(frame_info, width=18, date_pattern="yyyy-mm-dd")
entry_ngaysinh.grid(row=2, column=3, padx=5, pady=5)


lbl_lop = tk.Label(frame_info, text="Lớp:")
lbl_lop.grid(row=3, column=0, padx=5, pady=5, sticky="w")


entry_lop = tk.Entry(frame_info, width=20)
entry_lop.grid(row=3, column=1, padx=5, pady=5)


lbl_trangthai = tk.Label(frame_info, text="Trạng thái:")
lbl_trangthai.grid(row=3, column=2, padx=5, pady=5, sticky="w")

trangthai_values = ["Đang học", "Đã tốt nghiệp", "Bảo lưu", "Bị đình chỉ"]


cbb_trangthai = ttk.Combobox(frame_info, values=trangthai_values, width=18)
cbb_trangthai.grid(row=3, column=3, padx=5, pady=5)


lbl_diachi = tk.Label(frame_info, text="Địa chỉ:")
lbl_diachi.grid(row=4, column=0, padx=5, pady=5, sticky="w")

entry_diachi = tk.Entry(frame_info, width=60)
entry_diachi.grid(row=4, column=1, padx=5, pady=5, columnspan=3)


frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)


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

btn_thoat = tk.Button(frame_btn, text="Thoát", width=8, command=root.quit) 
btn_thoat.grid(row=0, column=5, padx=5)

btn_excel = tk.Button(frame_btn, text="Xuất Excel", width=10, bg="#90EE90", command=xuat_excel)
btn_excel.grid(row=0, column=6, padx=5) 

frame_timkiem = tk.Frame(root)
frame_timkiem.pack(pady=10)

lbl_tim = tk.Label(frame_timkiem, text="Nhập Tên hoặc Mã số:")
lbl_tim.grid(row=0, column=0, padx=5)

entry_timkiem = tk.Entry(frame_timkiem, width=30)
entry_timkiem.grid(row=0, column=1, padx=5)

btn_tim = tk.Button(frame_timkiem, text="Tìm kiếm", width=10, bg="#87CEEB", command=tim_kiem_hs)
btn_tim.grid(row=0, column=2, padx=5)

btn_hienthi = tk.Button(frame_timkiem, text="Hiện tất cả", width=10, command=load_data)
btn_hienthi.grid(row=0, column=3, padx=5)


lbl_ds = tk.Label(root, text="Danh sách học sinh", font=("Arial", 12, "bold"))
lbl_ds.pack(pady=5, padx=10, anchor="w")


columns = ("mahs", "holot", "ten", "phai", "ngaysinh", "lop", "trangthai", "diachi")

tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

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

tree.pack(padx=10, pady=5, fill="both", expand=True)

load_data()
clear_input()

root.mainloop() 