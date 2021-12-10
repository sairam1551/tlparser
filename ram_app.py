import sys
import datetime
import time
import streamlit as st
import base64

class Timespent:
    def TimeTotal(self,time_data):
        time_tot_author = datetime.timedelta()
        for tv in time_data:
            tv1 = datetime.datetime.strptime(tv[1], "%I:%M%p")
            tv2 = datetime.datetime.strptime(tv[0], "%I:%M%p")
            tv1_tv2 = (tv1 - tv2)
            if str(tv1_tv2).count('day') != 0:
                zero_c = "00:00:00"
                dd_fu = (str(tv1_tv2).split(",")[1].strip())
                tv4 = datetime.datetime.strptime(zero_c, "%H:%M:%S")
                tv3 = datetime.datetime.strptime(dd_fu, "%H:%M:%S")
                diff_v2 = (tv3 - tv4)
                time_tot_author += diff_v2
            else:
                time_tot_author += tv1_tv2
        seconds = time_tot_author.total_seconds()
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        st.write("Total time taken to complete (HH:MM:SS) : %d:%02d:%02d" % (hours, minutes, seconds))
    def fileRead(self,inputFilename):
        data_o = []
        Data_i = open(inputFilename, "r")
        data_o.extend(Data_i.readlines())
        Data_i.close()
        return data_o
    def timechange(self,timeData):
        try:
            time.strptime(timeData, '%I:%M%p')
            return "Y"
        except ValueError:
            return "N"
    def main(self,Data_i):
        cl_initial = 0
        ftd = []
        colist = Data_i.split("\n");
        if cl_initial != "TimeLog":
            for iv in range(int(cl_initial), len(colist)):
                fsd = (colist[iv].split(' - ')[0].split())
                ssd = (colist[iv].split(' - ')[1:])
                counter = (colist[iv].split(' - ')[1:])
                if len(fsd) != 0:
                    timeformatstatus = self.timechange(fsd[-1].strip())
                    if len(counter) != 0:
                        timeformatstatus_v1 = self.timechange(ssd[0].split()[0])
                        if timeformatstatus_v1 == "Y" and timeformatstatus == "Y":
                            ftd.append((fsd[-1], str(ssd[0].split()[0])))
                    else:

                        st.write("Time stamp not present in the line:  ", iv + 1)
                else:

                    st.write("No time stamp present in the line:  ", iv + 1)
            self.TimeTotal(ftd)
        else:
            st.write("Time Log not in the file :  ", Data_i)
if __name__ == '__main__':
    st.title("Web App for TL Parser")
    main_bg = "main.jpg"
    main_bg_ext = "jpg"
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>""",
    unsafe_allow_html=True
    )

    file = st.file_uploader(" Upload the Time Log file here")
    if st.button("Generate"):
        line = str(file.read(),"utf-8")
        call_data = Timespent()
        call_data.main(Data_i=line)

