USD_RATE: float = 1.57

cpu_price: float = float(input())
gpu_price: float = float(input())
ram_price: float = float(input())
ram_qty: int = int(input())
discount: float = float(input())

cpu_price_lv: float = cpu_price * USD_RATE
cpu_discount_lv: float = cpu_price_lv * discount
cpu_final_lv: float = cpu_price_lv - cpu_discount_lv

gpu_price_lv: float = gpu_price * USD_RATE
gpu_discount_lv: float = gpu_price_lv * discount
gpu_final_lv: float = gpu_price_lv - gpu_discount_lv

ram_price_lv: float = ram_price * USD_RATE
ram_final_lv: float = ram_price_lv * ram_qty

total: float = cpu_final_lv + gpu_final_lv + ram_final_lv

print(f'Money needed - {total:.2f} leva.')
