import re
import json

# Sample input data
input_data = """
G*L3005/07JUNDAC/DOCS/ET/PNRL
 BG  3005 07JUN   DAC       900   773 DOCS ET PNRL   Y405
  1  ABDULLAH    MD  M AE54 U   JED 32C-F  1 M  ET DOCV DOCS
 287                                         ETI APP HAJ
         P/BGD/A03337108/BGD/01MAR78/M/23MAR32/ABDULLAH/MD
         CFFJDO
         9972100131253  C01 07JUN U DACJED LFTD
  2  ABDURRAHIM  MD MR AC43 U   JED 20G-F NB M  ET DOCV DOCS
 363                                         ETI APP HAJ
         P/BD/BX0235989/BD/17JUL1964/M/29SEP2023/ABDURRAHIM/MD
         CEWECV
         9972100130281  C01 07JUN U DACJED LFTD
  3  ABEDIN      MUKTA AC43 U   JED 12J-F  2 F  ET DOCV DOCS
 123                                         ETI APP HAJ
         P/BD/EA0163873/BD/10JUL1969/F/20MAR2024/ABEDIN/MUKTA
         CEWECV
         9972100130271  C01 07JUN U DACJED LFTD
  4  AHAMAD      MD MO AD43 U   JED 26F-F  2 M  ET DOCV DOCS
 277                                         ETI APP HAJ
         P/BD/EF0735634/BD/26DEC58/M/09MAR25/AHAMAD/MD MONSUR¥
         CFSPMK                                                ¥
         9972100131108  C01 07JUN U DACJED LFTD
  5  AHAMED      MD NU AE54 U   JED  2F-F  1 M  ET DOCV DOCS
 203                                         ETI APP HAJ
         P/BD/BQ0952784/BD/25NOV57/M/20NOV22/AHAMED/MD NUR
         CFFJDO
         9972100131233  C01 07JUN U DACJED LFTD
  6  AHMED       MD AB AB44 U   JED 19C-F  1 M  ET DOCV DOCS
 284                                         ETI APP HAJ
         P/BD/EB0330188/BD/04JUN1962/M/03JUL2024/AHMED/MD ABDUL
AZIZ                         .
         CWQVPK
         9972100130905  C01 07JUN U DACJED LFTD
  7  AHMED       JAMAL AB44 U   JED 38H-F  1 M  ET DOCV DOCS
 033                                         ETI APP HAJ
         P/BD/EF0691943/BD/01DEC1965/M/04MAR2025/AHMED/JAMAL///S
1                         .
         CWQVPK
         9972100130919  C01 07JUN U DACJED LFTD                ¥
  8  AHMED       SEYED AC43 U   JED  8A-F  2 M  ET DOCV DOCS   ¥
 327                                         ETI APP HAJ
         P/BD/EG0890335/BD/14JUN1963/M/27SEP2025/AHMED/SEYED AYE
Z UDDIN                         .
         CEWECV
         9972100130266  C01 07JUN U DACJED LFTD
  9  AHMED       MIR S AD43 U   JED 12D-F  2 F  ET DOCV DOCS
 189                                         ETI APP HAJ
         P/BD/EF0278176/BD/02FEB69/F/02DEC25/AHMED/MIR SURAIYA
         CFSPMK
         9972100131113  C01 07JUN U DACJED LFTD
 10  AHMED       MD BE AE54 U   JED  2D-F  2 M  ET DOCV DOCS
 165                                         ETI APP HAJ
         P/BD/E00003801/BD/21JUN67/M/01JUN26/AHMED/MD BENJIR
         CFFJDO
         9972100131215  C01 07JUN U DACJED LFTD
 11  AHMED       ZAFOR AG45 U   JED 24A-F  1 M  ET DOCV DOCS
 302                                         ETI APP HAJ
         P/BD/EE0570572/BD/11JAN1962/M/27NOV2024/AHMED/ZAFOR   ¥
         ZJANFN                                                ¥
         9972100130830  C01 07JUN U DACJED LFTD
 12  AHMED       KAZI  AG45 U   JED 40H-F  1 M  ET DOCV DOCS
 140                                         ETI APP HAJ
         P/BGD/EA0602281/BGD/01OCT1964/M/10MAY2024/AHMED/KAZI HA
SIBUDDIN                         .
         ZJANFN
         9972100130835  C01 07JUN U DACJED LFTD
 13  AHMED       SHAMI AI43 U   JED 30J-F  1 M  ET DOCV DOCS
 024                                         ETI APP HAJ
         P/BGD/EE0720421/BGD/02APR1987/M/03NOV2024/AHMED/SHAMIM
         HFZZAM
         9972100130995  C01 07JUN U DACJED LFTD
 14  AHMED       MEHED AJ42 U   JED 44D-F  2 M  ET DOCV DOCS
 202                                         ETI APP HAJ
         P/BD/B00134560/BD/07OCT89/M/29MAY32/AHMED/MEHEDI HASAN
         UBERLU
         9972100131093  C01 07JUN U DACJED LFTD
 15  AKHTAR      DR HA AD43 U   JED 44F-F NB F  ET DOCV DOCS   ¥
 209                                         ETI APP HAJ       ¥
         P/BGD/EF0645010/BGD/07OCT58/F/28FEB25/AKHTAR/DR HALIMA
         CFSPMK
         9972100131103  C01 07JUN U DACJED LFTD
 16  AKHTARUAMA  MD MR AB44 U   JED 44B-F  1 M  ET DOCV DOCS
 200                                         ETI APP HAJ
         P/BGD/EB0910015/BGD/31DEC1963/M/16SEP2024/AKHTARUAMAN/M
D                         .
         CWQVPK
         9972100130937  C01 07JUN U DACJED LFTD
 17  AKHTER      MST K AD43 U   JED  6B-F  1 F  ET DOCV DOCS
 166                                         ETI APP HAJ
         P/BD/A03651920/BD/01AUG69/F/25APR32/AKHTER/MST KHURSHID
A///S1                         .
         CFSPMK
         9972100131138  C01 07JUN U DACJED LFTD
 18  AKHTER      SALIN AE54 U   JED 45C-F NB F  ET DOCV DOCS
 167                                         ETI APP HAJ
         P/BGD/A02429464/BGD/10DEC73/F/28NOV31/AKHTER/SALINA   ¥
         CFFJDO                                                ¥
         9972100131235  C01 07JUN U DACJED LFTD
 19  AKHTER      SALIN AI43 U   JED 26J-F  1 F  ET DOCV DOCS
 008                                         ETI APP HAJ
         P/BGD/EE0855599/BGD/20OCT1967/F/25JAN2025/AKHTER/SALINA
         HFZZAM
         9972100130994  C01 07JUN U DACJED LFTD
 20  AKOND       MD AB AD43 U   JED 11G-F  1 M  ET DOCV DOCS
 138                                         ETI APP HAJ
         P/BD/BY0028309/BD/05FEB58/M/25NOV23/AKOND/MD ABDUL MANN
AN                         .
         CFSPMK
         9972100131123  C01 07JUN U DACJED LFTD
"""
#raice platter - 2 # porota - 1
# Initialize an empty list to hold the passenger information
passenger_info_list = []

# Split the input data into lines
lines = input_data.strip().split("\n")

# Iterate over the lines and extract the passenger information
for line in lines:
    # Use regular expressions to extract the passenger information from lines that contain it
    match = re.match(r"^\s*(\d+)\s+(.+?)\s+(\w{2})\s+(\w{1,2}\d+)\s+(\w+)\s+(\w{3})\s+(.+)$", line)
    if match:
        passenger = {}
        passenger['number'] = match.group(1)
        passenger['name'] = match.group(2).strip()
        passenger['title'] = match.group(3)
        passenger['seat'] = match.group(4)
        passenger['status'] = match.group(5)
        passenger['destination'] = match.group(6)
        passenger['flight_info'] = match.group(7).strip()

        passenger_info_list.append(passenger)

# Convert the list of passenger information to a JSON object
passenger_info_json = json.dumps(passenger_info_list)

# Print the JSON object
print(passenger_info_json)
