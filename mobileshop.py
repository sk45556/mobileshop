import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Python Mobile Shop", layout="centered")
st.title("📱 Python Mobile Shop")
st.markdown("**" + "*" * 40 + "**")

# Initialize session_state for products
if "products" not in st.session_state:
    st.session_state.products = {
        "1": {"SNO": 1, "Product": "Smart Phone", "In Stock": 20, "Price": 200},
        "2": {"SNO": 2, "Product": "Head Phones", "In Stock": 100, "Price": 30},
        "3": {"SNO": 3, "Product": "Screen Guard", "In Stock": 200, "Price": 5},
        "4": {"SNO": 4, "Product": "Chargers", "In Stock": 100, "Price": 10},
        "5": {"SNO": 5, "Product": "Memory Cards", "In Stock": 120, "Price": 50}
    }

# Use session_state products
products = st.session_state.products

# Main Menu
menu = ["Show All Products", "Buy Product", "Add Products (Admin)", "Exit"]
choice = st.selectbox("Select an Option", menu)

# Show All Products
if choice == "Show All Products":
    st.subheader("📦 Product List")
    st.table([{**v} for v in products.values()])
    st.success("Program execution completed.")

# Buy Product
elif choice == "Buy Product":
    st.subheader("🛒 Buy a Product")
    st.table([{**v} for v in products.values()])
    product_id = st.selectbox("Select Product ID to Buy", list(products.keys()))
    customer_name = st.text_input("Enter Your Name")

    if customer_name and st.button("Buy Now"):
        selected = products[product_id]
        st.info("🧾 Order Summary")
        st.write(f"**Product:** {selected['Product']}")
        st.write(f"**Price:** ${selected['Price']}")

        confirm = st.radio("Confirm Purchase?", ("Yes", "No"))
        if confirm == "Yes":
            st.success("✅ Purchase Confirmed. Bill Generated.")
            st.write("**Bill No:** 12345")
            st.write("**Date:**", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            st.write("**Customer:**", customer_name)
            st.write("**Product:**", selected["Product"])
            st.write("**Amount:** $", selected["Price"])
        else:
            st.warning("❌ Purchase Cancelled.")

# Add Product (Admin)
elif choice == "Add Products (Admin)":
    st.subheader("🔐 Admin Login to Add Products")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username == "admin" and password == "pass":
        st.success("Admin login successful.")
        new_id = st.text_input("Enter New Product ID")
        new_name = st.text_input("Enter Product Name")
        new_stock = st.number_input("Enter Quantity", min_value=1, step=1)
        new_price = st.number_input("Enter Price", min_value=1, step=1)

        if st.button("Add Product"):
            new_product = {
                "SNO": int(new_id),
                "Product": new_name,
                "In Stock": new_stock,
                "Price": new_price
            }
            st.session_state.products[new_id] = new_product  # ✅ Persist the product
            st.success("✅ Product Added Successfully!")
            st.json(new_product)
    elif username or password:
        st.error("❌ Invalid Username or Password")

# Exit Option
elif choice == "Exit":
    st.info("👋 Thank you for visiting Python Mobile Shop!")
