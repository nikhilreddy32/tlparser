from datetime import datetime
import streamlit as st

st.title("Webpage for TimeLog Parser")
if __name__ ==  "__main__" :
  docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
  if st.button("Process"):
    if docx_file is not None:
        file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
        st.write(file_details)
        # Check File Type
        if docx_file.type == "text/plain":
          line = str(docx_file.read(),"utf-8")

    cnt = 1
    count = 0
    sum = 0
    while line:
      if "am" not in line or "pm" not in line :
           count += 1
      else:

        letter = line.split(': ')
        begin = letter[-1].split('- ')
        str2 = begin[-1].strip()
        finish = str2.split(" ")
        init = begin[0].strip()
        init = init.split(":")
        x = init[0] + ":" + init[1][:2] + " " + init[1][2:].upper()
        inis = finish[0].strip()
        inis = inis.split(":")
        y = inis[0] + ":" + inis[1][:2] + " " + inis[1][2:].upper()
        in_ = datetime.strptime(x,"%I:%M %p")
        int_time = datetime.strftime(in_, "%H:%M")
        int_time = datetime.strptime(int_time,"%H:%M")
        ou_ = datetime.strptime(y,"%I:%M %p")
        out_time = datetime.strftime(ou_, "%H:%M")
        out_time = datetime.strptime(out_time,"%H:%M")
        sum += (out_time - int_time).total_seconds()/60/60
      line = docx_file.readline()
      cnt += 1

    st.write(f" Time spend by the author on this file is - {abs(sum)} ")
    st.write(f" The number of lines which did not have any time values - {count}")
