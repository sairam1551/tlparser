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
        print("Total time taken to complete (HH:MM:SS) : %d:%02d:%02d" % (hours, minutes, seconds))
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
    def main(Data_i):
       workTime = re.compile(r'((\d{0,1})\d:\d\d)(am|pm)( )*-( )*((\d{0,1})\d:\d\d)(am|pm)')
        timeElapsedInMinutes = 0
        flag = True
        line_number = 0;
        for line in Data_i:
            line_number += 1
            if (line.find("Time Log") != -1):
              flag = False
              continue
            if flag:
              continue
            line = line.lower()
            line = line.strip()
            if line and workTime.search(line):
              time = workTime.search(line)
              startTime = time.group(1)
              startTimeMeridiem = time.group(3)
              endTime = time.group(6)
              endTimeMeridiem = time.group(8)

              #for start time
              timeString = startTime.split(":")
              if(timeString[0] == "12"):
                timeString[0] = "0"
              startTimeInMinutes = int(timeString[0])*60 + int(timeString[1]) + (0 if startTimeMeridiem=="am" else 720)

              #for end time
              timeString = endTime.split(":")
              if(timeString[0] == "12"):
                timeString[0] = "0"
              endTimeInMinutes = int(timeString[0])*60 + int(timeString[1]) + (0 if endTimeMeridiem=="am" else 720)

              timeElapsedInMinutes += endTimeInMinutes - startTimeInMinutes if endTimeInMinutes > startTimeInMinutes else endTimeInMinutes - startTimeInMinutes + 1440

            else:
              st.write('Could not parse time in line '+str(line_number))
        st.write("Total time author spent : " + str(timeElapsedInMinutes//60) +" hrs " + str(timeElapsedInMinutes%60) + " minutes")
if __name__ == '__main__':
    st.title("Webapp for tl Parser")
    main_bg = "4397636.jpg"
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

    file = st.file_uploader(" Upload the TimeLog file here")
    if st.button("Generate"):
        line = str(file.read(),"utf-8")
        call_data = Timespent()
        call_data.main(Data_i=line)

