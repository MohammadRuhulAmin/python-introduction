import re
import json

# message =  "G*L721/19APRDAC/DOCS\n  1  ABDULLAH              FNU MR                     K  MCT       F  0  M DOCS ETI           P/BGD/A05170263/BD/28MAR84/M/22OCT32/ABDULLAH/FNUMR//H\n  2  ABDUR ROSHID          RUBEL MR                   E  MCT       F  0  M IB DOCS ETI        P/BD/BX0586463/BD/12JAN1987/M/23OCT2023/ABDUR ROSHID/RUBEL\n  3  ABUL                  BASHAR MR                  V  MCT       F  0  M DOCS ETI           P/BGD/EJ0224656/BGD/17JUN85/M/06JUN26/ABUL/BASHAR\n  4  ADITTO                DHAR MSTR CHD         AC3  K  MCT       F  0  IB DOCS ETI          P/BGD/A05307225/BGD/28OCT15/M/15OCT27/DHAR/ADITTO\n  5  AFRIN                 SANJIDA MRS                K  MCT       F  0  F DOCS ETI           P/BGD/EH0468638/BGD/02JAN10/F/12JAN26/AFRIN/SANJIDAMRS\n  6  AHMAD                 SUHEL MR              AQ2  K  MCT       F  0  M DOCS ETI           P/BGD/A07012694/BGD/02JAN98/M/12FEB33/AHMAD/SUHEL\n  7  AHMED                 ABULBASHAR MSTR       AB7  K  MCT       F  0  CHD DOCS ETI         P/BGD/A00201471/BGD/01OCT18/M/16DEC25/AHMED/ABULBASHARMSTR\n  8  AHMED                 ABU TAHER MSTR        AB7  K  MCT       F  0  CHD DOCS ETI         P/BGD/A00201470/BGD/01OCT18/M/16DEC25/AHMED/ABUTAHERMSTR\n  9  AHMED                 SHAKERMR                   E  MCT       F  0  M IB DOCS ETI        P/BD/BT0496021/BD/19FEB1999/M/12MAY2023/SHAKER/AHMED\n 10  AHMED                 SALEH MR              AH2  K  MCT       F  0  M IB DOCS ETI        P/BGD/B00846346/BGD/30DEC81/M/06AUG32/AHMED/SALEH\n 11  AHMED                 SHAHIDMR                   K  MCT       F  0  M IB DOCS ETI        P/BGD/A03592430/BGD/12MAY78/M/14AUG27/AHMED/SHAHID\n 12  AHMED                 MD MUMIN MR                K  MCT       F  0  M IB DOCS ETI        P/BGD/A02809236/BGD/12JUL89/M/30JAN27/AHMED/MDMUMIN"
# pattern = re.compile("^[A-Z][*][A-Z0-9]+\/[0-9A-Z]+\/DOCS")
# print(pattern.match(message))
# print(pattern.search(message))
#
# text = "I have a dog.\n My dog is brown \nand my\n neighbor's dog is black."
# print(text)
# new_text = re.sub(r'\s', '', text)
# new_text = re.sub(r'\s',' + ',text)
# new_text = re.sub(r'\n','',text)
# print(new_text)
#
# pattern2 = r'\b\w{4}\b'
# res = re.findall(pattern2,message)
# print(res)

my_tuple = ('apple/banana/orange/mango')
for item in my_tuple:
    split_items = item.split('/')[0]
    print(split_items)
