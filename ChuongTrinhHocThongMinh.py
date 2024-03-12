#Bài 1:
def xemlich():
            m30=[4,6,9,11]
            mo=int(input("Chào mừng quý khách đến với mục xem lịch!\nNhập tháng: "))
            while mo < 1 or mo > 12:
                mo=int(input("Nhập lại tháng: "))
            if mo == 2:
                y = int(input("nhập năm: "))
                if y % 4 == 0 or y % 400 ==0:
                    return "Vì năm "+str(y)+" là năm nhuận nên tháng " +str(mo)+" có 29 ngày"
                else:
                    return "Vì năm "+str(y) +" không phải là năm nhuận nên tháng "+str(mo)+" có 28 ngày"
            elif mo in m30:
                return "Tháng "+str(mo)+" có 30 ngày"
            else:
                return "Tháng "+str(mo)+" có 31 ngày"
#Bài 2:
def tinhluong():
            sogiolam=float(input("Chào mừng quý khách đến với mục tính lương!\nNhập số giờ làm: "))
            luonggio=float(input("Lương giờ: "))
            tienluong = 0
            while sogiolam <= 0:
                sogiolam = float(input("Nhập lại số giờ làm: "))
            while luonggio <= 0:
                luonggio = float(input("Nhập lại lương giờ: "))
            if sogiolam > 40:
                tienluong = tienluong + ((sogiolam-40) * 1.5*luonggio) + sogiolam*luonggio
                return "Tổng số tiền nhân viên làm được, có tăng ca(40 giờ trở lên): "+str(tienluong)
            elif sogiolam <= 40:
                tienluong = sogiolam*luonggio
                return "Tổng số tiền nhân viên làm được, không tăng ca(40 giờ trở xuống): "+str(tienluong)    
#Bài 3:
def danhsachluong():
            snvcl = int(input("Chào mừng quý khách đến với mục xem danh sách lương của nhân viên!\nSố nhân vên có lương: "))
            danhsachluong=[]
            for i in range (snvcl):
                print("Lương nhân viên thứ",i+1,": ",end="")
                a=int(input())
                danhsachluong.append(a)
            for i in range(snvcl):
                for m in range(i+1,snvcl):
                    if danhsachluong[i] > danhsachluong[m]:
                        b = danhsachluong[i]
                        danhsachluong[i] = danhsachluong[m]
                        danhsachluong[m] = b
            return "Danh sách lương của nhân viên: "+str(danhsachluong)      
#Bài 4:
def thongtinnhanvien():
            nhapten=input("Chào mừng qúy khách đến với mục xem thông tin nhân viên!\nNhập họ và tên: ")
            vitri=0
            for i in range(len(nhapten)):
                if nhapten[i] ==" ":
                    vitri=i
            return "Họ và tên lót của nhân viên là: "+str(nhapten[:vitri].title())+"\n"+"Tên của nhân viên là: "+str(nhapten[1+vitri:].title())+"\n"+"Họ và tên đầy đủ của nhân viên là: "+str(nhapten.title())
#Bài 5:
def tinhdiemhocsinh():
            n = int(input("Chào mừng quý khách đến với mục tính điểm của học sinh!\nNhập số lượng môn tính điểm trung bình: "))
            all=""
            hesotong = 0
            diemtb = 0
            list=[1,1.5,2,2.5,3]
            diem2mon=0
            for i in range(n):
                diemmon = float(input("Nhập điểm môn thứ "+str(i+1)+": "))
                while diemmon > 10 or diemmon < 0:
                    diemmon = float(input("Nhập lại điểm môn thứ "+str(i+1)+": "))
                heso = float(input("Nhập hệ số môn thứ "+str(i+1)+": "))
                while heso not in list:
                    heso = float(input("Nhập lại hệ số môn thứ "+str(i+1)+": "))
                hesotong = hesotong + heso
                diem2mon = diem2mon + (heso * diemmon)
                diemtb = diem2mon / hesotong
            all=all+"Số môn tính điểm trung bình: "+str(n)+"\nTổng hệ số: "+str(hesotong)+"\nĐiểm trung bình của "+str(n)+" môn: "+str(round(diemtb,1))
            return all
#Bài 6:
def ketthuc():
    return "Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi. Chúc quý khách có một ngày tốt lành ❤ 🍀 !"  
while True:
    print(" "*26 + " * "*19+" "*8+"\n"+" "*26 + " * "*5+"Chương trình học thông minh" + " * " *5+" "*8+"\n"+" "*26 + " * "*19+" "*8+"\n"+"\n"+" "*13 + "="*40 + "MENU" +"="*40+"\n"+"\n"+"Xin vui lòng chọn:\n1. Xem lịch.\n2. Tính lương\n3. Xem lương.\n4. Xem thông tin nhân viên.\n5. Tính điểm của học sinh.\n6. Thoát chương trình.")
    choose=int(input("Lựa chọn của quý khách: "))
    cho=[1,2,3,4,5,6]
    while choose not in cho:
        choose=int(input("Nhập lại lựa chọn của quý khách: "))
    #Bài 1:
    if choose == 1:
        print(xemlich())
        bo=input("Nếu quý khách muốn quay lại menu vui lòng nhấn: back và ấn enter.\nNếu quý khách muốn thoát chương trình vui lòng nhấn: out và ấn enter.\nLựa chọn của quý khách la : ")
    #bài 2:
    elif choose == 2:
        print(tinhluong())
        bo=input("Nếu quý khách muốn quay lại menu vui lòng nhấn: back và ấn enter.\nNếu quý khách muốn thoát chương trình vui lòng nhấn: out và ấn enter.\nLựa chọn của quý khách la : ")
    #Bài 3:
    elif choose == 3:
        print(danhsachluong())
        bo=input("Nếu quý khách muốn quay lại menu vui lòng nhấn: back và ấn enter.\nNếu quý khách muốn thoát chương trình vui lòng nhấn: out và ấn enter.\nLựa chọn của quý khách la : ")
    #Bài 4:
    elif choose == 4:
        print(thongtinnhanvien())
        bo=input("Nếu quý khách muốn quay lại menu vui lòng nhấn: back và ấn enter.\nNếu quý khách muốn thoát chương trình vui lòng nhấn: out và ấn enter.\nLựa chọn của quý khách la : ")
    #Bài 5:
    elif choose == 5:
        print(tinhdiemhocsinh())
        bo=input("Nếu quý khách muốn quay lại menu vui lòng nhấn: back và ấn enter.\nNếu quý khách muốn thoát chương trình vui lòng nhấn: out và ấn enter.\nLựa chọn của quý khách la : ")
    #Bài 6:
    elif choose == 6:
        print(ketthuc())
        break
    if bo == "back":
        continue
    elif bo == "out":
        print("Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi. Chúc quý khách có một ngày tốt lành ❤ 🍀 !")
        break  
   

