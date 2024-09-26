def calculation(bill_amount, tip_percent):
    total= bill_amount*(1+0.01*tip_percent)
    total= round(total,2)
    print(f"please pay the ${total}")
calculation(150,20)
