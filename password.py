import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
symbols="!@#$%^&*()."
length=8
string=lower + upper +digits +symbols
password="" +(random.sample(string,length))