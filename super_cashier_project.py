# -*- coding: utf-8 -*-
"""Super Cashier-Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s2dgCsgYLlKmCAEDt0iHpr92Ng2OMckX
"""

import pandas as pd
import numpy as np

tabel1 = pd.DataFrame({'nama item':[], 'jumlah item':[],'harga per item':[]})

class Transaction():
  def add_item(self,nama_item,jumlah_item,harga_per_item):
    global tabel1
    new_item = pd.DataFrame({'nama item':[nama_item], 'jumlah item':[jumlah_item],'harga per item':[harga_per_item]})
    tabel1 = tabel1.append(new_item, ignore_index=True)

  def update_item_name(self,nama_item, update_nama_item):
    global tabel1
    tabel1.loc[tabel1['nama item'] == nama_item, 'nama item'] = update_nama_item

  def update_item_qty(self,jumlah_item,update_jumlah_item):
    global tabel1
    tabel1.loc[tabel1['jumlah item'] == jumlah_item, 'jumlah item'] = update_jumlah_item

  def update_item_price(self,harga_per_item,update_harga_per_item):
    global tabel1
    tabel1.loc[tabel1['harga per item'] == harga_per_item, 'harga per item'] = update_harga_per_item

  def delete_item(self,nama_item):
    global tabel1
    tabel1 = tabel1[tabel1['nama item']!= nama_item]

  def reset_item(self):
    global tabel1
    tabel1 = pd.DataFrame({'nama item':[],'jumlah item':[],'harga per item':[]})

  def check_order(self):
    global tabel1
    is_order_correct = True
    for column in tabel1.columns:
      if (tabel1[column] == "").any():
        is_order_correct = False
        break
    if is_order_correct:
      print("pemesanan sudah benar")
    else:
      print("terdapat kesalahan input data")

  def total_price(self):
    global tabel1
    rowprice = 0 #row price adalah total harga per baris
    totalprice = 0 #total price adalah harga keseluruhan
    for index, row in tabel1.iterrows():
      rowprice += row['jumlah item'] * row['harga per item']
    if rowprice >= 200000:
      totalprice = rowprice*0.95
      print(totalprice)
    elif rowprice >= 300000:
      totalprice = rowprice*0.92
      print(totalprice)
    elif rowprice >= 500000:
      totalprice = rowprice*0.90
      print(totalprice)
    else:
      print(rowprice)
    return totalprice

transaksi1 = Transaction()
transaksi1.add_item("minyak",23,123)
transaksi1.add_item("lobak",14,200)
print(tabel1)
transaksi1.update_item_name("minyak","sawi")
print(tabel1)
transaksi1.update_item_qty(23,45)
print(tabel1)
transaksi1.update_item_price(123,10000)
print(tabel1)
transaksi1.delete_item("sawi")
print(tabel1)
#transaksi1.reset_item
#print(tabel1)
transaksi1.check_order()
print(tabel1)
total_price = transaksi1.total_price()
print(total_price)
