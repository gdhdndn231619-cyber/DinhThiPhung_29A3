DSSV = []
def nhapds():
    sosv = int(input("Số lượng sinh viên: "))
    for i in range(sosv):
        print("Nhập sinh viên thứ", i + 1)
        masv = input("Nhập mã SV: ")
        ten = input("Nhập họ tên: ")
        gioitinh = input("Nhập giới tính: ")
        tuoi = int(input("Nhập tuổi: "))
        toan = float(input("Nhập điểm Toán: "))
        ly = float(input("Nhập điểm Lý: "))
        hoa = float(input("Nhập điểm Hoá: "))
        DTB = (toan + ly + hoa) / 3
        if DTB >= 8:
            xeploai = "giỏi"
        elif DTB >= 6.5:
            xeploai = "khá"
        elif DTB >= 5:
            xeploai = "trung bình"
        else:
            xeploai = "yếu"
        sv = {"Mã SV": masv, "Tên": ten, "Giới tính": gioitinh, "Tuổi": tuoi,
              "Toán": toan, "Lý": ly, "Hoá": hoa, "DTB": DTB, "Xếp loại": xeploai}
        DSSV.append(sv)

def inds():
    print("danh sách sinh viên")
    for sv in DSSV:
        print(sv["Mã SV"], "-", sv["Tên"], "-", sv["Giới tính"], "-", sv["Tuổi"], "-", sv["Toán"], "-", sv["Lý"], "-",
              sv["Hoá"], "-", sv["DTB"], "-", sv["Xếp loại"])

#a. Thêm SV
def themsinhvien():
    print("nhập thông tin sinh viên cần thêm: ")
    masv = input("Nhập mã SV: ")
    ten = input("Nhập họ tên: ")
    gioitinh = input("Nhập giới tính: ")
    tuoi = int(input("Nhập tuổi: "))
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hoá: "))
    DTB = (toan + ly + hoa) / 3
    if DTB >= 8:
        xeploai = "giỏi"
    elif DTB >= 6.5:
        xeploai = "khá"
    elif DTB >= 5:
        xeploai = "trung bình"
    else:
        xeploai = "yếu"
    sv = {"Mã SV": masv, "Tên": ten, "Giới tính": gioitinh, "Tuổi": tuoi,
          "Toán": toan, "Lý": ly, "Hoá": hoa, "DTB": DTB, "Xếp loại": xeploai}
    DSSV.append(sv)

#b.Cập nhật thông tin SV qua mã SV
def capnhatsv(masv):
    for sv in DSSV:
        if sv["Mã SV"] == masv:
            ten = input("Nhập họ tên: ")
            gioitinh = input("Nhập giới tính: ")
            tuoi = int(input("Nhập tuổi: "))
            toan = float(input("Nhập điểm Toán: "))
            ly = float(input("Nhập điểm Lý: "))
            hoa = float(input("Nhập điểm Hoá: "))
            DTB = (toan + ly + hoa) / 3
            if DTB >= 8:
                xeploai = "giỏi"
            elif DTB >= 6.5:
                xeploai = "khá"
            elif DTB >= 5:
                xeploai = "trung bình"
            else:
                xeploai = "yếu"
            sv["Tên"] = ten
            sv["Giới tính"] = gioitinh
            sv["Tuổi"] = tuoi
            sv["Toán"] = toan
            sv["Lý"] = ly
            sv["Hoá"] = hoa
            sv["DTB"] = DTB
            sv["Xếp loại"] = xeploai

#c.  Xoá SV bởi mã SV
def xoasv(masv):
    for sv in DSSV:
        if sv["Mã SV"] == masv:
            DSSV.remove(sv)
            print("Đã xoá sinh viên có mã:", masv)
            return
    print("Không tìm thấy sinh viên để xoá!")

#d. Tìm SV theo tên
def timkiemSV(tencantim):
    for sv in DSSV:
        if sv["Tên"]==tencantim:
            return "Có sinh viên cần tìm!"
    return "Không có sinh viên cần tìm!"

#Đếm số lượng sv có tên là cần tencantim(gv cho thêm)
def demSV(tencantim):
    dem=0
    for sv in DSSV:
        if sv["Tên"]==tencantim:
            dem+=1
    return dem

#Sắp xếp
def sapxeptheoDTB():
    return sorted(DSSV,key=lambda x:x["DTB"])
def sapxeptheoTEN():
    return sorted(DSSV,key=lambda x:x["Tên"])
def sapxeptheoMA():
    return sorted(DSSV,key=lambda x:x["Mã"])

def main():
    thuchien=True
    while thuchien:
        chon=input("1. Nhập danh sách sv \n"
                   "2. Hiển thị danh sách sv \n"
                   "3. Tìm kiếm sv \n"
                   "4. Xoá sv \n"
                   "5. Cập nhật sv\n"
                   "6. sắp xếp sv theo tên \n"
                   "7. Sắp xê theo mã sv \n"
                   "8. Sắp xếp theo ĐTB \n"
                   "9. Nhập 0 để thoát")
        if chon=="1":
            global sosv #biến toàn cục
            sosv=int(input("Số lượng sv: "))
            nhapds()
        if chon == "2":
            inds()
        if chon == "1":

#In DS
nhapds()
inds()

DSSV=sapxeptheoDTB()
print("Danh sách sv sau khi sắp xếp theo ĐTB:")
DSSV=sapxeptheoTEN()
print("Danh sách sv sau khi sắp xếp theo Tên:")
DSSV=sapxeptheoMA()
print("Danh sách sv sau khi sắp xếp theo Mã:")

themsinhvien()
print("Danh sách sinh viên sau khi thêm: ")
inds()

masv=input("Nhập mã sinh viên cần sửa: ")
capnhatsv(masv)
print("Danh sách sinh viên sau khi sửa: ")
inds()

masvxoa = input("nhập mã sinh viên cần xoá: ")
xoasv(masvxoa)
print("Danh sách sinh viên sau khi xoá: ")
inds()

tencantim=input("Nhập tên sinh viên cần tìm: ")
print(timkiemSV(tencantim))
print("Số sv có tên", tencantim, "là:",demSV(tencantim))


