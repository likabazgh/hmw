used_products = set()

for row in range(1, 10):
    output_row = []
    for col in range(1, row + 1):
        product = row * col
        
        if product not in used_products:
            output_row.append(f"{col} * {row} = {product}")
            used_products.add(product)
    
    print(output_row)