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

root.mainloop() # giu cho cua so luon hien thi khong thi no hien len roi tat lien