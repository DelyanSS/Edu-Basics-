bitcoin = int(input())
chinese_youan = float(input())
commision = float(input())

bit_leva = bitcoin*1168
bit_euro = bit_leva/1.95

youan_doll = chinese_youan*0.15
youan_leva = youan_doll*1.76
youan_euro = youan_leva/1.95

commision_minus = (bit_euro+youan_euro)*(commision*0.01)
money = bit_euro+youan_euro - commision_minus

print(f"{money:.2f}")