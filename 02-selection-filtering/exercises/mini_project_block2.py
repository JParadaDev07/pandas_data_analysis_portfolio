import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir.parent / "resources/products.csv")

def get_category(df, cat):
    result = (
        df.query('category == @cat')
        .loc[df['is_active'] == 1, ['product_name', 'category', 'rating', 'price']]
        .sort_values('rating', ascending=False)
    )    
    return result

def provider_analysis(df, prov):
    main_filter = 'supplier == @prov and is_active == 1'
    product_quantity, average_data, total_stock = (
        len(df.query(main_filter)),
        df.query(main_filter)[['price', 'rating']].mean(),
        df.query(main_filter)['stock'].sum())

    return product_quantity, average_data, total_stock
    
def reports(df, report_name):
    report_dir = current_dir / "reports" 

    if not report_dir.exists():
        report_dir.mkdir(parents=True, exist_ok=True)
        print(f"Se creó la carpeta: {report_dir}")
    
    report_path = report_dir / report_name
    
    try:
        df.to_csv(report_path, index=False)
        print(f"Los reportes se han creado satisfactoriamente en la ruta: {report_dir}")
    except PermissionError:
        print(f"\nPermiso denegado para exportar en: {report_dir}")
    except Exception as e:
        print(f"\nError innesperado: {e}")
    return current_dir
    
category_dict = {
    'electronic_category' : 'Electronics', 
    'furniture_category' : 'Furniture'
}

provider_dict = {
    'tech_provider' : 'TechSupply',
    'office_provider' : 'OfficeMax'
}


# ───────────────────────────────────────────────────────────────────────────
# TAREA 1: Reporte de Productos de Alto Valor
# ───────────────────────────────────────────────────────────────────────────
high_value_products = (
    df.loc[(df['price'] >= 800000) 
           & (df['rating'] >= 4.5) 
           & (df['is_active'] == 1), 
           ['product_name', 'price', 
            'rating', 'stock', 'supplier']]
    .sort_values('price', ascending=False)
)
print(f"\nProductos de 'Alto Valor':\n{high_value_products}\n")

# ───────────────────────────────────────────────────────────────────────────
# TAREA 2: Análisis de Stock Crítico
# ───────────────────────────────────────────────────────────────────────────
critical_stock = (
    df.loc[(df['stock'] < 25) 
           & (df['is_active'] == 1) 
           & ~(df['category'] == "Furniture"),
           ['product_name', 'category', 'stock','supplier']])

print(f"\nProductos con 'Stock Crítico':\n{critical_stock}\n")

# ───────────────────────────────────────────────────────────────────────────
# TAREA 3: Electronics de Rango Medio
# ───────────────────────────────────────────────────────────────────────────            
mid_range_electronics = (
    df.query('category == @category_dict["electronic_category"]')
    .loc[(df['price'].between(100000, 500000)) & (df['stock'] >= 30), 
        ['product_name', 'price', 'stock', 'rating']]
)

print(f"\nProductos de 'Rango Medio':\n{mid_range_electronics}\n")

# ───────────────────────────────────────────────────────────────────────────
# TAREA 4: Top 5 Productos por Categoría
# ───────────────────────────────────────────────────────────────────────────
top_electronics = get_category(df, category_dict['electronic_category'])
top_furniture = get_category(df, category_dict['furniture_category'])

print(f"\nTop 5 de productos de la categoría 'Electronics':\n{top_electronics}\n")
print(f"\nTop 5 de productos de la categoría 'Furniture':\n{top_furniture}\n")

# ───────────────────────────────────────────────────────────────────────────
# TAREA 5: Búsqueda de Productos Específicos
# ───────────────────────────────────────────────────────────────────────────
featured_products = (df.loc[df['product_name'].str.contains
                    ('Gaming|Ergonómica|HD|WiFi', case=False), 
                    ['product_name', 'category', 'price']])

print(f"\nProductos de 'Específicos':\n{featured_products}\n")

# ───────────────────────────────────────────────────────────────────────────
# TAREA 6: Análisis por Proveedor
# ───────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("ANÁLISIS POR PROVEEDOR")
print("=" * 70)


# TechSupply
tech_supply = provider_analysis(df, provider_dict['tech_provider'])
print("Reporte comparativo de proveedores - TECHSUPPLY:\n")
print(f"Cantidad de productos activos del proveedor: {tech_supply[0]}")
print(f"Promedio de precio: ${tech_supply[1]['price']:,.0f}")
print(f"Promedio de rating: {tech_supply[1]['rating']:.2f}")
print(f"Stock total: {tech_supply[2]}")

# OfficeMax
office_max = provider_analysis(df,provider_dict['office_provider'])
print("\nReporte comparativo de proveedores - OFFICEMAX:\n")
print(f"Cantidad de productos activos del proveedor: {office_max[0]}")
print(f"Promedio del precio: ${office_max[1]['price']:,.0f}")
print(f"Promedio de rating: {office_max[1]['rating']:.2f}")
print(f"Stock total: {office_max[2]}")



# ───────────────────────────────────────────────────────────────────────────
# TAREA 7: Exportación de Reportes
# ───────────────────────────────────────────────────────────────────────────
reports_dict = {
    "hvr" : "report_high_value.csv",
    "cls" : "report_critical_stock.csv",
    "mde" : "report_mid_range_electronics.csv"
}

hvr_report = reports(high_value_products, reports_dict['hvr'])
cls_report = reports(critical_stock, reports_dict['cls'])
mde_report = reports(mid_range_electronics, reports_dict['mde'])


# ───────────────────────────────────────────────────────────────────────────
# TAREA 8: Validación y Resumen
# ───────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("VALIDACIÓN DE RESULTADOS")
print("=" * 70)

df_var_dict = {
    "hvp_name": "high_value_products",
    "cls_name": "critical_stock",
    "mde_name": "mid_range_electronics",
    "tpe_name": "top_electronics",
    "tpf_name": "top_furniture",
    "fp_name": "featured_products",
}

def validation(var, df):        
    result = (
        print(f"\n- Nombre de la variable: {var}"),
        print(f"- Productos encontrados: {len(df)}"),
        print(f"- Columnas incluídas: {df.columns.tolist()}"),
        print(f"- Primeras 2 filas:\n{df.head(2)}")
    )
    return result

# high_value_products
hvp_validation = validation(df_var_dict['hvp_name'], high_value_products)

# critical_stock
cls_validation = validation(df_var_dict['cls_name'], critical_stock)

# mid_range_electronics
mde_validation = validation(df_var_dict['mde_name'], mid_range_electronics)

# top_electronics
tpe_validation = validation(df_var_dict['tpe_name'], top_electronics)

# top_furniture
tpf_validation = validation(df_var_dict['tpf_name'], top_furniture)

# featured_products
fp_validation = validation(df_var_dict['fp_name'], featured_products)


print("\n" + "=" * 70)
print("PROYECTO COMPLETADO ✅")
print("=" * 70)
