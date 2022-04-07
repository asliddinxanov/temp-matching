# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 09:01:20 2022

@author: asliddinxanov
"""
import sys
import cv2
if len(sys.argv)<3: #実行時に引数が2ない場合はこれが表示される
	print('表示したいファイル名を指定してください')
	sys.exit()#強制終了するため
file=sys.argv[1]#引数で指定されたファイル名
file_templ=sys.argv[2]

try:
	img=cv2.imread(file)#画像読み込み
	img_template=cv2.imread(file_templ)
	if (img is None) or (img_template is None):
		raise ValueError("ファイルが見つかりません")

	cv2.rectangle(img,(90,20),(400,60),(255,255,255),2,4)#四角を作る

	result_match = cv2.matchTemplate(img,img_template,cv2.TM_CCOEFF)#検索手法は色々あって、一つ読み込む
	cv2.imshow("Template Matching",result_match)#マッチング後の画像を表示する
	cv2.waitKey(0)#スペース入力で削除する(1)

	min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result_match)#類似度が大きく、小さきなる画素の位置を調べて抽出する
	top_left=max_loc
	bottom_right=(top_left[0]+img_template.shape[1],top_left[1]+img_template.shape[0])

	cv2.putText(img,'Face matchig...',(100,50),cv2.FONT_HERSHEY_COMPLEX,1.1,(234,36,98),2)#テキストを作る(1)
	cv2.putText(img,"Leo Messi!->",(5,400),cv2.FONT_HERSHEY_COMPLEX,1.1,(0,0,255),2)#テキストを作る(2)

	cv2.rectangle(img,top_left,bottom_right,(0,0,255),2)
	cv2.imshow('file+Text+View Rectangle',img)#ファイル名の画像を表示する
	cv2.waitKey(0)#スペース入力で削除する(2)
	cv2.destroyAllWindows()

except ValueError as e:
	print(e)
except:
	import traceback
	traceback.print_exc()